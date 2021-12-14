from jose import JOSEError, jwt
from datetime import datetime, time, timedelta
from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, oauth2
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

from jose.exceptions import JWTError

from app import schemas


SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRATION_TIME = settings.access_key_expire_time


def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRATION_TIME)
    to_encode.update({"exp" : expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt
    
def verify_access_token(token: str, credentials_exception):
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    
        id : str = payload.get("owner_id")
        name : str = payload.get("owner_name")
    
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id, name=name)
    except JWTError:
        raise credentials_exception
    
    return token_data
    
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials",
                                          headers={"WWW-Authenticate" : "Bearer"})
    
    return verify_access_token(token, credentials_exception)