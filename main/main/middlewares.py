from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

class BlockedIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        blocked_ips = []

        
        ip = request.META.get('REMOTE_ADDR')


        if ip in blocked_ips:
            
            return HttpResponseForbidden(render(request, 'errors/forbidden.html'))

        response = self.get_response(request)
        return response
    





class RedirectToProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        rev = ['login', 'register']
        if request.user.is_authenticated and request.path == reverse('login'):
            return redirect('profile')  # здесь 'profile' - это имя URL для страницы профиля
        response = self.get_response(request)
        return response