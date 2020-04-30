from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from to_do.models import Todo
from django.http import HttpResponseRedirect,HttpResponse


# Create your views here.
@csrf_exempt
def edit_link(request, todo_id):
  to_be_edited = Todo.objects.get(id=todo_id)
  return render(request, 'edit/edit.html', {
    "change" : to_be_edited
  })
@csrf_exempt
def edit_todo(request, todo_id):
  content = request.POST['content']
  current_date = timezone.now()
  edited_object = Todo.objects.get(id=todo_id)
  edited_object.text = content
  edited_object.added_Date = current_date
  edited_object.save()
  return HttpResponseRedirect('/')