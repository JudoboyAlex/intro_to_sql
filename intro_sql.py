# Find all the robots from Star Wars.

SELECT name FROM robots;

# Find the robot with an "anxious" personality.

SELECT name FROM robots WHERE personality = 'anxious';

# Find all recipes that are nut free.

SELECT * FROM recipes WHERE nut_free = True;

# Count the number of recipes that are gluten free but not vegetarian.

SELECT COUNT(gluten_free) FROM recipes WHERE vegetarian = False;

# Find the animal with the most legs.

SELECT MAX(number_of_legs) FROM animals;

# Find the board game that takes the least amount of time to play.

SELECT MIN(mins_to_play) FROM board_games;

# Find the recipe that takes the most time to prepare.

SELECT MAX(minutes_required) FROM recipes;

# Find all the robots whose name starts with the letter M.

SELECT name FROM robots WHERE name LIKE 'M%';

# Count the number of board games that can be played by 8 people.

SELECT name FROM board_games WHERE max_players > 7;

# Find all animals that are swimming and egg-laying.

SELECT name FROM animals WHERE swimming = True AND egg_laying = True;

# Find all animals that are swimming and egg-laying but not flying.

SELECT name FROM animals WHERE swimming = True AND egg_laying = True AND flying = False;

# Find the board game that supports the largest number of people.

SELECT name, max_players FROM board_games ORDER BY max_players;