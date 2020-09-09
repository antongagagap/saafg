import random
alphabet = "абвгдежзиклмнопрстуфхцчшщыьэюя"


def txt_read1():
    encrypt = ''
    with open('test.txt', 'r', encoding='utf-8') as f:
        encrypt = encrypt.join(f)
        encrypt = encrypt.replace(' ', 'ъ')
        ''' .replase Возвращает копию строки, в которой заменены все вхождения указанной строки указанным значением. '''
    return encrypt

def generate_key():
    alphabet_indexes = list(range(len(alphabet)))#создаем сисок элементов алфавита из строки
    random.shuffle(alphabet_indexes) # перемешиваем список
    key = ''.join([alphabet[i] for i in alphabet_indexes])# объеденям список в строку
    with open('key.txt', 'w', encoding='utf8') as f: 
        '''range(len()) используются вместе при итерации по изменяемой последовательности
        для доступа к каждому элементу в последовательности по индексу'''
        for i in range(len(alphabet)):
            f.write(f'{alphabet[i]} --> {key[i]}\n')
        f.write('[] --> ъ')
    return key
'''ищем ищешь индекс в алфавите и потом подставляем его в ключ'''
def encryption(encrypt, key):
    text = list(encrypt.lower())
    for i in range(len(text)):
        if text[i] in alphabet:
            index_in_alphabet = alphabet.index(text[i])
            text[i] = key[index_in_alphabet]
    return ''.join(text) # .join объеденяет список элементов в одну строку

def text_write(encrypt):
    with open('test1.txt', 'w', encoding='utf-8') as f:
        f.write(encrypt)

'''ищем индекс в ключе и подставляем его в алфавит'''
def decryption(encrypt, key):
    text = list(encrypt.lower())
    for i in range(len(text)):
        if text[i] in key:
            index_in_key = key.index(text[i])
            text[i] = alphabet[index_in_key]
    return ''.join(text) 

def decryption_write(encrypt):
    with open('test2.txt', 'w', encoding='utf-8') as f:
        encrypt = encrypt.replace('ъ', ' ')
        f.write(encrypt)

encrypt =  txt_read1()
key = generate_key()
encrypt = encryption(encrypt, key)
text_write(encrypt)
encrypt = decryption(encrypt, key)
decryption_write(encrypt)

print("Программа завершена")
