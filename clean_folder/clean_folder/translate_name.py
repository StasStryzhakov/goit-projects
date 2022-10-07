import re



CYRILLIC_SYMBOLS = tuple("абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ")
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")


def translate_file_name(name: str, extention: str, translate: dict): # функція яка повертає перекладене ім"я
    name_wo_extention = name.removesuffix('.' + extention)
    name_wo_extention = re.sub('[\W]', '_', name_wo_extention)
    return f'{name_wo_extention.translate(translate)}.{extention}'


def get_translate_dict(cyrilic=CYRILLIC_SYMBOLS, translation=TRANSLATION): # функція яка створює словник
    translate = {}
    for c, t in zip(cyrilic, translation): 
        translate[ord(c)] = t
        translate[ord(c.upper())] = t.upper()
    return translate


