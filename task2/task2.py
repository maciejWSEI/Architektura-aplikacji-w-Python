class Powers:
    def __init__(self, a, n):
        self.a = a
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration

        value = self.a ** self.current
        self.current += 1
        return value
    

for x in Powers(2, 5):
    print(x)
