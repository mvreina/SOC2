from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.core.cache import cache

User = get_user_model()

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the user is locked out
            cache_key = f'login_attempts:{username}'
            login_attempts = cache.get(cache_key, 0)

            if login_attempts == 2:
                print(login_attempts)
                user = User.objects.filter(username=username).first()
                user.is_active = False
                user.save()
                cache.set(cache_key, login_attempts + 1)
                return None  # Lock the user out

            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):
                # If login is successful, reset login attempts
                cache.delete(cache_key)
                return user
            else:
                # If login fails, increment login attempts
                #cache.set(cache_key, login_attempts + 1, timeout=3600)  # Lockout for 1 hour
                cache.set(cache_key, login_attempts + 1)
                return None
        except User.DoesNotExist:
            return None