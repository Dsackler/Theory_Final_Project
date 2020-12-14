from new_nfa import NFA, to_dfa, union, star_close


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
        }
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
        }
    },
    'machine1': {
        'description': {
            'transitions': {
                'H': {
                    '0': ['I']
                },
                'I': {
                    '0': ['J'],
                    'λ': ['K']
                },
                'J': {
                    '0': ['K']
                },
                'K': {
                    '0': ['K'],
                    '1': ['K']
                }
                
            },
            'accept_states': ['K'],
            'start': 'H'
        }
    },
    'machine2': {
        'description': {
            'transitions': {
                'A': {
                    '1': ['B']
                },
                'B': {
                    '0': ['B'],
                    '1': ['B', 'C']
                },
                'C': {
                    
                }
                
            },
            'accept_states': ['C'],
            'start': 'A'
        }
    },
    'machine3': {
        'description': {
            'transitions': {
                'A': {
                    'λ': ['E', 'F', 'B']
                },
                'E': {
                    '0': ['E'],
                    '1': ['F']
                },
                'F': {
                    '0': ['E'],
                    '1': ['F']
                },
                'B': {
                    '0': ['B'],
                    '1': ['C']
                },
                'C': {
                    '0': ['B'],
                    '1': ['C']
                }
            },
            'accept_states': ['C', 'E'],
            'start': 'A'
        }
    }
}


def test_transition():
    nfa = NFA(test_machines['div2']['description'])
    assert nfa.transition('S', '1') == {'S'}
    assert nfa.transition('A', '0') == set()

    # VIM bindings


def test_lambda():
    nfa = NFA(test_machines['lambda_test']['description'])
    assert to_dfa(nfa) == {
    "transitions": {
        "ACS": {
            "0": "BC",
            "1": "AD"
        },
        "AD": {
            "0": "BD",
            "1": "AC"
        },
        "AC": {
            "0": "BC",
            "1": "AD"
        },
        "BC": {
            "0": "AC",
            "1": "BD"
        },
        "BD": {
            "0": "AD",
            "1": "BC"
        }
    },
    "accept_states": [
        "ACS",
        "AD",
        "AC",
        "BC"
    ],
    "start": "ACS"
}

def test_machine1():
    nfa = NFA(test_machines['machine1']['description'])
    assert to_dfa(nfa) == {"transitions": {
            "H": {
                "0": "IK",
                "1": "Dead state"
            },
            "IK": {
                "0": "JK",
                "1": "K"
            },
            "K": {
                "0": "K",
                "1": "K"
            },
            "JK": {
                "0": "K",
                "1": "K"
            }
        },
        "accept_states": [
            "IK",
            "K",
            "JK"
        ],
        "start": "H"
    }

def test_machine2():
    nfa = NFA(test_machines['machine2']['description'])
    assert to_dfa(nfa) == {"transitions": {
            "A": {
                "0": "Dead state",
                "1": "B"
            },
            "B": {
                "0": "B",
                "1": "BC"
            },
            "BC": {
                "0": "B",
                "1": "BC"
            }
        },
        "accept_states": [
            "BC"
        ],
        "start": "A"
    }

def test_machine3():
    nfa = NFA(test_machines['machine3']['description'])
    assert to_dfa(nfa) == {"transitions": {
            "ABEF": {
                "0": "BE",
                "1": "CF"
            },
            "CF": {
                "0": "BE",
                "1": "CF"
            },
            "BE": {
                "0": "BE",
                "1": "CF"
            }
            
        },
        "accept_states": [
            "ABEF",
            "CF",
            "BE"
            
        ],
        "start": "ABEF"
    }

def test_union():
    nfa1 = NFA(test_machines['machine3']['description'])
    nfa2 = NFA(test_machines['machine2']['description'])
    assert union(nfa1, nfa2) == {'transitions': {
            'A': {'λ': ['E', 'F', 'B']}, 
            'E': {'0': ['E'], '1': ['F']}, 
            'F': {'0': ['E'], '1': ['F']}, 
            'B': {'0': ['B'], '1': ['C']}, 
            'C': {'0': ['B'], '1': ['C']}, 
            'A2': {'1': ['B2']}, 
            'B2': {'0': ['B2'], '1': ['B2', 'C2']}, 
            'C2': {}
        }, 
        'accept_states': ['C', 'E', 'C2'], 
        'start': 'S'
    }

def test_kleen_closure():
    nfa = NFA(test_machines['machine3']['description'])
    assert star_close(nfa) == {'transitions': {
            'S': {'λ': ['A']}, 
            'A': {'λ': ['E', 'F', 'B']}, 
            'E': {'0': ['E'], '1': ['F'], 'λ': ['S']}, 
            'F': {'0': ['E'], '1': ['F']}, 
            'B': {'0': ['B'], '1': ['C']}, 
            'C': {'0': ['B'], '1': ['C'], 'λ': ['S']}
        }, 
        'accept_states': ['S'], 
        'start': 'S'
    }