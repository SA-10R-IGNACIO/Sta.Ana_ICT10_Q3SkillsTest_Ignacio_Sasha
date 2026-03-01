from pyscript import document

def account_creation(e):
    output = document.getElementById("output")
    output.innerText = ""

    username = document.getElementById("username").value.strip()
    password = document.getElementById("password").value

    if len(username) < 7:
        output.innerText = "Username must be at least 7 characters long."
        return

    if len(password) < 10:
        output.innerText = "Password must be at least 10 characters long."
        return

    if not any(char.isalpha() for char in password):
        output.innerText = "Password must contain at least one letter."
        return

    if not any(char.isdigit() for char in password):
        output.innerText = "Password must contain at least one number."
        return

    output.innerText = "Account successfully created."
