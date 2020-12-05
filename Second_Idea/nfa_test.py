from new_nfa import NFA, to_dfa


test_machines = {
    'div2': {
        'description': {
            'transitions': {
                'S': {
                    '0': ['S', 'A'],
                    '1': ['S']
                }
            },
            'accept_states': [],
            'start': 'S'
        },
        'accepts': ['100'],
        'rejects': ['001']
    },
    'lambda_test': {
        'description': {
            'transitions': {
                'S': {
                    'λ': ['A', 'C']
                },
                'A': {
                    '0': ['B'],
                    '1': ['A']
                },
                'C': {
                    '0': ['C'],
                    '1': ['D']
                },
                'B': {
                    '0': ['A'],
                    '1': ['B']
                },
                'D': {
                    '0': ['D'],
                    '1': ['C']
                }
            },
            'accept_states': ['A', 'C'],
            'start': 'S'
        },
        'accepts': [],
        'rejects': ['01', '10']
    }
}


def test_transition():
    nfa = NFA(test_machines['div2']['description'])
    assert nfa.transition('S', '1') == ['S']
    assert nfa.transition('A', '0') == []

    # VIM bindings


def test_lambda():
    nfa = NFA(test_machines['lambda_test']['description'])
    assert to_dfa(nfa) == [('S', ['A', 'C'])]
