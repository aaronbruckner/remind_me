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
    [usage_code]{invoke} stats -pw myPassword[/]
    [usage_code]{invoke} love -pw myPassword[/]
    [usage_code]{invoke} story -pw myPassword[/]
    [usage_code]{invoke} sex -pw myPassword[/]
    """
    parser = LoveParser(
        description="""\
        [red]A utility written for Miranda to reminder her about all the ways I love her[/] ❤️
        Pulls encrypted data from online, decrypts it, displays one of the selected topics, and tracks progress.

        Log back in occasionally to see new submissions!

        Progress is saved in current working directory under ./remindme_progress.json
        """,
        usage=usage,
        formatter_class=argparse.RawTextHelpFormatter
    )
    action_description = """\
    specify a primary action for the script. Allowed values:
      * [bold red]stats[/] - Provides basic summary of the tool along with progress in each category.
      * [bold red]love[/] - Prints a love-based reminder. Widest category of topics.
      * [bold red]story[/] - Prints a story-based reminder recalling some of my favorite memories with you.
      * [bold red]sex[/] - Prints a sex/body-based reminder.
    """
    parser.add_argument("action", help=action_description, choices=["stats", "love", "story", "sex"])
    parser.add_argument("-pw", required=True, help="Love cannot defeat symmetric encryption. Ask Aaron for the password ❤️")
    parser.parse_args()