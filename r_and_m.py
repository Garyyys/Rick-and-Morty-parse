import cmd
# Возьмите url для api данных сериала Рик и Морти
url = 'https://rickandmortyapi.com/api/character/'

# используя модуль `requests` и функцию `get` из этого модуля получите json ответа
# и по ключу `results` получите список персонажей сериала


def get_characters():
    import requests

    return requests.get(url).json()['results']


# в результате вам вернется список словарей-персонажей, в которых вам необходимы следующие ключи:
# name - имя персонажа
# status - жив персонаж или нет
# species - раса персонажа
# gender - пол персонажа
# location - name - где персонаж проживает


# в вашей программе должно быть реализовано следующее
# 1. загруженные данные о персонажах должны быть сохранены в файл
# 2. при следующем запуске программы должна быть проверка: если файл с информацией о персонажах существует, то запрос к api делать нет необходимости и данные могут быть загружены в память из файла
# 3. при работе программы персонажи должны быть представлены объектами класса Character с необходимым набором аттрибутов
# то есть вам необходимо перевести список словарей о персонажах в объекты класса Character: List[Dict] -> List[Character]

# пример перевода словаря в объект
character = {
    'name': 'Rick',
    'species': 'Human',
}


class Character:
    def __init__(self, name, species, status):
        self.name = name
        self.species = species
        self.status = status


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

# 4*. реализуйте класс Aggregator, который аттрибутом принимает список объектов персонажей и, на основании списка всех персонажей, может вывести на экран саггрегированную информацию:
# подсказка: возможно, вам потребуется еще один класс, который запрос с клавиатуры конвертирует в объект запроса
#
# возможность получить кол-во персонажей по каждому признаку (ключу), указанному выше
# >>> show status alive
# >>> выводит на экран кол-во живых персонажей
#
# >>> show species human
# >>> выводит кол-во людей
#
# возможность вывести на экран общую аггрегацию по признаку
# >>> show status
# >>> Alive 100
# >>> unknown 37
# ...
#
# >>> show location
# >>> Citadel of Ricks 19
# >>> Earth (Replacement Dimension) 33
# ...
#