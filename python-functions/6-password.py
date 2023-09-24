def validate_password(password):
    password_length = len(password)
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    
    # and password.isupper() == True and password.islower() == True and password.isspace() == True
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    if password_length >= 8 and has_uppercase and has_lowercase and has_digit and not(" " in password):
        return True
    else:
        return False
    

print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))