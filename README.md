# Tourisme et patrimoine culturel de Côte d'Ivoire

Projet du Groupe 3 (Licence Informatique, Université Nangui Abrogoua, cours de Programmation WEB) :
un site qui regroupe les sites touristiques de Côte d'Ivoire avec leurs horaires, la présence de
guides et le coût des visites, ainsi que les pagnes traditionnels, masques, danses, festivals,
hôtels (prix de la nuitée) et prestataires.

Stack : Django 6.1 + Django REST Framework + PostgreSQL.

## Installation

1. Créer la base PostgreSQL et charger le script :

   ```
   createdb -U postgres tourisme_patrimoine_ci
   psql -U postgres -d tourisme_patrimoine_ci -f tourisme_patrimoine_ci_postgresql18_CORRIGE.sql
   ```

2. Créer l'environnement Python et installer les dépendances :

   ```
   python -m venv venv
   venv\Scripts\activate        # Windows (Linux/macOS : source venv/bin/activate)
   pip install -r requirements.txt
   ```

3. Définir le mot de passe PostgreSQL (il n'est pas dans le code) :

   ```
   set DB_PASSWORD=ton_mot_de_passe          # Windows (cmd)
   $env:DB_PASSWORD="ton_mot_de_passe"       # Windows (PowerShell)
   export DB_PASSWORD=ton_mot_de_passe       # Linux/macOS
   ```

   Variables facultatives : `DB_USER` (défaut `postgres`), `DB_HOST` (`localhost`), `DB_PORT` (`5432`).

4. Lancer le serveur :

   ```
   python manage.py migrate
   python manage.py runserver
   ```

## API

Toutes les adresses sont sous `/api/` : `zones/`, `sites/`, `activites/`, `aires-culturelles/`,
`peuples/`, `expressions-culturelles/`, `pagnes/`, `festivals/`, `unesco/`, `hebergements/`, `guides/`.

Exemples de filtres :

- `/api/sites/?guide_obligatoire=true`
- `/api/sites/?zone=1&q=musée`
- `/api/hebergements/?zone=29&prix_max=20000&type=Hôtel`
- `/api/pagnes/?zone=17`

Les tables sont gérées par le script SQL (`managed = False` dans `models.py`).
