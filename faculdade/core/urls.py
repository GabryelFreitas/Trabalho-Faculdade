from django.urls import path
from . import views
urlpatterns = [
    path('cursos/', views.lista_cursos, name='lista_cursos'),
    path('cursos/novo/', views.novo_curso, name='novo_curso'),
    path('cursos/editar/<int:pk>/', views.editar_curso, name='editar_curso'),
    path('cursos/deletar/<int:pk>/', views.deletar_curso, name='deletar_curso'),
    path('professores/', views.lista_professores, name='lista_professores'),
    path('professores/novo/', views.novo_professor, name='novo_professor'),
    path('professores/editar/<int:pk>/', views.editar_professor, name='editar_professor'),
    path('professores/deletar/<int:pk>/', views.deletar_professor, name='deletar_professor'),
    path('estudantes/', views.lista_estudantes, name='lista_estudantes'),
    path('estudantes/novo/', views.novo_estudante, name='novo_estudante'),
    path('estudantes/editar/<int:pk>/', views.editar_estudante, name='editar_estudante'),
    path('estudantes/deletar/<int:pk>/', views.deletar_estudante, name='deletar_estudante'),
 ]