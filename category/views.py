from django.shortcuts import render,redirect,reverse
from .models import Category
from play.models import Play
from .forms import CategoryForm
from django.contrib import messages
# Create your views here


def show_all_cates(request):
    cates = Category.objects.all()
    context = {}
    context['cates'] = cates
    return render(request,'category/show_cates.html',context=context)

def show_cate_detail(request,slug):
    try:
        cate_obj = Category.objects.get(slug=slug)
        play_list = Play.objects.filter(cate=cate_obj)
        context = {
            "cate":cate_obj,
            "play_list":play_list,
        }
        return render(request,'category/show_cate_detail.html',context=context)
    except Category.DoesNotExist:
        return redirect(reverse('category:create_cate'))

def create_cate(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Create Successfully')
            return redirect(reverse('category:category_list'))
        else:
            messages.error(request,'fail to create')
    else:
        form = CategoryForm()
    context = {
        "form":form,
    }
    return render(request,'category/create_form.html',context=context)

def index(request):
    return render(request,'play/index.html')














