with open("input.txt", "r") as file:
    nums=file.read().replace('\n','').split(",")

nums = list(map(int, nums))

def custo(x, constant):
    tot=0
    for n in nums:
        if constant:
            tot+=abs(n-x)
        else:
            for i in range(abs(n-x)):
                tot+=1+i
    return tot

def min_custo(constant):
    minimo = float('inf')
    for i in range(max(nums)):
        c = custo(i,constant)
        if c<minimo:
            minimo=c
    print(minimo)

# Part 1
min_custo(True)

# Part 2
min_custo(False)