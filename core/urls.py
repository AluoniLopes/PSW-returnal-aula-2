from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diario/', include('diario.urls')),
    path('', lambda request: HttpResponseRedirect('/diario'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
