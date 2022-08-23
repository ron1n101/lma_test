from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages

from django.views.generic import ListView, DetailView, CreateView

class HomeListView(ListView):
    model = Home
    template_name = 'shop/index.html'
    context_object_name = 'gallerys'

class ProductListView(ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'
    queryset = Product.objects.all()

class ProductDetailView(DetailView):
    model = Product
    slug_field = 'slug'




def feedback(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Feedback/Contact/Trouble'
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            html = render_to_string('shop/emails/contactforms.html', {
                'name': name,
                'email':email,
                'message':message
            })


            # mail = send_mail(subject, message, 'noreply@leavemealone.boutique', ['dev.ron1n2k@gmail.com'], html_message=html, fail_silently=True)
            # if mail:
            #     messages.success(request, 'Письмо отправлено!')
            # else:
            #     messages.error(request, 'Ваше письмо не было отправлено')
            try:
                send_mail(subject, message, 'noreply@leavemealone.boutique', ['LEAVEMEALONE', 'dev.ron1n2k@gmail.com'], html_message=html)
            except BadHeaderError:
                return HttpResponse('fail header')
            return redirect("home")
            
        


    form = ContactForm()
    return render(request, 'shop/feedback.html', {'form':form})

def get_product(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        context = {'product':product}
        if request.GET.get('size'):
            size = request.GET.get('size')
            context['selected_size'] = size
        return render(request, 'shop/products.html', context=context)

    except Exception as E:
        print(e)