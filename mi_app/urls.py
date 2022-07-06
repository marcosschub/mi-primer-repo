from django.urls import path
from mi_app.views import (saludo,saludar_a,
        mostrar_index,listar_cursos)

urlpatterns = [
    path('saludar/', saludo),
    path('saludar/<nombre>',saludar_a),
    path('mi-template/',mostrar_index),
    path('listar-cursos/',listar_cursos),
]