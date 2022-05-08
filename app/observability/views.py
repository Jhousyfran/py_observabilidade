from django.shortcuts import render
from django.http import HttpResponse
import time
import logging
logger = logging.getLogger('mysite')

# Create your views here.
def index(request):
    logger.warning(
        'This is a warning!',
        exc_info=True
    )
    context={'hour': time.strftime("%H:%M:%S")}
    return render(request, 'observability/index.html', context)


def pageerror(request):
    # calling vision that doesn't exist
    return render(request, 'observability/error.html')


def api(request):
    return HttpResponse("Hello, world. %s" % time.strftime("%H:%M:%S") )
