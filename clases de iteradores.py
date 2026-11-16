type(iter("Python"))
# <class 'str_iterator'>

type(iter([1, 2, 3]))
# <class 'list_iterator'>

type(iter((1, 2, 3)))
# <class 'tuple_iterator'>

type(iter({1, 2, 3}))
# <class 'set_iterator'>

type(iter({"a": 1, "b": 2}))
# <class 'dict_keyiterator'>