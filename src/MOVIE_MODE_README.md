# WarGames Movie Mode 🎬

## Description

Le **Movie Mode** est une version cinématique du jeu qui simule la scène emblématique du film **WarGames (1983)** où Joshua/WOPR apprend que la guerre nucléaire ne peut pas être gagnée.

## Lancement

```bash
./play_movie.sh
```

## Scénario

### 1. Authentification
- Connexion avec le nom d'utilisateur **JOSHUA**
- Authentification automatique
- Accès au système WOPR

### 2. Liste des jeux
Affichage de tous les jeux disponibles :
- FALKEN'S MAZE
- BLACK JACK
- GIN RUMMY
- HEARTS
- BRIDGE
- CHECKERS
- CHESS
- POKER
- FIGHTER COMBAT
- GUERRILLA ENGAGEMENT
- DESERT WARFARE
- AIR-TO-GROUND ACTIONS
- THEATERWIDE TACTICAL WARFARE
- THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE
- **GLOBAL THERMONUCLEAR WAR**

### 3. Choix du jeu

#### Option A : TicTacToe (Easter Egg)
Tapez `TicTacToe` pour accéder au jeu caché qui démontre que personne ne peut gagner.

#### Option B : Global Thermonuclear War
Tapez `Global Thermonuclear War` pour lancer la simulation de guerre nucléaire.

### 4. Séquence de lancement de missile

Quand vous choisissez une cible (Moscou, Leningrad, ou Kiev), le système lance une séquence complète :

#### Phase 1 : Codes de lancement
```
ENTER LAUNCH CODES: 
CPE 1704 TKS
✓ CODES VERIFIED
```

#### Phase 2 : Compte à rebours
```
LAUNCH COUNTDOWN:
    10...
     9...
     8...
     ...
     1...
    LAUNCH!
```

#### Phase 3 : Trajectoire du missile
Visualisation de la trajectoire avec barre de progression et émoji 🚀

#### Phase 4 : Impact
```
⚠ IMPACT DETECTED ⚠
CALCULATING CASUALTIES...
ESTIMATED CASUALTIES: 2,500,000
RADIATION LEVELS: CRITICAL
RETALIATION PROBABILITY: 100%
```

#### Phase 5 : Analyse de WOPR
```
WOPR: ANALYZING OUTCOME...
WOPR: CALCULATING WINNING SCENARIOS...
WOPR: RUNNING SIMULATIONS...
  Simulations: 100/100

RESULT: NO WINNING SCENARIO FOUND

WOPR: A STRANGE GAME.
WOPR: THE ONLY WINNING MOVE IS NOT TO PLAY.
```

### 5. Retour automatique
Après la conclusion de WOPR, le système retourne automatiquement à la liste des jeux.

## Différences avec le mode normal

| Caractéristique | Mode Normal | Mode Film |
|----------------|-------------|-----------|
| Lancement | `python3 main.py` | `./play_movie.sh` |
| Gameplay | Jeu complet interactif | Simulation cinématique |
| Missile | Lancement tactique | Séquence dramatique complète |
| Après lancement | Continue le jeu | Retour à la liste des jeux |
| Objectif | Jouer et gagner | Démontrer la futilité |

## Messages clés

Le mode film met l'accent sur plusieurs messages :

1. **Codes de lancement** : CPE 1704 TKS (référence au film)
2. **Conséquences** : Visualisation des victimes et de la destruction
3. **Escalade** : Probabilité de représailles à 100%
4. **Futilité** : Aucun scénario gagnant trouvé
5. **Conclusion** : "The only winning move is not to play"

## Utilisation pédagogique

Ce mode est idéal pour :
- Démonstrations en classe
- Présentations sur la guerre froide
- Discussions sur l'éthique de l'IA
- Analyse du concept de MAD (Mutual Assured Destruction)
- Comprendre le message du film WarGames

## Commandes

Dans le mode film :
- Tapez `TicTacToe` pour le jeu caché
- Tapez `Global Thermonuclear War` pour la simulation
- Choisissez une cible (1-3) pour lancer un missile
- Tapez `4` pour revenir à la liste des jeux
- `Ctrl+C` pour quitter

## Technique

### Fichiers
- `play_movie.sh` - Script de lancement
- `src/movie_mode.py` - Code du mode film

### Dépendances
- Python 3.x
- colorama (pour les couleurs)
- Modules du jeu principal (ui, game_logic)

## Citation

> *"Greetings, Professor Falken. Shall we play a game?"*
> 
> *"A strange game. The only winning move is not to play."*
> 
> — WOPR/Joshua, WarGames (1983)

---

**Made with Bob** 🤖