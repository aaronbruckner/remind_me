from rich.rule import Rule
from remindme.console import console

def log_password_issue():
    console.print(Rule(title="[error]!!!Failed to decrypt love!!![/]"))
    console.print("Did you use the right password?")