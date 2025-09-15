from faker.providers import BaseProvider
from faker import Faker

fake = Faker()

class StatusProvider(BaseProvider):
    def get_status(self) -> str:
        jira_statuses = [
            "Open",
            "In Progress",
            "Done",
            "To Do",
            "Reopened",
            "Resolved",
            "Closed",
            "In Review",
            "Pending",
            "Blocked",
            "Approved",
            "Waiting for Review",
            "Waiting for QA",
            "In Testing",
            "Failed QA",
            "Ready for Production",
            "Ready for Deployment",
            "Deployed",
            "Rejected",
            "Duplicate",
            "Won't Fix",
            "Cannot Reproduce"
        ]
        return self.random_element(jira_statuses)

fake.add_provider(StatusProvider)

status = fake.get_status()
print(status)

# Генерация уникальных значений
used_emails = set()
for _ in range(21):
    email = fake.unique.get_status()
    used_emails.add(email)

print(used_emails)

# Сброс уникальности
fake.unique.clear()

# Генерация уникальных значений
used_emails2 = set()
for _ in range(21):
    email = fake.get_status()
    used_emails2.add(email)

print(used_emails2)
