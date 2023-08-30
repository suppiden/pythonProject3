from django.urls import path


from . import views

app_name = 'learning_logs'

urlpatterns = [
   # Página de inicio
   path('', views.index, name='index'),
   path('topics/<int:topic_id>/', views.topics, name='topic'),
   path('all_topics/', views.all_topics, name='all_topics'),
   path('new_topic/', views.new_topic, name='new_topic'),
   path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
   path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
   
]
