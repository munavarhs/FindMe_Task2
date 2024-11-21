__Flask-Based RESTful API for Product Management__

__Project Overview__

This project is a Flask-based RESTful API designed to manage a collection of product information. The API supports CRUD operations, allowing users to add, retrieve, update, and delete product records. It is designed with simplicity and performance in mind, utilizing an in-memory data structure for testing purposes.
Features

__CRUD Operations:__
**Create:** Add new products with attributes like name, price, and optional description.
**Read:** Retrieve all products or a specific product by its ID.
**Update:** Modify product details, including name, price, and description.
**Delete:** Remove products by ID.
Concurrent Request Handling: Ensures API responsiveness and thread safety using locks.
Error Handling: Returns descriptive error messages with appropriate HTTP status codes for invalid inputs or missing resources.
RESTful Design: Clear and consistent API design with proper request/response formats.

__Endpoints:__

1. Add a Product (POST):
    URL: /products
    Request Body:
    {
      "name": "Product Name",
      "price": 20,
      "description": "Description(Optional)"
    }
    Response: Returns the created product with an ID.
2. Get All Products (GET):
    URL: /products
    Response: Returns a list of all products.
3. Get a Product by ID (GET):
    URL: /products/<id>
    Response: Returns the product details for the specified ID.
4. Update a Product (PUT):
    URL: /products/<id>
    Request Body:
   {
    "name": "Updated Product Name",
    "price": 180,
    "description": "Updated description"
   }
5. Delete a Product (DELETE):
    URL: /products/<id>
    Response: Confirms the deletion of the product.

__Technology Stack - Used:__
   
    Backend Framework: Flask
    Language: Python
    Data Storage: In-memory (Python list)
    Concurrency Management: Thread-safe operations using Lock.

__How to run the main python file(app.py)__

     1. Install Flask: pip install flask
     2. Run the application: python app.py
     3. Access the API via http://127.0.0.1:5000

