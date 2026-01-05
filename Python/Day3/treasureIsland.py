gameArt = r'''             
                           _
                      _,-"" ""-._
                   ,-'           `-.
                 ,'                 `.
               ,'                     `.
             ,'                         `.
            /                             \
           /   Y O U  D O N ' T  K N O W   \
          /                  ___            \
         :       |     /|   /   \  |  /      :
        :        |    / |  |       | /        :
        :        |   /__|  |       |/\        :
       :         |  /   |  |       |  \        :
       :     .__/  /    |   \___/  |   \       :
       |                                       |
       |                                       |
       |   ..::::::..             ..::::::..   |
   ,-. | .::"'____ """           """ ____`"::. | ,-.
   |\ \|    .' `8P`-.              .'`8P `.    |/ /|
   |/\ |     `-____-'  :       :   `-___-'     | /\|
   || \|               :       :               |/ ||
   ||_||              :         :              ||_||
8888888888888888888888888888888888888888888888888888888
888888888888888888888888888888888888888888888888[dd]888
8888888888888888888888888888888888888888888888888888888'''

print(gameArt)
print("Welcome to Treasure Island.\n Your mission is to find the treasure.")

move = input('You\'re at a cross road. Where do you want to go?\n\tType "left" or "right"\n')
if move == "left" or move == "Left":
    move = input('You\'ve come to a lake. There is an island in the middle of the lake.\n\tType "wait" to wait for a boat. Type "swim" to swim across.\n')
    if move == "wait" or move == "Wait":
        move = input('You arrive at the island unharmed. There is a house with 3 doors.\n\tOne red, one yellow and one blue. Which color do you choose?\n')
        if move == "red" or move == "Red":
            print("Burned by fire.\nGame Over.") 
        elif move == "yellow" or move == "Yellow":
            print("You Win!")
        elif move == "blue" or move == "Blue":
            print("Eaten by beasts.\nGame Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")