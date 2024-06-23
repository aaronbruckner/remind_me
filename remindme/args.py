import argparse
import sys
from rich.rule import Rule
from remindme import display
from remindme.console import console

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


def parse_command_line_arguments():
    invoke = "./remindme.py"
    usage = f"""
    [usage_comment]# A good starting point! Prints tool statistics.[/]
    [usage_comment]# Don't forget to include a password or love may not be decryptable.[/]
    [usage_code]{invoke} about -pw myPassword[/]
    """
    parser = LoveParser(
        description="[red]A utility written for Miranda to reminder her about all the ways I love her[/] ❤️",
        usage=usage
    )
    parser.add_argument("action", help="Specify")
    parser.parse_args()