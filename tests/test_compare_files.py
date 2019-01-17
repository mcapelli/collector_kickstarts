from click.testing import CliRunner

from collector_kickstarts.cli import main
import filecmp

def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0

def test_compare_files():
    #  set file1 to simple_kickstart.bad.txt

    #  set file2 to simple_kickstart.good.txt

    f = 'A'
    assert f == 'B'
    a = 3 + 5 * 8 / 2
    assert a == 23.0
    assert filecmp.cmp('simple_kickstart.bad.txt', 'simple_kickstart.good.txt')
    assert filecmp.cmp('simple_kickstart.bad.txt', 'simple_kickstart.bad.txt')
