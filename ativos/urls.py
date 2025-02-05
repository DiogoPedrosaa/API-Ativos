from django.urls import path
from ativos.views import (FabricanteListCreateView, FabricanteRetrieveUpdateDestroyView,TagListCreateView, TagRetrieveUpdateDestroyView,AtivoListCreateView, AtivoRetrieveUpdateDestroyView, login_view, SetorListCreateView, SetorRetrieveUpdateDestroyView)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="API de Ativos",
        default_version='v1',
        description="Documentação da API para gerenciamento de ativos",
        contact=openapi.Contact(email="diogopedrosa07@gmail.com"),
        license=openapi.License(name="Licença MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
  
    path('fabricantes/', FabricanteListCreateView.as_view(), name='fabricante-list-create'),
    path('fabricantes/<int:pk>/', FabricanteRetrieveUpdateDestroyView.as_view(), name='fabricante-detail'),

    
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagRetrieveUpdateDestroyView.as_view(), name='tag-detail'),

   
    path('ativos/', AtivoListCreateView.as_view(), name='ativo-list-create'),
    path('ativos/<int:pk>/', AtivoRetrieveUpdateDestroyView.as_view(), name='ativo-detail'),

     
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('login/', login_view, name='login'),

    path('setores/', SetorListCreateView.as_view(), name='setores-list-create'),
    path('setores/<int:pk>/', SetorRetrieveUpdateDestroyView.as_view(), name='setor-detail')


]
