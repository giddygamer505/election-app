from django.shortcuts import render,redirect
from .models import Candidate

# Create your views here.
def home_view(request):
    if request.method == 'POST':
        candidate_id = request.POST.get('candidate_id')
        candidate = Candidate.objects.get(id=candidate_id)
        candidate.votes += 1
        candidate.save()
        return redirect('.') 
    
    candidates = Candidate.objects.all()
    return render(request,'home.html',{'candidates' : candidates})
