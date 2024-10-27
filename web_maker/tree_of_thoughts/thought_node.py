class ThoughtNode:
    def __init__(self, thought, children=None):
        self.thought = thought
        self.children = children or []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def get_children(self):
        return self.children

    def get_thought(self):
        return self.thought

    def set_thought(self, thought):
        self.thought = thought

    def __iter__(self):
        yield self
        for child in self.children:
            yield from child

    def __repr__(self):
        return f"ThoughtNode({self.thought}, {self.children})"

    def __eq__(self, other):
        return self.thought == other.thought and self.children == other.children

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.thought) + hash(self.children)