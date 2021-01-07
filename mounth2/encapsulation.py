class UserProfile:

    def __init__(self, name, phone_number, password):
        self._name = name
        self._phone_number = phone_number
        self.__password = password

    def get_data(self):
        return self._name, self._phone_number, self.__password


u = UserProfile('Izat', 500422455, 'password')
print(u.get_data())
