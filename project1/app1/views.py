from django.shortcuts import render,HttpResponse,get_object_or_404
from . models import temp_details,temp2_details

# Create your views here.
def su1(request):
    return HttpResponse("hai")
def su2(request):
    return  render(request, "template/temp.html")
def su3(request):
    cd = temp_details()
    cd.Name = request.POST.get("name")
    cd.School = request.POST.get("school")
    cd.Place = request.POST.get("place")
    cd.Phone_Number = request.POST.get("phone")
    cd.save()
    return render(request, "template/temp.html")
def su4(request):
    return render(request,"template/temp2.html")
def su5(request):
    return render(request,"template/q.html")

def su55(request):
    ed = temp2_details()
    ed.Name = request.POST.get("name")
    ed.Email = request.POST.get("email")
    ed.Number = request.POST.get("number")
    ed.How_Much = request.POST.get("much")
    ed.You_Order = request.POST.get("order")
    ed.Address = request.POST.get("address")
    ed.save()
    return render(request, "template/q.html")
def su6(request):
    return render(request,"template/p.html")
def su7(request):
    acd = temp2_details.objects.all()
    return render(request,"template/p.html",{"acd":acd})
def su8(request,id):
    ace = temp2_details.objects.get(id=id)
    ace.delete()
    acd = temp2_details.objects.all()
    return render(request,"template/p.html",{"acd":acd})
# def su9(request):
#     acd = temp2_details.objects.all()
#     return render(request,"template/p.html",{"acd":acd})
def su10(request):
    return render(request,"template/q.html")

def su11(request,id):
    acd = temp2_details.objects.get(id=id)
    return render(request, "template/q.html", {"acd": acd})

def su12(request):
    ade=""
    name = request.POST.get("name")
    ade = temp2_details.objects.get(name=name)
    if (ade!= ""):
        ade.Name = request.POST.get("name")
        ade.Number = request.POST.get("number")
        ade.How_Much = request.POST.get("much")
        ade.You_Order = request.POST.get("order")
        ade.Address = request.POST.get("address")
        ade.save()
        acd = temp2_details.objects.all()
    return render(request, "template/q.html",{"abc":abc})


