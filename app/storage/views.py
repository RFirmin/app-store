from django.shortcuts import render, redirect

from .models import Equipment, Storage, Routeur

from .forms import EquipmentForm, StorageForm, RouteurForm, DeleteStorageForm 
# SerieStorageForm

from django.contrib.auth.decorators import login_required

from request.models import Requete

from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound, HttpResponse

from django.db.models import Q

from django.core.paginator import Paginator

# Create your views here.

def custom_404(request, exception):
    return render(request, '404.html', status=404)

@login_required
def all_equipments(request):
    equipments = Storage.objects.all()
    equipments_number = equipments.count()
    paginator = Paginator(equipments, 6)
    
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    
    message = f'{equipments_number} equipments :'
        
    if equipments_number == 1:
        message = f'{equipments_number} equipment :'
    context = {
        'equipments': page_object,
        'message': message,
    }
    
    return render(request, 'all_equipments.html', context)


@login_required
def all_elements(request):
    equipments = Equipment.objects.all()
    equipments_number = equipments.count()
    paginator = Paginator(equipments, 6)
    
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    
    message = f'{equipments_number} equipments :'
        
    if equipments_number == 1:
        message = f'{equipments_number} equipment :'
    
    context = {
        'equipments': page_object,
        'message': message,
    }
    
    return render(request, 'all_elements.html', context)


@login_required
def details_equipment(request, id):
    
    details = Storage.objects.get(number=id)
    
    context = {
        'details' : details
    }
    
    return render(request, 'details_equipment.html', context)
        

@login_required
def new_equipment(request):
        
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('storage:all_equipments')
   
    else:
        form = StorageForm()
        
    context = {
        'form': form,
    }
    return render(request, 'new_equipment.html', context)


@login_required
def new_element(request):

    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('storage:all_equipments')
   
    else:
        form = EquipmentForm()
    
    context = {
        'form':form
    }
    return render(request, 'new_element.html', context)


@login_required
def choice_element(request):
    pass
    demandes = Equipment.objects.all() 
    
    context = {
        'demandes': demandes,
    }
    return render(request, 'choice_element.html', context)


@login_required
def update_equipment(request, id):
    demande = Storage.objects.get(number=id)
    
    if request.method == 'POST':
        form = StorageForm(request.POST, instance=demande)
        if form.is_valid():
            form.save()
            return redirect('storage:all_equipments')
                
    else:
        form = StorageForm(instance=demande)
    
    context = {
        'form':form
    }
    return render(request, 'update_equipment.html', context)


@login_required
def delete_equipment(request, id):
    demande = Storage.objects.get(number=id)
    demande.delete()
    return redirect('storage:all_equipments')
#    return render(request, 'delete_equipment.html')


@login_required
def get_equipment(request):
    form = DeleteStorageForm()
    equipments = Equipment.objects.all()
    
    context = {
        'form': form,
        'equipments': equipments
    }
    return render(request, 'afficher_equipment.html', context)


@login_required
def load_serie(request):
    show_id = request.GET.get("show")
    print(show_id)
    series = Storage.objects.filter(show_id=show_id)
    print(series)
    
    context = {
        'series' : series
    }
    return render(request, 'serie_options.html', context)


@login_required
def graphic(request):
    demandes = Routeur.objects.all()
    
    context = {
        'demandes' : demandes
    }
    return render(request, 'graphic.html', context)


@login_required
def state(request):
    state = Storage.objects.all()
    
    context = {
        'routeurs' : state
    }
    
    return render(request, 'state.html', context)


@login_required
def routeur(request):
    routeurs = Routeur.objects.all()
    
    context = {
        'routeurs' : routeurs
    }
    
    return render(request, 'routeurs.html', context)


@login_required
def new_routeur(request):

    if request.method == 'POST':
        form = RouteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('storage:all_equipments')
            
    else:
        form = RouteurForm()
    
    context = {
        'form':form
    }
    return render(request, 'new_routeur.html', context)


@login_required
def search_equipment(request):
    search = request.GET.get('search')
    demandes = Storage.objects.filter(Q(description_equipment__icontains=search) |
                                      Q(projet__icontains=search) | 
                                      Q(date_de_livraison=search))
    demande_number = demandes.count()
    
    message = f'{demande_number} Results :'
    
    if demande_number == 1:
        message = f'{demande_number} Result :'
        
    context = {
        'demandes': demandes,
        'message': message,
    }
    
    return render(request, 'search_equipment.html', context)
