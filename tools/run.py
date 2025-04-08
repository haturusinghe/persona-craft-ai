from datetime import datetime as dt
from pathlib import Path

import click
from loguru import logger

@click.command(
    help="""
Welcome to the Persona Craft AI CLI!
This CLI tool is designed to help you run the Persona Craft AI application with ease.
    """
)

def main() -> None:
    root_dir = Path(__file__).resolve().parent.parent

if __name__ == "__main__":
    main()
    