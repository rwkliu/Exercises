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
  
  # Print the drink name, id, and description
  parsed.each do |item|
    if (item.fetch("id") == input.to_i)
      p "Drink name: #{item.fetch("title")}"
      p "Id: #{item.fetch("id")}"
      p "Description: #{item.fetch("description")}"
    end
  end
end
