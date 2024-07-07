# Spaghetti kód
# A Spaghetti kód egy olyan programozási stílus, amelyben a kód nagyon összefonódott és nehezen érthető.
# A Spaghetti kód nagy hátránya, hogy a kód nagyon nehezen karbantartható és bővíthető.


# Bad practice:
# Spagetti kód példa
def handle_user_data(users):
    for user in users:
        if "age" in user:
            if user["age"] < 18:
                user["category"] = "minor"
            else:
                if user["age"] < 65:
                    user["category"] = "adult"
                else:
                    user["category"] = "senior"
        else:
            user["category"] = "unknown"

        if "email" in user:
            if "@" in user["email"]:
                user["email_valid"] = True
            else:
                user["email_valid"] = False
        else:
            user["email_valid"] = False

    return users


users = [
    {"name": "Alice", "age": 17, "email": "alice@example.com"},
    {"name": "Bob", "age": 30, "email": "bobexample.com"},
    {"name": "Charlie", "age": 70},
    {"name": "Dave"},
]

handled_users = handle_user_data(users)
print(handled_users)


# Javított változat:
# Javított kód példa
def categorize_user(user):
    if "age" not in user:
        return "unknown"
    if user["age"] < 18:
        return "minor"
    if user["age"] < 65:
        return "adult"
    return "senior"


def validate_email(user):
    return "email" in user and "@" in user["email"]


def handle_user_data(users):
    for user in users:
        user["category"] = categorize_user(user)
        user["email_valid"] = validate_email(user)
    return users


users = [
    {"name": "Alice", "age": 17, "email": "alice@example.com"},
    {"name": "Bob", "age": 30, "email": "bobexample.com"},
    {"name": "Charlie", "age": 70},
    {"name": "Dave"},
]

handled_users = handle_user_data(users)
print(handled_users)
