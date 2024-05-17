from django.http import HttpResponse
from django.http import HttpRequest


def say_hello_with_name(request: HttpRequest, name):
    print(request.headers)

    return HttpResponse("Hello World! {}".format(name))
