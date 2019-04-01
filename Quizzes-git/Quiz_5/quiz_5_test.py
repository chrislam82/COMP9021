# Prompts the user for a positive integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived positive integer that codes the set of running sums
# ot the members of S when those are listed in increasing order.
#
# Written by *** and Eric Martin for COMP9021


from itertools import accumulate
import sys

try:
    encoded_set = int(input('Input a positive integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

def int_to_encoded_list(integer): # Since sets are unordered, I prefer lists
# My own function which can be used in both, pretty simple
    #  4  3  2  1  0 <-- Index
    #  2 -2  1 -1  0 <-- Encoding
    #  1  1  0  0  1 <-- Bin
    # new_digit = digit + 1
    # new_digit // 2 determines value
    # new_digit % 2 determines sign (if 1, then positive, if 0, determines negative)
    encoded_list = []
    integer_in_bin = bin(integer)[2:] # since we dont need 0b
    length = len(integer_in_bin) # so we dont have to recalculate every time

    for digit in range(length): # have to minus either way later, so doesnt matter if we count increasing or decreasing
        if integer_in_bin[digit] == '1':
            temp_value = (length - int(digit)) // 2 # So actual index = (length - 1) - digit, but then we also need to +1 for encoding
            if (length - int(digit)) % 2 == 0:
                temp_value *= -1
            encoded_list.append(temp_value)
    return sorted(encoded_list)

# POSSIBLY DEFINE OTHER FUNCTIONS
def display_encoded_set(encoded_set):
    # encoded_set is the input (an int > 0)
    # 1st fn simply does the conversion
    encoded_list = int_to_encoded_list(encoded_set)
    print ('{', end = '')
    for element in encoded_list:
        if element != encoded_list[-1]:
            print (element, end = ', ')
        else:
            print (element, end = '')
    print('}')

def code_derived_set(encoded_set):
    # encoded_set is the input (an int > 0)
    # So basically:
        # Encoded_set --> Set specified in Q1
    # Using elements in set from Q1...
        # Create a new set iterating elements, adding one at a time and adding their sum to a new set
        # Find the value that would generate this new set and return in code_derived_set
    encoded_running_sum = 0
    encoded_list = int_to_encoded_list(encoded_set)
    running_sum_list = accumulate(encoded_list)

    # Now we just have to use this to find the original number
    # Given a value, original index value = abs(value * 2 + 1), -1 if postive
    # then simply add 2 ** index value
    for element in set(running_sum_list):
        index_value = abs(element) * 2
        if element < 0:
            index_value -= 1
        encoded_running_sum += 2**index_value

    return encoded_running_sum

print('The encoded set is: ', end = '')
display_encoded_set(encoded_set)
encoded_running_sum = code_derived_set(encoded_set)
print('The derived encoded set is: ', end = '')
display_encoded_set(encoded_running_sum)
print('  It is encoded by:', encoded_running_sum)
    
