from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

userModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = userModel.objects.get(email=username)
        except userModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
    

    def get_user(self, user_id):
        try:
            return userModel.objects.get(pk=user_id)
        except userModel.objects.get(pk=user_id):
            return None