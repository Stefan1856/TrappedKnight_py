#!/usr/bin/python

def BubbleList(a):
    weiter = True
    while(weiter):
        weiter = False
        for i in range(len(a)-1):
            if(a[i][2] > a[i+1][2]):
                a[i] , a[i+1] = a[i+1] , a[i]
                weiter = True




def QuickList(*a):
    if(len(a) == 1):
        a = a + (0,len(a[0])-1)
    a = list(a)
    r = a[1]
    l = a[2]
    if(r < l):
        p = a[0][r][2]
        i = l
        j = r-1
        while(True):
            while((i <= j) and (a[0][i][2] <= p)):
                i = i+1
            while((i <= j) and (a[0][j][2] >= p)):
                j = j-1
            vertausche(a,i,j)
            if(i>=j):
                break
        vertausche(a,i,r)
        QuickList(a[0],l,i-1)
        QuickList(a[0],i+1,l)


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low , high):

        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
