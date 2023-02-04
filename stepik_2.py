def list_genteration(*args) -> list:
    res = []
    for i in args:
        if i % 2 == 0:
            res.append(i)
    return res


def list_generator(*args):
    for arg in args:
        if arg % 2 == 0:
            yield arg


lst = list_genteration(1, 2, 3, 3, 3, 3, 4, 5)
for i in lst:
    print(i)
print("-" * 3)
lst_2 = list_generator(1, 2, 3, 3, 3, 3, 4, 5)
for i in lst_2:
    print(i)
