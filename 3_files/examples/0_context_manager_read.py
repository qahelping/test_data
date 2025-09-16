import os

with expression [as variable]:
    pass
    # Блок кода, работающий в контексте
    # Ресурсы автоматически освобождаются после выхода из блока



# Без менеджера контекста
file = open('example.txt', 'r')
data = file.read()
file.close()  # Важно не забыть закрыть файл

# С менеджером контекста
with open('example.txt', 'r') as file:
    data = file.read()
    # Файл автоматически закроется после выхода из блока

# НЕСКОЛЬКО
with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
    for line in fin:
        fout.write(line.upper())

# кастомизация
@contextmanager
def temporary_env(**env_vars):
    old_env = dict(os.environ)
    os.environ.update(env_vars)
    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(old_env)

# Использование в тестах
with temporary_env(API_KEY='test_key', DEBUG='true'):
    # Тесты, зависящие от переменных окружения
    pass
# Оригинальные переменные восстановлены