# f = open("demo.txt", "a")

# f.write("\nThis is appended")
# f.close()


# using r+ doesn't truncate, but overwrites from the beginning
# f = open("demo.txt", "r+")

# f.write("W ")
# f.close()

# using w+ truncates all data from the file and also overwrites
# fop = open("sample.txt", "w+")
# fop.write("Truncated")
# fop.close()

# using a+ appends the data at the end
f = open("sample.txt", "a+")
f.write(" This is appended data.")
f.close()
