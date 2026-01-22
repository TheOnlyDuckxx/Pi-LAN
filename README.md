# LANHub

LANHub est un **hub de gestion pour LAN party** conçu pour fonctionner **sans accès Internet**.  
Il centralise les outils nécessaires à l’organisation et au bon déroulement de parties en réseau local : visualisation des machines connectées, diagnostics réseau, détection de serveurs de jeu et distribution de fichiers (jeux, correctifs, dépendances) via un PC hôte.

Le projet est pensé pour fonctionner sur du matériel modeste (Raspberry Pi 3B) et pour être **simple à déployer**, **robuste** et **transparent** pour les joueurs.

---

## Objectifs du projet

- Fournir un **dashboard web accessible à tous les joueurs** sur le LAN
- Garantir un **réseau local stable**, sans dépendance à Internet
- Faciliter le **diagnostic réseau** (latence, jitter, perte de paquets)
- Centraliser l’accès aux **installateurs et mises à jour de jeux**
- Simplifier l’organisation de LAN party (tournois, soirées entre amis, associations)

---

## Architecture générale

- **Raspberry Pi**  
  Héberge le dashboard, l’API, la base de données et les outils de diagnostic réseau.

- **Routeur / switch LAN**  
  Assure la connectivité Ethernet et Wi-Fi locale. Aucun trafic de jeu ne transite par le Raspberry Pi.

- **PC hôte (Windows)**  
  Héberge les fichiers volumineux (installateurs GOG, correctifs, redistribuables) via SMB ou HTTP.

- **Clients (joueurs)**  
  Accèdent au dashboard via un navigateur et téléchargent les fichiers directement depuis le PC hôte.

Le trafic est réparti de manière optimale :
- PC ↔ PC : jeu LAN (switch)
- Clients ↔ Raspberry Pi : dashboard et diagnostics
- Clients ↔ PC hôte : distribution des fichiers

---

## Fonctionnalités principales

### Dashboard LAN
- Liste des machines connectées (IP, MAC, dernière activité)
- Visualisation de l’état général du réseau
- Accès sans authentification sur le LAN

### Diagnostics réseau
- Ping, latence moyenne, jitter, perte de paquets
- Tests groupés sur l’ensemble des machines
- Historique des résultats
- Détection de ports ouverts (serveurs de jeu)

### Distribution de jeux
- Catalogue de jeux et versions de référence
- Liens directs vers les installateurs hébergés sur le PC hôte
- Vérification d’intégrité via checksums
- Liste des dépendances requises (VC++, DirectX, etc.)

### Administration (optionnelle)
- Alias des machines (nom du joueur, équipe)
- Export CSV des machines et résultats
- Configuration des ports à scanner

---

## Choix techniques

- **Backend** : FastAPI, Uvicorn
- **Base de données** : SQLite
- **Frontend** : HTML (Jinja2) + CSS léger
- **Système** : Linux (Raspberry Pi OS / Arch ARM)
- **Réseau** : commandes Linux standards (`ip`, `ping`, sockets TCP)
- **Déploiement** : systemd

Ces choix privilégient la simplicité, la lisibilité du code et la compatibilité avec du matériel limité.

---

## Contraintes et limites connues

- La détection des machines dépend du réseau et des pare-feu clients (ICMP parfois bloqué sous Windows)
- Sans agent côté client, les versions exactes des jeux installés ne peuvent pas être détectées automatiquement
- Le Raspberry Pi 3B n’est pas utilisé pour servir de gros fichiers afin d’éviter toute limitation de débit

Ces limites sont assumées et documentées dans le cadre du projet.

---

## Cas d’usage typiques

- LAN party entre amis sans connexion Internet
- Tournoi associatif ou scolaire
- Dépannage rapide de problèmes réseau en environnement isolé
- Distribution locale de jeux et correctifs hors ligne

---

## Licence

Le code source est distribué sous licence **PolyForm Noncommercial 1.0.0**.  
L’utilisation, la modification et la redistribution sont autorisées **à des fins non commerciales uniquement**.

Pour tout usage commercial, merci de contacter l’auteur.

---

## Statut du projet

Projet personnel en développement actif.  
L’architecture est stable, mais certaines fonctionnalités peuvent évoluer en fonction des besoins terrain et des retours d’utilisation.
