from flask import Flask

def create_app():
	app = Flask(__name__)
	app.config.from_mapping(
	SECRET_KEY = "bWrw5Gno2Y64E09rA59e"		
	)
	
	return app
