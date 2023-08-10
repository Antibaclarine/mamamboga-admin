from django.shortcuts import render,redirect
from .forms import BasketForm

def create_basket(request):
    if request.method =='POST':
        form=BasketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect( 'basket_list')
    else:
            form =BasketForm()
            return render(request, 'basket/basket_form.html', {'form':form})
