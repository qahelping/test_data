from files.files import TXT_FILE_PATH

with open(TXT_FILE_PATH, "r") as file:
    print(file.read())
    # No need to call close method

print("\n", 20 * "=", "\n")

with open(TXT_FILE_PATH, "r") as file:
    for line in file.readlines():
        # Break line fix end=""
        print(line)


with open("example.txt", "w") as file:
    for n in range(10):
        file.write(str(n) + "\n")
