class User:

    def __init__(self, data = None):
        self.userName = None
        self.email = None
        self.firstName = None
        self.lastName = None
        if data is not None:
            self.__dict__ = data
