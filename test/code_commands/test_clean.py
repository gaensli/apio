from apio.commands.clean import cli as cmd_clean


def test_apio_clean(clirunner):
    with clirunner.isolated_filesystem():
        result = clirunner.invoke(cmd_clean)
        assert result.exit_code == 0
        assert 'apio install scons' in result.output
