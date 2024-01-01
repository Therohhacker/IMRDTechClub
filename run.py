from app import create_app
from flask_sqlalchemy import SQLAlchemy
from app.db import db



# creating app instance 
app = create_app()
app.app_context().push()

# configuring app varible 
app.config['SECRET_KEY'] = 'fdsfsdfds4asd@dsaf'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/eventmanage"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# connecting to database 
try:
    db.init_app(app)
    print("Connected to database successfully")

    db.create_all()
    print("Databases created successfully")
except Exception as e:
    print("ERROR : DB Connection Failed", e)



if __name__ == "__main__":
    app.run(debug=True)
