import sys
from remindme import args
from remindme import data
from remindme import display
from remindme import state
from random import randrange

def _main():
    input = args.parse_command_line_arguments(sys.argv[1:])
    d = data.pull_latest_data(input.password)
    category_len = len(d["catagories"][input.action])
    index = randrange(category_len) if input.random else state.allocate_next_index_for_topic(input.action, category_len)
    display.log_reminder(
        index=index,
        topic=input.action,
        data=d
    )


_main()