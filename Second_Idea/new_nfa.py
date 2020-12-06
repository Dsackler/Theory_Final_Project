
import json
EPSILON = ""


class NFA:
    def __init__(self, description):
        self.transitions = description['transitions']
        self.accept_states = description['accept_states']
        self.start = description['start']

    def is_accept(self, string):
        return False
        # return bool

    def get_lambda_moves(self, state):
        for label in self.transitions[state].keys():
            if label == 'λ':
                return self.transitions[state]['λ']

    def transition(self, state, symbol):
        # deal with nulls. return empty list
        if state in self.transitions and symbol in self.transitions[state]:
            return self.transitions[state][symbol]
        else:
            return []
            # return set of states


def to_dfa(nfa):
    dfa_description = {'transitions': {}, 'accept_states': [], 'start': ''}
    # first, get all lambda moves from each state
    lambda_moves_from_states = []
    for state in nfa.transitions.keys():
        if 'λ' in nfa.transitions[state].keys():
            lambda_moves_from_states.append(
                (state, NFA.get_lambda_moves(nfa, state)))

    # 1) get start state
    start_state = nfa.start
    if 'λ' in nfa.transitions[start_state].keys():
        start_state = start_state + ''.join(nfa.transitions[start_state]['λ']) # the ''.join turns list elements into a string
    dfa_description['start'] = start_state

    # 2) get transitions from start state
    no_repeats = []
    todo = [start_state]
    while len(todo) != 0:
        current = todo.pop()
        if current in no_repeats:
            continue
        no_repeats.append(current)
        current_transition = {current: {'0': '', '1': ''}}
        for state in current:
            zero_label = ''.join(list(set(current_transition[current]['0'] + ''.join(NFA.transition(nfa, state, '0')))))
            one_label = ''.join(list(set(current_transition[current]['1'] + ''.join(NFA.transition(nfa, state, '1')))))
            current_transition[current]['0'] = zero_label
            current_transition[current]['1'] = one_label
            todo.append(zero_label)
            todo.append(one_label)
            dfa_description['transitions'].update(current_transition) #this is just to test it. Dont update dfa_description until you get lambda moves from each state
    #print(f'{dfa_description} + dfa transition')
    print(json.dumps(dfa_description, indent=4, sort_keys=False))
        
    # 3) get lambda moves from each transition
    # for index in dfa_description['transitions'][start_transition]['0']:
    #     for state in lambda_moves_from_states:
    #         if dfa_description['transitions']['SAC']['0'][0] == lambda_moves_from_states[state][0]:
    #             dfa_description['transitions'][start_transition]['0'] = dfa_description['transitions'][start_transition]['0'] + lambda_moves_from_states[state][0]
    #         if dfa_description['transitions']['SAC']['1'][0] == lambda_moves_from_states[state][0]:
    #             dfa_description['transitions'][start_transition]['1'] = dfa_description['transitions'][start_transition]['1'] + lambda_moves_from_states[state][0]

    # dfa_description['transitions'] = start_transition
    return lambda_moves_from_states


# Get accept funciton working
# Test
# Write union nfa's, concat nfa's, star closure
# Test
# https://github.com/neogeny/TatSu for context free grammer parsing for regular expression
