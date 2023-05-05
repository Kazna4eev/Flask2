from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    production_date = db.Column(db.Date)
    created_date = db.Column(db.Date, default=datetime.utcnow)
    image_path = db.Column(db.String(200))
    in_stock = db.Column(db.Boolean, default=True)


db.create_all()


@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = []
    for product in products:
        product_data = {}
        product_data['id'] = product.id
        product_data['name'] = product.name
        product_data['description'] = product.description
        product_data['production_date'] = product.production_date
        product_data['created_date'] = product.created_date
        product_data['image_path'] = product.image_path
        product_data['in_stock'] = product.in_stock
        result.append(product_data)
    return jsonify(result)

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    product_data = {}
    product_data['id'] = product.id
    product_data['name'] = product.name
    product_data['description'] = product.description
    product_data['production_date'] = product.production_date
    product_data['created_date'] = product.created
