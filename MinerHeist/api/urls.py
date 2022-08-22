from django.urls import include, path
from rest_framework import routers
from . import views

"""
router = routers.DefaultRouter()
router.register(r'lb', views.LBView.as_view(), basename="lb")
router.register(r'mem', views.MemberView.as_view(), basename="mem")
router.register(r'team', views.TeamView.as_view(), basename="team")
"""

urlpatterns = [
    #path('', include(router.urls)),
    path('api/lb/', views.LBView, name='lb'),
    path('api/mem/', views.MemberView, name='member'),
    path('api/team/', views.TeamView, name='team')
]