'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false

'''

dfa_state = [
    {'space': 0, 'number': 1},
    {'point': 2, 'number' : 1},
    {'number': 2, 'space' : 3},
    {'space' : 3}
]


def valid_number(str_to_valid):
    current_dict = dfa_state[0]
    key = None
    for ii in str_to_valid:
        if (ii >= '0' and ii <= "9"):
            key = "number"
        elif (ii == '.'):
            key = 'point'
        elif (ii == ' '):
            key = 'space'
        else:
            key = 'Unknown'
        if key in current_dict.keys():
            current_dict = dfa_state[current_dict[key]]
        else:
            return False
    if (key == None):
        return False
    return True

print (valid_number("0"))
print (valid_number(" 0.1 "))
print (valid_number("abc"))
print (valid_number("1 a"))
