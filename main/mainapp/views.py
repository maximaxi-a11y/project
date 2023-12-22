from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message
import openai

def main(request):
    return render(request, 'mainapp/index.html')


# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         # Далее проводите необходимую обработку данных, например, сохранение пользователя в базу данных
#         # Или вызывайте вашу функцию регистрации

#         # Пример сохранения пользователя
#         user = User.objects.create_user(username=username, password=password)
#         user.save()

#         return HttpResponseBadRequest('127.0.0.1:8000/mainapp/')  # Перенаправление на страницу успешной регистрации
#     return render(request, 'auth/register_form.html')



# #def login(request):
#     #if request.method == 'POST':
#      #   username = request.POST.get('username')
#       password = request.POST.get('password')

#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             return HttpResponseBadRequest("Неверные логин или пароль.")

#         if user.check_password(password):
#             # Вход выполнен успешно
#             return JsonResponse({'message': 'Аутентификация успешна!'})

#     return HttpResponseBadRequest("Неверные логин или пароль.")

