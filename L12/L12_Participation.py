# basic file write
filename = input("Enter filename: ")
content_ = "This is a test\n"
try:
    outfile = open(filename, "w")
    try:
        outfile.write(content_)
    finally:
        outfile.close()
except FileNotFoundError:
    print("File not found")
print('Continue with program')
