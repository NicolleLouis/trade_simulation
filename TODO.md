# DataLog
- Add a raw logger coming from everywhere in code. (Classic logging)
- Event Logger

# Engine improvement
- __Job utility is dependent on object average market value if possible instead of intrinsic value__
- Add a food_target_level to try and stockpile a little bit more food. To avoid death by food going stale and no backup
For this we need to compute every beginning of turn the amount of food owned + stomach level then compare it to an expected amount
- Inside the ProfileService replace the money need random value by a true computation

# Code improvement
- Add a config on top of the game to start game by config and avoid mixing things (Human + Hero)
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
- World Events (Event Base Class) vs Human Event
- Death of old age
- Croquemort
- Garden + Gardener with passive income (Active action to improve garden)
- Event: récolte abondante
- Event: perte des stocks de nourriture
- Add another cooking option: Apple -> Apple Pie (Both edible but giving way more in the second case)
- Add another cooking option: Multiple ingredients
- Add couple and children (human number might skyrocket? Maybe more death, ageing?). Transmit money and random job? 
- Add landlord and land renting to fish or gather or cook
- Teacher to give people experience? Hard to price
- Family name to track family across ages (Graph number of family member)
