from django.shortcuts import render

from IS.menu.forms import MenuForm


# Create your views here.

def order(request,table):
    if request.method == 'POST':
        
        
        
        return render(request,"menu/order_succes.html")
    
    return render(request,"menu/order.html")
    
def alltable(request):
    
    return render(request,"menu/alltable.html")


def addmenu(request):
    if request.method=='POST':
        menu=MenuForm(request.get["name"],request.get["price"],request.get["type"],request.FILES)
        if menu.is_valid():
            menu.save()
            
            return render(request,"menu/addmenu.html")
        
    return render(request,"menu/addmenu.html")