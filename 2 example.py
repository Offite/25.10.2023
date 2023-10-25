# def main(): point1 = Point3D(1, 2, 3)
# point2 = Point3D(4, 5, 6)
# print(point1.x, point1.y, point1.z)
# print(point2.x, point2.y, point2.z)

# class Point3D: def init(self "x", "y", "z"): "self.x = x" "self.y = y" "self.z = z"
#
# point1 = Point3D(1, 2, 3)
# print(point1.x)
# print(point1.y)
# print(point1.z) point1.x = 4 point1.y = 5 point1.z = 6
# print(point1.x)
# print(point1.y)
# print(point1.z)



# Задание №1

# def __init__(self, fio, date_birth, gender):
#     self.fio = fio
#     year, month, day = map(int, date_birth.split('-'))
#     self.date_birth = datetime.date(year, month, day)
#     self.gender = gender
#
# def __del__(self):
#
#     pass
#
# class Person:
#     (Иван Иванов = Person(fio: Иван Иванов, date_birth: 1980-01-01, gender: male))
#
# print(Иван Иванов.fio)
# print(Иван Иванов.date_birth)
# print(Иван Иванов.gender)



# Задание №2

# class Phone:
#
#  def init(self, number, model, weight):
#      self.number = number
#      self.model = model
#      self.weight = weight
# def receiveCall(self, name):
#
#  print(f"Звонит {name}")
# def getNumber(self):
#
#  return self.number
# phone1 = Phone("+79001234567", "iPhone 14", "300 г")
#
# phone2 = Phone("+79111111111", "Samsung Galaxy S22", "250 г")
#
# phone3 = Phone("+799123123446", "Nothing Phone 1", "400 г")
#
# for phone in (phone1, phone2, phone3):
#
#  print(f"Номер телефона: {phone.getNumber()}, Модель: {phone.model}, Вес: {phone.weight}")
# phone1.receiveCall("Anton")



class Reader:
    def __init__(self, first_name, last_name, reader_number, faculty, birth_date, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.reader_number = reader_number
        self.faculty = faculty
        self.birth_date = birth_date
        self.phone = phone

    def takeBook(self, book):
        print(f"{self.first_name} {self.last_name} took {book}")

    def returnBook(self, book):
        print(f"{self.first_name} {self.last_name} returned {book}")

