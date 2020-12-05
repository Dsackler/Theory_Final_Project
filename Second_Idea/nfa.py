from Second_Idea.state import State
from Second_Idea.edge import Edge


class NFA:
    def __init__(self, current_state, initial_state):
        self.current_state = current_state
        self.initial_state = initial_state

    def get_initial_state(self):
        return self.initial_state

    def get_current_state(self):
        return self.current_state

    def remove_initial_state(self):
        self.initial_state = None

    def concat(self, label):
        next_state = State.State()
        e = Edge.Edge(self.currentState, next_state, label)
        self.current_state.State.add_outgoing_edge(e)
        next_state.State.add_incoming_edge(e)
        next_state.State.make_accept()
        self.current_state.State.make_not_accept()
        self.current_state = next_state

    def union(self, temp):
        new_state = State.State()
        epsilon = Edge(temp, new_state, "E")
        temp.
