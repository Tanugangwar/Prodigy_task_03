import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    if strength == 5:
        return "Strong Password ✅", feedback
    elif strength >= 3:
        return "Moderate Password ⚠️", feedback
    else:
        return "Weak Password ❌", feedback

# Test run
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    result, suggestions = check_password_strength(user_password)
    print("\nResult:", result)
    if suggestions:
        print("Suggestions to improve:")
        for item in suggestions:
            print("-", item)
