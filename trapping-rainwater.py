
def count_water_units(wall):
    #print(f'wlen={len(wall)}, wall = {wall}')
    state='nowall'
    i=0
    water=0
    leftwall=0; rightwall=0
    while (i < len(wall)):
        if(state=='nowall'):
            if wall[i]<1:
                #print(f'i={i}')
                i+=1
                continue
            else:
                #print(f'i={i}')
                state='foundwall'
                leftwall=i
                #print(f'found wall at {i}')
        if (state=='foundwall'):
            i+=1
            if (i>=len(wall)):
                break
            #print(f'i={i}')
            if(wall[i]>0):
                rightwall=i
                #print(f'leftwall={leftwall}, rightwall={rightwall}')
                water=water+rightwall-leftwall-1
                leftwall=i
                rightwall=0
    print(f"water={water}")
    return water

def two_top_walls(walls):
    maxone=0; maxtwo=0; n=0
    max_2 = [0,0]
    for n in walls:
        if maxone<n:
            maxtwo=maxone
            maxone=n
        elif (maxtwo<n):
            maxtwo=n
    
    #print(f'max={maxone}, sec={maxtwo}')
    return [maxone, maxtwo]

def trapping_rainwater(walls):
    waterfound = True
    totalwater=0; secmax=0
    max_two = two_top_walls(walls)
    secmax=max_two[1]
    j=0
    while (j<=secmax):
        print(walls)
        totalwater += count_water_units(walls)
        i=0
        while (i<len(walls)):
            if(walls[i]>0):
                walls[i]-=1
            i+=1
        j+=1
    print(f'totalwater{totalwater}')

def trapping_rainwater_watercolumn(walls):
    p=0;i=0
    lp=p
    rp=p
    max_lw=0; max_rw=0
    water_column=0
    total_water=0
    while i<len(walls):
        p=i
        max_lw=walls[p]
        max_rw=walls[p]
        while (p>0): # Traverse left
            if walls[p]>max_lw:
                max_lw=walls[p]
            p-=1
        while (p<len(walls)): #Traverse right
            if walls[p]>max_rw:
                max_rw=walls[p]
            p+=1
        if (max_lw<=max_rw):
            min_wall=max_lw
        else:
            min_wall=max_rw
        water_column = min_wall-walls[i]
        total_water+=water_column
        print(f'watercolumn @ {i} = {water_column}, total_water={total_water}')
        i+=1

def trapping_rainwater_optimized(walls):
    lp=0
    rp=len(walls)-1
    maxleft=0; maxright=0
    totalwater=0
    i=0
    while (lp<rp):
        if(walls[lp]<=walls[rp]):
            if(walls[lp]>=maxleft):
                maxleft=walls[lp]
            else:
                totalwater+=maxleft-walls[lp]
            lp+=1
        else:
            if (walls[rp] > maxright):
                maxright=walls[rp]
            else:
                totalwater+=maxright-walls[rp]
            rp-=1
    print(f'totalwater={totalwater}')
        


walls=[0,2,0,0,1,0,2,0,3]
print("Method 1")
trapping_rainwater (walls)

walls=[0,2,0,0,1,0,2,0,3]
print("Method 2")
trapping_rainwater_watercolumn(walls)

walls=[0,2,0,0,1,0,2,0,3]
print("Method 3")
trapping_rainwater_optimized(walls)
