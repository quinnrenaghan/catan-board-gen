# Catan Board Generator

### Overview
This is a python script for generating fair and balanced catan game boards, in order to remove variance from the game. The user can run the program through the get_board function - which will generate and grade boards automatically. The more time you allow the generator to run, the more balanced and fair the resulting board will be. Note: the generator is imperfect, and I have plans to add more features soon. You can find more detail on these upcoming changes (and other stuff) below.

### Background
Settlers of Catan is a popular board game, where players build civilizations on a hexagonal playing board. The board consists of hexes, which each have a resource: brick, wheat, sheep, ore, wood, and desert, and a number: 2 through 12. There are also ports: trading outposts on the edge of the board. As a general rule, players aim to build their civilization adjacent to a variety of resources (but not desert), as well as numbers that have a high probability of being rolled with 2 dice (i.e. 6, 8). The board is different each game, and it being balanced and fair is crucial for a fun experience, especially for experienced players. 

Before I go any further, I'll clarify the difference between balanced and fair, as it pertains to my generator:

* A **balanced** board is a board where the resources are distributed evenly across the board, and numbers are distributed evenly across both the board and the resources.
* A **fair** board gives each player an equal chance to win, regardless of what order they play in. 

To illustrate the difference, imagine a board on which the resources and numbers are spread evenly - this board is balanced. However, it happens that they are spread in such a way that there are no extremely strong starting settlement locations, and 6 medium strength locations. As a result, if you play this board with 4 people, and everyone plays optimally, there will be 2 people that have 2 medium strength starting locations, and 2 people that have 1 medium and 1 weak starting locations. So, this board is balanced, but not fair. 

This may seem like a small difference, but starting location in Catan can make or break your game. 

### Process
The board is characterized by a set of tiles, and a set of vertices.  

The tiles are characterized by the coordinate system below, from the Red Blob Games article on hexagonal grids. Note: the Catan board only encompasses the inner hexagon with radius = 2 in the photo below.


<img width="467" alt="Screenshot 2024-06-20 at 10 04 13 PM" src="https://github.com/quinnrenaghan/catan-board-gen/assets/116096425/91d1bd7a-09c8-4c0f-9005-a2e05372620c">


The vertices are characterized by their ID, the hexes they border (and ports), and the IDs of adjacent vertices. I assigned the IDs manually - they are loaded the first time you run the program. After establishing the game pieces, the generator completes the board by randomly assigning the resources, numbers, and ports. 

Then, it evaluates the board on 7 different metrics, corresponding to the following questions:
1. Distribution of resources across the board: Are the resources evenly split across the 3 axis?
2. Resource clustering: Are there any clumps of the same resource type?
3. Resource probability equality: Does each resource have an equal probability to roll?
4. Distribution of numbers across the board: Are the numbers evenly split across the 3 axis?
5. Number clustering: Are there any clumps of the same number?
6. Harbor strength distribution: Are the harbors similar in strength?
7. 4 Player Fairness: Assuming a pick order of 1 2 3 4 4 3 2 1 (snake draft), does each player get an equal strength starting civilization?

Finally, it normalizes each measure to a score from 0-1, and returns the most fair and balanced board (the lowest total score).

Here is one good board:

<img width="430" alt="image" src="https://github.com/quinnrenaghan/catan-board-gen/assets/116096425/be184553-4c58-4ace-a6b1-ce77af879abd">


### Future Plans

Going forward, I want to modify the fairness metric so that it takes nearby harbors, longest road, and largest army into account. Also, I want to improve the visual display of the board - so that the generator can be used by people unfamiliar with the backend. 

