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
    assert f == 'A'
    a = 3 + 5 * 8 / 2
    assert a == 23.0
    # assert filecmp.cmp('simple_kickstart.bad.txt', 'simple_kickstart.good.txt')
    assert filecmp.cmp('resources/simple_kickstart.bad.txt', 'resources/simple_kickstart.bad.txt')


def test_create_file(tmp_path):
    with open('resources/simple_kickstart.good.txt', 'r') as data_file:
        contents = data_file.read()
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(contents)
    assert filecmp.cmp(p, 'resources/simple_kickstart.good.txt')


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