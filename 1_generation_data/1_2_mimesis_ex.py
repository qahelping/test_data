from mimesis import Person, Address, Datetime
from mimesis.locales import Locale

person = Person(Locale.RU)

print(person.full_name())  # Иван Иванов
print(person.email())  # ivan.petrov@example.com
print(person.telephone())  # +7 495 123-45-67

person = Person(locale=Locale.KO, seed=0xFF)
person.full_name()

print(person.full_name())  # 인주 마
print(person.email())  # uganda1931@example.org
print(person.telephone())  # +82-59-9440-1727

person = Person(locale=Locale.EN)
print(person.email(domains=['yopmail.com']))  # threat2031@yopmail.com
print(person.email(domains=['mimesis.name'], unique=True))  # 4d66822f97414187b514d624652c75d7@mimesis.name
print(person.telephone(mask='1-4##-8##-5##3'))  # 1-405-889-5543

address = Address(Locale.EN)
datetime = Datetime()

print(address.city())  # New York
print(address.address())  # 742 Evergreen Terrace
print(datetime.date())  # 2025-09-15
