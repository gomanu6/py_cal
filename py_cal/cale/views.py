from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Task
from django.http import Http404


# Create your views here.
def index(request):
    task_list = Task.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('cale/index.html')
    context = {
        'task_list': task_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'cale/index.html', context)


def date(request, cale_date):
    try:
        task = Task.objects.get(pk=cale_date)
    except Task.DoesNotExist:
        raise Http404("No Task Found")
    return render(request, 'cale/date.html', {
        'task': task
    })
    # return HttpResponse('The entered date is %s' % cale_date)


def day(request, cale_day):
    return HttpResponse('The requested day is %s' % cale_day)
