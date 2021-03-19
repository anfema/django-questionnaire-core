from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import BasicQuestionnaireView


urlpatterns = [
    path('questionnaire/<int:pk>/', BasicQuestionnaireView.as_view(), name='basic_questionnaire_form'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
