import os
import re

from dotenv import load_dotenv, dotenv_values

load_dotenv()
print(os.getenv("LOGIN"))
print(os.getenv("PASSWORD"))

# -------------------------------
env_values = dotenv_values("../.env.secret")

pattern = re.compile(r"\$\{([^}]+)\}")


def substitute(value: str, variables: dict) -> str:
    def replacer(match):
        var_name = match.group(1)
        return variables.get(var_name, match.group(0))

    return pattern.sub(replacer, value)


resolved_env = {k: substitute(v, env_values) for k, v in env_values.items()}

print(resolved_env)

# ENV=prod pytest 2_test_data_management/main.py
print(os.getenv("ENV"))