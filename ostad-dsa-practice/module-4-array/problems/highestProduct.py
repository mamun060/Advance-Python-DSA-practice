def sortArrry(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j]  = temp
    return arr

def highestProduct(arr):
    size = len(arr)
    result = arr[size-1] * arr[size-2] * arr[size-3]
    return result

arr = [ 2, 7, 9, 1,12,8,20]
secondArray = [0, -1, 3, 100, 70, 50]
thirdArray = [1,2,3,4]
result = sortArrry(secondArray)
multiplyValue = highestProduct(result)            
print(result)
print(multiplyValue)
    