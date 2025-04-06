from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def gallery(request):
    photos=Photo.objects.all()
    categories=Category.objects.all()
    context={'catagories':categories,'photos':photos}
    return render(request, 'App/gallery.html',context)

def view(request,pk):
    photo=Photo.objects.get(id=pk)
    context={'photo':photo}
    return render(request,'App/photo.html',context)

def add(request):
    categories=Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')
    context={'catagories':categories}
    return render(request,'App/add.html',context)