class calculator:
    def __init__(self, vector) -> None:
        self.vector = vector

    # your code here
    def __add__(self, object) -> None:
        if type(object) is float or type(object) is int:
            for i in range(len(self.vector)):
                self.vector[i] = self.vector[i] + object
        elif type(object) is list:
            for i in range(len(self.vector)):
                self.vector[i] = self.vector[i] + object[i]

        print(self.vector)

        # for n in self.vector:
        #     n +

    # your code here
    def __mul__(self, object) -> None:
        if type(object) is float or type(object) is int:
            for i in range(len(self.vector)):
                self.vector[i] = self.vector[i] * object
        elif type(object) is list:
            for i in range(len(self.vector)):
                self.vector[i] = self.vector[i] * object[i]

        print(self.vector)

    # #your code here
    def __sub__(self, object) -> None:
        if type(object) is float or type(object) is int:
            for i in range(len(self.vector)):
                self.vector[i] = self.vector[i] - object
        elif type(object) is list:
            for i in range(len(self.vector)):
                self.vector[i] = self.vector[i] - object[i]

        print(self.vector)

    # #your code here
    def __truediv__(self, object):
        if type(object) is float or type(object) is int:
            for i in range(len(self.vector)):
                self.vector[i] = self.vector[i] // object
        elif type(object) is list:
            for i in range(len(self.vector)):
                self.vector[i] = self.vector[i] // object[i]

        print(self.vector)
