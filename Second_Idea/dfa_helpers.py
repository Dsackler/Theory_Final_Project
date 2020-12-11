from new_nfa import NFA


def sorter(dfa_description):
    for state in dfa_description['transitions'].keys():
        dfa_description['transitions'][state]['0'] = ''.join(sorted(dfa_description['transitions'][state]['0']))
        if dfa_description['transitions'][state]['0'] == "":
            dfa_description['transitions'][state]['0'] = "Dead state"
        dfa_description['transitions'][state]['1'] = ''.join(sorted(dfa_description['transitions'][state]['1']))
        if dfa_description['transitions'][state]['1'] == "":
            dfa_description['transitions'][state]['1'] = "Dead state"


def find_lambda_moves(current_transition, current, dfa_description, nfa):
    lambda_set = set()
    for state in current_transition[current]['0']:
        lambda_set = lambda_set.union(NFA.get_lambda_moves(nfa, state))
    current_transition[current]['0'] = current_transition[current]['0'].union(lambda_set)
    lambda_set.clear()
    for state in current_transition[current]['1']:
        lambda_set = lambda_set.union(NFA.get_lambda_moves(nfa, state))
    current_transition[current]['1'] = current_transition[current]['1'].union(lambda_set)
    dfa_description['transitions'].update(current_transition)