import pytest
from remindme import args
from remindme.args import Action

class TestParseCommandLineArguments:

    @pytest.mark.parametrize("expected_action", [Action.LOVE, Action.MEMORY, Action.SEX])
    def test_basic_action(self, expected_action: Action):
        console_args = args.parse_command_line_arguments([expected_action, "-pw", "myPassword"])

        assert console_args.action == expected_action
        assert console_args.password == "myPassword"

    @pytest.mark.parametrize(
        "input_args", 
        [
            ["-pw", "myPassword"],
            ["love"],
            []
        ]
    )
    def test_bad_inputs(self, input_args):
        with pytest.raises(SystemExit):
            args.parse_command_line_arguments(input_args)