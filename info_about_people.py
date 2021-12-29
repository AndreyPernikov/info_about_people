from string import ascii_letters


class Person:
    R_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    R_RUS_UPPER = R_RUS.upper()

    def __init__(self, fio, age, passport, weight):
        self.verify_fio(fio)
        self.verify_age(age)
        self.verify_passport(passport)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.__age = age
        self.__passport = passport
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):

        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        a = fio.split()
        if len(a) != 3:
            raise TypeError("Введите корректрый данные")

        letters = ascii_letters + cls.R_RUS + cls.R_RUS_UPPER

        for s in a:
            if len(s) < 1:
                raise TypeError("ФИО должен быть хотя бы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО может быть только буквы и дефис")

    @classmethod
    def verify_age(cls, age):
        if type(age) != int or age < 14 or age > 120:
            raise TypeError("Возраст должен быть целым числом или быть от 14 до 120 лет")

    @classmethod
    def verify_passport(cls, passport):
        if type(passport) != str:
            raise TypeError("Пасспорт должет быть строкой")

        a = passport.split()
        if len(a) != 2 or len(a[0]) != 2 or len(a[1]) != 7:
            raise TypeError("Неверный ввод данных паспорта")

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError("Вес должет быть вещественным числом и быть сввыше 20")

    @property
    def fio(self):
        return self.__fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_passport(passport)
        self.__passport = passport

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight


p = Person('Ivanov Иван Иванович', 24, 'BU 1234567', 70.3)
print(p.__dict__)
print(p.fio)
print(p.age)
print(p.passport)
print(p.weight)