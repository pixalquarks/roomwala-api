from typing import List
from app.oauth2 import create_access_token
from app.schemas import EmailSchema, Owner, OwnerOut
from fastapi import BackgroundTasks, UploadFile, File, Form, Depends, HTTPException, status

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.config import settings

conf = ConnectionConfig(
    MAIL_USERNAME = settings.mail_username,
    MAIL_PASSWORD = settings.mail_password,
    MAIL_FROM = settings.mail_from,
    MAIL_PORT = settings.mail_port,
    MAIL_SERVER = settings.mail_server,
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True
)

# Only to be used for testing purposes
def generate_auth_url(user : OwnerOut):
    token = create_access_token(data = {"owner_id" : user.id})
    url = f"http://localhost:8000/auth/verification/?token={token}"
    with open("url.txt", "w") as fo:
        fo.write(url)




async def send_mail(email : List, user: OwnerOut):
    token = create_access_token(data={"owner_id" : user.id})

    url = f"http://localhost:8000/auth/verification/?token={token}"

    template = f"""
        <!DOCTYPE html>
        <html>
            <head>
            </head>
            <body>
                <div>
                    <h2>Account Verification</h2>
                    <br>
                    <h4>Thanks for registering on roomwala</h4>
                    <p>Please click on the link below to activate your account</p>
                    <a href="{url}">Activate your account</a>
                </div>
            </body>
        </html>
    """

    message = MessageSchema(
        subject = "Roomwala account activation mail",
        recipients = email,
        body = template,
        subtype = "html"
    )

    fm = FastMail(conf)
    await fm.send_message(message=message)