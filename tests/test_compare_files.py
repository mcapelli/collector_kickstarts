from click.testing import CliRunner

from collector_kickstarts.cli import main
import filecmp


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0


def test_single_template_output(tmp_path):
    from collector_kickstarts.render import Kickstart
    with open('resources/simple_kickstart.good.txt', 'r') as data_file:
        contents = data_file.read()
    ks = Kickstart()
    output = ks.run()
    d = tmp_path
    p = d / "file_under_test.txt"
    p.write_text(output)
    # assert filecmp.cmp(p, 'resources/simple_kickstart.good.txt')
    assert output == contents
