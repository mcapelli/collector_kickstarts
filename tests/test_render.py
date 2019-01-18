def test_single_template_output(tmp_path):
    from collector_kickstarts.render import Kickstart
    from collector_kickstarts.utility import FileUtility
    fu = FileUtility('resources/simple_kickstart.good.txt')
    contents = fu.get_file_string()
    ks = Kickstart()
    output = ks.run()
    d = tmp_path
    p = d / "file_under_test.txt"
    p.write_text(output)
    # assert filecmp.cmp(p, 'resources/simple_kickstart.good.txt')
    assert output == contents
