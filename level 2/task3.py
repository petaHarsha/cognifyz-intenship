def check_password_strength(password):
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~\\"
    length = len(password)

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in special_characters for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])

    # Detailed feedback
    print("\nPassword Analysis:")
    print(f"Length: {length} characters")
    print(f"Contains uppercase: {'Yes' if has_upper else 'No'}")
    print(f"Contains lowercase: {'Yes' if has_lower else 'No'}")
    print(f"Contains digits: {'Yes' if has_digit else 'No'}")
    print(f"Contains special characters: {'Yes' if has_special else 'No'}")

    # Strength decision
    if length < 8 or score <= 2:
        return " Weak Password"
    elif score >= 3 and length < 12:
        return " Moderate Password"
    elif score == 4 and length >= 12:
        return " Strong Password"
    else:
        return " Moderate Password"

# Example usage
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    result = check_password_strength(pwd)
    print("\nStrength:", result)
