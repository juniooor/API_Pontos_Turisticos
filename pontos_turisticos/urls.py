"""
URL configuration for pontos_turisticos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from atracoes.api.viewset import AtracaoViewset
from avaliacoes.api.viewset import AvaliacaoViewset
from comentarios.api.viewset import ComentarioViewset
from core.api.viewset import PontoTuristicoViewset
from enderecos.api.viewset import EnderecoViewset

router = routers.DefaultRouter()
router.register(r"pontosturisticos", PontoTuristicoViewset, basename="PontoTuristico")
router.register(r"atracoes", AtracaoViewset)
router.register(r"avaliacoes", AvaliacaoViewset)
router.register(r"comentarios", ComentarioViewset)
router.register(r"enderecos", EnderecoViewset)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
