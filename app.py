from flask import Flask, jsonify, request
from threading import Lock

app = Flask(__name__)

# Sample home route for testing
@app.route('/')
def home():
    return "Hello, Find Me Recruting team..."

# In-memory storage for products
products = []
product_lock = Lock()
product_id_counter = 1

# Helper function to find a product by ID
def find_product(product_id):
    return next((product for product in products if product["id"] == product_id), None)

# CRUD Operations for the task given

# 1. Add a product (Create)
@app.route('/products', methods=['POST'])
def add_product():
    global product_id_counter
    with product_lock:
        data = request.get_json()
        if not data or 'name' not in data or 'price' not in data:
            return jsonify({"error": "Invalid input"}), 400

        product = {
            "id": product_id_counter,
            "name": data["name"],
            "price": data["price"],
            "description": data.get("description", "")
        }
        products.append(product)
        product_id_counter += 1
        return jsonify(product), 201

# 2. Get all products (Read)
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

# 3. Get a single product by ID (Read)
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = find_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

# 4. Update a product (Update)
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    with product_lock:
        product = find_product(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400

        product["name"] = data.get("name", product["name"])
        product["price"] = data.get("price", product["price"])
        product["description"] = data.get("description", product["description"])
        return jsonify(product), 200

# 5. Delete a product (Delete)
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    with product_lock:
        product = find_product(product_id)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        products.remove(product)
        return jsonify({"message": "Product deleted"}), 200

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True, threaded=True)

