from django.shortcuts import render
from django.http import JsonResponse
from .models import QuestionModel
def index(request):
    if request.method == 'GET':
      data = {'data':'this is data'}
      return JsonResponse(data=data)

def get_all(request):
    if request.method =='GET':
        all_data = QuestionModel.object.all()
        result = []
        for question in all_data:
            result.append({'id':question.id,
                           'question_text':question.question_text,
                           'pub_date':question.pub_date})
        return JsonResponse(result)

def get_by_index(request):
    if request.method =='GET':
        try:
            data = QuestionModel.object.get(id=question_id)
        except QuestionModel.DoesNotExist:
            return JsonResponse({'msg':'Qusf gdsn  kom'})
        return JsonResponse({'id':data.id,
                             'question_text':data.question_text,
                             'pub_date':data.pub_date})