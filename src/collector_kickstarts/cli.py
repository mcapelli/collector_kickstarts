"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mcollector_kickstarts` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``collector_kickstarts.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``collector_kickstarts.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click


@click.command()
@click.argument('data_file')
@click.argument('output_path')
def main(data_file, output_path):
    from collector_kickstarts.render import Kickstart
    from collector_kickstarts.utility import FileUtility
    fu = FileUtility(data_file)
    yaml_data = fu.get_yaml()
    Kickstart.create_kickstart_files(yaml_data, output_path)

    click.echo('()')
