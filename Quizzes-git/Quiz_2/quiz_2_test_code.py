# Written by *** and Eric Martin for COMP9021


def rule_encoded_by(rule_nb):
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    values = [int(d) for d in f'{rule_nb:04b}'] #rule number converted into bin with 4 digit. So, stores as int in list for each digit in binary
    return {(p // 2, p % 2): values[p] for p in range(4)}
    # p=0 ==> (0, 0)
    # p=1 ==> (0, 1)
    # p=2 ==> (1, 0)
    # p=3 ==> (1, 1)
    # so always same order

    # So there are 0-15 for integers
    # THere are 4 elements to dictionary
    # Each element has 2 possibilities
    # so the total number of possibilities is 2**4 == 16
    # Therefore, it covers all possible dictionaries

def describe_rule(rule_nb): # All inputs are ints
    '''
    "rule_nb" is supposed to be an integer between 0 and 15.
    '''
    rule = rule_encoded_by(rule_nb)
    print('The rule encoded by', rule_nb, 'is: ', rule)
    print()
    for (bit_1, bit_2) in rule:
        print(f'After {str(bit_1)} followed by {str(bit_2)}, we draw {str(rule[(bit_1, bit_2)])}')
'''
    print(f'After 0 followed by 0, we draw {str(rule[(0, 0)])}')
    print(f'After 0 followed by 1, we draw {str(rule[(0, 1)])}')
    print(f'After 1 followed by 0, we draw {str(rule[(1, 0)])}')
    print(f'After 1 followed by 1, we draw {str(rule[(1, 1)])}')
    # Dictionaries are not ordered so you cannot print them in order of keys
    # So here, I am doing physically
    # Actually, fn above I believe returns always in the same order, so technically i could use non-hardcoded, but doesnt matter for quiz
'''

def describe_rule_test():
    for i in range(16):
        describe_rule(i)




def draw_line(rule_nb, first, second, length): # All inputs are ints
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

    # So the ways I thought of doing this would be either to generate a list or something first then unpack, or print one at a time like this
        # Much more lazy but so bad. write better later
    # all of the arguments are ints

    if length > 0: 
        print (first, end='')
    if length > 1:
        print (second, end='')
    for _ in range(length - 2): # to account for the first 2
        print (rule[first, second], end='') # just printing the following digit
        first, second = second, rule[(first, second)] # moving everything up by one
    print () # just to create a newline
# drawline now works, just need to account for edge cases of length = 0, 1, 2

def draw_line_test():
    draw_line(10, 1, 0, 0)
    draw_line(10, 1, 0, 1)
    draw_line(10, 1, 0, 2)
    draw_line(10, 1, 0, 3)




def uniquely_produced_by_rule(line): # All inputs are str
    '''
    "line" is assumed to be a string consisting of nothing but 0's and 1's.

    Returns an integer n between 0 and 15 if the rule encoded by n is the
    UNIQUE rule that can produce "line"; otherwise, returns -1.
    '''
    
    # REPLACE pass ABOVE WITH YOUR CODE

    # So lazy way is to generate a list of possible rules, access rules then pop if not a valid rule

    if len(line) < 6: # Need at minimum the initial 2 digits + 4 digits to get 4 different keys
        return -1 # also to prevent any index errors

    line_dictionary = {} # Empty dictionary (we fill in as we go)
    for i in range(len(line) - 2): # To account for edges
        first, second, third = int(line[i]), int(line[i+1]), int(line[i+2])
        if (first, second) in line_dictionary.keys(): # checking if key is in existing dictionary
            if line_dictionary[(first, second)] != third:
                return -1
        line_dictionary[(first,second)] = third # if it isn't, then we store key value pair
    if len(line_dictionary.keys()) != 4: # dictionary is incomplete; does not have 4 keys hence it is not unique
        return -1 # don't think you actually need this. if dictionary is incomplete, it will still return false
        # The alternative is just to return -1 after the last for loop, because if result is not in rules, then it will run that last line
    for i in range(16): # now comparing dictionaries
        if line_dictionary == rule_encoded_by(i):
            return i
    # Alternative is you can always sort the diction to make sure it's in order, then join to form bin, then int(bin, 2) to get rule
    # See dictionary compare below. Dont need to sort
'''
    {(0,1):0,(0,1):0,101001}
    01010101001
    dictionary = json.loads(string)


    temp_
    list(dictionaries)
'''

def uniquely_produced_by_rule_test():
    
    print (uniquely_produced_by_rule(''))
    print (uniquely_produced_by_rule('0'))
    print (uniquely_produced_by_rule('01'))
    print (uniquely_produced_by_rule('011'))
    print (uniquely_produced_by_rule('0111'))
    print (uniquely_produced_by_rule('01111'))
    print ('...\n')
    

    print (uniquely_produced_by_rule('011111'))
    print (uniquely_produced_by_rule('0111111'))
    print (uniquely_produced_by_rule('1100110011'))
    print (uniquely_produced_by_rule('0010001'))
    print (uniquely_produced_by_rule('11111111'))

def dictionary_compare():
    # Checking in case a different ordered dictionary can evaluate or not. It should, since dicts are unordered
    dict_1 = {'a':1, 'b':2} #True, so doesnt matter if in different order. Dont need to sort
    dict_2 = {'b':2, 'a':1}
    dict_3 = {'a':1, 'b':2, 'c':3}
    dict_4 = {'a':1, 'c':3}
    dict_5 = {'a':1}
    print (dict_1 == dict_2) #True
    print (dict_1 is dict_2) #False # Actually not the same!
    print (dict_1 == dict_3) #False
    print (dict_1 == dict_4) #False
    print (dict_3 == dict_4) #False
    print (dict_5 == dict_1) #False
    # Yep, so order doesnt matter, but they have to have exactly the same key-value pairs

#uniquely_produced_by_rule_test()
#dictionary_compare()
#describe_rule_test()