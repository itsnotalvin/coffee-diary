from flask import Flask
from flask_restx import Api, Resource
from config import DevConfig
from models import Recipe
from exts import db

app=Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)

api=Api(app, doc='/docs')

@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello World"}

@app.shell_context_processor
def make_shell_context():
    return {
        "db":db,
        "Recipe":Recipe
    }



if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            print("Database initialised successfully.")
        except Exception as e:
            print("Error has occured during database intialization:", e)
    app.run()