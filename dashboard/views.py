"""
Vistas para la aplicacion del dashboard
"""
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from rest_framework.response import Response
from eia_app.models import DatosProyecto
from .serializers import DatosProyectoSerializer
from request_middleware.middleware import get_request

# Create your views here.

class DashboardViewSet(viewsets.ViewSet): # pylint: disable=too-many-ancestors
    """
    Produce la vista con el json que contiene la informacion
    para que el dashboard la muestre
    """
    def list(self, request):
        '''
        Devuelve un json con solo los proyectos del
        usuario loggeado
        '''
        usuario_loggeado = request.user
        queryset = DatosProyecto.objects.filter(usuario=usuario_loggeado)
        serializer = DatosProyectoSerializer(queryset, many=True)
        return Response(serializer.data)

class DashboardView(LoginRequiredMixin, TemplateView):# pylint: disable=too-many-ancestors
    """
    Vista que va a mostrar el dashboard (home) del usuario.
    """
    template_name = "index.html"
