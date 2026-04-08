from files import TXT_FILE_PATH
# "r"	Чтение (по умолчанию)
# "w"	Запись (перезаписывает файл, если не существует — создаёт)
# "a"	Дозапись в конец файла
# "x"	Создание файла (ошибка, если файл существует)
# "b"	Бинарный режим ("rb", "wb")
# "+"	Открытие для чтения и записи ("r+", "w+")

some_file = open(TXT_FILE_PATH, "r")

# Read the exact bites amount
print("BITES", some_file.read(7))

# Read a single line
print("READLINE", some_file.readline())

# Get all lines as list
print("READLINES", some_file.readlines(), "\n")
print("------\n")

some_file.seek(0)
print("FULL", some_file.read())

some_file.seek(0)

some_file.write("------\n")

some_file.close()


