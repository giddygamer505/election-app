from django.shortcuts import render, redirect
from .models import Candidate, Voter
from django.contrib import messages

def home_view(request):
    v_id = request.session.get('voter_id')
    if not v_id:
        return redirect('login')

    if request.method == 'POST':
        candidate_id = request.POST.get('candidate_id')
        voter, created = Voter.objects.get_or_create(voter_id=v_id)

        if voter.has_voted:
            messages.error(request, "คุณได้ใช้สิทธิ์โหวตไปแล้ว")
        else:
            candidate = Candidate.objects.get(id=candidate_id)
            candidate.votes += 1
            candidate.save()
            voter.has_voted = True
            voter.save()
            messages.success(request, "โหวตสำเร็จ")
        return redirect('home')

    candidates = Candidate.objects.all()
    return render(request, 'home.html', {'candidates': candidates, 'voter_id': v_id})

def login_view(request):
    if 'voter_id' in request.session:
        return redirect('home')

    if request.method == 'POST':
        v_id = request.POST.get('voter_id')
        if v_id:
            request.session['voter_id'] = v_id
            return redirect('home')
            
    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')