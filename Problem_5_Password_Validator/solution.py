def password_validator():
    name = input("enter your name:")
    password = input("enter your password:")

    missing_rule = []
    if len(password) < 8:
        missing_rule.append("password should be at least six characters long.")
    if not any(char.isdigit() for char in password):
        missing_rule.append("password should contain at least two digit.")
    if password.lower() == name.lower():
        missing_rule.append("password should not be the same as your name.")
    if not missing_rule:
        print("password strength: STRONG")
    else:
        print("password strength: WEAK")
        print("missing rule:")
        for rule in missing_rule:
            print("-", rule)
password_validator()