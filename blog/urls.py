from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_post, name='create_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('view_post/<int:post_id>/', views.view_post, name='view_post'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/',views.logout_view,name='logout'),

]