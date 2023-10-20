
from django.contrib.auth import logout

class RestrictTemplateAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the session variable is present and restrict access
        if not request.session.get('allowed_access') and (request.path == '/activationSuccess/' or request.path == '/registrationSuccess/'):
            from django.shortcuts import redirect
            return redirect('accessDenied')
        elif request.session.get('allowed_access') and (request.path == '/registrationSuccess/' or request.path == '/activationSuccess/'):
            #Disallow access to registration success page
            request.session['allowed_access'] = False
            logout(request)

        return response