from django.shortcuts import render
from django.contrib.auth.models import User
import face_recognition
from django.conf import settings
from .forms import CustomSignupForm, EditUserPhoto
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserProfile
import numpy as np
# Create your views here.

known_face_names = []
known_face_encodings = []

for name in UserProfile.objects.all():
    known_face_names.append(name.user.first_name + name.user.last_name)
    known_face_encodings.append(np.array(name.face_codes, np.float128))


def index(request):
    reg_form = CustomSignupForm()
    return render(request, "index/index.html", {'form':reg_form})

def set_photo(request):
    if request.method == 'POST':
        form = EditUserPhoto(request.POST, request.FILES, instance=request.user.userprofile)
        # check whether it's valid:
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
