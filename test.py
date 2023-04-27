import random
from utils.function import *

def replace_random(data):
    if isinstance(data, dict):
        return {k: replace_random(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [replace_random(item) for item in data]
    elif isinstance(data, str) and "random" in data:
        return data.replace(data, str(eval(str(data))))
    else:
        return data


if __name__ == '__main__':
    data = {
        "foo": "random_number(10)",
        "bar": [1, 2, {"baz": "random_number(10)"}]
    }
    new_data = replace_random(data)
    print(new_data)