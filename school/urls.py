from django.contrib import admin
from django.urls import path, include
from school14 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path("", views.base),
    path('teacher/', views.teacher, name='teacher'),
    path('news/', views.news, name='news'),
    path('one_new/<post_id>/', views.one_new, name='one_new'),
    path("<str:url>/", views.menu_items, name='menu_items'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
