from models import db, User

# Create a new user
def create_user(name, email):
    # Check if the email is already in use
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return {"error": "Email already in use"}

    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return {"message": f"User '{name}' created successfully!"}

# Get a user by ID
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}
    
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }

# Update user details
def update_user(user_id, name=None, email=None):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}

    if name:
        user.name = name
    if email:
        # Check if the email is unique
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {"error": "Email already in use"}
        user.email = email

    db.session.commit()

    return {"message": f"User '{user.name}' updated successfully!"}

# Delete a user
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}

    db.session.delete(user)
    db.session.commit()

    return {"message": f"User '{user.name}' deleted successfully!"}
