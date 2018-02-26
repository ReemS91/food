from django.shortcuts import render
from .models import Hum
# Create your views here.
def hum_list(request):
	hums = hum.objects.all()
	context = {
	"list": hums,
	}
	return render (request, 'list.html', context)

def hum_detail(request, hum_id):
	hum = hum.objects.get(id=hum_id)
	context = {
	'object': hum
	}