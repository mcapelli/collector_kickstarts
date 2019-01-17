
from click.testing import CliRunner

from collector_kickstarts.cli import main
import filecmp


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0


# TODO: import and use filecmp
def test_compare_files():
    #  set file1 to simple_kickstart.bad.txt
    file1 = open("simple_kickstart.bad.txt", "w+")
    #  set file2 to simple_kickstart.good.txt
    file2 = open("simple_kickstart.good.txt", "w+")
    f = 'A'
    assert f == 'A'
    a = 3 + 5 * 8 / 2
    assert a == 32


def test_create_file(tmp_path):
    d = tmp_path /" sub"
    d.mkdir()
    p = d / "npm_hello.txt"
    with open("resources/simple_kickstart.good.txt", "r") as file_under_test:
        test_data = file_under_test.read()

    p.write_text(test_data)
    assert filecmp.cmp(p, 'resources/simple_kickstart.good.txt')
