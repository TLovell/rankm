import click
from merge import Merge
from curses import wrapper
from display import *

@click.group()
@click.version_option()
def cli():
    pass

@cli.command()
@click.argument('seperate_files', nargs=-1, type=click.File(mode='r'))
@click.argument('merge_file', nargs=1, type=click.File(mode='w+'))
def merge(seperate_files, merge_file):
    m = Merge(seperate_files, merge_file)
    wrapper(m.main_loop)


@cli.command()
@click.argument('display_file', nargs=1, type=click.File(mode='r'))
@click.option('--descending/--ascending', '-d/-a', default=True)
@click.option('--numbers/--no-numbers', '-n/ ', default=False)
def display(display_file, descending, numbers):
    click.echo(get_display_str(display_file, descending, numbers))
    
