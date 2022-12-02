from django.shortcuts import render
from django.http import HttpResponse
from .models import colorcombos
from json import dumps
c1 = None
c2 = None
def index(request):
	return render(request,'shit.html')
def vote(request):
	global c1,c2
	if request.method == 'GET':
		if request.GET.get('colorcombo1',None) != None:
			cc1 = request.GET.get('colorcombo1',None)
			if c1 != None and c2!= None:
				# The Elo ranking Algorithm
				deltac1 = 1/(1+10**((float(c2.rating) - float(c1.rating))/400))
				deltac2 = 1/(1+10**((float(c1.rating) - float(c2.rating))/400))
				c1.rating = float(c1.rating) - deltac1
				c2.rating = float(c2.rating) + deltac2
				c1.save()
				c2.save()
			if colorcombos.objects.filter(title=cc1).exists():
				c1 = colorcombos.objects.get(title=cc1)
			else:
				c1 = colorcombos(title=cc1)
				c1.save()
		if request.GET.get('colorcombo2',None) != None:
			cc2 = request.GET.get('colorcombo2',None)
			if c1 != None and c2!= None:
				deltac1 = 1/(1+10**((float(c2.rating) - float(c1.rating))/400))
				deltac2 = 1/(1+10**((float(c1.rating) - float(c2.rating))/400))
				c1.rating = float(c1.rating) + deltac1
				c2.rating = float(c2.rating) - deltac2
				c1.save()
				c2.save()
			if colorcombos.objects.filter(title=cc2).exists():
				c2 = colorcombos.objects.get(title=cc2)
			else:
				c2 = colorcombos(title=cc2)
				c2.save()
		return HttpResponse("Success!")
	else:
		return HttpResponse("Request method is not a GET")
def results(request):
	leads = colorcombos.objects.order_by('-rating')
	leadDict= {}
	for i in leads:
		leadDict[i.title] = float(i.rating)
	leadDict = dumps(leadDict)
	return render(request,"leads.html", {"data":(leadDict)})  