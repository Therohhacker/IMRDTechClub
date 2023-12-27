from app import create_app
from app.db import mysql

app = create_app()

try:
    mysql.init_app(app)
except Exception as e: 
    print("DATABASE CONNECTION FAILED :" ,e)


if __name__ == "__main__":
    app.run(debug=True)
