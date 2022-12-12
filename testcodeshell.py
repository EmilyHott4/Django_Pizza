import imp
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza

pizzas = Pizza.objects.all()

for p in pizzas:
    print(p.id, '  ', p)

p = Pizza.objects.get(id=1)

print(p.id)
print(p.pizza_name)

toppings = p.topping_set.all()
for t in toppings:
    print(t.topping_name)

    