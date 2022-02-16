from django.forms import EmailField
from django.http import HttpResponse
from django.shortcuts import render
from accountdetail.database import Connection
from django.contrib import messages
# Create your views here.

def index(request):
    db=Connection()
    x,y=db.checkUser()
    context={'abc':y}
    if 'add' in request.POST:
        code = int(request.POST.get('code'))
        itemcode =request.POST.get('itemcode')
        barcode = request.POST.get('barcode')
        hsn = request.POST.get('hsn')
        name = request.POST.get('name')
        groupname = request.POST.get('groupname')
        amtqty = request.POST.get('amtqty')
        packagingunit = request.POST.get('packagingunit')
        loose = request.POST.get('loose')
        conv = request.POST.get('conv')
        crates = request.POST.get('crates')
        wholesale = request.POST.get('wholesale')
        retail = request.POST.get('retail')
        retailrt = request.POST.get('retailrt')
        sales = request.POST.get('sales')
        tax = request.POST.get('tax')
        taxontax = request.POST.get('taxontax')
        additionaltax = request.POST.get('additionaltax')
        salesgroup = request.POST.get('salesgroup')
        purchase = request.POST.get('purchase')
        reorderstock = request.POST.get('reorderstock')
        opstock = request.POST.get('opstock')
        maxrate = request.POST.get('maxrate')
        recorder = request.POST.get('recorder')
        loosestock = request.POST.get('loosestock')
        oprate = request.POST.get('oprate')
        opamount = request.POST.get('opamount')
        db=Connection()
        x,y=db.storeUser(code,itemcode,barcode,hsn,name,groupname,amtqty,packagingunit,loose,conv,crates,wholesale,retail,retailrt,sales,tax,taxontax,additionaltax,salesgroup,purchase,reorderstock,opstock,maxrate,recorder,loosestock,oprate,opamount)
        context={'abc':y}
        
        if(x==True): 
            return render(request, 'accountdetail.html',context)
        else:
            return HttpResponse('Try Again')
    elif 'update' in request.POST:
        code = int(request.POST.get('code'))
        itemcode = request.POST.get('itemcode')
        barcode = request.POST.get('barcode')
        hsn = request.POST.get('hsn')
        name = request.POST.get('name')
        groupname = request.POST.get('groupname')
        amtqty = request.POST.get('amtqty')
        packagingunit = request.POST.get('packagingunit')
        loose = request.POST.get('loose')
        conv = request.POST.get('conv')
        crates = request.POST.get('crates')
        wholesale = request.POST.get('wholesale')
        retail = request.POST.get('retail')
        retailrt = request.POST.get('retailrt')
        sales = request.POST.get('sales')
        tax = request.POST.get('tax')
        taxontax = request.POST.get('taxontax')
        additionaltax = request.POST.get('additionaltax')
        salesgroup = request.POST.get('salesgroup')
        purchase = request.POST.get('purchase')
        reorderstock = request.POST.get('reorderstock')
        opstock = request.POST.get('opstock')
        maxrate = request.POST.get('maxrate')
        recorder = request.POST.get('recorder')
        loosestock = request.POST.get('loosestock')
        oprate = request.POST.get('oprate')
        opamount = request.POST.get('opamount')
        db=Connection()
        x,y=db.updateUser(code,itemcode,barcode,hsn,name,groupname,amtqty,packagingunit,loose,conv,crates,wholesale,retail,retailrt,sales,tax,taxontax,additionaltax,salesgroup,purchase,reorderstock,opstock,maxrate,recorder,loosestock,oprate,opamount)
        if(x==True):
            context={'abc':y}
            return render(request, 'accountdetail.html',context)
        else:
            return render(request, 'accountdetail.html',context)
    elif 'delete' in request.POST:
        code = int(request.POST.get('code'))
        db=Connection()
        x,y=db.deleteUser(code)
        if(x==True):
            context={'abc':y}
            return render(request, 'accountdetail.html',context)
        else:
            return HttpResponse("User Not Found") 
    elif 'print' in request.POST:
        db=Connection()
        db.printData()
        x,y=db.checkUser()
        context={'abc':y}
        messages.success(request,"Printed Successfully")
        return render(request, 'accountdetail.html',context)
    return render(request, 'accountdetail.html',context)