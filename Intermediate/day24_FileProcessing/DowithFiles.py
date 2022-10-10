with open("../../new_file.txt", mode="r") as file:
    # return String
    print(file.read())

with open("../../new_file.txt", mode="a") as file:
    # append
    # "a" mode can create a new file
    file.write("\nNew text")

with open("/Users/macbookpro/Desktop/new_file.txt", mode="w") as file:
    # "w" mode can create a new file
    file.write("\nNew text")

    # release the computer
    # use "with", don't need to close
    # file.close()
