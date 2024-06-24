#My approach
#Time o(n^2) space o(n)
def arrayOfProducts(arr):
    out = []
    for idx, i in enumerate(arr):
        mul = 1
        for jdx, j in enumerate(arr):
            if idx != jdx:
                mul *= j
        out.append(mul)
    return out

arr =  [5, 1, 4,  2]

print(arrayOfProducts(arr))