#!/usr/bin/python3
import click

from pathlib import Path

@click.command(help="Accepts a path as a command line argument and stores it as a variable.")
@click.argument('input_path', type=click.Path(exists=True))
def main(input_path):
    """
    Replaces spaces in filenames with underscores in given directory.

    Example usage:
    > python rename.py /path/to/directory
    """

    path = Path(input_path)
    click.echo("replacing spaces in filenames with unscores at path: {}".format(path))
    
    files_renamed = 0
    errors = []
    for file_path in path.iterdir():
        if file_path.is_file():
            new_name = file_path.name.replace(' ', '_')
            new_path = file_path.with_name(new_name)
            if new_path != file_path:
                try:
                    file_path.rename(new_path)
                    files_renamed += 1
                except Exception as e:
                    errors.append(f"Error renaming file '{file_path}': {e}")

    click.echo(f"{files_renamed} files renamed.")
    for error in errors:
        click.echo(error)

if __name__ == '__main__':
    main()
