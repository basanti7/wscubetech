from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service
# Method of --- Sending HttpResponse
# Use this method to urls.py file with your
# custom url


def aboutUs(request):
    return render(request, "about.html")


def homePage(request):
    service_data = Service.objects.all().order_by('service_title')
    # use loop inside html template to print all data
    for a in service_data:
        print(a.service_title)

    data = {
        'welcome_message': 'This is an welcome message from homePage(request) method located in views.py file. CSS file loaded from static for background color.',
        'simple_list': ['PHP', 'java', 'python'],
        'object_list': [{'name': 'Riton', 'designation': 'father'}, {'name': 'Soumik', 'designation': 'Son'}],
        'numbers': [1, 2, 3, 4, 5, 6, 8, 9, 99, 100],
        'service_data': service_data
    }
    return render(request, "index.html", data)


def services(request):
    return render(request, "service.html")


def courseDetails(request, courseId):
    return HttpResponse("Response from courseDetail - " + str(courseId))

def userForm(request):
    data = {}
    try:
        customer_name = request.GET['customer_name']
        customer_address = request.GET['customer_address']
        contact = request.GET['contact']
        data = {'customer_name':customer_name, 'customer_address' : customer_address, 'contact':contact}    
    except:
        pass
    return render(request, 'userform.html',data)

def userFormPost(request):
    data = {}
    try:
        customer_name = request.POST['customer_name']
        customer_address = request.POST['customer_address']
        contact = request.POST['contact']
        data = {'customer_name':customer_name, 'customer_address' : customer_address, 'contact':contact}
    except:
        pass
    return render(request, 'userform_post.html',data)
