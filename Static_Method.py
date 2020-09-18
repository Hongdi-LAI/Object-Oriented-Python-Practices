class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def pr():
        print("run")




m = Math.add5(5)

print(m)

Math.pr()

# Staticmethod = function not related to that class. Used for organization purposes 
# (For example, a Calculator class with add, subtract, multiplicate, etc methods). 
# You don't need to create one instance to use it.