# Hello World program in Python
theArray = [0,10,4,100,5,60,90,80,100]

def partion(theArray,start,end):
    pivotPos = start
    i = start + 1
    while i < end:
        if theArray[pivotPos]>theArray[i]:
            swapThem(theArray[i],theArray[pivotPos+1])
            swapThem(theArray[pivotPos],theArray[pivotPos+1])
            pivotPos += 1
        i += 1
    return pivotPos
    

def swapThem(item1, item2):
    temp = item1
    item1 = item2
    item2 = temp      

def quickSort(theArray,start,end):
    if(start < end):
        pivotPos = partion(theArray,start,end)
        quickSort(theArray,start,(pivotPos-1))
        quickSort(theArray,pivotPos+1,end)
    

quickSort(theArray,0,len(theArray))

print (theArray)