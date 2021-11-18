
def find_sum_in_num_array(nums):
    #nums = [1,3,7,9,2]
    compval = 10; ntf = 0
    i = 0; breakit = 0
    for a in nums:
        #print(f'num[{i}]={a}')
        j=0
        ntf = compval-a
        print(f'num to find = {ntf}')
        for b in nums:
            if(j!=i):
                #print(f'num1={a}, num2={b}')
                if (b==ntf):
                    print(f'num[{i}]={a}, num[{j}]={b},  compval = {compval}, sum={a+b}')
                    breakit=1
                    break
            j+=1
        if breakit:
            break

        i+=1

    return

nums = [1,3,7,8,2]
find_sum_in_num_array(nums)
