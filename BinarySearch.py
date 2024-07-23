def binarySearch(arr, start, end, key):
    while(start<=end):
        mid = int(start+((end-start)/2))
        if(arr[mid]==key):
            return f"Element found in index {mid}"
        elif(arr[mid]>key):
            end = mid - 1
        else:
            start = mid + 1
    return "Element Not found"

print("Enter the elements of the list(seperates by space)")
arr = list(map(int,input().strip().split()))
key = int(input("Enter the number to be searched: "))
result = binarySearch(arr,0,len(arr)-1,key)
print(result)