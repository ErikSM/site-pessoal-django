from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
#from site_pessoal.views import redirect_home  # caso queira usar, veja nota abaixo

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # mantido fora do i18n_patterns
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('site_pessoal.urls')),  # essa linha já resolve a home corretamente
)

