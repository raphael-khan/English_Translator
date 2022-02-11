from statistics import mode
from translate import Translator

translator = Translator(to_lang='zh')
try:
    with open('./translate.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as e:
    print('Check your file path')
