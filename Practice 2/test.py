class A:
    a = 'a'

    def __getitem__(self, key):
        return getattr(self, key)

aa = A()

print(aa['a'])