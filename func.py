"""
test for return function
"""
def hey(name = "MR.zhou"):
    def greet():
        return "this is greet function"

    def welcome():
        return "this is welcome function"

    if name == "greet" :
        return greet
    else:
        return welcome

if __name__ == "__main__":
    cc = hey()
    print("cc:",cc)
    print("output:",cc())
