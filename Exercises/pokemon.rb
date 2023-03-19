require 'poke-api-v2'

# Print the items held by Pikachu
p "Items held by Pikachu"
PokeApi.get(pokemon: 'pikachu').held_items.each { |held_item| p held_item.item.name }

# Print the first 3 moves that Charizard can perform
p "Charizard's moves"
PokeApi.get(pokemon: 'charizard').moves.each_with_index do
  |move, index| 
  break if index == 3
  p move.move.name 
end

# Print the pokemon that has the air-lock ability
p "Pokemon that has the air-lock ability"
p PokeApi.get(ability: 'air-lock').pokemon[0].pokemon.name

# Print the first 5 pokemon that have the flying type
p "Flying type pokemon"
PokeApi.get(type: 'flying').pokemon.each_with_index do
  |pokemon, index| 
  break if index == 5
  p pokemon.pokemon.name 
end
