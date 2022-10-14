from django.shortcuts import render,HttpResponseRedirect
from home.models import Todo

def home(request):
    if request.method == "POST":
        ne=request.POST.get('name','default')
        tle=request.POST.get('title','default')
        noe=request.POST.get('note','default')

        obj=Todo(name=ne,title=tle,note=noe)
        obj.save()
        return HttpResponseRedirect('/table/')
    return render(request,'home.html')

def table(request):
    t=Todo.objects.all()
    return render(request,'table.html',{'data':t})

def delete(request,id):
    obj=Todo(id=id)
    obj.delete()
    return HttpResponseRedirect('/table/')

def update(request,id):
    newid=id
    if request.method == "POST":
        ne=request.POST.get('name','default')
        tle=request.POST.get('title','default')
        noe=request.POST.get('note','default')
        obj=Todo(id=newid,name=ne,title=tle,note=noe)
        obj.save()
        return HttpResponseRedirect('/table/')

    obj=Todo.objects.get(pk=id)
    p={
        'id':newid,
        'name':obj.name,
        'title':obj.title,
        'note':obj.note,
    }
    return render(request,'update.html',p)   