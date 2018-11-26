'''Views del crud del consultor'''

from django.shortcuts import render
from django.views.generic import (CreateView, DetailView,
                                  ListView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy
from .models import (
    Organizacion, Responsable, Solicitante,
    DatosProyecto, DatosDocumento, DescripcionProyecto,
    CaracteristicaMedio, Medio
)
from .forms import (
    OrganizacionCreateForm, SolicitanteCreateForm,
    ResponsableCreateForm, DatosDocumentoCreateForm, DescripcionProyectoCreateForm
)


class OrganizacionList(ListView):  # pylint: disable=too-many-ancestors
    '''Listar las organizaciones'''
    model = Organizacion
    template_name = 'eia_app/organizaciones/list.html'


class OrganizacionDetail(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de una organizacion'''
    model = Organizacion
    template_name = 'eia_app/organizaciones/detail.html'


class OrganizacionCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una organizacion'''
    model = Organizacion
    form_class = OrganizacionCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(OrganizacionCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Organización"
        return context


class OrganizacionUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una organizacion'''
    model = Organizacion
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')
    fields = '__all__'


class OrganizacionDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una organizacion'''
    model = Organizacion
    template_name = 'eia_app/organizaciones/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-organizaciones')


class DatosProyectoList(ListView):  # pylint: disable=too-many-ancestors
    '''Listar los datos de los proyectos'''
    model = DatosProyecto
    template_name = 'eia_app/datos_proyectos/list.html'


class DatosProyectoCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear datos de un proyecto'''
    model = DatosProyecto
    fields = '__all__'
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(DatosProyectoCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Datos de un proyecto"
        return context


class DatosProyectoUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar los datos de un proyecto'''
    model = DatosProyecto
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')
    fields = '__all__'


class DatosProyectoDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar los datos de un proyecto'''
    model = DatosProyecto
    template_name = 'eia_app/datos_proyectos/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-proyectos')


class DatosProyectoDetail(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de los datos de un proyecto'''
    model = DatosProyecto
    template_name = 'eia_app/datos_proyectos/detail.html'


class ResponsableList(ListView):  # pylint: disable=too-many-ancestors
    '''Listar las Responsables'''
    model = Responsable
    template_name = 'eia_app/responsables/list.html'


class ResponsableDetail(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de una Responsable'''
    model = Responsable
    template_name = 'eia_app/responsables/detail.html'


class ResponsableCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una Responsable'''
    model = Responsable
    form_class = ResponsableCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-responsables')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(ResponsableCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Responsable"
        return context


class ResponsableUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una Responsable'''
    model = Responsable
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-responsables')
    fields = '__all__'


class ResponsableDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una Responsable'''
    model = Responsable
    template_name = 'eia_app/responsables/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-responsables')


class SolicitanteList(ListView):  # pylint: disable=too-many-ancestors
    '''Listar las Solicitantes'''
    model = Solicitante
    template_name = 'eia_app/solicitantes/list.html'


class SolicitanteDetail(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de una Solicitante'''
    model = Solicitante
    template_name = 'eia_app/solicitantes/detail.html'


class SolicitanteCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una Solicitante'''
    model = Solicitante
    form_class = SolicitanteCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-solicitantes')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(SolicitanteCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Solicitante"
        return context


class SolicitanteUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una Solicitante'''
    model = Solicitante
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-solicitantes')
    fields = '__all__'


class SolicitanteDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una Solicitante'''
    model = Solicitante
    template_name = 'eia_app/solicitantes/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-solicitantes')


class DatosDocumentoList(ListView):  # pylint: disable=too-many-ancestors
    '''Listar las DatosDocumentos'''
    model = DatosDocumento
    template_name = 'eia_app/datos_documentos/list.html'


class DatosDocumentoDetail(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de un DatosDocumento'''
    model = DatosDocumento
    template_name = 'eia_app/datos_documentos/detail.html'


class DatosDocumentoCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una DatosDocumento'''
    model = DatosDocumento
    form_class = DatosDocumentoCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-documentos')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(DatosDocumentoCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Datos de un documento"
        return context


class DatosDocumentoUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una DatosDocumento'''
    model = DatosDocumento
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-documentos')
    fields = '__all__'


class DatosDocumentoDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una DatosDocumento'''
    model = DatosDocumento
    template_name = 'eia_app/datos_documentos/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-datos-documentos')

class DescripcionProyectoList(ListView):  # pylint: disable=too-many-ancestors
    '''Listar las DescripcionProyecto'''
    model = DescripcionProyecto
    template_name = 'eia_app/descripcion_proyecto/list.html'


class DescripcionProyectoDetail(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de un DescripcionProyecto'''
    model = DescripcionProyecto
    template_name = 'eia_app/descripcion_proyecto/detail.html'


class DescripcionProyectoCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una DescripcionProyecto'''
    model = DescripcionProyecto
    form_class = DescripcionProyectoCreateForm
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-detalles-proyecto')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(DescripcionProyectoCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Detalles de un documento"
        return context


class DescripcionProyectoUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una DescripcionProyecto'''
    model = DescripcionProyecto
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-detalles-proyecto')
    fields = '__all__'


class DescripcionProyectoDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una DescripcionProyecto'''
    model = DescripcionProyecto
    template_name = 'eia_app/descripcion_proyecto/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-detalles-proyecto')

def consultor_index(request):
    '''Index de la vista del consultor'''
    template_name = 'eia_app/consultor-crud_index.html'
    return render(request, template_name)

class MedioList(ListView):
    ''' Index de los distintos medios'''
    model = Medio
    template_name = 'eia_app/caracterizacion_medio/medios_index.html'

class MedioCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una Medio'''
    model = Medio
    fields = "__all__"
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-medios')

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(MedioCreate, self).get_context_data(**kwargs)
        context["nombre"] = "Detalles de un medio ambiental"
        return context

class MedioDetail(DetailView):  # pylint: disable=too-many-ancestors
    '''Detalles de un Medio'''
    model = Medio
    template_name = 'eia_app/caracterizacion_medio/detail.html'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(MedioDetail, self).get_context_data(**kwargs)
        caracteristicas = CaracteristicaMedio.objects.filter(medio=self.kwargs['pk'])
        context["caracteristicas"] = caracteristicas
        return context

class MedioUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una Medio'''
    model = Medio
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-medios')
    fields = '__all__'


class MedioDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una Medio'''
    model = Medio
    template_name = 'eia_app/descripcion_proyecto/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-detalles-proyecto')

class CaracteristicaMedioDetail(ListView):
    '''Ver caracteristicas de un medio fisico'''
    model = CaracteristicaMedio
    template_name = 'eia_app/caracterizacion_medio/list.html'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CaracteristicaMedioList, self).get_context_data(**kwargs)
        if self.kwargs['medio'] == 'fisico':
            context['medio'] = 'medio físico'
        elif self.kwargs['medio'] == 'biologico':
            context['medio'] = 'medio biológico'
        elif self.kwargs['medio'] == 'socio':
            context['medio'] = 'medio socio-cultural'
        return context

class CaracteristicaMedioUpdate(UpdateView):  # pylint: disable=too-many-ancestors
    '''Actualizar una CaracteristicaMedio'''
    model = CaracteristicaMedio
    template_name = 'eia_app/create_form.html'
    success_url = reverse_lazy('consultor-crud:lista-detalles-proyecto')
    fields = ['caracteristica', 'descripcion']

    def get_success_url(self):
        caracteristica = CaracteristicaMedio.objects.get(pk=self.kwargs['pk'])
        return reverse_lazy('consultor-crud:detalles-medio', kwargs={'pk': caracteristica.medio.pk})


class CaracteristicaMedioDelete(DeleteView):  # pylint: disable=too-many-ancestors
    '''Eliminar una CaracteristicaMedio'''
    model = CaracteristicaMedio
    template_name = 'eia_app/descripcion_proyecto/delete.html'
    success_url = reverse_lazy('consultor-crud:lista-detalles-proyecto')

class CaracteristicaMedioCreate(CreateView):  # pylint: disable=too-many-ancestors
    '''Crear una Medio'''
    model = CaracteristicaMedio
    fields = "__all__"
    template_name = 'eia_app/create_form.html'

    def get_context_data(self, **kwargs):  # pylint: disable=arguments-differ
        context = super(CaracteristicaMedioCreate, self).get_context_data(**kwargs)
        medio = Medio.objects.get(pk=self.kwargs['pk'])
        context["nombre"] = "características del proyecto " + str(medio.proyecto) + " del medio " + str(medio.tipo)
        context["medio"] = medio.pk
        return context

    def get_success_url(self):
        return reverse_lazy('consultor-crud:detalles-medio', kwargs={'pk': self.kwargs['pk']})