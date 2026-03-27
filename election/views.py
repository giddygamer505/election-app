from django.shortcuts import render,redirect
from .models import Candidate,Voter
from django.contrib import messages

# Create your views here.
def home_view(request):
    if request.method == 'POST':
        candidate_id = request.POST.get('candidate_id')
        candidate = Candidate.objects.get(id=candidate_id)
        candidate.votes += 1
        candidate.save()
        return redirect('home') 
    
    candidates = Candidate.objects.all()
    return render(request,'home.html',{'candidates' : candidates})

def login_view(request):
    return render(request,'login.html')   
