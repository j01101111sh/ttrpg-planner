from django.http import HttpResponse


def index(request):  # pylint: disable=unused-argument
    return HttpResponse("Hello! Polls index")
