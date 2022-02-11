
def maxnumber(a,b) :
    if (a > b) :
        return a

    else :
        return b



if __name__ == "__main__" :
    a= input("Enter first number : ")
    b = input("Enter the second number : ")

    # if a > b :
    #     print("{} is maximum number".format(a))
    #
    # else :
    #     print("{} is maximum number".format(b))

    result = maxnumber(a,b)
    print("maximum number is :" +result)