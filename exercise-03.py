import os.path
import shelve
import yaml

def get_anagram_dict(file_path):
    anagram_dict = {}
    with open(file_path, 'r') as word_file:
        for word in word_file:
            word = word.strip()
            key = ''.join(sorted(word))
            anagram_dict.setdefault(key, []).append(word)
    return anagram_dict


def add_word_yaml(my_str:str, yaml_path: str):
    key = ''.join(sorted(my_str))
    db = load_yaml(yaml_path=yaml_path)
    if key in db:
        if my_str not in db[key]:
            db[key].append(my_str)
        else:
            db[key] = [my_str]
    save_dict_to_yaml(db, yaml_path)

def save_dict_to_yaml(my_dict:dict, file_path:str):
    with open(file_path,'w') as fp:
        yaml.safe_dump(my_dict, fp)

def load_yaml(file_path='Word_library/words.txt', yaml_path= 'files/db.yaml'):
    if not os.path.isfile(yaml_path):
        anagram_dict = get_anagram_dict(file_path)
        save_dict_to_yaml(anagram_dict,yaml_path)
    with open(yaml_path,'r') as fp:
        return yaml.safe_load(fp)


def create_anagram_shelf(file_path, shelf_path):
    anagram_shelf = shelve.open(shelf_path, 'c')
    with open(file_path, 'r') as words:
        for word in words:
            word = word.strip().lower()
            key = ''.join(sorted(word))
            if key in anagram_shelf:
                word_list = anagram_shelf[key]
                word_list.append(word)
                anagram_shelf[key] = word_list
            else:
                anagram_shelf[key] = [word]


def load_shelf(file_path='Word_library/words.txt', shelf_path='Word_library/anagram_shelf'):
    pass

def add_word(my_str: str, my_self:shelve.Shelf):
    shelve.open(my_str, 'c')
"""
    anagram_list = db[key]
    anagram_list.append(word)
    db[key] = anagram_list
"""

def main():
    yaml_path = 'Word_library/db.yaml'
    db = load_yaml(yaml_path=yaml_path)
    print(db['eorrtv'])

    #create_anagram_shelf('Word_library/words.txt','Word_library/anagram_shelf')
    #for k, v in shelve.open('Word_library/anagram_shelf').items():
    #   if len(v) > 1:
    #        print(k,v)

if __name__=='__main__':
    main()
