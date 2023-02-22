# CREATED BY VISHU SHARMA

while(True):
    print("ENTER 2 for two numbers")    
    print("ENTER 3 for three numbers")

    NUMBER = input("ENTER THE NUMBER OF NUMBERS : ")

    def two():
        FIRST_NUMBER = int(input("ENTER FIRST_NUMBER : "))
        SECOND_NUMBER = int(input("ENTER SECOND_NUMBER : "))

        print("1 for +")
        print("2 for -")
        print("3 for *")
        print("4 for /")
        print("5 for %")

        OPERATOR = input("ENTER OPERATOR : ")

        def add():
            print("sum = ", FIRST_NUMBER + SECOND_NUMBER)
        def multi():
            print("multi = ", FIRST_NUMBER * SECOND_NUMBER)
        def subt():
            print("difference = ", FIRST_NUMBER - SECOND_NUMBER)
        def div():
            print("qoutient = ", FIRST_NUMBER / SECOND_NUMBER)
        def rem():
            print("remainder = ", FIRST_NUMBER % SECOND_NUMBER)

        if OPERATOR == "1":
            add()
        if OPERATOR == "2":
            subt()
        if OPERATOR == "3":
            multi()
        if OPERATOR == "4":
            div()
        if OPERATOR == "5":
            rem()
        if FIRST_NUMBER == 'q' or SECOND_NUMBER == 'q':
            exit()
        print("Thanks for using!!!")

    def three():
        FIRST_NUMBER = int(input("ENTER FIRST_NUMBER : "))
        SECOND_NUMBER = int(input("ENTER SECOND_NUMBER : "))
        THIRD_NUMBER = int(input("ENTER THIRD_NUMBER : "))

        print("1 for +")
        print("2 for -")
        print("3 for *")
        print("4 for /")
        print("5 for %")

        OPERATOR = input("ENTER OPERATOR : ")

        def add():
            print("sum = ", (FIRST_NUMBER + SECOND_NUMBER) + THIRD_NUMBER)
        def multi():
            print("multi = ", (FIRST_NUMBER * SECOND_NUMBER) * THIRD_NUMBER)
        def subt():
            print("difference = ", (FIRST_NUMBER - SECOND_NUMBER) - THIRD_NUMBER)
        def div():
            print("qoutient = ", (FIRST_NUMBER / SECOND_NUMBER) / THIRD_NUMBER)
        def rem():
            print("remainder = ", (FIRST_NUMBER % SECOND_NUMBER) % THIRD_NUMBER)

        if OPERATOR == "1":
            add()
        if OPERATOR == "2":
            subt()
        if OPERATOR == "3":
            multi()
        if OPERATOR == "4":
            div()
        if OPERATOR == "5":
            rem()
        if FIRST_NUMBER =='q' or SECOND_NUMBER == 'q' or THIRD_NUMBER == 'q':
            exit()
        print("Thanks for using!!!")

    if NUMBER == "2":
        two()
    if NUMBER == "3":
        three()
    if NUMBER == 'q':
        exit()