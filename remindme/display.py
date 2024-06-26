from rich.rule import Rule
from rich.markdown import Markdown
from remindme.console import console

def log_password_issue():
    console.print(Rule(title="[error]!!!Failed to decrypt love!!![/]"))
    console.print("Did you use the right password?", justify="center")

def log_command_line_arg_error(err_msg: str):
    console.print("[error]Whoops! Looks like you made a mistake requesting love![/]", justify="center")
    console.print(f"Error: {err_msg}\n", justify="center")

def log_reminder(index: int | None, topic: str, data: dict):
    topic_count = len(data["catagories"][topic])
    console.print(Rule(f"Reminder: {topic}"))
    if index is not None:
        console.print(Markdown(data["catagories"][topic][index]))
    console.print(Rule())
    if index is not None and index < topic_count - 1:
        console.print(f"Reminders viewed: [green]{index + 1}/{topic_count}[/]")
    else:
        console.print(f"Reminders viewed: [red]{topic_count}/{topic_count}[/]")