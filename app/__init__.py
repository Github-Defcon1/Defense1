from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.modules import EPP, Data
from app.config import Configuration
from flask_migrate import Migrate
from app.database import db

def create_app():
	app = Flask(__name__)
	app.config.from_mapping(
	SECRET_KEY = "bWrw5Gno2Y64E09rA59e"		
	)
	
	# Configurações do App
	app.config.from_object(Configuration)

	# Database
	db.init_app(app)
	from app.models.dspm_table import DspmTable
	migrate = Migrate(app, db)

	# Módulos
	app.register_blueprint(EPP.blueprint)
	app.register_blueprint(Data.blueprint)

	return app
