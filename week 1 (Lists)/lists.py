
# a = 5
# b = 2 + 3
# c = [a, b]
#
# a = 5
# b = 2
# c = 3
# c = [a, b + c]
#
# a = "hiya"
# b = "hi" + "ya"
# c = "hi"
# d = "ya"
# c = [a, b, c + d]
#
# a = 1
# b = 2
# c = [a, 1, b]
#
# a = 1
# b = 2
# c = [3, a + b, 1 + 2]
#
# b = [1, 2, 2]
# c = [1, 2, 2]
# d = c
#
# p = [1, 1, 1]
# q = [1] + [1] + [1]
# r = [0, 0, 0]
# for i in range(len(p)):
#   r[i] = p[i]


# Please do not modify the following code.
# It shows information about
# everything defined above.

from collections import defaultdict


# Put _ in front of all variables to avoid
# overwriting any global variables above
def _aliases():
    _addr2vars = defaultdict(lambda: [])
    _g = dict(globals())

    while _g:
        _varname, _value = _g.popitem()
        if _varname[0] != "_" and _varname not in {"defaultdict"}:
            _addr2vars[eval(f"id({_varname})")].append(_varname)
            if isinstance(_value, list):
                for _i in range(len(_value)):
                    _element_name = f"{_varname}[{_i}]"
                    _g[_element_name] = eval(_element_name)

    print("Aliases:")

    # Ridiculous way to show ? rather than '?'
    class QuestionMark:
        def __repr__(self):
            return "?"

    _question_mark = QuestionMark()

    _lines = []
    for _address in _addr2vars:
        _vars = ", ".join(_addr2vars[_address])
        _val = eval(_addr2vars[_address][0])
        if isinstance(_val, str):
            _val = "'" + _val + "'"
        elif isinstance(_val, list):
            _val = [_question_mark for _ in _val]
        _line = f"{_vars}\n\tAddress {_address}, Value {_val}"
        _lines.append(_line)

    _lines.sort()

    for _line in _lines:
        print(_line)


_aliases()