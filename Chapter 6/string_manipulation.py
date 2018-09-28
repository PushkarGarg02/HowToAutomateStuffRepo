tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(tableData):
    tableLengthList = []
    
    for mainList in tableData:
        maximumLengthOfItem = 0
        
        for subItem in mainList:
            lengthOfItem = len(subItem)
            if lengthOfItem > maximumLengthOfItem:
                maximumLengthOfItem = lengthOfItem
        
        tableLengthList.append(maximumLengthOfItem)
        
    
    for i in range(len(tableData[0])):
        str = ''
        for j in range(len(tableLengthList)):
            str = str + tableData[j][i].rjust(tableLengthList[j]) + ' '
        print(str)   
        
printTable(tableData)

#  apples Alice  dogs
# oranges   Bob  cats
#cherries Carol moose
#  banana David goose
