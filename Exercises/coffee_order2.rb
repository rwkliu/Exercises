require 'httparty'
require 'json'

# This script continuously asks a user for a hot coffee drink and returns a receipt
# that contains the drink name, id, and description. This information is obtained 
# from the Coffee API. 

#Get the coffee drink data and parse the data into a list of hashes
response = HTTParty.get('https://api.sampleapis.com/coffee/hot')
parsed = JSON.parse(response.body)

run = true
while run
  print "Enter the coffee id: "
  input = gets.chomp
  break if input == "quit"
  
  #Use binary search to find the hash corresponding to the id specified by input
  left = 0
  right = parsed.length - 1
  until left > right
    middle = ((left + right) / 2).floor()
    current_id = parsed[middle].fetch("id")
    target_id = input.to_i
    if current_id < target_id
      left = middle + 1
    elsif current_id > target_id
      right = middle - 1
    else
      break
    end  
    middle = -1
  end
  
  if (middle == -1) 
    next 
  end

  p "Drink name: #{parsed[middle].fetch("title")}"
  p "Id: #{parsed[middle].fetch("id")}"
  p "Description: #{parsed[middle].fetch("description")}"
end
