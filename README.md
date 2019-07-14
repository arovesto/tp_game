# tp_game
This is my hometask on "Programming technologies" course on MIPT

Player contols a group of powerfull heroes, who have their own abilities skills and weatnesess.
By player's clever strategy and tactics this heroes could kill army of different opponents. 

In the future it will be possible to exlpore dungeon and find some interesting things there.

World is dynamic-created, it's changes in every game, so there are factory patterns implemented to obtain needed tools to create good-looking and easy to change worlds

World is full of things, so there are pretty ordinary hierarchy of classes to implement player-controlled powerfull heroes and hordes of mobs, that have factories to help with their creation in world. Also there are an idea to have an not-a-mob things in
world, such as pickups or chests, that could be implemented by inheriting from WorldObject class. Mobs got an Action class and it's
subclasses for interaction with game. Mobs got an special method "move" that says how them supposed to move. It has an piece of world, that mob could see as argument. 

Diretion class helps to move on square grid, for players and mobs. 

Action class wraps disare, that mob or player have. MoveDisposer tells is it possible to satisfy this disare and, and if answer is yes, it will do, what this entity wants.

Log is log, just a log for now.

So, there are four powerfull heroes, such as Wizard, who perfom some support and attack magic spells, but he could be killed easly.
Scout is fast, and could stay unseen for mobs, also he have a bow to deal a damage. Paladin do a close-combat situations, and engineer can set an traps, or automated turrets for helping heroes(will be implemented in far future)

This heroes once go into a Dungeon, to find some thresure or glory, but it is not so important, because them are stuck there. And now them should to find an exit, and this dungeon is full of surprizes, such as hordes of mobs. 
