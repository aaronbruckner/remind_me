import pytest
from remindme import args
from remindme.args import Action

class TestParseCommandLineArguments:

    @pytest.mark.parametrize("expected_action", [Action.STATS, Action.LOVE, Action.STORY, Action.SEX])
    def test_basic_action(self, expected_action: Action):
        console_args = args.parse_command_line_arguments([expected_action, "-pw", "myPassword"])

        assert console_args.action == expected_action

    @pytest.mark.parametrize(
        "input_args", 
        [
            ["-pw", "myPassword"],
            ["stats"],
            []
        ]
    )
    def test_bad_inputs(self, input_args):
        with pytest.raises(SystemExit):
            args.parse_command_line_arguments(input_args)