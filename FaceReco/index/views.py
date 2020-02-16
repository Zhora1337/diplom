from django.shortcuts import render
from django.contrib.auth.models import User
import face_recognition
from django.conf import settings
from .forms import CustomSignupForm, EditUserPhoto
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserProfile
import numpy as np
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from .serializers import UserProfileSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# Create your views here.

known_face_names = []
known_face_encodings = []

for name in UserProfile.objects.all():
    print("user",name)
    known_face_names.append(name.user.first_name + name.user.last_name)
    known_face_encodings.append(np.array(name.face_codes, np.float128))
print(known_face_encodings)

def index(request):
    reg_form = CustomSignupForm()
    return render(request, "index/index.html", {'form':reg_form})

def set_photo(request):
    if request.method == 'POST':
        form = EditUserPhoto(request.POST, request.FILES, instance=request.user.userprofile)
        # check whether it's valid:
        print(request.POST)
        if form.is_valid():
            request.user.userprofile.photo = form.cleaned_data['photo']
            print(request.user.userprofile.photo.path)
            form.save()
            request.user.userprofile.face_codes = request.user.userprofile.coding()
            form.save()
            return HttpResponseRedirect('')
    else:
        form = EditUserPhoto(instance=request.user.userprofile)

    return render(request, 'index/photo.html', {'form': form})


class UpdateUserProfileView(APIView):
    parser_class = (FileUploadParser,)
    def put(self, request, *args, **kwargs):
        for token in Token.objects.all():
            if (request.data['user'] == token.key):
                request.user = token.user
                request.auth = token.key
        file_serializer = UserProfileSerializer(data=request.data, instance=request.user.userprofile)
        #print(request.data, request.user, request.auth)
        #print(file_serializer.is_valid())
        if file_serializer.is_valid():
            print(file_serializer)
            userprofile = file_serializer.save()
            userprofile.face_codes = userprofile.coding()
            userprofile.save()
            return Response(file_serializer.data, status=status.HTTP_200_OK)
        else:
            print("huevo")
            return Response(file_serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    """def post(self, request, *args, **kwargs):
        for token in Token.objects.all():
            if (request.data['user'] == token.key):
                request.user = token.user
                request.auth = token.key
        file_serializer = UserProfileSerializer(data=request.data, instance=request.user.userprofile)
        #print(request.data, request.user, request.auth)
        #print(file_serializer.is_valid())
        if file_serializer.is_valid():
            print(file_serializer)
            userprofile = file_serializer.save()
            userprofile.face_codes = userprofile.coding()
            userprofile.save()
            return Response(file_serializer.data, status=status.HTTP_200_OK)
        else:
            print("huevo")
            return Response(file_serializer.data, status=status.HTTP_400_BAD_REQUEST)"""

