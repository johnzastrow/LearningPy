def nug():
    my_int = 103204934813
    print("Sammy the {0} has a pet {1}!".format("shark", "pilot fish"))
    print("Sammy ate {0:.3f} percent of a pizza!".format(75.765367))
    print("Sammy has {0:<4} red {1:^16}!".format(5, "balloons"))
    print("{:*^20s}".format("Sammy"))
    print()
    print("Raw numbers")
    for i in range(3, 13):
        print(i, i * i, i * i * i)
    print()
    print("Now decimals formatted")
    print()
    for i in range(3, 13):
        print("{:3d} {:4d} {:5d}".format(i, i ^ 2, i * i * i))
    print()
    print(my_int - 5493)
    my_string = "Hello, World!"
    print(my_string)
    my_bool = 5 > 9  # A Boolean value will return either True or False
    print(my_bool)

    my_list = ["item_1", "item_2", "item_3", "item_4"]
    print(my_list)
    my_tuple = ("one", "two", "three")
    print(my_tuple)
    my_dict = {"letter": "g", "number": "seven", "symbol": "&"}
    print(my_dict)
    print("I am done!")


def logfile():
    path = "days.txt"
    # every time you do something like read a file, you need to re-open it for the next op
    print(path)
    days_file = open(path, "r")
    reader = days_file.read()
    days_file.close()
    print()

    days_file = open(path, "r")
    readl = days_file.readline()
    days_file.close()
    print()

    days_file = open(path, "r")
    readl_s = days_file.readlines()
    days_file.close()
    print(reader)
    print()
    print(readl)
    print()

    print(readl_s)

    # now we will append data
    days_file = open(path, "a")
    days_file.write("\n I am a newline")
    days_file = open(path, "r")
    reader = days_file.read()
    days_file.close()
    print()


def main():
    nug()
    logfile()
    print("DONE!")


main()
