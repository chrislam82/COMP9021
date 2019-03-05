# Written by *** and Eric Martin for COMP9021


def rule_encoded_by(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    values = [int(d) for d in f'{rule_nb:04b}']
    return {(p // 2, p % 2): values[p] for p in range(4)}

    # So there are 0-15 for integers
    # THere are 4 elements to dictionary
    # Each element has 2 possibilities
    # so the total number of possibilities is 2**4 == 16
    # Therefore, it covers all possible dictionaries

def describe_rule(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    rule = rule_encoded_by(rule_nb)
    print('The rule encoded by', rule_nb, 'is: ', rule)
    print()
    print(f'After 0 followed by 0, we draw {str(rule[(0, 0)])}')
    print(f'After 0 followed by 1, we draw {str(rule[(0, 1)])}')
    print(f'After 1 followed by 0, we draw {str(rule[(1, 0)])}')
    print(f'After 1 followed by 1, we draw {str(rule[(1, 1)])}')
    # Dictionaries are not ordered so you cannot print them in order of keys
    # So here, I am doing physically

def describe_rule_test():
    for i in range(16):
        describe_rule(i)

def draw_line(rule_nb, first, second, length):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    "first" and "second" are supposed to be the integer 0 or the integer 1.
    "length" is supposed to be a positive integer (possibly equal to 0).

    
    Draws a line of length "length" consisting of 0's and 1's,
    that starts with "first" if "length" is at least equal to 1,
    followed by "second" if "length" is at least equal to 2,
    and with the remaining "length" - 2 0's and 1's determined by "rule_nb".
    '''
    rule = rule_encoded_by(rule_nb)
    # INSERT YOUR CODE HERE TO PRINT ONE LINE
    for _ in range(length):
        print ('1')

def draw_line_test():
    pass

def uniquely_produced_by_rule(line):
    '''
    "line" is assumed to be a string consisting of nothing but 0's and 1's.

    Returns an integer n between 0 and 15 if the rule encoded by n is the
    UNIQUE rule that can produce "line"; otherwise, returns -1.
    '''
    pass
    # REPLACE pass ABOVE WITH YOUR CODE

'''
    {(0,1):0,(0,1):0,101001}
    01010101001
    dictionary = json.loads(string)


    temp_
    list(dictionaries)
'''

def uniquely_produced_by_rule():
    pass