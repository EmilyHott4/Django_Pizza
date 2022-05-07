from django.shortcuts import render, redirect
from .models import Pizza
from .forms import Comment

# Create your views here.

def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()

    context = {'pizzas':pizzas}

    return render(request,'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    picture = Pizza.picture

    context = {'pizza':pizza,'toppings':toppings}

    return render(request, 'pizzas/pizza.html', context)

def new_comment(request, pizza_id):
    #topic_id is definedi n the url so it needs to be defined here as well
    pizza = Pizza.objects.get(id=pizza_id)
    #Uppercase T topic because it imports it form .models at the top of this file
    #lower case tpoic is just a variable name

    if request.method != 'POST':
        form = Comment()
    else:
        form = Comment(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)

    context = {'form':form}
    return render(request, 'pizzas/new_comment.html', context)