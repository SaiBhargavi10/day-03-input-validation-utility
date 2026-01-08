from flask import Flask, render_template, request
import re

app = Flask(__name__)

def validate_email(email):
    if not email:
        return False, "Email cannot be empty."

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern, email):
        return False, "Invalid email format."

    return True, "Valid email."

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters."

    if not any(c.isupper() for c in password):
        return False, "Must contain at least one uppercase letter."

    if not any(c.isdigit() for c in password):
        return False, "Must contain at least one number."

    if not any(c in "@$!%*?&" for c in password):
        return False, "Must contain at least one special character."

    return True, "Strong password."

def validate_age(age):
    if not age.isdigit():
        return False, "Age must be numeric."

    age = int(age)
    if age < 18 or age > 60:
        return False, "Age must be between 18 and 60."

    return True, "Valid age."

@app.route("/", methods=["GET", "POST"])
def index():
    messages = {}

    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")
        age = request.form.get("age", "")

        messages["email"] = validate_email(email)
        messages["password"] = validate_password(password)
        messages["age"] = validate_age(age)

        if all(msg[0] for msg in messages.values()):
            messages["success"] = "🎉 All inputs validated successfully!"

    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
