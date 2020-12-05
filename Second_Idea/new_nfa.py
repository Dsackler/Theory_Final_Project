
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

    # first, get all lambda moves from each state
    lambda_moves_from_states = []
    for state in nfa.transitions.keys():
        if 'λ' in nfa.transitions[state].keys():
            lambda_moves_from_states.append(
                (state, NFA.get_lambda_moves(nfa, state)))
    # 1) get start state
    start_state = nfa.start
    if 'λ' in nfa.transitions[start_state].keys():
        # the ''.join turns list elements into a string
        start_state = start_state + ''.join(nfa.transitions[start_state]['λ'])
    print(start_state)
    # 2) get transitions from start state
    # 3) get lambda moves from each transition

    return lambda_moves_from_states


# Get accept funciton working
# Test
# Write union nfa's, concat nfa's, star closure
# Test
# https://github.com/neogeny/TatSu for context free grammer parsing for regular expression
