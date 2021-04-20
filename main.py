import os
import json
from r_and_m import get_characters, Character

if __name__ == '__main__':
    FILE_NAME = input()

    if os.path.exists(FILE_NAME):
        f = open(FILE_NAME, 'r')
        characters = json.loads(f.read())
        f.close()
        print('loaded from disk')
    else:
        characters = get_characters()
        f = open(FILE_NAME, 'w')
        f.write(json.dumps(characters))
        f.close()
        print('loaded from api and saved to disk')

    characters = [Character(c['name'], c['species']) for c in characters]

#nothing new