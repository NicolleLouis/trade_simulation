# Graphs

# Engine improvement
- Inside the ProfileService replace the money need random value by a true computation

# Code improvement
- Add a config on top of the game to start game by config and avoid mixing things (Human + Hero)
- Add a Hero config to have a lot of option to customize the hero
- Create a service to generate human nicely (Lot of options -> payload -> list of humans or one if hero)
  - Jobs (Optional experience)
  - Money
  - Profile
  - Inventory
- Have an export function that transform a world into it's config file
- Have an import function that take a single config file and generate the whole game

# Analysis - Behaviour
- Compare the profile money to guess what's the best option.
- More Fisherman than Cook
- More Cook than Fisherman
- A Hero that is both Cook and Fisherman

# Perf improvement
- Optimize when more human or longer time -> trade book compression by 'erasing past data'

# Content
- Add Thief
  - Change the amount of money stolen depending on the level?
  - Or steal objects at first and money after a certain level?
- Add couple and children (human number might skyrocket? Maybe more death, ageing?). Transmit money and random job? 
- Add landlord and land renting to fish or gather or cook
- Teacher to give people experience? Hard to price