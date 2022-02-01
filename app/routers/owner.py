from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from .. import schemas, models, oauth2
from .. import utils
from ..database import get_db
from app.email import generate_auth_url, send_mail

router = APIRouter(
    prefix="/owner"
)


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=schemas.OwnerOut)
async def signup_user(n_user: schemas.Owner, db: Session = Depends(get_db)):
    n_user.password = utils.hash_password(n_user.password)
    new_user = models.Owner(**n_user.dict())
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError as err:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"User with email : {n_user.email} already exists.")

    # await send_mail([n_user.email], new_user)
    generate_auth_url(new_user)
    
    return new_user


@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_owner(id : int, db : Session = Depends(get_db), current_user : schemas.TokenData = Depends(oauth2.get_current_user)):
    owner_query = db.query(models.Owner).filter(models.Owner.id == id)

    if not owner_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Owner with id {id} does not exists")
    if owner_query.first().id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"forbidden to perform requested action")
    
    owner_query.delete(synchronize_session=False)
    db.commit()

    return {"message" : "user deleted successfully"}


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.OwnerOut)
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