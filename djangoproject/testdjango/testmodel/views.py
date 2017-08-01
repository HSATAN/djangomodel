from django.shortcuts import render
from django.http import HttpResponse
from .models import Test
from .forms import NameForm
import django
from django.core.urlresolvers import reverse
# Create your views here.
def index(response):
    return render(response,'index.html')

def adddb(request):
    print(request.COOKIES)
    if request.method=="GET":
        form=NameForm()
        return render(request,'addname.html',{'form':form})
    name=request.POST.get('name','detaulst')
    test=Test(name=name)
    test.save()
    return django.http.HttpResponseRedirect(reverse("testmodel:allname"))
    return HttpResponse("添加数据记录成功")
    pass
def private(request):
    return django.http.HttpResponseForbidden('<h1>Forbudden</h1>')


def allname(request):
    names=Test.objects.all().order_by('-id')
    return render(request,'allname.html',context={'names':names})