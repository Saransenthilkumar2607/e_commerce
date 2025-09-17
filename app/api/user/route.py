from flask import app
from controller import create_user, get_users, update_user, delete_user
    
# Register endpoints to call the function 
app.add_url_rule("/users", view_func=create_user, methods=["POST"])
app.add_url_rule("/users", view_func=get_users, methods=["GET"])
app.add_url_rule("/users/<int:user_id>", view_func=update_user, methods=["PUT"])
app.add_url_rule("/users/<int:user_id>", view_func=delete_user, methods=["DELETE"])

if __name__ == "__main__":
    app.run(debug=True)