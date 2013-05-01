# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse
from django.core import serializers
from world.models import World, Fortune
from django.shortcuts import render
import ujson
import random
from operator import attrgetter

def json(request):
  response = {
    "message": "Hello, World!"
  }
  return HttpResponse(ujson.dumps(response), mimetype="application/json")

def db(request):
  queries = int(request.GET.get('queries', 1))
  worlds  = []

  for i in range(queries):
    # get a random row, we know the ids are between 1 and 10000
    worlds.append(World.objects.get(id=random.randint(1, 10000)))

  return HttpResponse(serializers.serialize("json", worlds), mimetype="application/json")

def fortunes(request):
  fortunes = list(Fortune.objects.all())
  fortunes.append(Fortune(id=0, message="Additional message added at runtime."))

  fortunes = sorted(fortunes, key=attrgetter('message'))

  context = {'fortunes': fortunes}
  return render(request, 'fortunes.html', context)
