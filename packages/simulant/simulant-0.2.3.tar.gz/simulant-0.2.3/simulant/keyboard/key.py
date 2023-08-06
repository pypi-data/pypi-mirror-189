from collections import UserString

letters = {
    'а': 'Cyrillic_a',
    'б': 'Cyrillic_be',
    'в': 'Cyrillic_ve',
    'г': 'Cyrillic_ghe',
    'д': 'Cyrillic_de',
    'е': 'Cyrillic_ie',
    'ё': 'Cyrillic_io',
    'ж': 'Cyrillic_zhe',
    'з': 'Cyrillic_ze',
    'и': 'Cyrillic_i',
    'й': 'Cyrillic_shorti',
    'к': 'Cyrillic_ka',
    'л': 'Cyrillic_el',
    'м': 'Cyrillic_em',
    'н': 'Cyrillic_en',
    'о': 'Cyrillic_o',
    'п': 'Cyrillic_pe',
    'р': 'Cyrillic_er',
    'с': 'Cyrillic_es',
    'т': 'Cyrillic_te',
    'у': 'Cyrillic_u',
    'ф': 'Cyrillic_ef',
    'х': 'Cyrillic_ha',
    'ц': 'Cyrillic_tse',
    'ч': 'Cyrillic_che',
    'ш': 'Cyrillic_sha',
    'щ': 'Cyrillic_shcha',
    'ъ': 'Cyrillic_hardsign',
    'ы': 'Cyrillic_yeru',
    'ь': 'Cyrillic_softsign',
    'э': 'Cyrillic_e',
    'ю': 'Cyrillic_yu',
    'я': 'Cyrillic_ya',
}


class BaseKey(str):
    def __new__(cls, string):
        instance = super().__new__(cls, string)
        return instance

    def __add__(self, other):
        return f"{self}+{other}"


class Keys:
    F6 = BaseKey('F6')
    ESC = BaseKey('Escape')
    ENTER = BaseKey('Return')
    TAB = BaseKey('Tab')
    CTRL = BaseKey('ctrl')
    RIGHT = BaseKey('Right')
    LEFT = BaseKey('Left')
    UP = BaseKey('Up')
    DOWN = BaseKey('Down')
    SPACE = BaseKey('space')
    SHIFT = BaseKey('Shift_L')
