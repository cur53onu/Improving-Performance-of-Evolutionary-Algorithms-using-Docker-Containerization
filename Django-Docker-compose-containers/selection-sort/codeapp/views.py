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
    selection(x)
    print(x)

    return JsonResponse({'arr':x,'text':'this sorted array comes from selection sort-container!!!'})
    # return HttpResponse('You are in container 1!!! + Result : '+str(arr))

def selection(A):
    # Traverse through all array elements
    for i in range(len(A)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        A[i], A[min_idx] = A[min_idx], A[i]
