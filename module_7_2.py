def custom_write(file_name, strings):
    _dict = {}
    index = 0
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        index += 1
        position = file.tell()
        _dict[(index, position)] = string
        file.write(string + '\n')
    file.close()
    return _dict

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)




