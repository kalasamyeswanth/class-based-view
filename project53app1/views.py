from django.shortcuts import render, HttpResponse
from django.views import View
# Create your views here.
def link1(request):
    if request.method == 'GET':
        return HttpResponse('happy to see this')

class viewclass(View):
    def get(self, request):
        return HttpResponse('this is a http responce of class based views in get method')


class viewclass2(View):
    def post(self,request):
        return HttpResponse('this is a http responce of class based vies in post method')

class viewclass3(View):
    def get(self, request):
        return render(request,'happy.html')
