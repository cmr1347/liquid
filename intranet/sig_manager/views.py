from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from intranet.sig_manager.models import SIG, SIGMember, Project

# Create your views here.
def main(request):
  sigs = SIG.objects.all()
  return render_to_response('intranet/sig_manager/main.html',{"page":'sig','sigs':sigs})
  
def new(requset):
  return render_to_response('intranet/sig_manager/form.html',{"page":'sig',"page_title":"Create new SIG"})
  
def edit(request,id):
  return render_to_response('intranet/sig_manager/form.html',{"page":'sig',"page_title":"Edit SIG"})
  