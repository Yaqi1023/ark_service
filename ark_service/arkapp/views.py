from django.shortcuts import render
from django.http import HttpResponse, Http404

from ark.models import Ark, Minter


# Create your views here.
def mint(request, minter_id, quantity)
    minter = get_object_or_404(Minter, pk = minter_id)
    return minter.mint(quantity = quantity)

def bind(request, key, url):
	ark = get_object_or_404(Ark, key = key)
	ark.url = url
	ark.save
	return ark

def resolve(request, key):
    ark = get_object_or_404(Ark, key = key)
    return HttpResponse(ark.url)