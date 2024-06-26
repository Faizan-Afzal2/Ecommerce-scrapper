# from flask import Flask, render_template
# from flask_mysqldb import MySQL
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # app.config["MYSQL_HOST"] = "localhost"
# # app.config["MYSQL_USER"] = "root"
# # app.config["MYSQL_PASSWORD"] = ""
# # app.config["MYSQL_DB"] = "scrapper"

# # mysql = MySQL(app)


# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/scrapper"
# db = SQLAlchemy(app)


# # Define User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return "<User %r>" % self.username


# with app.app_context():
#     db.create_all()


# @app.route("/")
# def index():
#     # Inserting a new user
#     new_user = User(username="jhn", email="john@eample.com")
#     db.session.add(new_user)
#     db.session.commit()

#     # Querying all users
#     users = User.query.all()
#     for user in users:
#         print(user.username, user.email)

#     return "Check your console for user details!"


# if __name__ == "__main__":
#     app.run(debug=True)
# # # Create the database tables (you need to do this once)
# # db.create_all()
# # @app.route("/")
# # def home():
# #     qur = mysql.connection.cursor()
# #     qur.execute("SELECT * FROM users")
# #     fetchdata = qur.fetchall()
# #     qur.close()
# #     print(fetchdata)
# #     return "hellow world-2"


# # if __name__ == "__main__":
# #     app.run(debug=True)


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/scrapper"
db = SQLAlchemy(app)

productData = [
    {
        "title": "Laptop",
        "price": "2000",
        "description": "black color laptop",
    },
    {
        "title": "Mobile",
        "price": "23300",
        "description": "black color phone",
    },
    {
        "title": "Car",
        "price": "5000000",
        "description": "black color Car",
    },
]


# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return "<Product %r>" % self.title


with app.app_context():
    db.create_all()


@app.route("/getProducts")
def index():
    # Inserting product data into the database
    for product in productData:
        new_product = Product(
            title=product["title"],
            price=product["price"],
            description=product["description"],
        )
        db.session.add(new_product)
        db.session.commit()

    # Querying all products
    products = Product.query.all()
    for product in products:
        print(product.title)
    return "Check console"


if __name__ == "__main__":
    app.run(debug=True)
