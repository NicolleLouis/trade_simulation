# DataLog
- Add a raw logger coming from everywhere in code.

# Engine improvement
- Add a food_target_level to try and stockpile a little bit more food. To avoid death by food going stale and no backup
- Inside the ProfileService replace the money need random value by a true computation

# Code improvement
- Add a config on top of the game to start game by config and avoid mixing things (Human + Hero)
- Add a Hero config to have a lot of option to customize the hero
- Create a service to generate human nicely (Lot of options -> payload -> list of humans or one if hero)
  - Jobs (Optional experience)
  - Money
  - Profile
  - Inventory
- Add an option to display jobs/job for the hero/human
- Have an export function that transform a world into it's config file
- Have an import function that take a single config file and generate the whole game

# Analysis - Behaviour
- Write a chapter on the impact of item destruction (No price impact directly but job repartition + item repartition
(duh) and death rate more steady)
- Compare the profile money to guess what's the best option.

# Perf improvement
- No crazy bottleneck for now. Maybe reduce the number of inventory space or amount of trade doable
- Other solution is to store the trade event into a compacted form day by day. And after 60 day, sum into the big one?

# Content
- Add Thief
  - Change the amount of money stolen depending on the level?
  - Or steal objects at first and money after a certain level?
- Add another cooking option: Apple -> Apple Pie (Both edible but giving way more in the second case)
- Add another cooking option: Multiple ingredients
- Add couple and children (human number might skyrocket? Maybe more death, ageing?). Transmit money and random job? 
- Add landlord and land renting to fish or gather or cook
- Teacher to give people experience? Hard to price