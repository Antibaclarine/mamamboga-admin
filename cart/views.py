from django.shortcuts import render,redirect

from .models import Cart
from .forms import CartForm
# Create your views here.

def add_to_cart(request):
    if request.method =='POST':
        form=CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart_list')
        else:
            form =CartForm()
            return render (request,'create_cart.html',{'form':form})
        
def cart_list(request):
    cart = Cart.objects.all()
    return render(request, 'cart/cart_list.html', {'cart': cart})


