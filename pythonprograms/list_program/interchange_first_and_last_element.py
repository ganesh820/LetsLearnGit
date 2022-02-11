if __name__ == '__main__' :
    newList = [12, 35, 9, 56, 24]
    def swapelement(vals) :
        temp = vals[0]
        length = len(newList)
        vals[0] = vals[length-1]
        vals[length-1] = temp
        return vals



    print(swapelement(newList))