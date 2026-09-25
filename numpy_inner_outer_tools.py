import numpy as np

arr_a=list(map(int,input().split()))
arr_b=list(map(int,input().split()))

print(np.inner(arr_a,arr_b))
print(np.outer(arr_a,arr_b))