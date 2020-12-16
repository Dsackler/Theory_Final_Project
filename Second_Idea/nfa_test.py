from new_nfa import NFA, to_dfa, union, star_close, concatenate


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
    },
    'machine4': {
        'description': {
            'transitions': {
                'A': {
                    '0': ['B']
                },
                'B': {
                    '1': ['C']
                },
                'C': {
                    '0': ['D']
                },
                'D': {
                    '0': ['D'],
                    '1': ['E']
                },
                'E': {
                    '0': ['D'],
                    '1': ['F']
                },
                'F': {
                    '0': ['F'],
                    '1': ['F']
                }
            },
            'accept_states': ['F'],
            'start': 'A'
        }
    },
    'machine5': {
        'description': {
            'transitions': {
                'A': {
                    '1': ['B']
                },
                'B': {
                    'λ': ['C'],
                    '0': ['D']
                },
                'C': {

                },
                'D': {

                }
            },
            'accept_states': ['C', 'D'],
            'start': 'A'
        }
    }
}


def test_transition():
    nfa = NFA(test_machines['div2']['description'])
    assert nfa.transition('S', '1') == {'S'}
    assert nfa.transition('A', '0') == set()

    # VIM bindings


def test_to_dfa():
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
    nfa1 = NFA(test_machines['machine1']['description'])
    assert to_dfa(nfa1) == {"transitions": {
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

    nfa2 = NFA(test_machines['machine2']['description'])
    assert to_dfa(nfa2) == {"transitions": {
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

    nfa3 = NFA(test_machines['machine3']['description'])
    assert to_dfa(nfa3) == {"transitions": {
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

def test_concat():
    nfa1 = NFA(test_machines['machine4']['description'])
    nfa2 = NFA(test_machines['machine5']['description'])
    assert concatenate(nfa1, nfa2) == {'transitions': {
            'A': {'0': ['B']}, 
            'B': {'1': ['C']}, 
            'C': {'0': ['D']}, 
            'D': {'0': ['D'], '1': ['E']}, 
            'E': {'0': ['D'], '1': ['F']}, 
            'F': {'0': ['F'], '1': ['F'], 'λ': ['A2']}, 
            'A2': {'1': ['B2']}, 
            'B2': {'λ': ['C2'], '0': ['D2']}, 
            'C2': {}, 
            'D2': {}
        }, 
        'accept_states': ['C2', 'D2'], 
        'start': 'A'
    }
    assert concatenate(nfa2, nfa1) == {'transitions': {
            'A': {'1': ['B']}, 
            'B': {'λ': ['C'], '0': ['D']}, 
            'C': {'λ': ['A2']}, 
            'D': {'λ': ['A2']}, 
            'A2': {'0': ['B2']}, 
            'B2': {'1': ['C2']}, 
            'C2': {'0': ['D2']}, 
            'D2': {'0': ['D2'], '1': ['E2']}, 
            'E2': {'0': ['D2'], '1': ['F2']}, 
            'F2': {'0': ['F2'], '1': ['F2']}
        }, 
        'accept_states': ['F2'], 
        'start': 'A'
    }