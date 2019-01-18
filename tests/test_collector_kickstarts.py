
from click.testing import CliRunner

from collector_kickstarts.cli import main
import filecmp


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0


