from unidecode import unidecode
import uuid

def remove_accents(input_str):
    return unidecode(input_str)  


def make_username(name):
    name = remove_accents(name)
    name_list = name.split(' ')
    last_name = name_list.pop(-1)
    initial_names = [n[0] for n in name_list[:2]]
    initial_names.extend([last_name, str(uuid.uuid4().hex)[:4]])
    return ''.join(initial_names).lower()