class animal:
    pass

class pets(animal):
    pass

class dog(pets):
    @staticmethod
    def show():
        print(" bow bow")

d = dog
d.show()

