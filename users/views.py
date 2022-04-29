from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


# Create your views here. hello999##R

def register(request):
    form = UserCreationForm()
    return render (request, "users/register.html", {'form': form})

