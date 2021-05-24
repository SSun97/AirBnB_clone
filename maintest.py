import re

line = "User.all()"
command = re.search(r"^(\w*)\.(\w+)", line)

a = command.group(1)
b = command.group(2)


print(a)
print(b)

