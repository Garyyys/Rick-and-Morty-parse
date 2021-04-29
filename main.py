import cmd
import os
import json

from r_and_m import get_characters, Character, Aggregator


class Terminal(cmd.Cmd):
    intro = 'Hello! Follow the commands.'
    characters = []

    @property
    def prompt(self):
        return f"(\/)o_O(\/): "

    def do_load(self, filename='base.json'):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.characters = json.loads(f.read())

            print('loaded from disk')
        else:
            self.characters = get_characters()

            with open(filename, 'w') as f:
                f.write(json.dumps(self.characters))

            print(f'loaded from api and saved to {filename}')

    def do_show(self, args: str):
        characters = [Character(
            c['name'],
            c['species'],
            c['status']) for c in self.characters]

        args = args.split()

        if not args:
            print("Arguments missing")
            return

        aggr = Aggregator(characters)
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