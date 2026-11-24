# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activites(models.Model):
    id_activite = models.AutoField(primary_key=True)
    nom_activite = models.CharField(unique=True, max_length=150)
    categorie = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'activites'


class AiresCulturelles(models.Model):
    id_aire = models.AutoField(primary_key=True)
    nom_aire = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aires_culturelles'


class ElementPeuple(models.Model):
    pk = models.CompositePrimaryKey('id_element', 'id_peuple')
    id_element = models.ForeignKey('ElementsCulturels', models.DB_CASCADE, db_column='id_element')
    id_peuple = models.ForeignKey('Peuples', models.DB_CASCADE, db_column='id_peuple')

    class Meta:
        managed = False
        db_table = 'element_peuple'


class ElementZone(models.Model):
    pk = models.CompositePrimaryKey('id_element', 'id_zone')
    id_element = models.ForeignKey('ElementsCulturels', models.DB_CASCADE, db_column='id_element')
    id_zone = models.ForeignKey('ZonesGeographiques', models.DB_CASCADE, db_column='id_zone')

    class Meta:
        managed = False
        db_table = 'element_zone'


class ElementsCulturels(models.Model):
    id_element = models.AutoField(primary_key=True)
    nom_element = models.CharField(max_length=150)
    type_element = models.TextField()  # This field type is a guess.
    sous_categorie = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'elements_culturels'


class EvenementPeuple(models.Model):
    pk = models.CompositePrimaryKey('id_evenement', 'id_peuple')
    id_evenement = models.ForeignKey('EvenementsFestivals', models.DB_CASCADE, db_column='id_evenement')
    id_peuple = models.ForeignKey('Peuples', models.DB_CASCADE, db_column='id_peuple')

    class Meta:
        managed = False
        db_table = 'evenement_peuple'


class EvenementZone(models.Model):
    pk = models.CompositePrimaryKey('id_evenement', 'id_zone')
    id_evenement = models.ForeignKey('EvenementsFestivals', models.DB_CASCADE, db_column='id_evenement')
    id_zone = models.ForeignKey('ZonesGeographiques', models.DB_CASCADE, db_column='id_zone')

    class Meta:
        managed = False
        db_table = 'evenement_zone'


class EvenementsFestivals(models.Model):
    id_evenement = models.AutoField(primary_key=True)
    nom_evenement = models.CharField(max_length=160)
    localite = models.CharField(max_length=150, blank=True, null=True)
    periodicite = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField()
    restrictions_acces = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evenements_festivals'


class Hebergements(models.Model):
    id_hebergement = models.AutoField(primary_key=True)
    id_zone = models.ForeignKey('ZonesGeographiques', models.DO_NOTHING, db_column='id_zone')
    nom_etablissement = models.CharField(max_length=180)
    ville_localite = models.CharField(max_length=120, blank=True, null=True)
    type_hebergement = models.TextField()  # This field type is a guess.
    tarif_min_fcfa = models.IntegerField(blank=True, null=True)
    tarif_max_fcfa = models.IntegerField(blank=True, null=True)
    tarif_texte = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=180, blank=True, null=True)
    site_web = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hebergements'


class PagneAire(models.Model):
    pk = models.CompositePrimaryKey('id_pagne', 'id_aire')
    id_pagne = models.ForeignKey('PagnesTraditionnels', models.DB_CASCADE, db_column='id_pagne')
    id_aire = models.ForeignKey(AiresCulturelles, models.DB_CASCADE, db_column='id_aire')

    class Meta:
        managed = False
        db_table = 'pagne_aire'


class PagneZone(models.Model):
    pk = models.CompositePrimaryKey('id_pagne', 'id_zone')
    id_pagne = models.ForeignKey('PagnesTraditionnels', models.DB_CASCADE, db_column='id_pagne')
    id_zone = models.ForeignKey('ZonesGeographiques', models.DB_CASCADE, db_column='id_zone')

    class Meta:
        managed = False
        db_table = 'pagne_zone'


