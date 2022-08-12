from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'lb', views.LBViewSet, basename="lb")
router.register(r'mem', views.MemberViewSet, basename="mem")
router.register(r'team', views.TeamViewSet, basename="team")

urlpatterns = [
    path('', include(router.urls)),
    path('api', include('rest_framework.urls',
        namespace='rest_framework')
    )
]