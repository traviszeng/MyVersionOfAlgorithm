def InsertSort(a):
    """
    :params: unsorted list

    :return: sorted list
    """
    for i in range(1,len(a)):
        key = a[i]
        j = i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j = j-1

        a[j+1]=key

    return a

def MergeSort(a,p,r):
    """
    Merge sort algorithm

    :param a: array of unsorted list
    :param p: start to merge
    :param r: end to merge sort
    :return: sorted array
    """
    if p<r:
        l = int((p+r)/2)
        MergeSort(a,p,l)
        MergeSort(a,l+1,r)
        Merge(a,p,l,r)

def Merge(a,p,l,r):
    """
    merge procedure of merge sort

    :param a:
    :param p:
    :param l:
    :param r:
    :return:
    """
    n1 = l-p+1
    n2 = r-l

    L = a[p:l+1]
    L.append(999999)

    R = a[l+1:r+1]
    R.append(999999)

    i = 0
    j = 0
    for k in range(p,r):
        if L[i]<=R[j]:
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1



a = [5,4,3,6,1]

a = InsertSort(a)
print(a)

a=[6,5,4,3,1,2,4,6,8]
MergeSort(a,0,len(a))
print(a)