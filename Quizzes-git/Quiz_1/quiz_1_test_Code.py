'''
We consider as alphabet a set of digits. # alphabet are the numbers

We accept partial transition functions (that is, there might be no transition
for a given state and symbol).

With the accepts() function, we will deal with a single accept state rather than
a set of accept states.

In the test cases below, transitions_2 is the wikipedia example
(with 'S1' and 'S2' renamed as 'state_1' and 'state_2', respectively),
so the automaton that with 'state_1' as both initial and unique accept state,
accepts words with an even number of occurrences of 0's.

'''


def describe_automaton(transitions):
    '''
    The output is produced with the print() function.
    
    >>> transitions_1 = {('q0', 0): 'q1', ('q1', 1): 'q0'}
    >>> describe_automaton(transitions_1)
    When in state "q0" and processing "0", automaton's state becomes "q1".
    When in state "q1" and processing "1", automaton's state becomes "q0".

    >>> transitions_2 = {('state_1', 0): 'state_2', ('state_1', 1): 'state_1',\
                         ('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
    >>> describe_automaton(transitions_2)
    When in state "state_1" and processing "0", automaton's state becomes "state_2".
    When in state "state_1" and processing "1", automaton's state becomes "state_1".
    When in state "state_2" and processing "0", automaton's state becomes "state_1".
    When in state "state_2" and processing "1", automaton's state becomes "state_2".
    '''
    print ("ready to print!")
    for key in transitions:
        print ('When in state \"'+key[0]+'\" and processing \"'+str(key[1])+'\", automaton\'s state becomes \"'+transitions[key]+'\".')
        #print (f'When in state \" {key[0]} \" and processing \"' {str(key[1])} '\", automaton\'s state becomes \"' {transitions[key]} '\".')
    print ('')

def describe_automaton_tests():
	#describe_automaton({}) # Empty dictionary
	#describe_automaton({('q0', 0): 'q1', ('q1', 1): 'q0', ('q1', 2): 'q0', ('q1', 3): 'q0', ('q1', 4): 'q0', ('q1', 5): 'q0'}) # more than 2
	#print ('-----')
	#describe_automaton({('q0', 0): 'q1', ('q0', 0): 'q1', ('q0', 0): 'q1', ('q0', 0): 'q2', ('q0', 0): 'q1'}) # not sure if this is valid but python ignores
		#identical key-value pairs
	#print ('-----')
	pass

def transitions_as_dict(transitions_as_list):
	'''
	transitions = {}
	for element in transitions_as_list:
		key, new_state = element.split(':')
		state, number = key[0].split(',')
		transitions[(state, int(number))] = new_state
	return transitions
	'''
	'''
    transitions_as_list is a list of strings of the form 'state_1,symbol:state_2'
    where 'state_1' and 'state_2' are words and 'symbol' is one of the 10 digits.
    We assume that there is at most one 'state_2' for given 'state_1' and 'symbol'.
    
    >>> transitions_as_dict(['q0,0:q1', 'q1,1:q0'])
    {('q0', 0): 'q1', ('q1', 1): 'q0'}
    >>> transitions_as_dict(['state_1,0:state_2', 'state_1,1:state_1',\
                             'state_2,0:state_1', 'state_2,1:state_2'])
    {('state_1', 0): 'state_2', ('state_1', 1): 'state_1', \
('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
    '''

	transitions = {}
	for element in transitions_as_list:
		split_Element = element.split(':')
		split_Key = split_Element[0].split(',')
		transitions[(split_Key[0], int(split_Key[1]))] = split_Element[1]
	return transitions

