from flask import Flask
from app.modules import EPP, Data
from app.config import Configuration

def create_app():
	app = Flask(__name__)
	app.config.from_mapping(
	SECRET_KEY = "bWrw5Gno2Y64E09rA59e"		
	)
	
	app.config.from_object(Configuration)

	app.register_blueprint(EPP.blueprint)
	app.register_blueprint(Data.blueprint)

	return app
