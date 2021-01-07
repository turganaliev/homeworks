class User:
    def __init__(self, name, surname, email, gender, password):
        self._name = name
        self._surname = surname
        self._email = email
        self._gender = gender
        self._password = password

    @property
    def password(self):
        return self._password

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def email(self):
        return self._email

    @property
    def gender(self):
        return self._gender

    @password.setter
    def password(self, value):
        if value != self._password:
            print("Incorrect password! Please, try again.")
        else:
            print("Correct!")

    @name.setter
    def name(self, value):
        if value != self._name:
            print('Incorrect name! Please, try again.')
        else:
            print('Correct!')

    @surname.setter
    def surname(self, value):
        if value != self._surname:
            print('Incorrect surname! Please, try again.')
        else:
            print('Correct')

    @email.setter
    def email(self, value):
        if value != self._email:
            print('Incorrect email! Please, try again.')
        else:
            print('Correct!')

    @gender.setter
    def gender(self, value):
        if value != self._gender:
            print('Probably, you just accidentally clicked! Please, try again.')
        else:
            print('Correct!')

class Validation(User):
    def __init__(self, name, surname, email, gender, password, date_of_birthday):
        super(Validation, self).__init__(name, surname, email, gender, password)
        self.date_of_birthday = date_of_birthday


a = Validation("Will", "Smith", "willsmith@gmail.com", 'male', 'cherniy#1', 20/11/1980)
a.password = 'cherniy#2'
a.password = 'cherniy#1'
a.name = 'Will'
a.surname = 'smith'
a.email = 'willsmith@gmail.com'
a.gender = 'female'
