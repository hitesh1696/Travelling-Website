from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from travello.api import views
from .views import DestinationAPIView,DestinationList,DestinationRUD

urlpatterns = [

    path('', views.DestinationList.as_view()),
    path('<pk>', views.DestinationRUD.as_view()),
    path('<pk>/id', views.DestinationAPIView.as_view()),

]

