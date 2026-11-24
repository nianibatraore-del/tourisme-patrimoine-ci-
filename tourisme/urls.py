from django.urls import path

from .views import (
    ActivitesListAPIView,
    AiresCulturellesListAPIView,
    ElementsCulturelsListAPIView,
    EvenementsFestivalsListAPIView,
    HebergementsListAPIView,
    PagnesTraditionnelsListAPIView,
    PatrimoineUnescoListAPIView,
    PeuplesListAPIView,
    PrestatairesGuidesListAPIView,
    SitesTouristiquesDetailAPIView,
    SitesTouristiquesListAPIView,
    ZonesGeographiquesDetailAPIView,
    ZonesGeographiquesListAPIView,
)

urlpatterns = [
    path('zones/', ZonesGeographiquesListAPIView.as_view(), name='liste-zones'),
    path('zones/<int:pk>/', ZonesGeographiquesDetailAPIView.as_view(), name='detail-zone'),

    path('sites/', SitesTouristiquesListAPIView.as_view(), name='liste-sites'),
    path('sites/<int:pk>/', SitesTouristiquesDetailAPIView.as_view(), name='detail-site'),

    path('activites/', ActivitesListAPIView.as_view(), name='liste-activites'),

    path('aires-culturelles/', AiresCulturellesListAPIView.as_view(), name='liste-aires'),
    path('peuples/', PeuplesListAPIView.as_view(), name='liste-peuples'),
    path('expressions-culturelles/', ElementsCulturelsListAPIView.as_view(), name='liste-expressions'),
    path('pagnes/', PagnesTraditionnelsListAPIView.as_view(), name='liste-pagnes'),
    path('festivals/', EvenementsFestivalsListAPIView.as_view(), name='liste-festivals'),
    path('unesco/', PatrimoineUnescoListAPIView.as_view(), name='liste-unesco'),

    path('hebergements/', HebergementsListAPIView.as_view(), name='liste-hebergements'),
    path('guides/', PrestatairesGuidesListAPIView.as_view(), name='liste-guides'),
]
