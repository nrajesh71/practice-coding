def most_water(vlist):
    print(vlist)
    w1=vlist[0]; w2=vlist[1]
    volume=0; maxht=0; base=1
    i=0; j=0
    maxvol=0

    for i in range (0,len(vlist)):
        w1=vlist[i]
        for j in range(i+1, len(vlist)):
            w2=vlist[j]
            if(w1<=w2):
                maxht=w1
            else:
                maxht=w2
            vol=maxht*(j-i)
            base=j-1
            print(f'maxht={maxht}, base={base}, vol{vol}')
            if vol>maxvol:
                maxvol=vol
            j+=1
        i+=1
            

    print (f'maxvol={maxvol}')

def most_water_optimized(vlist):
    w1=vlist[0]
    w2=vlist[len(vlist)-1]
    print(f'w1={w1}, w2={w2}')
    i=0; j=len(vlist)-1
    maxvol=0
    while(i<j):
        vol = min([vlist[i],vlist[j]]) * abs(j-i)
        print(f'wall1={vlist[i]}, wall2={vlist[j]}, volume={vol}')
        if maxvol<vol:
            maxvol=vol
        if vlist[i]<=vlist[j]:
            i+=1
        else:
            j-=1
    print (f'maxvol={maxvol}')
    
   
vlist = [1,9,40,40,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
most_water(vlist)
most_water_optimized(vlist)
