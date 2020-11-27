from django.shortcuts import render
from django.http import JsonResponse
import psycopg2
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
    try:
        connection = psycopg2.connect(user = "postgres",
                                    password = "password",
                                    host = "db",
                                    port = "5432",
                                    database = "postgres")
        postgreSQL_select_Query = "SELECT codeinput FROM codeapp_codeinput where code_type='sorting';"
        cursor = connection.cursor()
        cursor.execute(postgreSQL_select_Query)
        s=cursor.fetchone()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")
        
        s=str(s)
        s=s.replace("('","")
        s=s.replace("',)","")
        print(s)
        lisofintnum=s.split(",")
        for i in range(0,len(lisofintnum)):
            lisofintnum[i]=int(lisofintnum[i])
        selection(lisofintnum)
        verify_str=''
        for i in lisofintnum:
            verify_str+=str(i)
            verify_str+=', '
        return JsonResponse({'arr':str(verify_str),'text':'Selection Sort Container'})
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
        return JsonResponse({'arr':'Error','text':'Selection Sort Container'})
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return JsonResponse({'arr':'Error','text':'Selection Sort Container'})

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