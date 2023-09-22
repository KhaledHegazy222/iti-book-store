from django.shortcuts import render

from authentication.views import attach_user_context


def Home(request):

    return render(request, "book_store/base.html", attach_user_context(request, {}))
