# static classes (don't change anything)
# not specific to the instance

class Math:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("run")



print(Math.add10(5))
Math.pr()

