import sys
from remindme import args
from remindme import data
from remindme import display
from remindme import state

def _main():
    input = args.parse_command_line_arguments(sys.argv[1:])
    d = data.pull_latest_data(input.password)

    display.log_reminder(
        index=state.allocate_next_index_for_topic(input.action, len(d["catagories"][input.action])),
        topic=input.action,
        data=d
    )


_main()