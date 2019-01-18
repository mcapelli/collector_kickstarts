
from click.testing import CliRunner

from collector_kickstarts.cli import main
import filecmp


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0


def test_create_file(tmp_path):
    d = tmp_path /" sub"
    d.mkdir()
    p = d / "npm_hello.txt"
    with open("resources/simple_kickstart.good.txt", "r") as file_under_test:
        test_data = file_under_test.read()

    p.write_text(test_data)
    assert filecmp.cmp(p, 'resources/simple_kickstart.good.txt')
