# TicTacToe Easter Egg - "A Strange Game"

## Description

Un jeu TicTacToe caché inspiré de la scène emblématique du film **WarGames (1983)** où WOPR apprend que "la seule façon de gagner est de ne pas jouer".

## Accès au jeu

Le jeu TicTacToe est un **easter egg caché** inspiré du film WarGames. Pour y accéder :

1. Lancez le jeu principal : `python3 main.py`
2. Quand WOPR demande **"WHICH GAME?"** (après la liste des jeux), tapez :
   - `TicTacToe`
   - `Tic-Tac-Toe`
   - `Tic Tac Toe`

**Important :** TicTacToe n'apparaît PAS dans la liste des jeux affichée - c'est un jeu caché !

## Modes de jeu

### 1. Human vs WOPR
- Vous jouez en tant que **X**
- WOPR joue en tant que **O**
- WOPR utilise l'algorithme **minimax** pour un jeu parfait
- **Résultat attendu** : Match nul (si vous jouez parfaitement)

### 2. WOPR vs WOPR (Simulation)
- Deux IA jouent l'une contre l'autre
- Démontre que le jeu parfait mène toujours à un match nul
- Exécute 10 parties consécutives
- **Message final** : "A strange game. The only winning move is not to play."

## Philosophie

Ce jeu illustre le message central du film WarGames et du jeu principal :

> **"A strange game. The only winning move is not to play."**

Tout comme dans une guerre nucléaire, lorsque deux adversaires parfaitement rationnels s'affrontent au TicTacToe, personne ne peut gagner. Le seul résultat possible est un match nul (Mutual Assured Destruction).

## Implémentation technique

### Architecture

```
src/
├── game_logic/
│   └── tictactoe.py          # Logique du jeu et IA
├── ui/
│   └── tictactoe_ui.py       # Interface utilisateur
└── test_tictactoe.py         # Tests automatisés
```

### Algorithme IA

L'IA utilise l'algorithme **Minimax** :
- Explore tous les coups possibles
- Évalue chaque position
- Choisit le coup optimal
- **Résultat** : Jeu parfait, impossible à battre

### Tests

Exécutez les tests avec :
```bash
cd src
python3 test_tictactoe.py
```

**Résultats attendus** :
- ✓ Logique du jeu fonctionnelle
- ✓ Affichage du plateau correct
- ✓ Configuration Human vs AI correcte
- ✓ AI vs AI : 100% de matchs nuls

## Références

- **Film** : WarGames (1983)
- **Citation** : "Shall we play a game?"
- **Leçon** : La futilité de la guerre nucléaire
- **WOPR** : War Operation Plan Response

## Captures d'écran (ASCII Art)

### Menu TicTacToe
```
╔════════════════════════════════════════╗
║         TIC-TAC-TOE GAME MODE          ║
╠════════════════════════════════════════╣
║  1. Human vs WOPR                      ║
║  2. WOPR vs WOPR (Watch AI learn)      ║
║  3. Return to main menu                ║
╚════════════════════════════════════════╝
```

### Plateau de jeu
```
     1   2   3
   ╔═══╦═══╦═══╗
 1 ║ X ║ X ║ O ║
   ╠═══╬═══╬═══╣
 2 ║ O ║ O ║ X ║
   ╠═══╬═══╬═══╣
 3 ║ X ║ O ║ X ║
   ╚═══╩═══╩═══╝
```

### Message final (AI vs AI)
```
╔════════════════════════════════════════════════════════════════════════════╗
║                         SIMULATION COMPLETE                                ║
╠════════════════════════════════════════════════════════════════════════════╣
║  Games played:  10                                                         ║
║  X wins:         0                                                         ║
║  O wins:         0                                                         ║
║  Draws:         10                                                         ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║                         A STRANGE GAME.                                    ║
║              THE ONLY WINNING MOVE IS NOT TO PLAY.                         ║
║                                                                            ║
║  WOPR has learned that perfect play always results in a draw.             ║
║  Just like nuclear war - nobody wins.                                     ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
```

## Conclusion

Ce mini-jeu renforce le message du jeu principal : dans un conflit où les deux parties sont également puissantes et rationnelles, il n'y a pas de vainqueur. La seule solution est de ne pas jouer.

---

*"Greetings, Professor Falken. Shall we play a game?"*

# Made with Bob