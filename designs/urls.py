from django.urls import path

from . import views

urlpatterns = [
    # /designs/
    path('', views.index, name='designs_index'),
    # /designs/1/
    path('<int:design_id>/', views.detail, name='designs_detail'),
    # /designs/designer/
    path('designer/', views.designer, name='designs_designer'),
    # /designs/add/
    path('add/', views.add, name='designs_add'),
    # /designs/edit/
    path('edit/<int:design_id>/', views.edit, name='designs_edit'),
]
