my_dict = {'key1': 'value1', 'key2': 'value2'}

if my_dict.get('key1') is not None:
    print(my_dict.get('key1'))
else:
    print('Key not found.')