import pytest
from click.testing import CliRunner

from collector_kickstarts.cli import main


def test_main(tmpdir):
    runner = CliRunner()
    result = runner.invoke(main, ['resources/render_multiple_files.yml', tmpdir.dirname])

    assert result.output == '()\n'
    assert result.exit_code == 0


