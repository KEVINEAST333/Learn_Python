class math:

    def __init__(self):
        pass

    def max(self, a, b):
        if a >= b:
            return a
        else:
            return b

ma = math()
print ma.max(12, 3)
