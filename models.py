import os
import json
from dataclasses import dataclass, field
from typing import List

from r_and_m import get_characters


@dataclass
class Character:
    name: str
    species: str
    status: str


@dataclass
class Human(Character):
    pass


@dataclass
class Alien(Character):
    pass

class Catalog:
    characters: List[Character] = []

    def __init__(self, filename='base.json'):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                items = json.loads(f.read())
            print('loaded from disk')
        else:
            items = get_characters()

            with open(filename, 'w') as f:
                f.write(json.dumps(items))

            print(f'loaded from api and saved to {filename}')

        for row in items:
            if row['species'] == 'human':
                obj = Human(row['name'], row['species'], row['status'])
            else:
                obj = Alien(row['name'], row['species'], row['status'])

            self.characters.append(obj)