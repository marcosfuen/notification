from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from notificationApp.form import ContactForm
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator 
from django.contrib.auth.models import User
from notificationApp.models import RegistrationExternalities 
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.template.loader import get_template
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template.context import RequestContext, Context
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
import os

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login/')
def accountProfile(request):
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        raise Http404(u'Requested user not found.')
    # allIncidents = RegistrationExternalities.objects.all().order_by('-date')
    allIncidents = RegistrationExternalities.objects.all()
    totalIncidents = RegistrationExternalities.objects.count()
    paginator = Paginator(allIncidents, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        descarga1 = paginator.page(page)
    except (EmptyPage, InvalidPage):
        descarga1 = paginator.page(paginator.num_pages)
    
    return render_to_response('profiles.html', { 'user': user,'username': request.user.username, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email':request.user.email, 'descarga1': descarga1, 'allIncidents': allIncidents, 'totalIncidents': totalIncidents })

@login_required(login_url='/login/')
def classificationIncidentsInRed(request):
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        raise Http404(u'Requested user not found.')
    
    allRedIncidents = RegistrationExternalities.objects.filter(classification='red')
    totalRedIncidents = RegistrationExternalities.objects.filter(classification='red').count()
    
    paginator = Paginator(allRedIncidents, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        descarga1 = paginator.page(page)
    except (EmptyPage, InvalidPage):
        descarga1 = paginator.page(paginator.num_pages)
    
    return render_to_response('red.html', { 'user': user,'username': request.user.username, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email':request.user.email, 'descarga1': descarga1, 'allRedIncidents': allRedIncidents, 'totalRedIncidents': totalRedIncidents })

@login_required(login_url='/login/')
def classificationIncidentsInSecurity(request):
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        raise Http404(u'Requested user not found.')
    
    allSecurityIncidents = RegistrationExternalities.objects.filter(classification='seguridad')
    totalSecurityIncidents = RegistrationExternalities.objects.filter(classification='seguridad').count()

    paginator = Paginator(allSecurityIncidents, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        descarga1 = paginator.page(page)
    except (EmptyPage, InvalidPage):
        descarga1 = paginator.page(paginator.num_pages)
    
    return render_to_response('seguridad.html', { 'user': user,'username': request.user.username, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email':request.user.email, 'descarga1': descarga1, 'allSecurityIncidents': allSecurityIncidents, 'totalSecurityIncidents': totalSecurityIncidents })

@login_required(login_url='/login/')
def revisedIncidentsYes(request):
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        raise Http404(u'Requested user not found.')
    
    allYesIncidents = RegistrationExternalities.objects.filter(revised=True)
    totalYesIncidents = RegistrationExternalities.objects.filter(revised=True).count()
    
    paginator = Paginator(allYesIncidents, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        descarga1 = paginator.page(page)
    except (EmptyPage, InvalidPage):
        descarga1 = paginator.page(paginator.num_pages)
    
    return render_to_response('yes.html', { 'user': user,'username': request.user.username, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email':request.user.email, 'descarga1': descarga1, 'allYesIncidents': allYesIncidents, 'totalYesIncidents': totalYesIncidents })

@login_required(login_url='/login/')
def revisedIncidentsNo(request):
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        raise Http404(u'Requested user not found.')
    
    allNoIncidents = RegistrationExternalities.objects.filter(revised=False)
    totalNoIncidents = RegistrationExternalities.objects.filter(revised=False).count()
    
    paginator = Paginator(allNoIncidents, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        descarga1 = paginator.page(page)
    except (EmptyPage, InvalidPage):
        descarga1 = paginator.page(paginator.num_pages)
    
    return render_to_response('no.html', { 'user': user,'username': request.user.username, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email':request.user.email, 'descarga1': descarga1, 'allNoIncidents': allNoIncidents, 'totalNoIncidents': totalNoIncidents })

@login_required(login_url='/login/') 
def search(request):
    try:
        user = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        raise Http404(u'Requested user not found.')
   
    query = request.GET.get('q', '')
    results = []
    if query:
        results = RegistrationExternalities.objects.filter(name__icontains=query)
        print(results)
        
    return render_to_response('search.html', { 'user': user,'username': request.user.username, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'email':request.user.email, 'query': query, 'results': results, 'username': request.user.username })

@method_decorator(login_required(login_url='/login/'), name='dispatch')
@method_decorator(staff_member_required(login_url='/login/'), name='dispatch')
class contactView(TemplateView):
    template_name = "contactForm.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()

        return context
    
    def post(self, request, *args, **kwargs):
        name=request.POST.get('name')
        email=request.POST.get('email')
        to=request.POST.get('to')
        message=request.POST.get('message')
        attach = request.FILES['attach']
        to1 = str(to).replace(',', '').split()
        
        body=render_to_string('emailContect.html',{'name': name, 'email':email, 'to':to, 'message': message, 'attach':attach},)

        emailMessage = EmailMessage(
            subject = 'Reporte de Incidencia Universidad de Camagüey',
            body = body,
            from_email = email,
            to = to1,
        )

        emailMessage.attach(attach.name, attach.read(), attach.content_type)
        emailMessage.content_subtype = 'html'
        emailMessage.send()

        return redirect('/accounts/')
