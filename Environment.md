# SETTING UP THE ENVIROMENT VARAIBLES

If you open the .evn.txt file it would look something like this
```
DATABASE_HOSTNAME=
DATABASE_TYPE=
DATABASE_PORT=
DATABASE_PASSWORD=
DATABASE_NAME=
DATABASE_USERNAME=
SECRET_KEY=
ALGORITHM=
ACCESS_KEY_EXPIRE_TIME=
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM=
MAIL_PORT=
MAIL_SERVER=
```

From here on I will assume that you are using a MySQL database, on a normal xampp installation on windows.

### DATABASE HOSTNAME
It is the url where your database it being hosted. If you're running the project and database locally it should be localhost
```
DATABASE_HOSTNAME=localhost
```

### DATABASE TYPE
It is the SQL database you're using. In my case it's a MySQL database
```
DATABASE_TYPE=mysql
```

### DATABASE PORT
It is the port on which your database is running. You can get it from xampp control panel.
For my case
```
DATABASE_PORT=3306
```
Please check your port, as it may be different from this.

### DATABASE USERNAME
You can use the root username
```
DATABASE_USERNAME=root
```

### DATABASE PASSWORD
For a normal xampp installation password is empty.
```
DATABASE_PASSWORD=
```
### DATABASE NAME
Give any name you like for the database for this project use.
I'm using the name roomwala
```
DATABASE_NAME=roomwala
```
### SECRET KEY
This is the key that will be used to encrypt and decrypt the [jwt tokens](https://jwt.io/) that we use for authentication.
You can put any string in here, but make sure it's strong and secure
```
SECTER_KEY=<insert the key here>
```

### ALGORITHM
The algorithm that is used to encrypt and decrypt the jwt tokens. We are using HS256 here.
```
ALGORITHM=HS256
```

### ACCESS KEY EXPIRE TIME
The time for which the jwt token will be valid for.
The value is in minutes
```
ACCESS_KEY_EXPIRE_TIME=<enter time here>
```

Now from here on you'll need an email, that will be used to send emails to user for different purposes.

### MAIL USERNAME
```
MAIL_USENAME=<enter the email here>
```

### MAIL PASSWORD
```
MAIL_PASSWORD=<enter the password here>
```

### MAIL FROM
```
MAIL_FROM=<enter the same email address as earlier>
```

### MAIL_SERVER
You need to enter the smtp server address for the email service you're using. If you're using gmail then
```
MAIL_SERVER=smtp.gmail.com
```

### MAIL PORT
Port for the smtp server address for the email service you're using. If you're using gmail then
```
MAIL_PORT=587
```
## **IMPORTANT**
Please make sure you never share your secret key and email credentials with others, or push them to a version control. Also make a new dummy email for testing with. Also make sure to enable
smtp on your email service. For gmail refer to [this](https://support.google.com/mail/answer/7126229?hl=en#zippy=%2Cstep-check-that-imap-is-turned-on%2Cstep-change-smtp-other-settings-in-your-email-client)
