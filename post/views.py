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
    kolonner = [
        ('ny', 'bg-green-200', 'Ny'),
        ('under_vurdering', 'bg-yellow-200', 'Under vurdering'),
        ('konkludert', 'bg-red-200', 'Konkludert'),
    ]
    return render(request, 'post/tavle.html', {'forslag':forslag, 'kolonner':kolonner})

def oppdater_status(request, id): 
    if request.method == 'POST':
        post = PostIT.objects.get(id=id)
        post.status = request.POST.get('status')
        post.save()
        
        return redirect('tavle')
    
def slett(request, id): 
    if request.method == 'POST':
        PostIT.objects.get(id=id).delete()
        
        return redirect('tavle')