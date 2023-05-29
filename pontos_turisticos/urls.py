from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

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
    path("api-token-auth/", obtain_auth_token),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
