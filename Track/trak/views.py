from rest_framework.views import APIView
from rest_framework.response import Response
from .models import task

# def main(request):
#     quests = quest.objects.all()
#     if request.method == "POST":
#         nameQu = request.POST.get('nameQu')
#         comments = request.POST.get('comments')
#         exp = request.POST.get('exp')
#         quest.objects.create(nameQu=nameQu, comments=comments, exp=exp)
#     return render(request,'trak/main.html',{'quests':quests})
# def deleters(request,id):
#         Quest = quest.objects.get(id=id)
#         Quest.delete()
#         return HttpResponseRedirect('/')


class TaskAPI(APIView):
   def get_object(self, pk):
      try:
         return task.objects.get(pk=pk)
      except task.DoesNotExist:
            return Response({'message':'Ошибка'})
   def get(self, req):
      t = task.objects.all().values()
      return Response({'task':list(t)})

   def post(self,request):
      nTask = task.objects.create(
         title= request.data['title'],
         desc = request.data['desc'],
         exp = request.data['exp']
      )
      return Response({'message':'Задача добавлена'})
   def delete(self, request, pk):
      s = self.get_object(pk)
      s.delete()
      return Response({'message':'Удалено'})
   def put(self, request, pk):
      s = self.get_object(pk)
      s.done = True
      s.save(update_fields=['done'])
      return Response({'message':'Успех'})
