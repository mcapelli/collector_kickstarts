import pytest
from click.testing import CliRunner

from collector_kickstarts.cli import main


def test_main(tmpdir):
    runner = CliRunner()
    result = runner.invoke(main, ['resources/config_data.yml',
                                  'resources/partial_data.yml',
                                  tmpdir.dirname])

    assert result.output == '\n'
#    assert result.output == ''
    assert result.exit_code == 0


