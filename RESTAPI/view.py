import json

import facebook
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render


def dashboard(request):
    return render(request,"dashboard.html")


def testAPI(request):
    #request.

    my_access_token = request.GET.get('token')#'EAACWZB7zVOZC8BAADGnlNPUXOiLzfOFu4dxJs6BwyJ3Ra5dA2isXYZBpZCMPYWfLLZCoN6wjE2MrYdyxUQL4wWmH83h6psk6yZBgdDTmg1WsRu46W8FomDzWZBhBmNXqxBxF3pZCM4Sed8hBBTZCfyQ0a9A2wDYyorp5OEf9rOwutJdqQZAxyWoii6vdPXZBam6pzcweBL9YYIZBea5tghmNm1mZBTYqEc7Uh1Idj224MpKOG9Y6OfXuVH0zd'
    graph= facebook.GraphAPI(my_access_token)
    profile= graph.get_object('me',fields='first_name,last_name,link,email,posts')


    print('Printing profile:')
    #print(type(profile))

    #print(json.dumps(profile, indent=5))
    #print(type(json.dumps(profile, indent=5)))



    return render(request, "testAPI.html",{"profile":json.dumps(profile, indent=5)})