from time import time


class MyString(str):

    def __new__(cls, value, line_writer):

        instance = super().__new__(cls, value)
        instance.line_writer = line_writer
        instance.time_of_creation = time()

        return instance


if __name__ == '__main__':

    myString = MyString('текст автора', 'Имя автора')

    print(f"\nИмя автора - {myString.line_writer}")
    print(f"\nвремя создания(time.time) - {myString.time_of_creation}")
    print(f"\nТекст автора - {myString}")
    print(f"\nТекст автора в верхнем регитстре - {myString.upper()}\n")
