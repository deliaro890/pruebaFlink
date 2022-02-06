from django import forms
from empresas.models import Empresa
import random

class SignUpForm(forms.Form): 
    
  nombre = forms.CharField(max_length=50,required=True)
  descripcion = forms.CharField(max_length=100,required=True) 
  simbolo = forms.CharField(max_length=10,required=True)
  valores = forms.CharField(required=False)
  
  class Meta:
    model = Empresa
    fields = ['nombre','descripcion','simbolo','valores'] 

  def clean_simbolo(self): 
    """simbolo must be unique"""
    simbolo = self.cleaned_data['simbolo'] 
    simbolo_taken = Empresa.objects.filter (simbolo=simbolo).exists() #si usamos get y no encuentra algo, lanzaria una exception, filter trae un arreglo, exist regresa solo un boolean y no todo el dato
        
    if simbolo_taken:
      print(simbolo_taken)
      raise forms.ValidationError('simbolo ya existe')

    return simbolo
  
  def clean_valores(self):
    chain = ''
    for i in range(50):
      chain = chain+str(round(random.uniform(100, 110),2))+'_'
    print('cadena2!!!: ',chain)
    valores = chain
    return valores
    
  def save (self):
    data = self.cleaned_data
    empresa = Empresa.objects.create(**data) 
    empresa.save()






        