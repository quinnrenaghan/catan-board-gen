# Catan Board Generator

This is a python script for generating fair and balanced catan game boards, for use in game. To use it, run the get_board function found in the balanced_util file, and print the resulting board out. Note: the more time you allow the generator to run, the more balanced/fair the resulting board will be.

The board is characterized by a set of tiles, and a set of vertices, which should both be printed out in order to view the board. 

The generator judges boards on 6 different metrics:
1. Distribution of resources across the board
2. Resource clustering
3. Resource probability equality
4. Distribution of numbers acorss the board
5. Number clustering
6. Harbor strength distribution
