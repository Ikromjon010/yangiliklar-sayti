
from django.shortcuts import render

from .models import Profile



def profile_view(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context = {
        'user': user,
        'profile':profile
    }

    return render(request, 'pages/user_profile.html', context)
