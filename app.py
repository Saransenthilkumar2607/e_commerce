# import app 
# from app import create_app

# app = create_app()
 
# if __name__ == "__main__":
#     app.run(debug=True, port=5000, host='0.0.0.0')


from flask import Flask
from app.api.customer.route import customer_bp

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(customer_bp, url_prefix='/api/customers')
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000, host='0.0.0.0')