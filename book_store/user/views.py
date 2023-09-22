from django.shortcuts import render
from django.http import HttpResponse

from authentication.views import attach_user_context, is_admin, is_logged_in
from .models import BUser


def ListUsers(request):
    if not is_logged_in(request):
        return HttpResponse(status=401)

    if not is_admin(request):
        return HttpResponse(status=403)

    busers = BUser.objects.all()
    context = {
        "busers": busers
    }
    return render(request, "user/list_users.html", attach_user_context(request, context))


def GetUser(request, pk):

    if not is_logged_in(request):
        return HttpResponse(status=401)

    if not is_admin(request):
        return HttpResponse(status=403)

    buser = BUser.objects.get(pk=pk)
    context = {
        "buser": buser
    }
    return render(request, "user/get_user.html", attach_user_context(request, context))
