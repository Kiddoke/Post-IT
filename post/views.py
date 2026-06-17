from django.shortcuts import render, redirect
from .models import PostIT
# Create your views here.



def tavle(request):
    if request.method == 'POST':
        tittel = request.POST.get('tittel')
        innhold = request.POST.get('innhold')
        PostIT.objects.create(tittel = tittel, innhold = innhold)
        return redirect('tavle')
    
    forslag = PostIT.objects.all().order_by('-opprettet')
    return render(request, 'post/tavle.html', {'forslag' : forslag})

