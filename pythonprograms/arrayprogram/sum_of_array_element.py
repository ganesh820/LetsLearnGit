

def sum_array(vals) :
    global  sum
    for x in vals :
        sum = sum + x

    return sum


if __name__ == '__main__' :
    arr = [12, 3, 4, 15]

    sum = 0

    result = sum_array(arr)
    print("final sum value is :  "+ str(result))