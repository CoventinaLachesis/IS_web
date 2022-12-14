from django.shortcuts import render
from django.contrib.auth import get_user_model

from .forms import *

User =get_user_model()
# Create your views here.

def order(request,table):
    if request.method == 'POST':
        
        form = OrderForm(request.POST,request.FILES)
        print("FORM")
        print(form)
        if form.is_valid():
            if not Table_Order.objects.filter(table_number=table).exists():
                print("NEW TABLE")
                # Table_Order.objects.create(table_number=table)
                data = form.cleaned_data
                new_order = Table_Order()
                new_order.table_number = table
                new_order.ordermenu.set(data['ordermenu'])
            
            # item = menu.cleaned_data['ordermenu']
            # instance = menu.save(commit=False)
            # instance.table_number = Table_Order.objects.get(table_number=table)
            # instance.save()
            # for i in item:
            #     instance.ordermenu.add(i)

            
            return render(request,"menu/order_succes.html")
            
    else:
        form = OrderForm()
            
    return render(request,"menu/order.html",{"form":form})
    
def alltable(request):
    table=Table_Order.objects.all()
    for i in table:
        print(str(i.table_number))
        print(i.ordermenu.all())
    return render(request,"menu/alltable.html",{"table":reversed(table)})


def addmenu(request):
    if request.method=='POST':
        menu=MenuForm(request.POST,request.FILES)
        if menu.is_valid():
            menu.save()
            
    else:
        menu = MenuForm()
    return render(request, "menu/addmenu.html", {"menu": menu})


def home(request):
    
    return render(request,"menu/home.html")
