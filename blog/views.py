from django.shortcuts import render
from django.http import HttpResponse

students = [
    {
        'stud_name': 'Kanishq',
        'class': '6N',
        'school': 'DPS'
    },
    {
        'stud_name': 'Tanay',
        'class': '6B',
        'school': 'DPS'
    }
]


def home(request):
    context = {
        'stds': students,
        'title' : "Myhome"
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse("eh")


def about(request):
    return render(request, 'blog/about.html',{'title': "About Me"})
