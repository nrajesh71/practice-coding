def two_way_mergesort(a,b):
    print (f'a = {a}, b = {b}')
    i=0; j=0; k=0
    c=[]
    maxlen=len(a)+len(b)
    while k<maxlen:
        if(i<len(a) and j <len(b)):
            if(a[i]<b[j]):
                c.append(a[i])
                i+=1
            else:
                c.append(b[j])
                j+=1
        elif j<len(b):
            c.append(b[j])
            j+=1
        elif i < len(a):
            c.append(a[i])
            i+=1
        
        print(f'i={i},j={j},k={k},c={c}')
        k+=1


first = [0,0,1,3,4,7,8,10,12,15]
second = [1,1,1,2,5,6,9,11,13,14]
two_way_mergesort(first,second)
