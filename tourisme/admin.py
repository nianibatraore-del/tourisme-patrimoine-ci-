from django.contrib import admin

from . import models

# Tables gérées en lecture : managed = False, donc on interdit l'ajout/suppression
# depuis l'admin pour ne pas contourner le script SQL. Retire ces méthodes si tu veux
# modifier les données depuis /admin/.


class LectureSeule(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.ZonesGeographiques)
class ZonesAdmin(LectureSeule):
    list_display = ('nom_zone', 'type_zone', 'grande_aire')
    search_fields = ('nom_zone',)


@admin.register(models.SitesTouristiques)
class SitesAdmin(LectureSeule):
    list_display = ('nom_site', 'localite', 'categorie', 'guide_obligatoire', 'classe_unesco')
    search_fields = ('nom_site', 'localite')
    list_filter = ('guide_obligatoire', 'classe_unesco')


@admin.register(models.Hebergements)
class HebergementsAdmin(LectureSeule):
    list_display = ('nom_etablissement', 'ville_localite', 'id_zone', 'tarif_min_fcfa', 'tarif_max_fcfa')
    search_fields = ('nom_etablissement', 'ville_localite')


@admin.register(models.PrestatairesGuides)
class PrestatairesAdmin(LectureSeule):
    list_display = ('nom_structure_ou_guide', 'zone_intervention', 'telephone')
    search_fields = ('nom_structure_ou_guide',)


@admin.register(models.PagnesTraditionnels)
class PagnesAdmin(LectureSeule):
    list_display = ('nom_pagne', 'appellations_locales', 'centres_production')
    search_fields = ('nom_pagne',)


@admin.register(models.EvenementsFestivals)
class EvenementsAdmin(LectureSeule):
    list_display = ('nom_evenement', 'localite', 'periodicite')
    search_fields = ('nom_evenement',)


@admin.register(models.ElementsCulturels)
class ElementsAdmin(LectureSeule):
    list_display = ('nom_element', 'type_element')
    search_fields = ('nom_element',)


@admin.register(models.PatrimoineUnesco)
class UnescoAdmin(LectureSeule):
    list_display = ('nom_inscription', 'type_patrimoine', 'annee_inscription')


@admin.register(models.Peuples)
class PeuplesAdmin(LectureSeule):
    list_display = ('nom_peuple', 'id_aire')
    search_fields = ('nom_peuple',)


admin.site.register(models.AiresCulturelles, LectureSeule)
admin.site.register(models.Activites, LectureSeule)
