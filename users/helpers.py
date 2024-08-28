import re

def validate_fields(first_name, last_name, email):
    if not first_name:
        return {"error": "Missing first name field."}
    
    if not last_name:
        return {"error": "Missing last name field."}
    
    if not email:
        return {"error": "Missing email field."}

    if not (2 <= len(first_name) <= 30) or not re.match("^[A-Za-z]*$", first_name):
        return {"error": "First name must be 2-30 characters and contain only letters"}
    
    if not (2 <= len(last_name) <= 30) or not re.match("^[A-Za-z]*$", last_name):
        return {"error": "Last name must be 2-30 characters and contain only letters"}

    if not (5 <= len(email) <= 254) or not re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email):
        return {"error": "Email must be 5-254 characters and a valid email format"}
    
    return None

def validate_password(password):
    if not password:
        return {"error": "Missing password field."}

    if not (8 <= len(password) <= 128) or not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password):
        return {"error": "Password must be 8-128 characters and contain both letters and numbers"}
    
    return None