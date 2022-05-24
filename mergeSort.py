def merge_sort_recursive(a):
    
    if len(a) > 1:
        mid = len(a) // 2
        
        #rather than passing the lengths in we can just passes them as arrays split from the midpoint
        left = a[:mid]
        right = a[mid:]
        
        # recursively break down the arrays
        merge_sort_recursive(left)
        merge_sort_recursive(right)
        merge(a,left,right)
    #return the sorted array and the global counter
    return[a,count]

#merge algorithm 
def merge(a,left,right):
        i=j=k=0 # index for left array, index for right array,index for merged array
        #count = 0
        global count
        # while both arrays have content
        while i < len(left) and j < len(right):
            #count comparison
            count+=1

            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            k += 1

        # left array still has values 
        while i < len(left):
            #count comparison
            count+=1
            a[k] = left[i]
            i += 1
            k += 1

        # right array still has values
        while j < len(right):
            #count comparison
            count+=1
            a[k] = right[j]
            j += 1
            k += 1

def merge_sort(a):
    #for some reason we are asked to have this caller function to the recusive function
    #did not understand the point and made the code more complicated than it would have been without
    #due to the helper function place global counter here. 
    global count
    count  = 0
    # Implement the code for merge sort
    # Use a function merge_sort_recursive to implement the recursive call
    # Be careful in counting number of comparisons since you should include comparisons in the merge part.
    # Also: code needs to sort the array a. You may have to copy things over from a temp array back into a.
    return merge_sort_recursive(a)

def create_leftOdd_rightEven_array(a_size,increment):
    #create two arrays of asize//2
    even = list(range(2,(a_size)*increment,increment))
    odd = list(range(1,increment*(a_size),increment))
    return odd + even

# I have the function split the arrays into left and right based of the mid computed using floor division so the function takes on input here. 
#merge_sort_recursive(a, 0, len(a)-1)

"""     # TESTING CODE
a = [3, 10, 1, 29, -1, 4, 3, 15, 2, -2]
nc = mergesort(a)
print('Num Comparison = ', nc)
#print('Sorted Result = ', a) """

a = list(range(1,10,1))
#a = [1,3,5,7,2,4,6,8]
r = [6,5,4,3,2,1]
#s = [1,2,3,4,5,6,7,8]
w = [1, 9, 5, 13, 3, 11, 7, 15, 2, 10, 6, 14, 4, 12, 8, 16]
s = create_leftOdd_rightEven_array(100000//2,1)

[a,nc] = merge_sort(a)
print('Num Comparison for a = ', nc)
#print('Sorted Result a = ', a)

[s,snc] = merge_sort(s)
print('Num Comparison for r = ', snc)
#print('Sorted Result a = ', s)