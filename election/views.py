from django.shortcuts import render,redirect

# Create your views here.
def home_view(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request,'home.html')