def transitions_as_dict_test():
	try:
		assert (transitions_as_dict([]) == {})
		print (1)
		assert (transitions_as_dict(['q0,0:q1']) == {('q0', 0): 'q1'})
		print (2)
		assert (transitions_as_dict(['q0,0:q1', 'q1,1:q0']) == {('q0', 0): 'q1', ('q1', 1): 'q0'})
		print (3)
		assert (transitions_as_dict(['q0,0:q1', 'q1,1:q0', 'q1,1:q0', 'q1,1:q0']) == {('q0', 0): 'q1', ('q1', 1): 'q0'})
		print (4)
		assert (transitions_as_dict(['q0,9:q1']) == {('q0', 9): 'q1'})
		print (5)
		assert (transitions_as_dict(['qwerty,0:q1']) == {('qwerty', 0): 'q1'})
		print (6)
		assert (transitions_as_dict(['q0,9:q1', 'qwerty,0:q1']) == {('q0', 9): 'q1', ('qwerty', 0): 'q1'})
		print (7)
		print ("PASSED transitions_as_dict() testing")
	except:
		print ("failed transitions_as_dict() testing")

def accepts(transitions, word, initial_state, accept_state):
    '''
    Starting in 'initial_state', if the automaton can process with 'transitions'
    all symbols in 'word' and eventually reach 'accept_state', then the function
    returns True; otherwise it returns False.
    
    >>> transitions_1 = {('q0', 0): 'q1', ('q1', 1): 'q0'} 
    >>> accepts(transitions_1, '00', 'q0', 'q1')
    False
    >>> accepts(transitions_1, '2', 'q0', 'q0')
    False
    >>> accepts(transitions_1, '0101010', 'q0', 'q0')
    False
    >>> accepts(transitions_1, '01010101', 'q0', 'q0')
    True
    >>> not accepts(transitions_1, '01', 'q0', 'q1') and\
        accepts(transitions_1, '010', 'q0', 'q1')
    True

    >>> transitions_2 = {('state_1', 0): 'state_2', ('state_1', 1): 'state_1',\
                         ('state_2', 0): 'state_1', ('state_2', 1): 'state_2'}
    >>> accepts(transitions_2, '011', 'state_1', 'state_1')
    False
    >>> accepts(transitions_2, '001110000', 'state_1', 'state_1')
    True
    >>> accepts(transitions_2, '1011100101', 'state_1', 'state_1')
    True
    >>> accepts(transitions_2, '10111000101', 'state_1', 'state_1')
    False
    '''
    current_state = initial_state
    for char in word:
        if (current_state, int(char)) in transitions: # checking if key(tuple) in dictionary
            current_state = transitions[(current_state, int(char))] # if so, change the state
        else:
            return False
    return current_state == accept_state

def accepts_test():

# def accepts(transitions, word, initial_state, accept_state):

# try passing in empty transotions
# try passing in empty words

	try:
		# -------------------------------------------------------
		transitions_1 = {('q0', 0): 'q1', ('q1', 1): 'q0'} # simple case

		# -------------------------------------------------------
		transitions_2 = {('q0', 0): 'q1', ('q1', 1): 'q2', ('q2', 2): 'q0'} # transitions more than 2, and of integers other than 01
		assert accepts(transitions_2, '', 'q1', 'q1') == True ####################<======== # length 0, valid
		assert accepts(transitions_2, '', 'q4', 'q4') == True ####################<======== # length 0, 
			# whats meant to happen here???

		assert accepts(transitions_2, '1', 'q1', 'q2') == True # length 1, valid state
		assert accepts(transitions_2, '1', 'q1', 'q0') == False # length 1, False final

		assert accepts(transitions_2, '1', 'q4', 'q1') == False # Invalid initial
		assert accepts(transitions_2, '1', 'q1', 'q9') == False # Invalid final
		assert accepts(transitions_2, '4', 'q1', 'q1') == False # Invalid word

		assert accepts(transitions_2, '012012012', 'q0', 'q0') == True
		assert accepts(transitions_2, '', 'q1', 'q1') == True
		# -------------------------------------------------------
		transitions_3 = {} # an empty transitions
        assert accepts(transitions_3, '', 'q1', 'q1') == True
        assert accepts(transitions_3, '', 'q9', 'q9') == True
        assert accepts(transitions_3, '', 'q1', 'q2') == False
        assert accepts(transitions_3, '1', 'q1', 'q1') == False
        assert accepts(transitions_3, '112312312', 'q1', 'q1') == False
        

		print ("PASSED accepts()")        
	except:
		print ("FAILED accepts()")

        # w
#if __name__ == '__main__':
#    import doctest
#    doctest.testmod()
