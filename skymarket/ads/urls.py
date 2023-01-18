from django.conf.urls.static import static
from django.urls import include, path

from skymarket import settings

# TODO настройка роутов для модели


urlpatterns = [

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)