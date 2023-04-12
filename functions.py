import re
from typing import TextIO, Union, List, Iterator


def commands(it: Iterator, command: str, value: str, file: TextIO) -> Union[List, str]:
    result = []
    if command == 'filter':
        result = list(filter(lambda val: value in val, file))
    if command == 'map':
        result = list(map(lambda val: val.split()[int(value)], file))
    if command == 'unique':
        result = list(set(file))
    if command == 'sort':
        if value == 'desc':
            result = sorted(file, reverse=True)
        elif value == 'asc':
            result = sorted(file)
    if command == "limit":
        return list(file)[:int(value)]

    if command == 'regex':
        regexp: re.Pattern = re.compile(value)
        return list(filter(lambda y: regexp.findall(y), file))
    return result


# x = [
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3]
# ]
#
# '''
# 1 2 3
# 1 2 3
# 1 2 3
# '''