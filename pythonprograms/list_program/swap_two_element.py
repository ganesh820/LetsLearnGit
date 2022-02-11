if __name__ == '__main__' :
    list1 = [10,20,30,40]

    position1 = 2
    position2 = 3

    def swapelement(lst, val1, val2) :

        temp = lst[val1-1]
        lst[val1-1] = lst[val2-1]
        lst[val2-1] = temp
        return lst


    finallist = swapelement(list1, position1, position2)
    print(finallist)