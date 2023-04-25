#!/usr/bin/python3
import click
import os

@click.command(help="Accepts a path as a command line argument and stores it as a variable.")
@click.argument('path', type=click.Path(exists=True))
def main(path):

    click.echo("replacing spaces in filenames with unscores at path: {}".format(path))
    
    dir_list = os.listdir(path)
    for i in dir_list:
        j = i.split(' ')
        if len(j) > 1:
            x = '_'.join(j)
            print(f"file '{i}' >>> '{x}'")
            os.rename(f"{path}/{i}",f"{path}/{x}")

if __name__ == '__main__':
    main()
