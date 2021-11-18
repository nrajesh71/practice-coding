
def merge_sort (mylist):
    leftarr=[]
    rightarr=[]
    if (len(mylist)>1):
        mid = int(len(mylist)/2)
        leftarr  = mylist[:mid]
        rightarr = mylist[mid:]
        merge_sort(leftarr)
        merge_sort(rightarr)

        i = 0
        j = 0
        k = 0

        while i<len(leftarr) and j < len(rightarr):
            if leftarr[i] <= rightarr[j]:
                mylist[k]=leftarr[i]
                i+=1
            else:
                mylist[k]=rightarr[j]
                j+=1
            k+=1
        while i < len(leftarr):
            mylist[k]=leftarr[i]
            i+=1
            k+=1
        while j < len(rightarr):
            mylist[k]=rightarr[j]
            j+=1
            k+=1


somelist = [22,1,3,99,33,5,99,7,6]
merge_sort(somelist)
print(somelist)
