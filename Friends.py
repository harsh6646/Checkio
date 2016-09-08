class Friends:
    def __init__(self, connections):
        self.connections = [list(x) for x in connections]

    def add(self, connection):
        connection = list(connection)
        check = True
        for x in self.connections:
            if connection[0] in x and connection [1] in x:
                check = False
        if check:
            self.connections.append(connection)
        return check

    def remove(self, connection):
        connection = list(connection)
        check = False
        value = 0
        for x in range(len(self.connections)):
            if connection[0] in self.connections[x] and connection[1] in self.connections[x]:
                value = x
                check = True
        if check:
            del self.connections[value]
        return check

    def names(self):
        name = []
        for x in self.connections:
            for y in x:
                if y not in name:
                    name.append(y)
        return set(name)

    def connected(self, name):
        names = []
        for x in self.connections:
            if name in x:
                print(x)
                for y in x:
                    if y != name and y not in names:
                        names.append(y)
        print(set(names))
        return set(names)
        



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
