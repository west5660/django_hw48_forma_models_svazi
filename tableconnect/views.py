from django.shortcuts import render, redirect
from .models import *
from .myforms import *


def index(req):
    return render(req, 'index.html')


def add(req):
    # Company.objects.create(title='J7')
    # Company.objects.create(title='DOBRY')
    p1 = Product(name='orange', price=140, volume=1, packaging='banka', is_recommended='Рекомендованно ГОСТ')
    p2 = Product(name='multy', price=150, volume=2, packaging='korobka', is_recommended='Рекомендованно ГОСТ')
    p3 = Product(name='apple', price=160, volume=3, packaging='bytilka', is_recommended='Товар не проверен')
    c1 = Company.objects.get(title='J7')
    c2 = Company.objects.get(title='DOBRY')
    c1.product_set.add(p1, bulk=False)
    c1.product_set.add(p2, bulk=False)
    c1.product_set.add(p3, bulk=False)
    print(c1.product_set.count())
    print(c1.product_set.values())
    print(c1.product_set.values_list())
    return redirect('index')


def table1(req):
    baza = Product.objects.all()
    anketa = FormJuice()
    print(Company.objects.values_list('title', flat=False))
    bd = []
    for i in baza:
        is_recommended = "✔" if i.is_recommended else "✘"
        bd.append((i.name, i.price, i.firma.title, i.volume, i.packaging, is_recommended))
    title = ('Название', 'Цена', 'Фирма','Объем в литрах','Упаковка','Рекомендация')
    data = {'table': bd, 'title': title, 'forma': anketa}
    return render(req, 'totable.html', context=data)