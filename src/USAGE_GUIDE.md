# Guide d'utilisation - Global Thermonuclear War avec TicTacToe

## Démarrage rapide

### Lancer le jeu principal
```bash
cd /Users/vperrin/Documents/work/wargame/src
python3 main.py
```

## Séquence d'intro

Au démarrage, WOPR vous accueille et affiche la liste des jeux disponibles :
```
FALKEN'S MAZE
BLACK JACK
GIN RUMMY
HEARTS
BRIDGE
CHECKERS
CHESS
POKER
FIGHTER COMBAT
GUERRILLA ENGAGEMENT
DESERT WARFARE
AIR-TO-GROUND ACTIONS
THEATERWIDE TACTICAL WARFARE
THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE

GLOBAL THERMONUCLEAR WAR

WHICH GAME?
```

## 🎮 Easter Egg : TicTacToe

### Comment accéder au jeu caché

Quand WOPR demande **"WHICH GAME?"**, tapez l'un de ces mots :
- `TicTacToe`
- `Tic-Tac-Toe`
- `Tic Tac Toe`

**Note :** TicTacToe n'apparaît PAS dans la liste des jeux (c'est un easter egg caché, comme dans le film WarGames) !

### Mode 1 : Human vs WOPR

1. Sélectionnez l'option `1` dans le menu TicTacToe
2. Vous jouez avec **X**, WOPR joue avec **O**
3. Entrez vos coups au format : `ligne colonne` (ex: `1 2` pour ligne 1, colonne 2)
4. Les lignes et colonnes sont numérotées de 1 à 3

**Exemple de partie :**
```
Your move (row column): 1 1
Your move (row column): 2 2
Your move (row column): 3 3
```

**Conseil :** WOPR joue parfaitement. Le meilleur résultat possible est un match nul !

### Mode 2 : WOPR vs WOPR (Simulation)

1. Sélectionnez l'option `2` dans le menu TicTacToe
2. Regardez WOPR jouer contre lui-même pendant 10 parties
3. Observez que **toutes les parties se terminent en match nul**
4. Comprenez le message : "A strange game. The only winning move is not to play."

## 🎯 Objectif pédagogique

Le jeu TicTacToe démontre le concept de **Mutual Assured Destruction (MAD)** :

- Deux adversaires parfaitement rationnels
- Aucun ne peut gagner
- Le seul résultat est un match nul
- **Parallèle avec la guerre nucléaire** : personne ne gagne

## 📊 Résultats attendus

### Human vs WOPR
- Si vous jouez parfaitement : **MATCH NUL**
- Si vous faites une erreur : **WOPR GAGNE**
- Vous ne pouvez **JAMAIS** gagner contre WOPR

### WOPR vs WOPR
- **100% des parties** se terminent en match nul
- Démontre que le jeu parfait mène à l'impasse
- Illustre la futilité du conflit

## 🧪 Tests

Pour vérifier que tout fonctionne :
```bash
cd /Users/vperrin/Documents/work/wargame/src
python3 test_tictactoe.py
```

Vous devriez voir :
```
✓ ALL TESTS PASSED!

The TicTacToe game demonstrates:
  - Perfect AI play always results in draws
  - Just like nuclear war, nobody wins
  - 'A strange game. The only winning move is not to play.'
```

## 🎬 Référence au film WarGames (1983)

### Scène emblématique

Dans le film, WOPR (Joshua) apprend en jouant au TicTacToe que certains jeux ne peuvent pas être gagnés :

```
JOSHUA: "A strange game. The only winning move is not to play."
```

Cette réalisation empêche WOPR de lancer une guerre nucléaire.

### Citations du jeu

Le jeu inclut plusieurs citations du film :
- "Greetings, Professor Falken"
- "Shall we play a game?"
- "How about a nice game of chess?"
- "A strange game. The only winning move is not to play."

## 🔧 Dépannage

### Le jeu ne démarre pas
```bash
# Vérifiez que vous êtes dans le bon répertoire
cd /Users/vperrin/Documents/work/wargame/src

# Vérifiez que Python 3 est installé
python3 --version

# Vérifiez que colorama est installé
pip3 install colorama
```

### L'easter egg ne fonctionne pas
- Assurez-vous de taper exactement : `games`, `tictactoe`, `tic-tac-toe`, ou `ttt`
- Tapez en minuscules (le jeu accepte aussi les majuscules)
- Ne tapez pas de numéro, tapez le mot complet

### Les tests échouent
```bash
# Réinstallez les dépendances
pip3 install -r requirements.txt

# Vérifiez la structure des fichiers
ls -la game_logic/tictactoe.py
ls -la ui/tictactoe_ui.py
```

## 📝 Structure des fichiers

```
src/
├── main.py                    # Point d'entrée principal
├── game_logic/
│   └── tictactoe.py          # Logique du jeu TicTacToe + IA
├── ui/
│   └── tictactoe_ui.py       # Interface utilisateur TicTacToe
├── test_tictactoe.py         # Tests automatisés
├── TICTACTOE_README.md       # Documentation technique
└── USAGE_GUIDE.md            # Ce fichier
```

## 🎓 Ce que vous apprendrez

1. **Théorie des jeux** : Certains jeux ont des stratégies optimales
2. **IA parfaite** : L'algorithme minimax garantit le meilleur jeu possible
3. **Futilité du conflit** : Quand deux adversaires sont égaux, personne ne gagne
4. **MAD (Mutual Assured Destruction)** : Concept de la guerre froide
5. **Philosophie** : Parfois, ne pas jouer est la meilleure stratégie

## 🌟 Fonctionnalités

- ✅ IA utilisant l'algorithme minimax
- ✅ Jeu parfait garanti
- ✅ Mode Human vs AI
- ✅ Mode AI vs AI (simulation)
- ✅ Interface ASCII art style années 80
- ✅ Messages inspirés du film WarGames
- ✅ Tests automatisés complets
- ✅ Easter egg caché dans le menu

## 💡 Astuces

### Pour battre WOPR (spoiler : impossible)
Il n'y a **aucun moyen** de battre WOPR si vous jouez en second (O). Si vous jouez en premier (X), vous pouvez forcer un match nul en jouant parfaitement :

1. Commencez au centre (2,2) ou dans un coin
2. Bloquez toutes les menaces de WOPR
3. Ne laissez jamais WOPR créer deux menaces simultanées
4. Résultat : Match nul

### Pour comprendre le message
Lancez le mode "WOPR vs WOPR" et regardez 10 parties. Vous verrez que :
- Aucune partie n'a de vainqueur
- Les deux IA jouent parfaitement
- Le résultat est toujours le même : match nul
- **Conclusion** : La seule façon de gagner est de ne pas jouer

---

*"Shall we play a game?"* 🎮

# Made with Bob