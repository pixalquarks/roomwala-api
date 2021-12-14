from fastapi import status, HTTPException, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import delete
from starlette.responses import Response
from starlette.status import HTTP_201_CREATED
from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(
    prefix = "/flats"
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def post_flat(flatData : schemas.Flat, db: Session = Depends(get_db), current_user : schemas.TokenData = Depends(oauth2.get_current_user)):
    print(current_user)
    print(current_user.id)
    new_flat = models.Flat(owner_id = current_user.id, **flatData.dict())
    db.add(new_flat)
    db.commit()
    db.refresh(new_flat)
    
    return new_flat

@router.get("/", response_model=List[schemas.FlatOut], status_code=status.HTTP_200_OK)
def get_flats(db: Session = Depends(get_db), limit : int = 5, skip : int = 0):
    flats = db.query(models.Flat).limit(limit).offset(skip).all()
    
    return flats

@router.get("/{id}", response_model=schemas.FlatOut, status_code=status.HTTP_200_OK)
def get_flat_by_id(id: int, db : Session = Depends(get_db)):
    flat = db.query(models.Flat).filter(models.Flat.id == id).first()
    
    if not flat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"flat with id {id} does not exist"
        )
        
    return flat

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_flat(id: int, db : Session = Depends(get_db), current_user : schemas.TokenData = Depends(oauth2.get_current_user)):
    flat_query = db.query(models.Flat).filter(models.Flat.id == id)
    
    print(flat_query.first().owner_id)
    print(current_user.id)
    
    if not flat_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"flat with id {id} does not exist")
        
    if flat_query.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"forbidden to perform requested action")
        
    
    flat_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.FlatOut, status_code=HTTP_201_CREATED)
def update_flat(id: int, flat : schemas.Flat, db : Session = Depends(get_db), current_user : schemas.TokenData = Depends(oauth2.get_current_user)):
    flat_query = db.query(models.Flat).filter(models.Flat.id == id)
    
    if not flat_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"flat with id {id} does not exist")
        
    if flat_query.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"forbidden to perform requested action")
        
    flat_query.update(flat.dict())
    db.commit()
    
    return flat_query.first()