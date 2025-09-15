import faker
from faker import Faker

# "r"	Чтение (по умолчанию)
# "w"	Запись (перезаписывает файл, если не существует — создаёт)
# "a"	Дозапись в конец файла
# "x"	Создание файла (ошибка, если файл существует)
# "b"	Бинарный режим ("rb", "wb")
# "+"	Открытие для чтения и записи ("r+", "w+")

some_file = open("example_write.txt", "w")

text = """О сколько нам открытий чудных
Готовят просвещенья дух
И Гений парадоксов друг
И Опыт сын ошибок трудных
"""

some_file.write(text)
fake = Faker()
some_file.writelines([fake.sentence(), fake.sentence(), fake.sentence()])

some_file.close()

# encoding
some_file = open("example_write.txt", "x", encoding="utf-8")
some_file.close()