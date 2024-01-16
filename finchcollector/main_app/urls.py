from django.urls import path
from . import views

# from django.conf import settings
# from django.conf.urls.static import static

# ... your url patterns here ...



urlpatterns = [ 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('creatures/', views.creature_index, name='index'),
    path('creatures/<int:creature_id>/', views.creature_detail, name='detail')
]


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)