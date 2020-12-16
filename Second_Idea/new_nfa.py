import copy



class NFA:
    def __init__(self, description):
        self.transitions = description['transitions']
        self.accept_states = description['accept_states']
        self.start = description['start']

    def is_accept(self, string):
        for symbol in string:
            if symbol in self.accept_states:
                return True
        return False

    def get_lambda_moves(self, state):
        for label in self.transitions[state].keys():
            if label == 'λ':
                return set(self.transitions[state]['λ'])
            else:
                continue
        return set()

    def transition(self, state, symbol):
        if state in self.transitions and symbol in self.transitions[state]:
            return set(self.transitions[state][symbol])
        else:
            return set()
class Helper:
    def sorter(self, dfa_description):
        for state in dfa_description['transitions'].keys():
            dfa_description['transitions'][state]['0'] = ''.join(sorted(dfa_description['transitions'][state]['0']))
            if dfa_description['transitions'][state]['0'] == "":
                dfa_description['transitions'][state]['0'] = "Dead state"
            dfa_description['transitions'][state]['1'] = ''.join(sorted(dfa_description['transitions'][state]['1']))
            if dfa_description['transitions'][state]['1'] == "":
                dfa_description['transitions'][state]['1'] = "Dead state"

    def append_lambda_moves(self, current_transition, current, dfa_description):
        lambda_set = set()
        for state in current_transition[current]['0']:
            lambda_set = lambda_set.union(NFA.get_lambda_moves(self, state))
        current_transition[current]['0'] = current_transition[current]['0'].union(lambda_set)
        lambda_set.clear()
        for state in current_transition[current]['1']:
            lambda_set = lambda_set.union(NFA.get_lambda_moves(self, state))
        current_transition[current]['1'] = current_transition[current]['1'].union(lambda_set)
        dfa_description['transitions'].update(current_transition)
    



def to_dfa(nfa):
    dfa_description = {'transitions': {}, 'accept_states': [], 'start': ''}

    # 1) get start state
    start_state = nfa.start
    if 'λ' in nfa.transitions[start_state].keys():
        start_state = start_state + ''.join(nfa.transitions[start_state]['λ'])
    dfa_description['start'] = ''.join(sorted(start_state))

    # 2) get transitions from start state
    no_repeats = []
    todo = [start_state]
    while len(todo) != 0:
        current = ''.join(sorted(todo.pop()))
        if current in no_repeats:
            continue
        no_repeats.append(current)
        current_transition = {current: {'0': set(), '1': set()}}
        for state in current: 
            #Get 1 and 0 transitions 
            current_transition[current]['0'] = current_transition[current]['0'].union(NFA.transition(nfa, state, '0'))
            current_transition[current]['1'] = current_transition[current]['1'].union(NFA.transition(nfa, state, '1'))
            Helper.append_lambda_moves(nfa, current_transition, current, dfa_description) #get lambda moves
        #append to todo    
        todo.append(''.join(current_transition[current]['0']))
        todo.append(''.join(current_transition[current]['1']))

    #Figure out which states are accept states
    for state in dfa_description['transitions']:
        if NFA.is_accept(nfa, state) == True:
            dfa_description['accept_states'].append(''.join(sorted(state)))
    Helper.sorter(nfa, dfa_description) #Sort key names and value names
    return dfa_description


def star_close(nfa):
    dfa_description = {'transitions': {}, 'accept_states': [], 'start': 'S'}
    dfa_description['accept_states'].append('S')
    dfa_description['transitions']['S'] = {'λ': [nfa.start]}

    dfa_description['transitions'].update(nfa.transitions)

    for state in nfa.transitions:
        if state in nfa.accept_states:
            dfa_description['transitions'][state]['λ'] = ['S']
    return dfa_description
            



def union(nfa1, nfa2):
    dfa_description = {'transitions': {}, 'accept_states': [], 'start': 'S'}

    dfa_description['transitions'].update(nfa1.transitions)
    dfa_description['accept_states'].append(nfa1.accept_states)

    nfa2_copy = copy.deepcopy(nfa2)
    for state in nfa2_copy.transitions:
        old = nfa2_copy.transitions[state]
        del nfa2_copy.transitions[state]
        new = {f'{state}2': old}
        nfa2_copy.transitions.update(new)
    
    inner_transitions = []
    for updated_state in nfa2_copy.transitions:
        for label in nfa2_copy.transitions[updated_state]:
            if len(nfa2_copy.transitions[updated_state][label]) == 1:
                temp = ''.join(nfa2_copy.transitions[updated_state][label])
                nfa2_copy.transitions[updated_state][label] = [f'{temp}2']
            if len(nfa2_copy.transitions[updated_state][label]) > 1:
                for symbol in nfa2_copy.transitions[updated_state][label]:
                    temp = f'{symbol}2'
                    inner_transitions.append(temp)
                    nfa2_copy.transitions[updated_state][label] = inner_transitions

    new_accept_states = [i for i in nfa1.accept_states]
    for state in nfa2_copy.accept_states:
        new_accept_states.append(f'{state}2')
    nfa2_copy.accept_states = new_accept_states

    dfa_description['transitions'].update(nfa2_copy.transitions)
    dfa_description['accept_states'] = nfa2_copy.accept_states
    return dfa_description



def concatenate(nfa1, nfa2):
    dfa_description = {'transitions': {}, 'accept_states': [], 'start': ''}
    dfa_description['transitions'].update(nfa1.transitions) 
    dfa_description['start'] = nfa1.start
    
    nfa2_copy = copy.deepcopy(nfa2)
    for state in nfa2.transitions:
        old = nfa2_copy.transitions[state]
        del nfa2_copy.transitions[state]
        new = {f'{state}2': old}
        nfa2_copy.transitions.update(new)
    
    inner_transitions = []
    for updated_state in nfa2_copy.transitions:
        for label in nfa2_copy.transitions[updated_state]:
            if len(nfa2_copy.transitions[updated_state][label]) == 1:
                temp = ''.join(nfa2_copy.transitions[updated_state][label])
                nfa2_copy.transitions[updated_state][label] = [f'{temp}2']
            if len(nfa2_copy.transitions[updated_state][label]) > 1:
                for symbol in nfa2_copy.transitions[updated_state][label]:
                    temp = f'{symbol}2'
                    inner_transitions.append(temp)
                    nfa2_copy.transitions[updated_state][label] = inner_transitions

    dfa_copy = copy.deepcopy(dfa_description)
    for state in dfa_description['transitions']:
        if state in nfa1.accept_states and 'λ' in dfa_description['transitions'][state]:
            dfa_copy['transitions'][state]['λ'].append(f'{nfa2_copy.start}2')
        if state in nfa1.accept_states and 'λ' not in dfa_description['transitions'][state]:
            dfa_copy['transitions'][state].update({'λ': [f'{nfa2_copy.start}2']})

    
    dfa_copy['transitions'].update(nfa2_copy.transitions)

    for state in nfa2_copy.accept_states:
        dfa_copy['accept_states'].append(f'{state}2')
    return dfa_copy
    
    
    

    


    
    



    







# Get accept funciton working
# Test
# Write union nfa's, concat nfa's, star closure
# Test
# https://github.com/neogeny/TatSu for context free grammer parsing for regular expression
