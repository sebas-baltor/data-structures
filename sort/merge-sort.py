import math


def MergeSort(arr):
    if len(arr) <= 1: return arr

    middle = math.floor(len(arr)/2)
    left = MergeSort(arr[:middle])
    right = MergeSort(arr[middle:])

    return Merge(left,right)

def Merge(left,right):
    merged=[]
    i = j=0

    while i<len(left) and j<len(right):
        if left[i]<= right[j]:
            merged.append(left[i])
            i+=1
        else: 
            merged.append(right[i])
            j+=1

    if i < len(left): merged.extend(left[i:])
    if j< len(right): merged.extend(right[j:])

    return merged

if __name__ == "__main__":

    example = [8, 5, 6, 7, 5, 6, 6, 7, 8, 12]
    print(MergeSort(example))