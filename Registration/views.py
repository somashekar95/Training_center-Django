from django.shortcuts import render
from django.http import HttpResponse
from Registration.models import Course,Batch,Student

# Create your views here.
def index(Request):
    return HttpResponse("<h1>Welcome to Prime Intuit Registartion page</h1>")


def Home(Request):
    # return HttpResponse("<h1>Welcome to Prime Intuit Home page</h1>")
    # my_dict={'Insert_Me':" I am a text from Registration/views.py subtemplates"}
    batch_list=Batch.objects.raw('select * from  Registration_Batch ')
    data_dict={'access_record':batch_list,'Insert_Me':" I am a text from Registration/views.py subtemplates"}
    return render(Request,'Registration/index.html',context=data_dict)




