from django.urls import path
from . import views

urlpatterns = [
    path('list', views.matrices_list, name='matrices_list'),
    path('<int:id>', views.view_matrix, name='view_matrix'),
    path('new', views.create_matrix, name='create_matrix'),
    path('<int:id>/edit', views.edit_matrix, name='edit_matrix'),
    path('<int:id>/delete', views.delete_matrix, name='delete_matrix'),
    path('<int:matrix_id>/flow/add', views.create_flow, name='create_flow'),
    path('<int:matrix_id>/flow/<int:flow_id>/edit', views.edit_flow, name='edit_flow'),
    path('<int:matrix_id>/flow/<int:flow_id>/toggle', views.toggle_flow, name='toggle_flow'),
    path('<int:matrix_id>/flow/<int:flow_id>/delete', views.delete_flow, name='delete_flow'),
    path('<int:matrix_id>/comment', views.create_comment, name='create_comment'),
    path('<int:matrix_id>/comment/<int:comment_id>/delete', views.delete_comment, name='delete_comment')
]