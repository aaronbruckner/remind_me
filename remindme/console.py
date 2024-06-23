from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    "error": "bold red",
    "usage_code": "green",
    "usage_comment": "blue_violet"
})
console = Console(theme=custom_theme)