


class GreetUser:
    def __init__(self, username):
        self.name = username

    def Greet(self):

        print("Hello {}!".format(self.name))
        return self.name