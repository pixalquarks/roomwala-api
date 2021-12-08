from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, models, oauth2
from .. import utils
from ..database import get_db

router = APIRouter(
    prefix="/owner"
)


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def signup_user(n_user: schemas.User, db: Session = Depends(get_db)):
    n_user.password = utils.hash_password(n_user.password)
    new_user = models.Owner(**n_user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.Owner).filter(models.Owner.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id : {id} does not exist")
    
    return user

@router.post("/verify")
def verify_owner(owner_data : schemas.TokenData = Depends(oauth2.get_current_user)):
    # print(owner_data)
    return {"message" : "verified successfully", "data" : owner_data}