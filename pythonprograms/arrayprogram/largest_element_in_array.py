if __name__ == '__main__' :
    arr = [10, 324, 45, 90, 9808]

    maximum_num = 0

    def max_num_from_array(vals) :
        global maximum_num
        for x in range(len(vals)) :
            if vals[x] > maximum_num :
                maximum_num = vals[x]
        return maximum_num


    result = max_num_from_array(arr)
    print("maximum Number from array is : " + str(result))