from django.shortcuts import render, redirect

from .models import Return

from .forms import ReturnForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.http import Http404, HttpResponseRedirect

from django.db.models import Q

from django.core.paginator import Paginator

# Create your views here.

@login_required
def index_return(request):
    user = request.user     
    demandes_user = Return.objects.filter(user=user).order_by('id') 
    
    context = {
        'demandes' : demandes_user
    }
    
    return render(request, 'index_return.html', context)


@login_required
def warehouse_return(request):
    demandes = Return.objects.all()
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
    
    return render(request, 'warehouse_return.html', context)


@login_required
def details_return(request, id):
    details = Return.objects.get(id=id)
    # type_service = request.GET.get('type_service')
    # checkbox = request.GET.get('checkbox')
    
    context = {
        'details': details,
    }
    
    return render(request, 'details_return.html', context)


@login_required
def new_return(request):
    
    if request.method =='POST':
        form = ReturnForm(request.POST)
        if form.is_valid(): 
            form = form.save(commit=False)
            form.user = request.user
            form.save()            
            return redirect('return:index_return')        
    
    else:
        form = ReturnForm()
        
    context = {
        'form': form,
    }
    
    return render(request, 'new_return.html', context)


@login_required
def update_return(request, id):
    demande = Return.objects.get(id=id)
    
    if demande.user == request.user:
        if request.method == 'POST':
            form = ReturnForm(request.POST, instance=demande)
            if form.is_valid():
                form.save()
                return redirect('return:index_return')
                
        else:
            form = ReturnForm(instance=demande)
    else:
        raise Http404
    
    context = {
        'form':form
    }
    return render(request, 'update_return.html', context)


@login_required
def search_return(request):
    search = request.GET.get('search')
    demandes = Return.objects.filter(Q(project_code__icontains=search) |
                                      Q(staff_name__icontains=search))
    demande_number = demandes.count()
    
    message = f'{demande_number} Results :'
    
    if demande_number == 1:
        message = f'{demande_number} Result :'
        
    context = {
        'demandes': demandes,
        'message': message,
    }
    
    return render(request, 'search_return.html', context)
