#BUBBLE SORT n^2 unless break is added. 
def bubble_sort(a,*args):
    #outer and inner loop run run n times giving us O(n^2)
    # decrement outer loop each time 
    
    if not args:
        boolean = 0
    else:
         boolean = args[0]

    
    num_compares  = 0
    for i in range(len(a)-1, 0, -1):
        #optional break for bubble sort. 
        if boolean == 1:
            flag = False
            
        # examine each item pair
        for j in range(i):
            #count the number of times we execute 
            num_compares += 1
            # swap
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp 
                #check if user wants to use break 
                if boolean == 1:
                    flag = True
        if boolean == 1:
        #if no swaps were made we have a sorted array and can exit
            if(flag == False):
                break
    return num_compares

# TESTING CODE
#a = [3, 10, 1, 29, -1, 4, 3, 15, 2, -2]
a = [1,2,3,4,5,6,7,8,9]
nc = bubble_sort(a)
print('Num Comparison = ', nc)
#print('Sorted Result = ', a)