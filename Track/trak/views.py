from django.shortcuts import render
from trak.models import quest

def main(request):
    context = {
        'quests': quest.objects.all()
    }
    if request.method == "POST":
        nameQu = request.POST.get('nameQu')
        comments = request.POST.get('comments')
        exp = request.POST.get('exp')
        quest.objects.create(nameQu=nameQu, comments=comments, exp=exp)
    return render(request,'trak/main.html', context)