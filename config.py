import os #FOR SETTING EVIRONMENT VARIABLES

class Config:
	SECRET_KEY='de74e7b0fad76d362bfd1fcd0c0fd885'
	#init db
	SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringaschool:joe@localhost/blog'
	UPLOADED_PHOTOS_DEST = 'app/static/profile_pics'
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT =  587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
	SIMPLEMDE_JS_IIFE = True
	SIMPLEMDE_USE_CDN = True
	@staticmethod
	def init_app(app):
		pass

class ProdConfig(Config):
	'''
	pekejeng
	'''
	SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")



class TestConfig(Config):
	pass


class DevConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:joe@localhost/blog'
	DEBUG = True


config_options = {
'development': DevConfig,
'production': ProdConfig,
'test': TestConfig
}
