from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from .models import Product
from .forms import ProductForm


def product_create(request):
    initial_data = {
        'name': "My initial product name",
    }
    #obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, '''instance= obj''')
    if form.is_valid():
        form.save()
        form = ProductForm()
        
    context = {
        'form': form,
        }
    return render(request,'product/product_create.html', context)

# Create your views here.
def product_page(request):
    obj = Product.objects.get(id = 3)
    """
    context = {
        "title": obj.name,
        "desc": obj.description,
        "price": obj.price,
    }
    """
    context = {
        "object": obj
    }

    return render(request, "product/detail.html",context)

#look up dynamic url routing
def lookup_view(request, my_id):
    #obj = Product.objects.get(id = my_id)
    #obj = get_object_or_404(Product, id=my_id)
    try:
        obj = Product.objects.get(id = my_id)
    except Product.DoesNotExist:
        raise Http404 
    
    context  = {
        "object": obj
    }
    return render(request, "product/detail.html", context)

def product_delete(request, my_id):
    obj = Product.objects.get(id = my_id)

    if request.method == "POST":
        obj.delete()
        return redirect("../../")
    context ={
            "object": obj
        }
    return render(request,"product/delete.html", context)

def products_display(request):
    dataset  = Product.objects.all()
    context = {
        "products": dataset
    }
    return render(request, 'product/allprod.html', context)

'''def product_create(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            Product.objects.create(**my_form.cleaned_data)
            my_form = RawProductForm()
        else:
            my_form.errors

    context = {
        'form': my_form,
        }
    return render(request,'product/product_create.html' ,context)
'''