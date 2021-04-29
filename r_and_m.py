url = 'https://rickandmortyapi.com/api/character/'




def get_characters():
    import requests

    return requests.get(url).json()['results']


character = {
    'name': 'Rick',
    'species': 'Human',
}




class Aggregator:
    def __init__(self, characters):
        self.characters = characters

    @staticmethod
    def _is_equal(a, b):
        if type(b) == dict:
            b = b.get('name', '')

        return a.lower() == b.lower()

    def show(self, field, only_value=None):
        result = {}

        for c in self.characters:
            value = getattr(c, field)

            if only_value and not self._is_equal(only_value, value):
                continue

            result[value] = result.get(value, 0) + 1

        if only_value and len(result.keys()) == 0:
            print("{} 0".format(only_value))
        else:
            for k, v in result.items():
                print("{} {}".format(k, v))
