from django.shortcuts import render,redirect
from .models import Candidate

# Create your views here.
def home_view(request):
    if request.method == 'POST':
        return redirect('home')
    candidates = Candidate.objects.all()
    return render(request,'home.html',{'candidates' : candidates})
