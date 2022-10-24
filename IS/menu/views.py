from django.shortcuts import render


def order(request,table):
    if request.method == 'POST':
        return render(request,"menu/order_succes.html")
    
    return render(request,"menu/order.html")
    
def alltable(request):
    
    return render(request,"menu/alltable.html")
# Create your views here.
