from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic.edit import UpdateView
# from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from . models import Book,Create
from .forms import MyModelForm


def edit_Create(request, id):
    my_object = get_object_or_404(Create, pk=id)
    if request.method == 'POST':
        form = MyModelForm(request.POST, instance=my_object)
        if form.is_valid():
            form.save()
            messages.success(request, ' updated successfully')

            # redirect to success page or view
    else:
        form = MyModelForm(instance=my_object)
    return render(request, 'book/update.html', {'form': form})




# # Create your views here.
# def create(request):
#     return HttpResponse("Hello, world. You're at the book index")

# def index(request):
#     return render(request, 'book/index.html')

def index(request):
    mymodels = Create.objects.all()
    return render(request, 'book/index.html', {'mymodels': mymodels})

def create(request):
    if request.method == 'POST':

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        # mymodels = Create.objects.create(name=name, email=email, phone=phone)
        mymodels = Create(name=name, email=email, phone=phone)
        mymodels.save()
        # mymodels = Create.objects.all()
        # return render(request, 'book/index.html', {'mymodels': mymodels})
    return render(request, 'book/create.html')

def delete(request, id):
    users = get_object_or_404(Create, id=id)
    users.delete()
    messages.success(request, ' deleted successfully')
    return redirect('read')

    return render(request, 'book/delete.html')

def read(request):
    # users = get_object_or_404(Book, id=id)
    users = Create.objects.all()
    return render(request, 'book/read.html', {'users': users})