
from rest_framework import serializers
from empresas.models import Empresa
 
class EmpresaModelSerializer(serializers.ModelSerializer):
    class Meta:
       """Meta class."""
       model = Empresa
       fields = (
           'id',
           'nombre',
           'descripcion',
           'simbolo',
           'valores',
           'is_active'  
       )
