class Edge:
    def __init__(self, source, target, label):
        self.source = source
        self.target = target
        self.label = label

    def get_source(self):
        return self.source

    def get_target(self):
        return self.target

    def get_label(self):
        return self.label
