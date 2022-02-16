from django import http
from django.forms import EmailField
from django.http import HttpResponse
from django.shortcuts import render
from accountprofile.database import Connection
from django.contrib import messages
# Create your views here.


def index(request):
    db=Connection()
    x,y=db.checkUser()
    context={'abc':y}
    
    if 'add' in request.POST:
        code = int(request.POST.get('code'))
        first = request.POST.get('first')
        middle = request.POST.get('middle')
        last = request.POST.get('last')
        address = request.POST.get('address')
        ap = request.POST.get('ap')
        village = request.POST.get('village')
        city = request.POST.get('city')
        taluka = request.POST.get('taluka')
        district = request.POST.get('district')
        state = request.POST.get('state')
        aadhar = request.POST.get('aadhar')
        phone = request.POST.get('phone')
        db=Connection()
        x,y=db.storeUser(code,first,middle,last,address,ap,village,city,taluka,district,state,aadhar,phone)
        context={'abc':y}
        if(x==True): 
            return render(request, 'accountpage.html',context)
        else:
            return HttpResponse('Try Again')

    elif 'update' in request.POST:
        code = int(request.POST.get('code'))
        first = request.POST.get('first')
        middle = request.POST.get('middle')
        last = request.POST.get('last')
        address = request.POST.get('address')
        ap = request.POST.get('ap')
        village = request.POST.get('village')
        city = request.POST.get('city')
        taluka = request.POST.get('taluka')
        district = request.POST.get('district')
        state = request.POST.get('state')
        aadhar = request.POST.get('aadhar')
        phone = request.POST.get('phone')
        db=Connection()
        x,y=db.updateUser(code,first,middle,last,address,ap,village,city,taluka,district,state,aadhar,phone)
        if(x==True):
            context={'abc':y}
            return render(request, 'accountpage.html',context)
        else:
            return render(request, 'accountpage.html',context)

    elif 'delete' in request.POST:
        code = int(request.POST.get('code'))
        db=Connection()
        x,y=db.deleteUser(code)
        if(x==True):
            context={'abc':y}
            return render(request, 'accountpage.html',context)
        else:
            return HttpResponse("User Not Found")

    elif 'print' in request.POST:
        db=Connection()
        db.printData()
        x,y=db.checkUser()
        context={'abc':y}
        return render(request, 'accountpage.html',context)
    return render(request, 'accountpage.html',context)