from Second_Idea.edge import Edge


# https://github.com/meghdadFar/sregex/blob/master/src/s/reg/ex/State.java
# https://github.com/meghdadFar/sregex/blob/master/src/s/reg/ex/NFA.java
# https://github.com/meghdadFar/sregex/blob/master/src/s/reg/ex/Sregex.java
# https://github.com/meghdadFar/sregex/blob/master/src/s/reg/ex/Edge.java


class State:
    def __init__(self, acceptState, outgoing, incoming):
        self.accept_state = accept_state  # bool
        self.outgoing = outgoing  # list of outgoing edges
        self.incoming = incoming  # list of incoming edges

    def is_accept(self):
        self.accept_state

    def make_accept(self):
        self.accept_state = True

    def make_not_accept(self):
        self.accept_state = False

    def get_outgoing_edges(self):
        return self.outgoing

    def add_outgoing_edge(self, edge):
        self.outgoing.append(edge)

    def get_incoing_edges(self):
        return self.incoming

    def add_incoming_edge(self, edge):
        self.incoming.append(edge)


def find_source(self, label):
    source = State()
    for in_link in self.incoming:
        if in_link == label:
            source = in_link.Edge.get_source()
    return source


def remove_outgoing(self, label):
    for out_link in self.outgoing:
        if out_link.Edge.get_label() == label:
            self.outgoing.remove(out_link.Edge.get_label())
