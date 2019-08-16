import os #FOR SETTING EVIRONMENT VARIABLES
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////tmp/site.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
class Config:
	SECRET_KEY = 'de74e7b0fad76d362bfd1fcd0c0fd885'
	#init db
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT =  587
	MAIL_USE_TLS = True
	MAIL_USERNAME =  os.environ.get('EMAIL_USER')
	MAIL_PASSWORD=  os.environ.get('EMAIL_PASS')
