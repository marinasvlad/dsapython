import math

def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1

        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    return customList

cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
insertionSort(cList)



def bucketSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    max_value = max(customList)
    arr = []

    for i in range(numberOfBuckets):
        arr.append([])

    for element in customList:
         indexBucket = math.ceil(element * numberOfBuckets/max_value)
         arr[indexBucket - 1].append(element)

    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])
    
    k = 0

    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    
    return customList

cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]

cList = bucketSort(cList)
print(cList)

