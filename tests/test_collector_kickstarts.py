
from click.testing import CliRunner

from collector_kickstarts.cli import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0


def test_compare_files():
    #  set file1 to simple_kickstart.bad.txt
    file1 = open("simple_kickstart.bad.txt", "w+")
    #  set file2 to simple_kickstart.good.txt
    file2 = open("simple_kickstart.good.txt", "w+")

    assert file1 == file2
