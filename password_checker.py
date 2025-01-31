import re

def check_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Scoring system
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
    # Feedback
    if score == 5:
        return "Strong Password"
    elif 3 <= score < 5:
        return "Moderate Password"
    else:
        return "Weak Password"

# Main program
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")
