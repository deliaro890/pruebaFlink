from django.shortcuts import render
from django.http import HttpResponse

from empresas.models import Empresa
from rest_framework import status, viewsets,mixins
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from .  import serializers
from empresas.forms import SignUpForm
from django.http import JsonResponse

class EmpresaViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    

  queryset = Empresa.objects.filter(is_active=True)
  serializer_class = serializers.EmpresaModelSerializer

  def destroy(self, request, *args, **kwargs): 
    """Disable a empresa"""
    instance = self.get_object()
    instance.is_active = False
    instance.save()
    mensaje = 'empresa desactivada'
    return Response(mensaje,status=status.HTTP_200_OK)

def signUpView(request): 

  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid(): 
      data = form.cleaned_data
      form.save()
      nombre = data ['nombre']
      context={'name': nombre}
      return render (request,'empresas/registroEmpresaExito.html',context)
        
  else:
    form = SignUpForm()
  return render(
    request = request,
    template_name = 'empresas/index.html',
    context = {'form':form}
  )

def menu_view(request):
  return render (request,'empresas/menu.html')

def list_empresas(request):
  empresas = Empresa.objects.filter(is_active=True)
  cantidad = len(empresas)
  return render( 
    request = request,
    template_name = 'empresas/list_empresas.html',
    context = {'empresas':empresas,'cantidad':cantidad}
  )

def valores(request):
  if 'term' in request.GET:
    qs = Empresa.objects.filter(simbolo=request.GET.get('term'))
    valores = qs.valores  
    empresa = qs.nombre 
    return render( 
      valores = valores,
      empresa = empresa,
      template_name = 'empresas/valores.html'
    )
