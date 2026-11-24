from rest_framework import generics

from .models import (
    Activites,
    AiresCulturelles,
    ElementsCulturels,
    EvenementsFestivals,
    Hebergements,
    PagnesTraditionnels,
    PatrimoineUnesco,
    Peuples,
    PrestatairesGuides,
    SitesTouristiques,
    ZonesGeographiques,
)
from .serializers import (
    ActivitesSerializer,
    AiresCulturellesSerializer,
    ElementsCulturelsSerializer,
    EvenementsFestivalsSerializer,
    HebergementsSerializer,
    PagnesTraditionnelsSerializer,
    PatrimoineUnescoSerializer,
    PeuplesSerializer,
    PrestatairesGuidesSerializer,
    SitesTouristiquesSerializer,
    ZonesGeographiquesSerializer,
)


def _bool(valeur):
    """Convertit 'true'/'1'/'oui' en True, 'false'/'0'/'non' en False, sinon None."""
    v = (valeur or '').strip().lower()
    if v in ('true', '1', 'oui'):
        return True
    if v in ('false', '0', 'non'):
        return False
    return None


# ---------- Zones ----------
class ZonesGeographiquesListAPIView(generics.ListAPIView):
    queryset = ZonesGeographiques.objects.all().order_by('id_zone')
    serializer_class = ZonesGeographiquesSerializer


class ZonesGeographiquesDetailAPIView(generics.RetrieveAPIView):
    queryset = ZonesGeographiques.objects.all()
    serializer_class = ZonesGeographiquesSerializer


# ---------- Sites ----------
class SitesTouristiquesListAPIView(generics.ListAPIView):
    """Filtres : ?zone=<id>  ?categorie=<texte>  ?guide_obligatoire=true|false
    ?unesco=true|false  ?q=<mot du nom ou de la localité>"""
    serializer_class = SitesTouristiquesSerializer

    def get_queryset(self):
        qs = (SitesTouristiques.objects.all().order_by('id_site')
              .prefetch_related('sitezone_set__id_zone', 'siteactivite_set__id_activite'))
        p = self.request.query_params
        if p.get('zone'):
            qs = qs.filter(sitezone__id_zone=p['zone'])
        if p.get('categorie'):
            qs = qs.filter(categorie=p['categorie'])
        g = _bool(p.get('guide_obligatoire'))
        if g is not None:
            qs = qs.filter(guide_obligatoire=g)
        u = _bool(p.get('unesco'))
        if u is not None:
            qs = qs.filter(classe_unesco=u)
        if p.get('q'):
            from django.db.models import Q
            qs = qs.filter(Q(nom_site__icontains=p['q']) | Q(localite__icontains=p['q']))
        return qs.distinct()


class SitesTouristiquesDetailAPIView(generics.RetrieveAPIView):
    queryset = SitesTouristiques.objects.all().prefetch_related(
        'sitezone_set__id_zone', 'siteactivite_set__id_activite')
    serializer_class = SitesTouristiquesSerializer


# ---------- Activités ----------
class ActivitesListAPIView(generics.ListAPIView):
    queryset = Activites.objects.all().order_by('id_activite')
    serializer_class = ActivitesSerializer


# ---------- Culture ----------
class AiresCulturellesListAPIView(generics.ListAPIView):
    queryset = AiresCulturelles.objects.all().order_by('id_aire')
    serializer_class = AiresCulturellesSerializer


class PeuplesListAPIView(generics.ListAPIView):
    """Filtre : ?aire=<id>"""
    serializer_class = PeuplesSerializer

    def get_queryset(self):
        qs = Peuples.objects.select_related('id_aire').order_by('id_peuple')
        if self.request.query_params.get('aire'):
            qs = qs.filter(id_aire=self.request.query_params['aire'])
        return qs


class ElementsCulturelsListAPIView(generics.ListAPIView):
    """Filtres : ?type=Masque|Danse|Instrument de musique|Pratique rituelle  ?zone=<id>"""
    serializer_class = ElementsCulturelsSerializer

    def get_queryset(self):
        qs = (ElementsCulturels.objects.all().order_by('id_element')
              .prefetch_related('elementpeuple_set__id_peuple', 'elementzone_set__id_zone'))
        p = self.request.query_params
        if p.get('type'):
            qs = qs.filter(type_element=p['type'])
        if p.get('zone'):
            qs = qs.filter(elementzone__id_zone=p['zone'])
        return qs.distinct()


class PagnesTraditionnelsListAPIView(generics.ListAPIView):
    """Filtre : ?zone=<id>"""
    serializer_class = PagnesTraditionnelsSerializer

    def get_queryset(self):
        qs = (PagnesTraditionnels.objects.all().order_by('id_pagne')
              .prefetch_related('pagnezone_set__id_zone', 'pagneaire_set__id_aire'))
        if self.request.query_params.get('zone'):
            qs = qs.filter(pagnezone__id_zone=self.request.query_params['zone'])
        return qs.distinct()


class EvenementsFestivalsListAPIView(generics.ListAPIView):
    """Filtre : ?zone=<id>"""
    serializer_class = EvenementsFestivalsSerializer

    def get_queryset(self):
        qs = (EvenementsFestivals.objects.all().order_by('id_evenement')
              .prefetch_related('evenementzone_set__id_zone', 'evenementpeuple_set__id_peuple'))
        if self.request.query_params.get('zone'):
            qs = qs.filter(evenementzone__id_zone=self.request.query_params['zone'])
        return qs.distinct()


class PatrimoineUnescoListAPIView(generics.ListAPIView):
    queryset = PatrimoineUnesco.objects.all().order_by('id_unesco').prefetch_related(
        'patrimoinesite_set__id_site')
    serializer_class = PatrimoineUnescoSerializer


# ---------- Hébergements et guides ----------
class HebergementsListAPIView(generics.ListAPIView):
    """Filtres : ?zone=<id>  ?type=Hôtel|Résidence hôtelière|Lodge / Écolodge|
    Auberge / Guesthouse|Camping  ?prix_max=<FCFA> (tarif minimum ≤ prix_max)
    ?q=<mot du nom ou de la ville>"""
    serializer_class = HebergementsSerializer

    def get_queryset(self):
        qs = Hebergements.objects.select_related('id_zone').order_by('id_hebergement')
        p = self.request.query_params
        if p.get('zone'):
            qs = qs.filter(id_zone=p['zone'])
        if p.get('type'):
            qs = qs.filter(type_hebergement=p['type'])
        if p.get('prix_max', '').isdigit():
            qs = qs.filter(tarif_min_fcfa__lte=int(p['prix_max']))
        if p.get('q'):
            from django.db.models import Q
            qs = qs.filter(Q(nom_etablissement__icontains=p['q']) | Q(ville_localite__icontains=p['q']))
        return qs


class PrestatairesGuidesListAPIView(generics.ListAPIView):
    """Filtres : ?zone=<id>  ?type=Guide local|Guide national|..."""
    serializer_class = PrestatairesGuidesSerializer

    def get_queryset(self):
        qs = PrestatairesGuides.objects.select_related('id_zone').order_by('id_prestataire')
        p = self.request.query_params
        if p.get('zone'):
            qs = qs.filter(id_zone=p['zone'])
        if p.get('type'):
            qs = qs.filter(type_prestataire=p['type'])
        return qs
