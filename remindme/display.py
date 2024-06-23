from rich.rule import Rule
from remindme.console import console

def log_password_issue():
    console.print(Rule(title="[error]!!!Failed to decrypt love!!![/]"))
    console.print("Did you use the right password?", justify="center")

def log_command_line_arg_error(err_msg: str):
        console.print("[error]Whoops! Looks like you made a mistake requesting love![/]", justify="center")
        console.print(f"Error: {err_msg}\n", justify="center")