from app import db

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    image_path = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Customer {self.name}>"