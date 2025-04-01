# devlog/cli.py

import click
from devlog.log_manager import create_or_open_today_log

@click.group()
def cli():
    """DevLog CLI - your daily dev journal."""
    pass

@cli.command()
def new():
    """Create or open today's log."""
    create_or_open_today_log()

if __name__ == '__main__':
    cli()
