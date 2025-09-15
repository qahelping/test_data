# pip install Faker
# https://faker.readthedocs.io/en/master/
from faker import Faker

# fake = Faker('ru_RU')  # Для русскоязычных данных
fake = Faker()  # Для данных по умолчанию (en_US)

# Имя
print(fake.name())  # 'Иванов Иван Иванович'
print(fake.first_name())  # 'Иван'
print(fake.last_name())  # 'Иванов'

# Адрес
print(fake.address())  # 'ул. Ленина, д. 123, кв. 45'
print(fake.city())  # 'Москва'
print(fake.country())  # 'Россия'

# Контакты
print(fake.email())  # 'ivanov@example.com'
print(fake.phone_number())  # '+7 (123) 456-78-90'


print(fake.date_of_birth())  # datetime.date(1990, 5, 15)
print(fake.date_this_decade())  # '2023-07-22'
print(fake.time())  # '15:30:45'

print(fake.text())  # Полный абзац текста
print(fake.sentence())  # Отдельное предложение
print(fake.word())  # Случайное слово


print(fake.credit_card_number())  # '4455 5299 1152 2450'
print(fake.credit_card_expire())  # '03/25'
print(fake.currency_code())  # 'USD'

print(fake.url())  # 'https://example.com/'
print(fake.ipv4())  # '192.168.0.1'
print(fake.user_agent())  # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'

print(fake.company())  # 'ООО "ТехноПром"'
print(fake.job())  # 'Менеджер по продажам'
print(fake.bs())  # 'интегрировать инновационные решения'



# Генерация уникальных значений
used_emails = set()
for _ in range(100):
    email = fake.unique.email()
    used_emails.add(email)

print(used_emails)

# Сброс уникальности
fake.unique.clear()

# Генерация уникальных значений
used_emails2 = set()
for _ in range(100):
    email = fake.email()
    used_emails.add(email)

print(used_emails2)