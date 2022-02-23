if __name__ == '__main__' :
    a = int(input("Enter the number : "))
    j = 1

    for i in range(0, a) :
        j = j + (i*j)

    print(j)

    # def fact(n) :
    #     x = 0
    #     x = n * fact(n - 1)
    #     return x
    #
    # result = fact(a)
    # print("result is : "+ str(result))