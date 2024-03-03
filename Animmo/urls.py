from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf.urls.i18n import i18n_patterns


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),

    path('api/', include('home.urls', namespace='home')),
    path('api/accounts/', include('accounts.urls', namespace='accounts')),
    path('api/course/', include('course.urls', namespace='course')),
    path('api/blog/', include('blog.urls', namespace='blog')),
    path('api/user_panel/', include('user_panel.urls', namespace='user_panel')),
    path('api/cart/', include('cart.urls', namespace='cart')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    prefix_default_language=False)
# ]

# urlpatterns += [
#     path("i18n/", include("django.conf.urls.i18n"))
# ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)