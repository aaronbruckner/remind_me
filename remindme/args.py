import argparse
from dataclasses import dataclass
import sys
from enum import StrEnum
from rich.rule import Rule
from remindme import display
from remindme.console import console
from remindme.state import STATE_FILE_NAME

class LoveParser(argparse.ArgumentParser):
    def error(self, err_msg):
        display.log_command_line_arg_error(err_msg)
        self.print_help()
        sys.exit(2)
    
    def print_help(self, file = None) -> None:
        console.print(Rule(title="remindme.py"))
        super().print_help(file=file)
        console.print(Rule())

    def _print_message(self, message: str, file = None) -> None:
        # Hijack print method to reroute to rich console for better formatting.
        console.print(message)

class Action(StrEnum):
    LOVE = 'love'
    MEMORY = 'memory'
    SEX = 'sex'

@dataclass
class ConsoleInput:
    action: Action
    password: str
    random: bool

def parse_command_line_arguments(args) -> ConsoleInput:
    invoke = "./remindme.pex"
    usage = f"""
    [usage_code]{invoke} love -pw myPassword[/]
    [usage_code]{invoke} memory -pw myPassword[/]
    [usage_code]{invoke} sex -pw myPassword[/]
    """
    parser = LoveParser(
        description=f"""\
        [red]A utility written for Miranda to reminder her about all the ways I love her[/] ❤️
        Pulls encrypted data from online, decrypts it, displays one of the selected topics, and tracks progress.

        Progress is saved in current working directory under ./{STATE_FILE_NAME}
        """,
        usage=usage,
        formatter_class=argparse.RawTextHelpFormatter
    )
    action_description = """\
    specify a primary action for the script. Allowed values:
      * [bold red]love[/] - Prints a love-based reminder. Widest category of topics.
      * [bold red]memory[/] - Prints a memory-based reminder recalling some of my favorite memories with you.
      * [bold red]sex[/] - Prints a sex/body-based reminder.
    """
    parser.add_argument("action", help=action_description, choices=["love", "memory", "sex"])
    parser.add_argument("-pw", required=True, help="Love cannot defeat symmetric encryption. Ask Aaron for the password ❤️")
    parser.add_argument("-r", action="store_true")
    parser.parse_args(args)
    
    parsed_args = parser.parse_args(args)

    return ConsoleInput(action=parsed_args.action, password=parsed_args.pw, random=parsed_args.r)