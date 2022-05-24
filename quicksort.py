#implement global counter
comparisons = 0

def quicksort(a, first, last):
    if first < last:
        # calculate the split point
        pivotIdx = lomuto_partition(a, first, last)

        
        # now sort the two partitions
        quicksort(a, first, pivotIdx-1)
        quicksort(a, pivotIdx+1, last)
    return [a,comparisons]

#Lomuto Partitioning
def lomuto_partition(a,first,last):
    x = a[last] #start at last element for pivot
    
    #start j at 1 and i at 0
    i = first -1

    for j in range(first,last,1):
        global comparisons

        if a[j]< x:
            comparisons += 1
            temp = a[i+1]
            a[i+1] = a[j]
            a[j] = temp 
           
            i += 1
            #print(i,j)
            #print(a)

    temp = a[i+1]
    a[i+1] = a[last]
    a[last] = temp 
    print(a)

    return i+1


    # TESTING CODE
a = [3, 10, 1, 29, -1, 4, 3, 15, 2, -2]
nc = quicksort(a,0,len(a)-1)
print('Num Comparison = ', nc)
#print('Sorted Result = ', a)