from django.shortcuts import render, redirect

from swideaSite.models import Devtool, Idea

# Create your views here.
def main(request):
    sort = request.GET.get('sort', None)
    if sort == "name":
        ideas = Idea.objects.all().order_by('title')
    elif sort == "recent":
        ideas = Idea.objects.all().order_by('updated_at')
    elif sort == "postly":
        ideas = Idea.objects.all().order_by('created_at')
    else:
        ideas = Idea.objects.all()
    context={
        "ideas":ideas
    }
    return render(request, template_name="sites/main.html", context=context)

def ideacreate(request):
    if request.method =="POST":
        print(request.POST)
        title = request.POST["title"]
        req_image = request.FILES["image"]
        content = request.POST["content"]
        interest = request.POST["interest"]
        devtname = request.POST["devtool"]
        devtool = Devtool.objects.get(name=devtname)

        Idea.objects.create(title=title, image=req_image, content=content, interest=interest, devtool=devtool)
        return redirect("/")
    devtools = Devtool.objects.all()
    context = {
        "devtools":devtools
    }

    return render(request, template_name="sites/ideacreate.html", context=context)

def ideaupdate(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        req_image = request.FILES["image"]
        content = request.POST["content"]
        interest = request.POST["interest"]
        devtname = request.POST["devtool"]
        devtool = Devtool.objects.get(name=devtname)

        Idea.objects.filter(id=id).update(title=title, image=req_image, content=content, interest=interest, devtool=devtool)
        return redirect("/")

    elif request.method == "GET":
        idea = Idea.objects.get(id=id)
        devtools = Devtool.objects.all()
        devt_name = idea.devtool.name
        context={"idea":idea,
        "devt_name":devt_name,
        "devtools":devtools,
        }
        return render(request, template_name="sites/ideaupdate.html", context=context)

def ideadetail(request, id):
    idea = Idea.objects.get(id=id)
    devt_name = idea.devtool.name

    context={
        "idea":idea,
        "devt_name":devt_name,
    }
    return render(request, template_name="sites/ideadetail.html", context=context)

def ideadelete(request, id):
    if request.method == "POST":
        idea = Idea.objects.get(id=id)
        idea.delete()
        return redirect("/")

def devtcreate(request):
    if request.method =="POST":
        print(request.POST)
        name = request.POST["name"]
        kind = request.POST["kind"]
        content = request.POST["content"]

        Devtool.objects.create(name=name, kind=kind, content=content)
        return redirect("/devtlist")
        
    context = {
    }

    return render(request, template_name="sites/devtcreate.html", context=context)

def devtlist(request):
    devtools = Devtool.objects.all()
    context={
        "devtools":devtools
    }
    return render(request, template_name="sites/devtlist.html", context=context)

def devtdetail(request, id):
    devtool = Devtool.objects.get(id=id)

    all_idea = devtool.tool_name.all()
    context={
        "devtool":devtool,
        "all_idea":all_idea,
    }
    return render(request, template_name="sites/devtdetail.html", context=context)

def devtupdate(request, id):
    if request.method =="POST":
        print(request.POST)
        name = request.POST["name"]
        kind = request.POST["kind"]
        content = request.POST["content"]

        Devtool.objects.filter(id=id).update(name=name, kind=kind, content=content)
        return redirect("/devtlist")

    elif request.method == "GET":
        devtool = Devtool.objects.get(id=id)
        context={
            "devtool":devtool
        }
        return render(request, template_name="sites/devtupdate.html", context=context)

def devtdelete(request, id):
    if request.method == "POST":
        devtool = Devtool.objects.get(id=id)
        devtool.delete()
        return redirect("/devtlist")