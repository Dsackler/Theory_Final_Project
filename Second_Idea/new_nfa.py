import json


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
            #get lambda moves
            lambda_set = set()
            for state in current_transition[current]['0']:
                lambda_set = lambda_set.union(NFA.get_lambda_moves(nfa, state))
            current_transition[current]['0'] = current_transition[current]['0'].union(lambda_set)
            lambda_set.clear()
            for state in current_transition[current]['1']:
                lambda_set = lambda_set.union(NFA.get_lambda_moves(nfa, state))
            current_transition[current]['1'] = current_transition[current]['1'].union(lambda_set)
            
            dfa_description['transitions'].update(current_transition)
        todo.append(''.join(current_transition[current]['0']))
        todo.append(''.join(current_transition[current]['1']))

    #Figure out which states are accept states
    for state in dfa_description['transitions']:
        if NFA.is_accept(nfa, state) == True:
            dfa_description['accept_states'].append(''.join(sorted(state)))
        

    #Sort key names and value names
    for state in dfa_description['transitions'].keys():
        
        dfa_description['transitions'][state]['0'] = ''.join(sorted(dfa_description['transitions'][state]['0']))
        if dfa_description['transitions'][state]['0'] == "":
            dfa_description['transitions'][state]['0'] = "Dead state"
        dfa_description['transitions'][state]['1'] = ''.join(sorted(dfa_description['transitions'][state]['1']))
        if dfa_description['transitions'][state]['1'] == "":
            dfa_description['transitions'][state]['1'] = "Dead state"

    print(json.dumps(dfa_description, indent=4, sort_keys=False))
    return dfa_description




# Get accept funciton working
# Test
# Write union nfa's, concat nfa's, star closure
# Test
# https://github.com/neogeny/TatSu for context free grammer parsing for regular expression
