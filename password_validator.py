def validator(password:str)-> list:
    failed_validations = []
    if not 6 <= len(password) <= 10:
        failed_validations.append("Password must be between 6 and 10 characters")

    if not password.isalnum():
        failed_validations.append("Password must consist only of letters and digits")

    digits_count = 0
    for char in password:
        if char.isdigit():
            digits_count += 1
    if digits_count < 2:
        failed_validations.append("Password must have at least 2 digits")

    if not failed_validations:
        failed_validations.append("Password is valid")

    return failed_validations

def main():
    password_for_validation = input()

    result = validator(password_for_validation)

    print("\n".join(result))

main()