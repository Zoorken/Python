# Hello World program in Python
theArray = [3,10,4,100,5,60,90,80,100]

def partion(theArray,start,end):
    pivotPos = start
    i = start + 1
    while i <= end:
        if theArray[pivotPos]>theArray[i]:
            swapThem(i,pivotPos+1)
            swapThem(pivotPos,pivotPos+1)
            pivotPos += 1
        i += 1
    return pivotPos
    

def swapThem(index1, index2):
    temp = theArray[index1]
    theArray[index1] = theArray[index2]
    theArray[index2] = temp      

def quickSort(theArray,start,end):
    if(start < end):
        pivotPos = partion(theArray,start,end)
        quickSort(theArray,start,(pivotPos-1))
        quickSort(theArray,pivotPos+1,end)
    

quickSort(theArray,0,len(theArray)-1)

print (theArray)