from django.shortcuts import redirect
from django.urls import reverse

class AuthRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        path = request.path

        if user.is_authenticated and path in [reverse('login'), reverse('register')]:
            return redirect('dashboard')

        protected_paths = ['/dashboard/']
        if not user.is_authenticated and path in protected_paths:
            return redirect('landing')

        return self.get_response(request)