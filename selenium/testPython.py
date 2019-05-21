def testInput():
    dataT = str(input("Enter your data: "))
    if dataT:
        print("Search " + str(dataT))
    else:
        dataT = "Gmail"
        print("Search " + str(dataT))
    return dataT



def testReadFile():
    file = open("../testData/target.txt ", "r")
    dataT = file.readline()

    if dataT.__eq__(''):
        dataT = "Gmail"

    print(dataT)

    return dataT



testReadFile()