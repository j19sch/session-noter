import argparse

from cli import CLI
import curses_cli
from utils import read_config_file


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--curses", help="enables curses interface", action="store_true")
    args = parser.parse_args()

    config = read_config_file()

    print('Welcome to session-noter!\n')
    print(config)

    if args.curses or config['general']['interface'] == "curses":
        curses_cli.main()
    else:
        interface = CLI(config)
