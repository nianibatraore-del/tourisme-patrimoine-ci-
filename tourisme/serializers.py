from rest_framework import serializers

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


class ZonesGeographiquesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZonesGeographiques
        fields = '__all__'


class ActivitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activites
        fields = '__all__'


class SitesTouristiquesSerializer(serializers.ModelSerializer):
    """Site avec ses zones et ses activités (horaires, tarifs, guide inclus)."""
    zones = serializers.SerializerMethodField()
    activites = serializers.SerializerMethodField()

    class Meta:
        model = SitesTouristiques
        fields = '__all__'

    def get_zones(self, obj):
        return [sz.id_zone.nom_zone for sz in obj.sitezone_set.all()]

    def get_activites(self, obj):
        return [sa.id_activite.nom_activite for sa in obj.siteactivite_set.all()]


class AiresCulturellesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiresCulturelles
        fields = '__all__'


class PeuplesSerializer(serializers.ModelSerializer):
    nom_aire = serializers.CharField(source='id_aire.nom_aire', read_only=True)

    class Meta:
        model = Peuples
        fields = '__all__'


class ElementsCulturelsSerializer(serializers.ModelSerializer):
    peuples = serializers.SerializerMethodField()
    zones = serializers.SerializerMethodField()

    class Meta:
        model = ElementsCulturels
        fields = '__all__'

    def get_peuples(self, obj):
        return [ep.id_peuple.nom_peuple for ep in obj.elementpeuple_set.all()]

    def get_zones(self, obj):
        return [ez.id_zone.nom_zone for ez in obj.elementzone_set.all()]


class PagnesTraditionnelsSerializer(serializers.ModelSerializer):
    zones = serializers.SerializerMethodField()
    aires = serializers.SerializerMethodField()

    class Meta:
        model = PagnesTraditionnels
        fields = '__all__'

    def get_zones(self, obj):
        return [pz.id_zone.nom_zone for pz in obj.pagnezone_set.all()]

    def get_aires(self, obj):
        return [pa.id_aire.nom_aire for pa in obj.pagneaire_set.all()]


class EvenementsFestivalsSerializer(serializers.ModelSerializer):
    zones = serializers.SerializerMethodField()
    peuples = serializers.SerializerMethodField()

    class Meta:
        model = EvenementsFestivals
        fields = '__all__'

    def get_zones(self, obj):
        return [ez.id_zone.nom_zone for ez in obj.evenementzone_set.all()]

    def get_peuples(self, obj):
        return [ep.id_peuple.nom_peuple for ep in obj.evenementpeuple_set.all()]


class PatrimoineUnescoSerializer(serializers.ModelSerializer):
    sites = serializers.SerializerMethodField()

    class Meta:
        model = PatrimoineUnesco
        fields = '__all__'

    def get_sites(self, obj):
        return [ps.id_site.nom_site for ps in obj.patrimoinesite_set.all()]


class HebergementsSerializer(serializers.ModelSerializer):
    nom_zone = serializers.CharField(source='id_zone.nom_zone', read_only=True)

    class Meta:
        model = Hebergements
        fields = '__all__'


class PrestatairesGuidesSerializer(serializers.ModelSerializer):
    nom_zone = serializers.CharField(source='id_zone.nom_zone', read_only=True, default=None)

    class Meta:
        model = PrestatairesGuides
        fields = '__all__'
