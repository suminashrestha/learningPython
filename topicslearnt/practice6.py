# File
# qn1
# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)

# qn2 search if the word 'learning' exists or not
def search_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if (data.find(word) != -1):
            print("Found")
        else:
            print("not Found")

# q3


def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no += 1
    return -1


# q4  from a file containing numbers separated
# by comma, print the count of even numbers

# 1.  individual number
# 2.  parse/casting to integer(as it is in substring)


count = 0

with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    # num = ""
    # for i in range(len(data)):
    #     if (data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]
    nums = data.split(",")

    for val in nums:
        if (int(val) % 2 == 0):
            count += 1
    print(count)
