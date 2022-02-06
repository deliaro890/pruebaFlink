from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'empresas',views.EmpresaViewSet,basename='empresa')
urlpatterns = [
  path('',include(router.urls)),
  path(
    route='signup_form/',
    view = views.signUpView,
    name='signup_form'
  ),
  path(
    route='menu/',
    view = views.menu_view,
    name='menu'
  ),
  path(
    route = 'empresas_list',
    view = views.list_empresas,
    name = 'empresas_list'
  ),
  path(
    route = 'valores/<str:simbolo>',
    view = views.valores,
    name = 'valores'
  )
]
