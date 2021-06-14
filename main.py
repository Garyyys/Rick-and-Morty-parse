import cmd
import os
import json
from models import Catalog

from r_and_m import get_characters, Aggregator


class Terminal(cmd.Cmd):
    intro = 'Hello! Follow the commands.'
    catalog = None

    @property
    def prompt(self):
        return f"(\/)o_O(\/): "

    def do_load(self, filename='base.json'):
        self.catalog = Catalog(filename)

    def do_show(self, args: str):
        args = args.split()

        if not args:
            print("Arguments missing")
            return

        aggr = Aggregator(self.catalog.characters)
        aggr.show(*args)


if __name__ == '__main__':
    terminal = Terminal()
    terminal.do_load()
    terminal.cmdloop()
    # FILE_NAME = input('Enter filename:')
    #
    # if os.path.exists(FILE_NAME):
    #     f = open(FILE_NAME, 'r')
    #     characters = json.loads(f.read())
    #     f.close()
    #     print('loaded from disk')
    # else:
    #     characters = get_characters()
    #     f = open(FILE_NAME, 'w')
    #     f.write(json.dumps(characters))
    #     f.close()
    #     print('loaded from api and saved to disk')
    #
    # characters = [Character(
    #     c['name'],
    #     c['species'],
    #     c['status']) for c in characters]
    #
    # aggr = Aggregator(characters)
    # aggr.show('status')