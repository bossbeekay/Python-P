import re

def password_strength(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Include lowercase letters.")

    # Uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Include uppercase letters.")

    # Digit
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add some numbers.")

    # Special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters like !, @, #, etc.")

    # Return result
    if score == 5:
        return "Strong", []
    elif 3 <= score < 5:
        return "Moderate", suggestions
    else:
        return "Weak", suggestions

# Main loop
while True:
    user_password = input("Enter your password: ")
    strength, feedback = password_strength(user_password)
    print("\nYour password is:", strength)

    if strength in ["Weak", "Moderate"]:
        print("Suggestions to improve your password:")
        for tip in feedback:
            print("- " + tip)

    input("\nPress Enter to try another password...\n")
