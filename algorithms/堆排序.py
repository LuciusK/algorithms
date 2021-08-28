def heapify(array, n, k):
	left = 2 * k + 1
	right = 2 * k + 2
	max_i = k
	if left < n and array[max_i] < array[left]:
		max_i = left
	if right < n and array[max_i] < array[right]:
		max_i = right
	if max_i != k:
		array[max_i], array[k] = array[k], array[max_i]
		heapify(array, n, max_i)

def heapSort(arr): 
	n = len(arr) 
	for i in range(n // 2 - 1, -1, -1): 
		heapify(arr,n, i)
	for i in range(n - 1, 0, -1): 
		arr[0], arr[i] = arr[i], arr[0] # swap 
		heapify(arr,i, 0)

  
arr = [99,12,54,12, 11, 13, 5, 6, 7,8,0,45,88] 
heapSort(arr) 
n = len(arr) 
print ("排序后") 
for i in range(n): 
    print ("%d" %arr[i]),