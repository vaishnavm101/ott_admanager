from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # Auth
    path('', views.user_admin_login, name="user_admin_login"),
    path('logout', views.user_admin_logout, name="user_admin_logout"),


    path('home/', views.user_admin_home, name="user_admin_home"),
    path("view-posts/", views.view_posts, name="view_posts"),
 
    # Search Orders
    path("search-orders/", views.user_admin_search_orders, name="user_admin_search_orders"),

    # Search Marketer's Clients
    path("marketer/clients-search/", views.search_marketers_clients, name="search_marketers_clients"),

]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL,
                              document_root=settings.STATIC_ROOT)
