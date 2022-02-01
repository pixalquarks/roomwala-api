from fastapi import APIRouter, HTTPException, status, Depends, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import schemas, models, utils, oauth2
from ..database import get_db

router = APIRouter(
    tags=['Authentication'],
    prefix="/auth"
    )


@router.post("/login", status_code=status.HTTP_202_ACCEPTED)
def owner_login(owner_credentials: OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    print("getting user")
    owner = db.query(models.Owner).filter(models.Owner.email == owner_credentials.username).first()
    
    if not owner:
        print("no user")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid login credentials")
    
    if not utils.verify_password(owner_credentials.password, owner.password):
        print("invalid pass")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid login credentials")
    
    if not owner.activated:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"account is not activated, cannot login")
    
    access_token = oauth2.create_access_token(data={"owner_id" : owner.id})
    
    return {"access_token" : access_token, "token_type" : "bearer"}

@router.get("/verification", status_code=status.HTTP_201_CREATED, response_model=schemas.OwnerOut)
def owner_verification(db : Session = Depends(get_db), token : str = ""):
    user = oauth2.get_current_user(token)

    owner_query = db.query(models.Owner).filter(models.Owner.id == user.id)

    if owner_query.first().activated:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"account has already been activated")

    owner_query.update({models.Owner.activated: 1})
    db.commit()

    return owner_query.first()