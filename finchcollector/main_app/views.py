from django.shortcuts import render

# Create your views here.

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.shortcuts import render

from .models import Creature


# define home view here - '/'
# GET - Home
def home(request):
    # unlike with ejs, we need our .html file extension
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# index view - shows all the cats at '/cats'
def creature_index(request):
    # just like in ejs, we can pass some data to our views
    creatures = Creature.objects.all()

    return render(request, 'creatures/index.html', { 'creatures': creatures })

def creature_detail(request, creature_id):
    #find one cat with its id
    creature = Creature.objects.get(id=creature_id)
    return render(request, 'creatures/detail.html', {'creature': creature})

# Using class-based views
class CreatureCreate(CreateView):
    model = Creature
    fields = '__all__'
    success_url = '/creatures/'
    
class CreatureUpdate(UpdateView):
    model = Creature
    fields = ['name', 'scientific_name', 'family', 'diet', 'description', 'habitat', 'picture', 'predators', 'prey', 'appearance']
    
    
class CreatureDelete(DeleteView):
    model = Creature
    success_url = '/creatures/'  
    
    