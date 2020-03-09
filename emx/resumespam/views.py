from django.shortcuts import render
from django.http import HttpResponse
from .puzzle import Puzzle


def index(request):
  """ 
  Returns suitable response for a GET request. Otherwise, returns warning message.

  """
  if request.method == 'GET':
    params = request.GET
    if params.get('q') and params.get('d'):
      return _processed_response(params['q'], params['d'])
    else:
      return HttpResponse("Welcome to Resume spam filter. Expected parameters missing!")
  else:
    return HttpResponse("Welcome to Resume spam filter. Only GET request supported!")

def _processed_response(request_param, value):
  if request_param == 'Name':
    return HttpResponse("Dilip Raj Gajendran")
  elif request_param == 'Email Address':
    return HttpResponse("dilip.raj.gajendran@gmail.com")
  elif request_param == 'Phone':
    return HttpResponse("480-740-6341")
  elif request_param == 'Position':
    return HttpResponse("Senior Pipeline Engineer")
  elif request_param == 'Years':
    return HttpResponse("3+")
  elif request_param == 'Referrer':
    return HttpResponse("LinkedIn")
  elif request_param == 'Degree':
    return HttpResponse("Master of Science in Software Engineering")
  elif request_param == 'Resume':
    return HttpResponse("https://drive.google.com/open?id=1zvq2EUbDc2F9T9eaj2_bELG7JxpKaK_t")
  elif request_param == 'Source':
    return HttpResponse("")
  elif request_param == 'Status':
    return HttpResponse("Yes")
  elif request_param == 'Puzzle':
    return HttpResponse(Puzzle(value)())
  elif request_param == 'Ping':
    return HttpResponse("OK")
  else:
    return HttpResponse("Incorrect param value!")
