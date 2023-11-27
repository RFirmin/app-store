from django.shortcuts import render, redirect

from .models import Requete

from .forms import RequeteForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.http import Http404, HttpResponseRedirect

from django.db.models import Q

from django.core.paginator import Paginator

# Create your views here.

@login_required
def index(request):
    user = request.user     
    demandes_user = Requete.objects.filter(user=user).order_by('id') 
    
    context = {
        'demandes' : demandes_user
    }
    
    return render(request, 'index.html', context)


@login_required
def warehouse(request):
    demandes = Requete.objects.all()
    demande_number = demandes.count()
    paginator = Paginator(demandes, 4)
    
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    
    message = f'{demande_number} Requêtes :'
        
    if demande_number == 1:
        message = f'{demande_number} Requête :'
    context = {
        'demandes': page_object,
        'message': message,
    }
    
    return render(request, 'warehouse.html', context)


@login_required
def details_request(request, id):
    details = Requete.objects.get(id=id)
    equipments = request.GET.get('equipment')
        
    context = {
        'details': details,
        'equipments': equipments,
    }
    
    return render(request, 'details_request.html', context)


@login_required
def new_request(request):
    
    if request.method =='POST':
        form = RequeteForm(request.POST)
        if form.is_valid(): 
            form = form.save(commit=False)
            form.user = request.user
            form.save()            
            return redirect('request:index')
        
    else:
        form = RequeteForm()
        
    context = {
        'form': form,
    }

    return render(request, 'new_request.html', context)


@login_required
def update_request(request, id):
    demande = Requete.objects.get(id=id)
    
    if demande.user == request.user:
        if request.method == 'POST':
            form = RequeteForm(request.POST, instance=demande)
            if form.is_valid():
                form.save()
                return redirect('request:index')
                
        else:
            form = RequeteForm(instance=demande)
    else:
        raise Http404
    
    context = {
        'form':form
    }
    return render(request, 'update_request.html', context)


@login_required
def search_request(request):
    search = request.GET.get('search')
    demandes = Requete.objects.filter(Q(project_code__icontains=search) |
                                      Q(staff_name__icontains=search))
    demande_number = demandes.count()
    
    message = f'{demande_number} Results :'
    
    if demande_number == 1:
        message = f'{demande_number} Result :'
        
    context = {
        'demandes': demandes,
        'message': message,
    }
    
    return render(request, 'search_request.html', context)