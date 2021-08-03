from django.shortcuts import render
from .models import alllist


# Create your views here.
def travel(request):
	return render(request, 'travel.html')
	
def Dhaka(request):
	return render(request, 'Dhaka.html')
def dynamicshow(request):
	return render(request, 'dynamicshow.html')
	
def Chittagong(request):
	return render(request, 'Chittagong.html')
	
def Barisal(request):
	return render(request, 'Barisal.html')
def Rajshahi(request):
	return render(request, 'Rajshahi.html')
	
def Khulna(request):
	return render(request, 'Khulna.html')
def Rangpur(request):
	return render(request, 'Rangpur.html')
	
def Sylhet(request):
	return render(request, 'Sylhet.html')
	
def showitem(request):
	uniquename=request.POST.get('name', ' ')
	allcontent=alllist.objects.filter(uname=uniquename)
	makedictionary={
		'detailsss':allcontent
	}
	return render(request, 'dynamicshow.html', context=makedictionary)
	
	
def searchItem(request):
	srcname=request.POST.get('searcitem',' ')
	contentsrc=alllist.objects.filter(uname=srcname)
	makedictionary={
		'detailsss':contentsrc
	}
	return render(request, 'dynamicshow.html', context=makedictionary)