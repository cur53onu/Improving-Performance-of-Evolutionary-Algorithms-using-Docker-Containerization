from django.shortcuts import render
from django.http import JsonResponse

from django.http import HttpResponse

def home(request):
    return render(request,'codeapp/home.html')
def code(request):
    if request.method=="POST":
        query=request.POST['array']
        listofnum=query.split(',')
        lisofintnum=[]
        for i in listofnum:
            lisofintnum.append(int(i))
        inp = lisofintnum
        inp.sort()
        returnstring=''
        cnt=1
        for i in inp:
            returnstring+=str(i)
            if cnt<len(listofnum):
                returnstring+=", "
            cnt=cnt+1
        return HttpResponse('Sorted Array : '+returnstring)

    return HttpResponse('Please give input')


def check(request):
    query=request.GET.get('arr')
    print(query)
    #getting full url of requesting website
    arr=query.split(',')
    print(arr)
    listofnum=arr
    lisofintnum=[]
    for i in listofnum:
        lisofintnum.append(int(i))
    x = lisofintnum
    bubbleSort(x)
    print(x)

    return JsonResponse({'arr':x,'text':'this sorted array comes from bubble sort-container!!!'})
    # return HttpResponse('You are in container 1!!! + Result : '+str(arr))

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
