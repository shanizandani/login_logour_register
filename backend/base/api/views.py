# from django.http import JsonResponse
# from rest_framework import permissions
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView


# from .serializers import NoteSerializer
# from base.models import Note


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         # ...

#         return token


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         '/api/token',
#         '/api/token/refresh',
#     ]

#     return Response(routes)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getNotes(request):
#     user = request.user
#     notes = user.note_set.all()
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)





from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions  import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import  UserRegistrationSerializer   
# from base.models import Note
from rest_framework import status



from rest_framework.views import APIView
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from .serializers import ForgotPasswordSerializer


# --------------------------------
from django.utils.crypto import get_random_string




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView) :
    serializer_class= MyTokenObtainPairSerializer  


@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/token',
        '/api/token/refresh'
    ]

    return Response(routes)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getNotes(request):
#    user = request.user
#    notes = user.note_set.all()
#    seralizer = NoteSerializer(notes, many=True)
#    return Response(seralizer.data)


@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --------------------------------------------------------------

# class ForgotPasswordView(APIView):
#     def post(self, request):
#         serializer = ForgotPasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             try:
#                 user = User.objects.get(email=email)
#                 token = get_random_string(length=32)
#                 user.reset_token = token  # Store token in user's profile or temporary table
#                 user.save()

#                 subject = 'Password Reset'
#                 message = f'Click the link to reset your password: http://localhost:3000/reset-password/{token}'

#                 from_email = 'shanilevi88761234@gmail.com'
#                 recipient_list = [email]
#                 send_mail(subject, message, from_email, recipient_list, fail_silently=False)

#                 return Response({'message': 'Email sent with reset instructions.'})
#             except User.DoesNotExist:
#                 return Response({'message': 'No user with that email.'})
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
                token = get_random_string(length=32)
                user.reset_token = token  # Store token in user's profile or temporary table
                user.save()

                subject = 'Password Reset'
                message = f'Click the link to reset your password: http://localhost:3000/reset-password/{token}'

                from_email = 'shanilevi88761234@gmail.com'
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

                return Response({'message': 'Email sent with reset instructions.'})
            except User.DoesNotExist:
                return Response({'message': 'No user with that email.'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from django.contrib.auth.hashers import make_password
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import CustomUser

# class UpdatePasswordView(APIView):
#     def post(self, request):
#         reset_token = request.data.get('token')
#         new_password = request.data.get('new_password')

#         try:
#             user = CustomUser.objects.get(reset_token=reset_token)
#             user.set_password(new_password)
#             user.reset_token = None  # Reset the reset token
#             user.save()
            
#             return Response({'message': 'Password updated successfully.'})
#         except CustomUser.DoesNotExist:
#             return Response({'message': 'Invalid reset token.'}, status=status.HTTP_400_BAD_REQUEST)

