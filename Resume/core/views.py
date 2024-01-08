from django.shortcuts import render, redirect
from .forms import StudentRegisteration
from .models import User
from django.contrib import messages

# Create your views here.
def home(request):
    context={'home': 'active'}
    return render(request,'core/home.html',context)

def contact(request):
    if request.method == 'POST':
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            # Save the form data
            fm.save()
            messages.add_message(request, messages.SUCCESS,'Your Data have been Submitted Successfully!!!')
    else:
        fm = StudentRegisteration()
    return render(request, 'core/contact.html', {'form': fm})
