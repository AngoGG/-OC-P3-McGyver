J’ai lu ton code sur ma pause ;-)

### Comme promis, retours en vrac :
- Je commence par le commentaire le plus violent : ton anglais est bourré de fautes (mais bon, c’est annexe :p). Comme ça s’est dit ! (désolé)
- Il faut impérativement que tu utilises pipenv. Je ne conseille plus d’utiliser virtualenv car il est dépassé. pipenv est désormais le gestionnaire recommandé officiellement : https://packaging.python.org/tutorials/managing-dependencies/ En l’état, il n’est pas possible de lancer ton P3 efficacement : les modules requis n’étant pas précisés, on est obligé de lancer le script, regarder les dépendances manquantes, les installer puis relancer :


Traceback (most recent call last):
  File "main.py", line 10, in <module>
    import pygame
ModuleNotFoundError: No module named 'pygame'

-          Crée peut-être une classe pour tes constantes plutôt qu’une simple énumération de variables. Ça sera plus propre ; l’utilisation des variables constantes est à proscrire du scope global. Tu gères tes constantes en attributs de classe et tu passes par la classe. Et comme ça serait une classe, pense à la placer avec les autres.

-          Il serait intéressant de revoir ton modèle afin de mieux gérer la structuration de ton projet. Typiquement, on aura tendance à créer une classe maîtresse qui se chargera de piloter l’ensemble de processus. Grosso modo, tu déplaces tout le contenu de ta fonction main() de main.py dans une classe App (ou ce que tu veux) et ton main.py devient minimal genre (extrait de mon P3) :

```
from app.Game import Game

def main():
    game = Game()
    game.play()

if __name__ == '__main__':
    main()
```
Et c’est dans Game.play() que tout se pilote.

- Je n’aime pas trop les level.Level() ou items.Item() mais après il y a certains codeurs qui préfère garder les noms de package donc c’est un avis personnel.
J’aurais tendance à remplacer ta ligne
```
  from classes import character, items, level
```
par des lignes éclatées
```
  from classes.character import Character
  from classes.level import Level
  from classes.items import Item
```
**Mais concrètement, voici ce que je ferais :**

dans classes/__init__.py
```
from .character import Character
from .level import Level
from .items import Item
```
dans main.py (ou ta classe maîtresse si tu en fais une)
               from classes import Character, Item, Level
et tu supprimes tous les level., character. et items..

- Pour tous tes event.type, utilise le code genre pygame.K_LEFT et pas le code numérique : imagine que pygame change le numéro pour une raison X ou Y, ils modifieront leur constante donc ça sera transparent pour toi. Par contre, si tu laisses le code chiffré, ben, ça buggera. Les constantes de pygame sont là pour ça ;-) Et puis c’est plus parlant : la preuve, tu as mis les noms des constantes en commentaires :p
- Lie également q à quit.
- Quand tu fais un print, c’est un peu c*n de le faire en console, je le ferais apparaître dans l’interface pygame. De même, quand le jeu se termine (gagné ou perdu), il faudra l’afficher dans pygame (et par exemple attendre un keystroke pour fermer l’UI).
- Il y a certainement moyen de factoriser les lignes 72 à 89 dans main.py
- Pourquoi nommer la classe Level si elle est employée en tant que « game » dans main.py ?
- Dans Level, tu crées window_generation() en méthode de classe (@classmethod) alors que tu ne te sers pas de la classe (variable cls) => autant la déclarer en méthode statique (@staticmethod).
- La classe Level gère des tâches de fond (le jeu lui-même) ainsi que des tâches d’affichage (pygame). Je ferais deux classes distinctes : une classe == une responsabilité.
- Dans get_labyrinth_structure(), je ne comprends pas l’intérêt de faire une variable temporaire level_structure au lieu d’employer directement self.level_structure.
- get_labyrinth_structure() doit être refactorisée, il y a moyen de la réduire fortement
- set_labyrinth() ibidem
- Quid d’autres formats en entrée ? L’objectif de la formation est d’apprendre à exploiter python. Pourquoi ne pas proposer une map du labyrinthe en excel ou en xml par exemple ?
- L’interface n’est pas suffisamment robuste : si l’on rajoute des lignes dans le fichier map, ça déconne (par exemple avec des lignes en plus on ne voit plus la ligne avec le gardien)
- Tu pourrais envisager de rendre la taille du labyrinthe plus flexible : si le fichier map contient 50 lignes et 100 colonnes, pourquoi limiter à 15*15 ?
- Je ne comprends pas la logique : un personnage MacGyver a une map qui lui appartient ? parce que c’est ce que veut dire cette ligne dans character.py :
```
self.map = map_structure
```
- Pour moi, ça n’est pas à la classe Character de gérer les contrôles des keystrokes. Le personnage bouge sur le plateau, mais il n’a pas à contrôler l’input utilisateur. A nouveau une classe == une responsabilité.
- position devrait être un tuple plutôt qu’une liste à mon sens car l’attribut est immutable
- Grosso modo les mêmes commentaires de Character pour Item (map et position)
- Je ne comprends pas du tout item_position() : déjà je ne vois aucune différence entre les if/elif/elif. Puis je créerais un attribut contenant le type de l’item (needle, ether, tube) et je ferais mon contrôle sur self.type (par exemple) mais en dehors . La en fait c’est comme si un objet Item ne représentait pas un Item mais des Items => erreur de modèle (une classe == une responsabilité, ici définir ce qu’est un item). Et il y a de la redondance de code
-          Même remarque pour display()
-          display() : c’est quoi ce item_number == 3 ?? pas clair (j’ose ? oui j’ose : on dirait du Jonathan aaaaaahhhhhh !!!!)
-          Et à nouveau, en mettant en dur les positions (40, 450 etc.), tu perds en flexibilité. A minima les mettre dans ta classe constantes comme ça c’est plus facilement paramétrable et centralisé.


### Conclusion générale :
1. C’est cool, ça fonctionne et ça fonctionne bien J
2. Le code est clair (hormis ce item_number == 3, là :p)
3. Utilise pipenv
4. Le modèle objet déconne par endroits (surtout dans Item)
5. Comme tu le disais hier toi-même, il faudrait séparer le fond de la forme
6. T’es pas PEP 8 :p
7. Tu peux éventuellement t’intéresser aux type hints, si cela t’intéresse, mais limite-toi d’abord aux signatures des méthodes uniquement (attention, ce n’est pas demandé pour le P3 – ni aucun projet – donc si tu les mets, tu risques de devoir argumenter leur présence lors de la soutenance).
8. N’hésite pas à faire plus que ce qui est demandé afin d’apprendre plus. C’est toi qui es responsable de ta formation, libre à toi d’élargir tes horizons (mais fais gaffe aux délais également)

Voilà pour un premier retour J
C’est à dessein que je ne te donne pas de code mais juste des pistes : tu assimileras bien mieux en cherchant tout seul (politique employée sur le discord) mais n’hésite pas à revenir avec des questions (vers moi ou qui tu veux).

@+!
