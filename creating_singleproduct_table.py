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
        print(product)
