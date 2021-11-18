
from typing import Hashable


def find_sum_using_hash(sumtofind, numsarray):
    i=0; j=0; p=-1
    ntf=0
    hash_table = {}
    print(f'sumtofind={sumtofind}, numsarray={numsarray}')

    

    i=0
    for num in numsarray:
        hash_table.update({num:i})

        ntf=sumtofind-num
        print (f'for {num}, num to find  ={ntf}')
        p=hash_table.get(ntf)
        if p:
            print(f'num[{i}]={num}, num[{p}] = {ntf}')
        i+=1    
    print(hash_table)

    return 


numsarray=[1,3,5,7,9,2]
sumtofind=12
find_sum_using_hash(sumtofind,numsarray)