class PagnesTraditionnels(models.Model):
    id_pagne = models.AutoField(primary_key=True)
    nom_pagne = models.CharField(max_length=150)
    appellations_locales = models.TextField(blank=True, null=True)
    matiere_technique = models.TextField(blank=True, null=True)
    centres_production = models.TextField(blank=True, null=True)
    caracteristiques = models.TextField()

    class Meta:
        managed = False
        db_table = 'pagnes_traditionnels'


class PatrimoineSite(models.Model):
    pk = models.CompositePrimaryKey('id_unesco', 'id_site')
    id_unesco = models.ForeignKey('PatrimoineUnesco', models.DB_CASCADE, db_column='id_unesco')
    id_site = models.ForeignKey('SitesTouristiques', models.DB_CASCADE, db_column='id_site')

    class Meta:
        managed = False
        db_table = 'patrimoine_site'


class PatrimoineUnesco(models.Model):
    id_unesco = models.AutoField(primary_key=True)
    nom_inscription = models.CharField(max_length=220)
    type_patrimoine = models.TextField()  # This field type is a guess.
    annee_inscription = models.SmallIntegerField(blank=True, null=True)
    annee_extension = models.SmallIntegerField(blank=True, null=True)
    numero_dossier = models.CharField(max_length=50, blank=True, null=True)
    details = models.TextField()

    class Meta:
        managed = False
        db_table = 'patrimoine_unesco'


class Peuples(models.Model):
    id_peuple = models.AutoField(primary_key=True)
    id_aire = models.ForeignKey(AiresCulturelles, models.DO_NOTHING, db_column='id_aire')
    nom_peuple = models.CharField(unique=True, max_length=100)
    sous_groupes = models.TextField(blank=True, null=True)
    pratiques_notables = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peuples'


class PrestatairesGuides(models.Model):
    id_prestataire = models.AutoField(primary_key=True)
    id_zone = models.ForeignKey('ZonesGeographiques', models.DO_NOTHING, db_column='id_zone', blank=True, null=True)
    nom_structure_ou_guide = models.CharField(max_length=180)
    type_prestataire = models.TextField()  # This field type is a guess.
    zone_intervention = models.CharField(max_length=180)
    langues = models.CharField(max_length=150, blank=True, null=True)
    specialite = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=180, blank=True, null=True)
    site_web_ou_reseau = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prestataires_guides'


class SiteActivite(models.Model):
    pk = models.CompositePrimaryKey('id_site', 'id_activite')
    id_site = models.ForeignKey('SitesTouristiques', models.DB_CASCADE, db_column='id_site')
    id_activite = models.ForeignKey(Activites, models.DB_CASCADE, db_column='id_activite')

    class Meta:
        managed = False
        db_table = 'site_activite'


class SiteZone(models.Model):
    pk = models.CompositePrimaryKey('id_site', 'id_zone')
    id_site = models.ForeignKey('SitesTouristiques', models.DB_CASCADE, db_column='id_site')
    id_zone = models.ForeignKey('ZonesGeographiques', models.DB_CASCADE, db_column='id_zone')

    class Meta:
        managed = False
        db_table = 'site_zone'


class SitesTouristiques(models.Model):
    id_site = models.AutoField(primary_key=True)
    nom_site = models.CharField(max_length=180)
    localite = models.CharField(max_length=150, blank=True, null=True)
    categorie = models.TextField()  # This field type is a guess.
    description = models.TextField()
    horaires = models.TextField(blank=True, null=True)
    tarifs_details = models.TextField(blank=True, null=True)
    guide_obligatoire = models.BooleanField(blank=True, null=True)
    infos_guide_acces = models.TextField(blank=True, null=True)
    est_fiche_majeure = models.BooleanField(blank=True, null=True)
    classe_unesco = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sites_touristiques'


class ZonesGeographiques(models.Model):
    id_zone = models.AutoField(primary_key=True)
    nom_zone = models.CharField(unique=True, max_length=150)
    type_zone = models.TextField()  # This field type is a guess.
    grande_aire = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zones_geographiques'
