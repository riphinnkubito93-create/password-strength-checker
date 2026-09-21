def check_password_strength(password):
    # Check requirements
    has_length = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    # Calculate score based on met requirements
    score = sum([has_length, has_digit, has_upper, has_symbol])

    # Determine strength
    if score == 4:
        return "Strong"
    elif score >= 2:
        return "Medium"
    else:
        return "Weak"

# Test the program
user_password = input("Enter a password to test: ")
print(f"Password Strength: {check_password_strength(user_password)}")