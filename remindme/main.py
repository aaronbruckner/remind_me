import sys
from remindme import args

def _main():
    args.parse_command_line_arguments(sys.argv[1:])

_main()