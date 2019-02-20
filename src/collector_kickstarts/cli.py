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
@click.argument('config_file')
@click.argument('data_file')
@click.argument('output_path')
def main(config_file, data_file, output_path):
    from collector_kickstarts.render import Kickstart
    from collector_kickstarts.utility import FileUtility, merge_config_data


    cf = FileUtility(config_file)
    config_data = cf.get_yaml()

    pf = FileUtility(data_file)
    partial_data = pf.get_yaml()

    template_data = merge_config_data(config_data, partial_data)
    Kickstart.create_kickstart_files(template_data, output_path)

    click.echo('on')
