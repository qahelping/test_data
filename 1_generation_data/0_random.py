import random
import secrets
import string



print(random.randint(-100, 10))
print(random.choice([
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
        ]))


random.seed(42)
print(random.randint(-100, 10))

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + '!@#$%'
    return ''.join(secrets.choice(chars) for _ in range(length))

print(generate_password())
