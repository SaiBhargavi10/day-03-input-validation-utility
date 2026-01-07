import re
import getpass

def validate_email(email):
    email = email.strip()

    if not email:
        return False, "Email cannot be empty."

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern, email):
        return False, "Invalid email format."

    return True, "Valid email."

def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    else:
        return "Strong"

def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters."

    if password_strength(password) == "Weak":
        return False, "Password is too weak."

    return True, f"Password strength: {password_strength(password)}"

def validate_age(age_input):
    if not age_input.isdigit():
        return False, "Age must be numeric."

    age = int(age_input)
    if age < 1 or age > 120:
        return False, "Age must be between 1 and 120."

    return True, "Valid age."

def get_valid_input(prompt, validator, hidden=False):
    while True:
        user_input = getpass.getpass(prompt) if hidden else input(prompt)
        valid, message = validator(user_input)

        if valid:
            print(f"✅ {message}")
            return user_input
        else:
            print(f"❌ {message}\nPlease try again.\n")

def main():
    print("=== Input Validation Utility ===\n")

    email = get_valid_input("Enter your email: ", validate_email)
    password = get_valid_input("Enter your password: ", validate_password, hidden=True)
    age = get_valid_input("Enter your age: ", validate_age)

    print("\n🎉 All inputs validated successfully!")

if __name__ == "__main__":
    main()
