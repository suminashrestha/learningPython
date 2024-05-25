# with Syntax
with open("demo.txt", "r") as f:  # as means alias
    data = f.read()
    print(data)

with open("demo.txt", "w") as f:
    f.write("This overwrites the demo codeHello.")
