'''Modulo de urls del crud del consultor '''

from django.urls import path, re_path
from .views import * #pylint: disable=wildcard-import, unused-wildcard-import

app_name = 'eia_app' #pylint: disable=invalid-name

urlpatterns = [ #pylint: disable=invalid-name
    path('organizaciones/', OrganizacionList.as_view(),
         name='lista-organizaciones'),
    path('organizaciones/nuevo/', OrganizacionCreate.as_view(),
         name='nueva-organizacion'),
    re_path(r'^organizaciones/(?P<pk>\d+)/$', OrganizacionDetail.as_view(),
            name='detalles-organizacion'),
    re_path(r'^organizaciones/editar/(?P<pk>\d+)/$', OrganizacionUpdate.as_view(),
            name='editar-organizacion'),
    re_path(r'^organizaciones/borrar/(?P<pk>\d+)/$', OrganizacionDelete.as_view(),
            name='borrar-organizacion'),
    path('datos_proyectos/', DatosProyectoList.as_view(),
         name='lista-datos-proyectos'),
    path('datos_proyectos/nuevo/', DatosProyectoCreate.as_view(),
         name='nueva-datos-proyecto'),
    re_path(r'^datos_proyectos/(?P<pk>\d+)/$', DatosProyectoDetail.as_view(),
            name='detalles-datos-proyecto'),
    re_path(r'^datos_proyectos/editar/(?P<pk>\d+)/$', DatosProyectoUpdate.as_view(),
            name='editar-datos-proyecto'),
    re_path(r'^datos_proyectos/borrar/(?P<pk>\d+)/$', DatosProyectoDelete.as_view(),
            name='borrar-datos-proyecto'),
    path('responsables/', ResponsableList.as_view(),
         name='lista-responsables'),
    path('responsables/nuevo/', ResponsableCreate.as_view(),
         name='nuevo-responsable'),
    re_path(r'^responsables/(?P<pk>\d+)/$', ResponsableDetail.as_view(),
            name='detalles-responsable'),
    re_path(r'^responsables/editar/(?P<pk>\d+)/$', ResponsableUpdate.as_view(),
            name='editar-responsable'),
    re_path(r'^responsables/borrar/(?P<pk>\d+)/$', ResponsableDelete.as_view(),
            name='borrar-responsable'),
    path('solicitantes/', SolicitanteList.as_view(),
         name='lista-solicitantes'),
    path('solicitantes/nuevo/', SolicitanteCreate.as_view(),
         name='nuevo-solicitante'),
    re_path(r'^solicitantes/(?P<pk>\d+)/$', SolicitanteDetail.as_view(),
            name='detalles-solicitante'),
    re_path(r'^solicitantes/editar/(?P<pk>\d+)/$', SolicitanteUpdate.as_view(),
            name='editar-solicitante'),
    re_path(r'^solicitantes/borrar/(?P<pk>\d+)/$', SolicitanteDelete.as_view(),
            name='borrar-solicitante'),
    path('datos_documentos/', DatosDocumentoList.as_view(),
         name='lista-datos-documentos'),
    path('datos_documentos/nuevo/', DatosDocumentoCreate.as_view(),
         name='nuevo-datos-documento'),
    re_path(r'^datos_documentos/(?P<pk>\d+)/$', DatosDocumentoDetail.as_view(),
            name='detalles-datos-documento'),
    re_path(r'^datos_documentos/editar/(?P<pk>\d+)/$', DatosDocumentoUpdate.as_view(),
            name='editar-datos-documento'),
    re_path(r'^datos_documentos/borrar/(?P<pk>\d+)/$', DatosDocumentoDelete.as_view(),
            name='borrar-datos-documento'),
    path('descripcion_proyecto/', DescripcionProyectoList.as_view(),
         name='lista-detalles-proyecto'),
    path('descripcion_proyecto/nuevo/', DescripcionProyectoCreate.as_view(),
         name='nuevo-detalles-proyecto'),
    re_path(r'^descripcion_proyecto/(?P<pk>\d+)/$', DescripcionProyectoDetail.as_view(),
            name='detalles-proyecto'),
    re_path(r'^descripcion_proyecto/editar/(?P<pk>\d+)/$', DescripcionProyectoUpdate.as_view(),
            name='editar-detalles-proyecto'),
    re_path(r'^descripcion_proyecto/borrar/(?P<pk>\d+)/$', DescripcionProyectoDelete.as_view(),
            name='borrar-detalles-proyecto'),
    path('caracteristicas_medio/', MedioList.as_view(),
         name='lista-medios'),
    path('caracteristicas_medio/nuevo/', MedioCreate.as_view(),
         name='nuevo-medio'),
    re_path(r'^caracteristica_medio/(?P<pk>\d+)/$', MedioDetail.as_view(),
            name='detalles-medio'),
    re_path(r'^caracteristica_medio/editar/(?P<pk>\d+)/$', MedioUpdate.as_view(),
            name='editar-detalles-medio'),
    re_path(r'^caracteristica_medio/borrar/(?P<pk>\d+)/$', MedioDelete.as_view(),
            name='borrar-detalles-medio'),
    path('caracteristica_medio/<int:pk>/nueva_caracteristica/', CaracteristicaMedioCreate.as_view(),
         name='nueva-caracteristica'),
    path('caracteristica_medio/editar/caracteristica/<int:pk>/', CaracteristicaMedioUpdate.as_view(),
            name='editar-detalles-caracteristica'),
    path('caracteristica_medio/borrar/caracteristica/<int:pk>/', CaracteristicaMedioDelete.as_view(),
            name='borrar-detalles-caracteristica'),  
    path('caracteristica_medio/detalles/caracteristica/<int:pk>/', CaracteristicaMedioDetail.as_view(),
            name='detalles-caracteristica'),
    path('caracteristica_medio/<int:pk>/nueva_subcaracteristica/', SubaracteristicaMedioCreate.as_view(),
         name='nueva-subcaracteristica')    
        
]
