# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("jack")
define b = Character("bob") 
define a  = Character ("angel")
define e  = Character ("emma")
define l  = Character ("leo")
define m  = Character ("max")
define b = Character ("bear")
define pm = Character ("police man")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    show maxy scared at left 
    m "in the dark of the night there was broken plane and childrens was scared and i protected the childrens and there was a big scary bear"
    show police man at right 
    pm "okay now we will try to find the bear and search"
    
    e "im scared i wanna go to my home "
    pm " do not worry kid we will send you home soon "
    b "is that is the bear " 
    pm "hahaha no kid its not "
    j "uh no i think it is the bear "
    a "no i think its really the bear ahhhh" 
    l "ahhhhhh its the bear"
    pm "oh no kids get in the car right now "
    m "oh okay now the kids are in the car ahhh what should we do "
    pm "you will help me to get out this bear from here"
    m " uh okay but i am scared"
    pm "scared . scared what do not  be scared never ever !"
    m "umm okay lets go !!"
    pm "get the flashlight from the car"
    m "okay here i am going "
    pm "here give me it "
    m "okay but what you will do with it "
    pm "you will see boy "
    m "oh okay i understand it the bears are scared of light "
    pm " yes boy you need to learn more and now lets go to the car to let the kids go to their home"
    m "okay lets go"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
