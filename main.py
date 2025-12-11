from drafter import *
from bakery import assert_equal
from dataclasses import dataclass
import random
#import pygame

#############################################################################
# Assignment required code

set_site_information(
    author="Arielle Davis (ellyward@udel.edu)",
    description="""A short choose-your-own-adventure game about
    a witch moving into her new home and encountering something strange.""",
    sources=["Official Drafter documentation, Google"],
    planning=["CISC108_FinalProject_DesignPhase.pdf"],
    links=["https://github.com/UD-F25-CS1/cs1-website-f25-ellyward", "https://youtu.be/E54YkotXk4s?si=wOTlMJGYxgO0J7-B"]
)
#hide_debug_information()
set_website_title("Housewitching")
set_website_framed(False)

#############################################################################
# Website styling

#Takes away default website styling
set_website_style("none")

#Custom website styling
add_website_css("""
body {
    background-color: #222222;
    color: White;
    font-size: 40px;
    font-family: "Papyrus", sans-serif;
    width: 960px;
    margin: 0 auto;
    text-align: center;
    line-height: 1.5;
    justify-content: center;
}

p {
    line-height: 1.5;
    color: White;
}

h1 {
    color: White;
}

img {
    display: block;
    margin: auto;
    width: 500;
    border: 15px solid White;
    border-radius: 30px;
    padding: 10px;
  
}

button {
    background-color: #656565;
    font-family: "Papyrus", sans-serif;
    font-size: 30px;
    color: White;
    text-align: center;
    border-radius: 30px;
    padding: 10px;
    border: 5px solid White;
}

input[type="text"] {
    background-color: #656565;
    font-family: "Papyrus", sans-serif;
    font-size: 30px;
    color: White;
    text-align: center;
    border-radius: 30px;
    padding: 10px;
    border: 5px solid White;
}
""")

#############################################################################
# All dataclasses

@dataclass
class Item:
    """
    Any items the player may find - potions, weapons, etc.
    
    Attributes:
        name: The name of the item.
        quantity: The amount of the item found.
        health: If the item replenishes health, this is how much it will give.
        damage: If the item deals damage, this is how much it will do.
    """
    name: str
    quantity: int
    health: int
    damage: int
    
@dataclass
class Monster:
    """
    Monsters that can appear during the game.
    
    Attributes:
        name: The name of the monster.
        health: How much health the monster has.
        damage: How much damage the monster can do with attacks.
    """
    name: str
    health: int
    damage: int

@dataclass
class Status:
    """
    Status of the monsters surrounding the player.
    
    Attributes:
        is_monsters: If there are any monsters nearby.
        monsters: A list of the monsters nearby.
    """
    is_monsters: bool
    monsters: list[Monster]
    
@dataclass
class Updates:
    """
    Updates that are able to be modified to progress the story.
    
    Attributes:
        routes: Name of the routes corresponding with the progression of the story.
        is_hidden: If the player is hidden or not.
    """
    routes: str
    is_hidden: bool

@dataclass
class State:
    """
    The state of the player through-out the game.
    
    Attributes:
        name: The name of the player.
        items: List of any items the player has obtained.
        health: The players current health.
        damage: The damage the player can deal when attacking.
        status: Status of the surrounding area of the player.
        updates: Corresponding actions taken by the player.
    """
    name: str
    items: list[Item]
    health: int
    damage: int
    status: Status
    updates: Updates

#############################################################################
# Global variables

#potions
potion_1 = Item("Invisibility Potion", 1, 0, 0)
potion_2 = Item("Health Potion", 0, 0, 0)

#weapons
knife = Item("Knife", 1, 0, 0)

#monsters
monsters = [Monster("???", 80, 0),
            Monster("The Tall Man", 50, 0),
            Monster("Mr. Smiles", 30, 0)]
enemy = monsters[random.randint(0,2)]

#############################################################################
# Helper functions

# Initialize mixer
#pygame.mixer.init()

#############################################################################
# Introduction routes

@route
def index(state: State) -> Page:
    """ The main page of the game, letting the player enter their name. """
    #Loads and loops the audio in the background
    #pygame.mixer.music.load("once_upon_a_time.mp3")
    #pygame.mixer.music.play(-1, 0.0)  
    return Page(state,[
        "<audio><source src='once_upon_a_time.mp3' type='audio/mpeg'></audio>"
        "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
        "<br>",
        "<h1> HOUSEWITCHING </h1>",
        "<br>",
        "Welcome to your newly-bought home, young witch. What is your name?",
        "<br>",
        TextBox("name", "Young Witch"),
        "<br>",
        Button("Move In", move_in),
        "<br>",
        "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
        ])

@route
def move_in(state: State, name: str) -> Page:
    """ Updates the state with the new player name, then redirects to front_door. """
    state.name = name
    state.updates.routes = "move_in" 
    return front_door(state)

#############################################################################
# Area routes

@route
def front_door(state: State) -> Page:
    """ The page for the front door of the house. """
    state.updates.is_hidden == False
    #First time entering house
    if state.updates.routes == "move_in":
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "" + "Your name is " + state.name + ".",
            "You step into your new home, finding yourself in a hallway past your front door.",
            "Ahead of you seems to be the living room.",
            Image("front_door.jpg", 500),
            "<br>",
            Button("Explore your living room", living_room),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])
    #If you choose to leave running from the monster, but without items
    if state.updates.routes == "run":
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "You rush for the front door,",
            "hearing the crash of the attic door being broken off it's hinges behind you.",
            "You sprint faster towards the front door,",
            "loud thumping and scraping rapidly growing closer behind you.",
            "You narrowly avoid a giant hand grasping at your back,",
            "just as you throw open the door and cross the threshold onto the front lawn.",
            "You stop running, turning to see the crude monster slink back into the shadows of your home.",
            "For a moment, you breathe a sigh of relief, just happy to have escaped.",
            "Honestly, no one can blame you for forgetting all the other monsters outside your house.",
            "At the very least, they're quick to rip you apart - you don't feel a thing.",
            "...Almost.",
            Image("monsters_woods.jpg", 800),
            "<br>",
            Button("You Died", game_over),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])
    #If you choose to leave running from the monster, but with items
    if state.updates.routes == "confrontation":
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "As you move to run, you hear something drop and roll across the floor.",
            "It's an Invisibility Potion!",
            "It must've been with the items you found.",
            "You grab the potion and take off towards the front door.",
            "As you run, you hear the crash of the attic door being broken off it's hinges behind you.",
            "You sprint faster towards the front door,",
            "hearing loud thumping and scraping come to a halt behind you.",
            "It looks like the monster can't see you!",
            "You close in on the door, throwing it open and crossing the threshold onto the front lawn.",
            "You stop running and turn to look through the front door,",
            "seeing the crude monster still stalking around your living room.",
            "You breathe a sigh of relief, just happy to have escaped.",
            "As you turn to leave, you almost bump into another sizeable and horrifying creature.",
            "It's a good thing you took that invisibility potion -",
            "you entirely forgot about the monsters outside!",
            "You head off into the forest, further and further away from your new home.",
            "Hopefully, the monsters don't mess the place up too bad - you would like your deposit back.",
            Image("got_away.jpg", 700),
            "<br>",
            Button("Escape", win_screen),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])
    
@route
def living_room(state: State) -> Page:
    """ The page for the living room. """
    #First time entering living room
    if state.updates.routes == "move_in":
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "You step into the living room, ready to decorate your brand new abode.",
            "You begin unpacking the boxes sitting in the corner.",
            "After a while of setting out books and other knick knacks, you come across a photo.",
            "Looking closer, you see its a bunch of old childhood photos.",
            "Some are cute and nostalgic - making you look back on those old memories with fondness.",
            "Others... well, lets just say anyone could tell you were definitely a troublemaker back then.",
            "You find yourself getting lost in the little scrapbook, just remembering the good 'ol times.",
            "So much so, that you almost miss that faint voice, whispering in the distance.",
            Image("living_room.jpeg", 700),
            "<br>",
            Button("What is that?", updated),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])
    #After you begin unpacking in the living room
    if state.updates.routes == "living_room":
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            italic("" + "'" + state.name + "." + "'"),
            "A voice calls your name from somewhere within the house...",
            "It's coming from the attic.",
            Image("living_room.jpeg", 700),
            "<br>",
            Button("Go to the attic", attic),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])
    #Re-entering the living room after seeing monster in the attic
    if state.updates.routes == "run":
        state.updates.is_hidden == False
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "Loud cracks and bangs echo from beyond the attic door.",
            "It'll only hold that monster off for so long.",
            "What will you do?",
            Image("living_room.jpeg", 700),
            "<br>",
            Button("Hide", hide),
            Button("Run to kitchen", kitchen),
            Button("Leave", front_door),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])
    #In the living room after you've hidden
    if state.updates.routes == "hiding":
        state.updates.routes = "run"
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "You peek out from your hiding spot.",
            "From the living room, you can see the attic door bowing in, creaking and whining loudly.",
            "That thing will get in any second now.",
            "What will you do?",
            Image("peeking.jpg", 700),
            "<br>",
            Button("Stay put", hide),
            Button("Run to kitchen", kitchen),
            Button("Fight", updated),
            Button("Leave", front_door),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])
    #In the living room after you've chosen to fight
    if state.updates.routes == "confrontation":
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "A deafening crash rings out from the living room.",
            "As you leave the kitchen, you come face to face with the monstrous creature.",
            "You've been spotted.",
            "Looks like there's no turning back now.",
            Image("monster_2.jpg", 700),
            "<br>",
            Button("Fight", fight),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])

@route
def kitchen(state: State) -> Page:
    """ Page for the kitchen. """
    state.updates.is_hidden = False
    #In the kitchen after running from the monster
    if state.updates.routes == "run":
        state.updates.routes = "in_kitchen"
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "The kitchen is silent, though faintly,",
            "you can still hear the creature trying to break it's way through the attic door.",
            "Maybe something in here can be of use to you.",
            Image("kitchen.jpeg", 700),
            "<br>",
            Button("Look around.", updated),            
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])
    #Finding items in the kitchen
    if state.updates.routes == "in_kitchen" and state.items != []:
        state.updates.routes = "confrontation"
        all_items = ""
        for item in state.items:
            items = (str(item.quantity) + " " + item.name + ".<br>")
            all_items += items
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "Looks like you found something!",
            "You got:",
            all_items,
            "Nice! Maybe now you can do something about that monster!",
            Image("found_items.jpg", 700),
            "<br>",
            Button("Face the monster", living_room),
            Button("Try to leave again", front_door),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])

@route
def attic(state: State) -> Page:
    """ The page for the attic. """
    #Entering the attic
    if state.updates.routes == "living_room":
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "As you open the attic door,",
            "you can't help but cough due to the sheer amount of dust released into the air.",
            "You climb the ladder carefully, peeking your head through the attic entrance and looking around.",
            "The room is empty and dark,",
            "save for for the one patch of floor illuminated by the setting sun outside the singular window.",
            "What?",
            "You look closer... there's something on the ground.",
            "You walk into the strip of light, eyeing the object on the floor.",
            "It looks like a little statue of a woman, holding a glowing orb in its hands.",
            "The orb is swirling with a shining rainbow of colors, leaving you enamored and drawing you in.",
            "Wanting to inspect the artifact further, you pick it up - ",
            "Only for it to crumble in your hands almost immediately.",
            "You sit in dumfounded silence as you watch the bits of statue tumble onto the floor,",
            "and that little orb roll away from you and extinguish in the darkness.",
            "You're about to retrieve it when suddenly, it feels as if the entire house is being shaken.",
            "You fall to the ground, looking up to window, just to find a pitch black void beyond the glass.",
            "'Welp.', you think, 'That can't be good.'",
            Image("attic.jpg", 700),
            "<br>",
            Button("Try to look out the window anyway", attic_window),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])

@route
def attic_window(state: State) -> Page:
    """ The page for the attic_window. """
    #Looking through the attic window
    if state.updates.routes == "living_room":
        if state.status.is_monsters == False:
            return Page(state,[
                "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
                "<br>",
                "As you stare outside your attic window,",
                "you can no longer see the forest trees that surrounded your property.",
                "The void stretches on, making you think there's nothing there at all.",
                "That's when something smacks against the window pane, hard.",
                "You fall back onto the ground, startled, eyes wide.",
                "There's a face in the window.",
                Image("attic_window.jpg", 500),
                "<br>",
                Button("What is that", status),
                "<br>",
                "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
                ])
    #Seeing monster through attic window
    if state.updates.routes == "living_room":
        if state.status.is_monsters ==  True:
            #Stops current audio and plays new audio
            #pygame.mixer.music.stop()
            #pygame.mixer.music.load("in_my_way.mp3")
            #pygame.mixer.music.play(-1, 0.0)
            return Page(state,[
                "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
                "<br>",
                "A grotesque figure looks back at you from the window,",
                "it's face a distorted white mask surrounded by matted black hair.",
                "It hold eye contact with you for a moment -",
                "even with it's lack of eyes, you know its staring at you.",
                "Then a large palm rises from below the window - and begins pounding on the glass.",
                "Immediately, you head for the attic door, scrambling to grasp the handle.",
                "Just as you begin to descend, you hear a crack, followed by a loud shatter.",
                "It got inside.",
                Image("monster_1.gif", 700),
                "<br>",
                Button("Run.", updated),
                "<br>",
                "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
                ])
        
@route
def the_end(state: State) -> Page:
    """Final scene after winning fight against monster"""
    #After you won the fight against the monster
    if state.updates.routes == "fighting":
        state.updates.routes = "ending"
        #Stops current audio and plays new audio
        #pygame.mixer.music.stop()
        #pygame.mixer.music.load("fallen_down_reprise.mp3")
        #pygame.mixer.music.play(-1, 0.0)
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "You stand there for a moment - breathing heavy as you try to steady yourself.",
            "After a few seconds you sink to the floor,",
            "sighing in relief as the last of your adrenaline wears off.",
            "You look down at the knife in your hand, covered in the blood of that wretched creature.",
            "It glints in the sunlight, as pristine as when you bought it.",
            "Wait?",
            "Sunlight?",
            "Its then that you notice the thick fog of darkness that once enveloped your home is no more.",
            "Rays of sunlight are cast from your living room window,",
            "shining upon the disintegrating body of the slain monster.",
            "?",
            "Whats that on the floor?",
            Image("the_orb.jpg", 700),
            "<br>",
            Button("Pick it up", the_end),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])
    #Good ending
    if state.updates.routes == "ending":
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "You reach for the item on the ground, holding it up in the sunlight for a better look.",
            "The small sphere is only slightly bigger than a marble and feels smooth to the touch.",
            "However, it glows a brilliant variety of colors,",
            "swirling together, reminiscent of the cosmos in the starry night sky.",
            "It kinda looks like that orb you broke earlier.",
            "The orb glows brighter for a moment,",
            "and outside your window, you see the last of the monsters slip away into the treeline.",
            "You don't know why the monster had this, but you definitely feel like you should keep it.",
            "If nothing else, it at least seems to keep other creatures off your property.",
            "You place the orb in a little jewlery box and place it on the mantle above your fireplace.",
            "For your own sanity (and physical well-being),",
            "you'll be careful not to break this one.",
            Image("the_end.png", 800),
            "<br>",
            Button("Guess we'll have to see about that", win_screen),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])
        
#############################################################################
# Action routes

@route
def status(state: State) -> Page:
    """ Updates the status class to indicate that there are monsters in the area. """
    state.status.is_monsters = True
    return attic_window(state)

@route
def hide(state: State) -> Page:
    """ Page for when the player chooses to hide after the monster breaks in. """    
    state.updates.is_hidden = True
    #Choosing to hide after running from the monster to the living room
    if state.updates.routes == "run":
        state.updates.routes = "hiding"
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "You hide behind a couch in the corner of your living room, trying to still your rapid breathing.",
            "You can still hear the rhythmic thumping from the attic.",
            "The monster hasn't gotten in yet.",
            "Maybe there's something else you can do?",
            Image("hiding.png", 700),
            "<br>",
            Button("Try something else", living_room),
            Button("Keep hiding", updated),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])
    #Chose to keep hiding
    if state.updates.routes == "kept_hiding":
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "You keep hiding.",
            "With a deafening crash, the monster makes it's way into your home.",
            "You shrink back into the closet at the beast stalks around the living room.",
            "Through the slats on the closet door, you can see the light slowly dimming,",
            "leaving your living room pitch black.",
            "You don't know how much time passed while you sat in that closet.",
            "The darkness felt almost heavy around you - and soon, you find yourself drifting into sleep.",
            "When the darkness finally lifts from your home, the monsters are gone - and so are you.",
            "Your house goes up for sale again and everyone wonders where you could have possibly gone.",
            "At the very least, your demise was peaceful.",
            Image("sleep_forever.jpg", 700),
            "<br>",
            Button("You'll sleep forever", game_over),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])
    
@route
def fight(state: State) -> Page:
    """ Page for when the player chooses to fight after the monster breaks in. """
    #Player health can't go above 100
    if state.health >= 100:
        state.health = 100
    #Player health cannot go below 0
    if state.health <= 0:
        state.health = 0
    #Enemy health cannot go below 0
    if enemy.health <= 0:
        enemy.health = 0
    #Choosing to fight the monster without items
    if state.updates.routes == "confrontation":
        if state.items == []:
            return Page(state,[
                "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
                "<br>",
                "Looks like you decided to fight.",
                "Which seems like a pretty stupid decision on your part -",
                "considering you have nothing to fight with.",
                "Even the monster thought that was kind of dumb.",
                "Not that you had much time to dwell on it as it was tearing you limb from limb.",
                "Maybe look for a weapon next time!",
                Image("KO.jpg", 800),
                "<br>",
                Button("You died", game_over),
                "<br>",
                "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
                ])
        #Choosing to fight the monster with items
        elif state.items != []:
            #Stops current audio and plays new audio
            #pygame.mixer.music.stop()
            #pygame.mixer.music.load("battle_against_a_true_hero.mp3")
            #pygame.mixer.music.play(-1, 0.0)
            return Page(state,[
                "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
                "<br>",
                "Looks like you decided to fight.",
                "Hopefully, luck is on your side.",
                Image("fight_stance.jpg", 600),
                "<br>",
                Button("Make a move", updated),
                "<br>",
                "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
                ])
    #During the fight while you and the monster still have health
    if state.updates.routes == "fighting":
        if state.health > 0 and enemy.health > 0:
            return Page(state,[
                "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
                "<br>",
                state.name,
                "Your Health: " + str(state.health),
                "Your Items:",
                potion_2.name + ": " + str(potion_2.quantity),
                "⊹ ࣪ ˖ ꒰ঌ ♡ ໒꒱ ⊹ ࣪ ˖",
                enemy.name,
                "Enemy Health: " + str(enemy.health),
                "⊹ ࣪ ˖ ꒰ঌ ♡ ໒꒱ ⊹ ࣪ ˖",
                Image("fighting.jpeg", 800),
                "<br>",
                Button("Attack", fighting),
                Button("Take Health Potion", take_potion),
                "<br>",
                "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
                ])
        #During the fight while you have no health
        elif state.health <= 0:            
            return Page(state,[
                "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
                "<br>",
                state.name,
                "Your Health: " + str(state.health),
                "Your Items:",
                potion_2.name + ": " + str(potion_2.quantity),
                "⊹ ࣪ ˖ ꒰ঌ ♡ ໒꒱ ⊹ ࣪ ˖",
                enemy.name,
                "Enemy Health: " + str(enemy.health),
                "⊹ ࣪ ˖ ꒰ঌ ♡ ໒꒱ ⊹ ࣪ ˖",
                "Unfortunately, it looks like you never stood a chance.",
                Image("KO.jpg", 800),
                "<br>",
                Button("You died", game_over),
                "<br>",
                "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
                ])
        #During the fight where you still have health and the monster has no health
        elif state.health > 0 and enemy.health <= 0:            
            return Page(state,[
                "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
                "<br>",
                state.name,
                "Your Health: " + str(state.health),
                "Your Items:",
                potion_2.name + ": " + str(potion_2.quantity),
                "⊹ ࣪ ˖ ꒰ঌ ♡ ໒꒱ ⊹ ࣪ ˖",
                enemy.name,
                "Enemy Health: " + str(enemy.health),
                "⊹ ࣪ ˖ ꒰ঌ ♡ ໒꒱ ⊹ ࣪ ˖",
                "Wow, that went better than expected.",
                Image("battle_won.png", 800),
                "<br>",
                Button("You win!", the_end),
                "<br>",
                "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
                ])

@route
def fighting(state: State) -> Page:
    """ Functions for calculating health and damage during the fight. """
    #Player and monster will do random amount of damage
    enemy.damage = random.randint(1,10)
    state.damage = random.randint(1,10)
    #When attacking damage will be taken from player and monster's health
    enemy.health -= state.damage
    state.health -= enemy.damage
    #Player health cannot go below 0
    if state.health <= 0:
        state.health = 0
    #Enemy health cannot go below 0
    if enemy.health <= 0:
        enemy.health = 0
    return Page(state,[        
        "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
        "<br>",
        "You attack the monster.",
        "It takes " + str(state.damage) + " damage.",
        "The monster strikes back.",
        "You take " + str(enemy.damage) + " damage.",
        Image("punching.gif", 700),
        "<br>",
        Button("Keep fighting", fight),
        "<br>",
        "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
                ])

@route
def take_potion(state: State) -> Page:
    """ Functions for calculating health and damage during the fight. """
    #Player health can't go above 100
    if state.health >= 100:
        state.health = 100
    #Only if potions are available
    if potion_2.quantity > 0:
        #Number of potions can't go below 0
        if potion_2.quantity <= 0:
            potion_2.quantity = 0
        #Every time the player uses a potion, the quantity will decrease by 1
        potion_2.quantity -= 1
        #The potion will replenish a random amount of health
        potion_2.health = random.randint(1,10)
        #Player health will be increased by given amount in potion
        state.health += potion_2.health
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "You drink a Healing Potion.",
            "You recover " + str(potion_2.health) + " health.",
            Image("drink.gif", 500),
            "<br>",
            Button("Keep fighting", fight),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])
    #Only if there are no potions left
    elif potion_2.quantity == 0:
        state.health += 0
        return Page(state,[
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
            "<br>",
            "That was your last healing potion.",
            "You don't have anymore.",
            Image("No_potions.png", 500),
            "<br>",
            Button("Keep fighting", fight),
            "<br>",
            "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
            ])

@route
def updated(state: State) -> Page:
    """ Updates the updates class to indicate that the player has taken an action,
    then redirects back to the living room. """
    #After you move in and hear a noise whilst unpacking
    if state.updates.routes == "move_in":
        state.updates.routes = "living_room"
        return living_room(state)
    #Running away from the monster in the attic
    if state.updates.routes == "living_room" and state.status.is_monsters == True:
        state.updates.routes = "run"        
        return living_room(state)
    #You choose to keep hiding from the monster
    if state.updates.routes == "hiding":
        state.updates.routes = "kept_hiding"        
        return hide(state)
    #Fighting after hiding
    if state.updates.routes == "run" and state.updates.is_hidden == True:
        state.updates.routes = "confrontation"        
        return fight(state)
    #You look around the kitchen
    if state.updates.routes == "in_kitchen":
        potion_2.quantity = random.randint(1,5)
        state.items = [potion_1, potion_2, knife]
        return kitchen(state)
    #Fighting after coming from the kitchen
    if state.updates.routes == "confrontation":
        state.updates.routes = "fighting"
        return fight(state)

#############################################################################    
# Game screens

@route
def win_screen(state: State) -> Page:
    """ The page for when the player wins the game. """
    #Stops current audio and plays new audio
    #pygame.mixer.music.stop()
    #pygame.mixer.music.load("yippie.mp3")
    #pygame.mixer.music.play(1, 0.0)
    return Page(state,[
        "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
        "<br>",
        "You Survived!",
        Image("you_win.jpg", 700),
        "<br>",
        Button("Restart", reset),
        "<br>",
        "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
        ])

@route
def game_over(state: State) -> Page:
    """ The page for the game over screen. """
    #Stops current audio and plays new audio
    #pygame.mixer.music.stop()
    #pygame.mixer.music.load("small_shock.mp3")
    #pygame.mixer.music.play(1, 0.0)
    return Page(state,[
        "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
        "<br>",
        "You've met with a terrible fate, haven't you?",
        Image("game_over.jpg", 800),
        "<br>",
        Button("Try Again", reset),
        "<br>",
        "✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°."
        ])

@route
def reset(state: State) -> Page:
    """ Resets the state class. """
    
    state = State(
    "",
    [],
    100,
    10,
    Status(False, []),
    Updates("", False)
    )
    
    monsters[0].health = 80
    monsters[1].health = 50
    monsters[2].health = 30
    
    #Stops the music
    #pygame.mixer.music.stop()
    
    return index(state)

#############################################################################    
# Start server

start_server(State(
    "",
    [],
    100,
    10,
    Status(False, []),
    Updates("", False)
))

#############################################################################
# Unit tests

assert_equal(
 index(State(name='', items=[], health=100, damage=10, status=Status(is_monsters=False, monsters=[]), updates=Updates(routes='', is_hidden=False))),
 Page(state=State(name='',
                 items=[],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=False, monsters=[]),
                 updates=Updates(routes='', is_hidden=False)),
     content=["<audio><source src='once_upon_a_time.mp3' "
              "type='audio/mpeg'></audio>✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.",
              '<br>',
              '<h1> HOUSEWITCHING </h1>',
              '<br>',
              'Welcome to your newly-bought home, young witch. What is your name?',
              '<br>',
              TextBox(name='name', kind='text', default_value='Young Witch'),
              '<br>',
              Button(text='Move In', url='/move_in'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 move_in(State(name='', items=[], health=100, damage=10, status=Status(is_monsters=False, monsters=[]), updates=Updates(routes='', is_hidden=False)), 'Young Witch'),
 Page(state=State(name='Young Witch',
                 items=[],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=False, monsters=[]),
                 updates=Updates(routes='move_in', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'Your name is Young Witch.',
              'You step into your new home, finding yourself in a hallway past your front door.',
              'Ahead of you seems to be the living room.',
              Image(url='front_door.jpg', width=500, height=None),
              '<br>',
              Button(text='Explore your living room', url='/living_room'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 living_room(State(name='Young Witch', items=[], health=100, damage=10, status=Status(is_monsters=False, monsters=[]), updates=Updates(routes='move_in', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=False, monsters=[]),
                 updates=Updates(routes='move_in', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'You step into the living room, ready to decorate your brand new abode.',
              'You begin unpacking the boxes sitting in the corner.',
              'After a while of setting out books and other knick knacks, you come across a photo.',
              'Looking closer, you see its a bunch of old childhood photos.',
              'Some are cute and nostalgic - making you look back on those old memories with fondness.',
              'Others... well, lets just say anyone could tell you were definitely a troublemaker back then.',
              "You find yourself getting lost in the little scrapbook, just remembering the good 'ol times.",
              'So much so, that you almost miss that faint voice, whispering in the distance.',
              Image(url='living_room.jpeg', width=700, height=None),
              '<br>',
              Button(text='What is that?', url='/updated'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 updated(State(name='Young Witch', items=[], health=100, damage=10, status=Status(is_monsters=False, monsters=[]), updates=Updates(routes='move_in', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=False, monsters=[]),
                 updates=Updates(routes='living_room', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              Text("'Young Witch.'", {'style_font-style': 'italic'}),
              'A voice calls your name from somewhere within the house...',
              "It's coming from the attic.",
              Image(url='living_room.jpeg', width=700, height=None),
              '<br>',
              Button(text='Go to the attic', url='/attic'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 attic(State(name='Young Witch', items=[], health=100, damage=10, status=Status(is_monsters=False, monsters=[]), updates=Updates(routes='living_room', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=False, monsters=[]),
                 updates=Updates(routes='living_room', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'As you open the attic door,',
              "you can't help but cough due to the sheer amount of dust released into the air.",
              'You climb the ladder carefully, peeking your head through the attic entrance and looking around.',
              'The room is empty and dark,',
              'save for for the one patch of floor illuminated by the setting sun outside the singular window.',
              'What?',
              "You look closer... there's something on the ground.",
              'You walk into the strip of light, eyeing the object on the floor.',
              'It looks like a little statue of a woman, holding a glowing orb in its hands.',
              'The orb is swirling with a shining rainbow of colors, leaving you enamored and drawing you in.',
              'Wanting to inspect the artifact further, you pick it up - ',
              'Only for it to crumble in your hands almost immediately.',
              'You sit in dumfounded silence as you watch the bits of statue tumble onto the floor,',
              'and that little orb roll away from you and extinguish in the darkness.',
              "You're about to retrieve it when suddenly, it feels as if the entire house is being shaken.",
              'You fall to the ground, looking up to window, just to find a pitch black void beyond the glass.',
              "'Welp.', you think, 'That can't be good.'",
              Image(url='attic.jpg', width=700, height=None),
              '<br>',
              Button(text='Try to look out the window anyway', url='/attic_window'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 attic_window(State(name='Young Witch', items=[], health=100, damage=10, status=Status(is_monsters=False, monsters=[]), updates=Updates(routes='living_room', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=False, monsters=[]),
                 updates=Updates(routes='living_room', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'As you stare outside your attic window,',
              'you can no longer see the forest trees that surrounded your property.',
              "The void stretches on, making you think there's nothing there at all.",
              "That's when something smacks against the window pane, hard.",
              'You fall back onto the ground, startled, eyes wide.',
              "There's a face in the window.",
              Image(url='attic_window.jpg', width=500, height=None),
              '<br>',
              Button(text='What is that', url='/status'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 status(State(name='Young Witch', items=[], health=100, damage=10, status=Status(is_monsters=False, monsters=[]), updates=Updates(routes='living_room', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='living_room', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'A grotesque figure looks back at you from the window,',
              "it's face a distorted white mask surrounded by matted black hair.",
              'It hold eye contact with you for a moment -',
              "even with it's lack of eyes, you know its staring at you.",
              'Then a large palm rises from below the window - and begins pounding on the glass.',
              'Immediately, you head for the attic door, scrambling to grasp the handle.',
              'Just as you begin to descend, you hear a crack, followed by a loud shatter.',
              'It got inside.',
              Image(url='monster_1.gif', width=700, height=None),
              '<br>',
              Button(text='Run.', url='/updated'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 updated(State(name='Young Witch', items=[], health=100, damage=10, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='living_room', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='run', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'Loud cracks and bangs echo from beyond the attic door.',
              "It'll only hold that monster off for so long.",
              'What will you do?',
              Image(url='living_room.jpeg', width=700, height=None),
              '<br>',
              Button(text='Hide', url='/hide'),
              Button(text='Run to kitchen', url='/kitchen'),
              Button(text='Leave', url='/front_door'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 hide(State(name='Young Witch', items=[], health=100, damage=10, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='run', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='hiding', is_hidden=True)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'You hide behind a couch in the corner of your living room, trying to still your rapid breathing.',
              'You can still hear the rhythmic thumping from the attic.',
              "The monster hasn't gotten in yet.",
              "Maybe there's something else you can do?",
              Image(url='hiding.png', width=700, height=None),
              '<br>',
              Button(text='Try something else', url='/living_room'),
              Button(text='Keep hiding', url='/updated'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 updated(State(name='Young Witch', items=[], health=100, damage=10, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='hiding', is_hidden=True))),
 Page(state=State(name='Young Witch',
                 items=[],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='kept_hiding', is_hidden=True)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'You keep hiding.',
              "With a deafening crash, the monster makes it's way into your home.",
              'You shrink back into the closet at the beast stalks around the living room.',
              'Through the slats on the closet door, you can see the light slowly dimming,',
              'leaving your living room pitch black.',
              "You don't know how much time passed while you sat in that closet.",
              'The darkness felt almost heavy around you - and soon, you find yourself drifting into sleep.',
              'When the darkness finally lifts from your home, the monsters are gone - and so are you.',
              'Your house goes up for sale again and everyone wonders where you could have possibly gone.',
              'At the very least, your demise was peaceful.',
              Image(url='sleep_forever.jpg', width=700, height=None),
              '<br>',
              Button(text="You'll sleep forever", url='/game_over'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 updated(State(name='Young Witch', items=[], health=100, damage=10, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='kept_hiding', is_hidden=True))),
 None)

assert_equal(
 game_over(State(name='Young Witch', items=[], health=100, damage=10, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='kept_hiding', is_hidden=True))),
 Page(state=State(name='Young Witch',
                 items=[],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='kept_hiding', is_hidden=True)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              "You've met with a terrible fate, haven't you?",
              Image(url='game_over.jpg', width=800, height=None),
              '<br>',
              Button(text='Try Again', url='/reset'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 front_door(State(name='Young Witch', items=[], health=100, damage=10, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='run', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='run', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'You rush for the front door,',
              "hearing the crash of the attic door being broken off it's hinges behind you.",
              'You sprint faster towards the front door,',
              'loud thumping and scraping rapidly growing closer behind you.',
              'You narrowly avoid a giant hand grasping at your back,',
              'just as you throw open the door and cross the threshold onto the front lawn.',
              'You stop running, turning to see the crude monster slink back into the shadows of your home.',
              'For a moment, you breathe a sigh of relief, just happy to have escaped.',
              'Honestly, no one can blame you for forgetting all the other monsters outside your house.',
              "At the very least, they're quick to rip you apart - you don't feel a thing.",
              '...Almost.',
              Image(url='monsters_woods.jpg', width=800, height=None),
              '<br>',
              Button(text='You Died', url='/game_over'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 kitchen(State(name='Young Witch', items=[], health=100, damage=10, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='run', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='in_kitchen', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'The kitchen is silent, though faintly,',
              "you can still hear the creature trying to break it's way through the attic door.",
              'Maybe something in here can be of use to you.',
              Image(url='kitchen.jpeg', width=700, height=None),
              '<br>',
              Button(text='Look around.', url='/updated'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 front_door(State(name='Young Witch', items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0), Item(name='Health Potion', quantity=5, health=0, damage=0), Item(name='Knife', quantity=1, health=0, damage=0)], health=100, damage=10, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='confrontation', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0),
                        Item(name='Health Potion', quantity=5, health=0, damage=0),
                        Item(name='Knife', quantity=1, health=0, damage=0)],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='confrontation', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'As you move to run, you hear something drop and roll across the floor.',
              "It's an Invisibility Potion!",
              "It must've been with the items you found.",
              'You grab the potion and take off towards the front door.',
              "As you run, you hear the crash of the attic door being broken off it's hinges behind you.",
              'You sprint faster towards the front door,',
              'hearing loud thumping and scraping come to a halt behind you.',
              "It looks like the monster can't see you!",
              'You close in on the door, throwing it open and crossing the threshold onto the front lawn.',
              'You stop running and turn to look through the front door,',
              'seeing the crude monster still stalking around your living room.',
              'You breathe a sigh of relief, just happy to have escaped.',
              'As you turn to leave, you almost bump into another sizeable and horrifying creature.',
              "It's a good thing you took that invisibility potion -",
              'you entirely forgot about the monsters outside!',
              'You head off into the forest, further and further away from your new home.',
              "Hopefully, the monsters don't mess the place up too bad - you would like your deposit back.",
              Image(url='got_away.jpg', width=700, height=None),
              '<br>',
              Button(text='Escape', url='/win_screen'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 win_screen(State(name='Young Witch', items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0), Item(name='Health Potion', quantity=5, health=0, damage=0), Item(name='Knife', quantity=1, health=0, damage=0)], health=100, damage=10, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='confrontation', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0),
                        Item(name='Health Potion', quantity=5, health=0, damage=0),
                        Item(name='Knife', quantity=1, health=0, damage=0)],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='confrontation', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'You Survived!',
              Image(url='you_win.jpg', width=700, height=None),
              '<br>',
              Button(text='Restart', url='/reset'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 living_room(State(name='Young Witch', items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0), Item(name='Health Potion', quantity=4, health=0, damage=0), Item(name='Knife', quantity=1, health=0, damage=0)], health=100, damage=10, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='confrontation', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0),
                        Item(name='Health Potion', quantity=4, health=0, damage=0),
                        Item(name='Knife', quantity=1, health=0, damage=0)],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='confrontation', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'A deafening crash rings out from the living room.',
              'As you leave the kitchen, you come face to face with the monstrous creature.',
              "You've been spotted.",
              "Looks like there's no turning back now.",
              Image(url='monster_2.jpg', width=700, height=None),
              '<br>',
              Button(text='Fight', url='/fight'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 fight(State(name='Young Witch', items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0), Item(name='Health Potion', quantity=4, health=0, damage=0), Item(name='Knife', quantity=1, health=0, damage=0)], health=100, damage=10, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='confrontation', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0),
                        Item(name='Health Potion', quantity=4, health=0, damage=0),
                        Item(name='Knife', quantity=1, health=0, damage=0)],
                 health=100,
                 damage=10,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='confrontation', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'Looks like you decided to fight.',
              'Hopefully, luck is on your side.',
              Image(url='fight_stance.jpg', width=600, height=None),
              '<br>',
              Button(text='Make a move', url='/updated'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 fighting(State(name='Young Witch', items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0), Item(name='Health Potion', quantity=4, health=0, damage=0), Item(name='Knife', quantity=1, health=0, damage=0)], health=100, damage=10, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='fighting', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0),
                        Item(name='Health Potion', quantity=4, health=0, damage=0),
                        Item(name='Knife', quantity=1, health=0, damage=0)],
                 health=92,
                 damage=9,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='fighting', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'You attack the monster.',
              'It takes 9 damage.',
              'The monster strikes back.',
              'You take 8 damage.',
              Image(url='punching.gif', width=700, height=None),
              '<br>',
              Button(text='Keep fighting', url='/fight'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 take_potion(State(name='Young Witch', items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0), Item(name='Health Potion', quantity=4, health=0, damage=0), Item(name='Knife', quantity=1, health=0, damage=0)], health=73, damage=2, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='fighting', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0),
                        Item(name='Health Potion', quantity=3, health=10, damage=0),
                        Item(name='Knife', quantity=1, health=0, damage=0)],
                 health=83,
                 damage=2,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='fighting', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'You drink a Healing Potion.',
              'You recover 10 health.',
              Image(url='drink.gif', width=500, height=None),
              '<br>',
              Button(text='Keep fighting', url='/fight'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 take_potion(State(name='Young Witch', items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0), Item(name='Health Potion', quantity=0, health=5, damage=0), Item(name='Knife', quantity=1, health=0, damage=0)], health=99, damage=2, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='fighting', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0),
                        Item(name='Health Potion', quantity=0, health=5, damage=0),
                        Item(name='Knife', quantity=1, health=0, damage=0)],
                 health=99,
                 damage=2,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='fighting', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'That was your last healing potion.',
              "You don't have anymore.",
              Image(url='No_potions.png', width=500, height=None),
              '<br>',
              Button(text='Keep fighting', url='/fight'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 fight(State(name='Young Witch', items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0), Item(name='Health Potion', quantity=0, health=5, damage=0), Item(name='Knife', quantity=1, health=0, damage=0)], health=34, damage=9, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='fighting', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0),
                        Item(name='Health Potion', quantity=0, health=5, damage=0),
                        Item(name='Knife', quantity=1, health=0, damage=0)],
                 health=34,
                 damage=9,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='fighting', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'Young Witch',
              'Your Health: 34',
              'Your Items:',
              'Health Potion: 0',
              '⊹ ࣪ ˖ ꒰ঌ ♡ ໒꒱ ⊹ ࣪ ˖',
              '???',
              'Enemy Health: 0',
              '⊹ ࣪ ˖ ꒰ঌ ♡ ໒꒱ ⊹ ࣪ ˖',
              'Wow, that went better than expected.',
              Image(url='battle_won.png', width=800, height=None),
              '<br>',
              Button(text='You win!', url='/the_end'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 the_end(State(name='Young Witch', items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0), Item(name='Health Potion', quantity=0, health=5, damage=0), Item(name='Knife', quantity=1, health=0, damage=0)], health=34, damage=9, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='fighting', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0),
                        Item(name='Health Potion', quantity=0, health=5, damage=0),
                        Item(name='Knife', quantity=1, health=0, damage=0)],
                 health=34,
                 damage=9,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='ending', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'You stand there for a moment - breathing heavy as you try to steady yourself.',
              'After a few seconds you sink to the floor,',
              'sighing in relief as the last of your adrenaline wears off.',
              'You look down at the knife in your hand, covered in the blood of that wretched creature.',
              'It glints in the sunlight, as pristine as when you bought it.',
              'Wait?',
              'Sunlight?',
              'Its then that you notice the thick fog of darkness that once enveloped your home is no more.',
              'Rays of sunlight are cast from your living room window,',
              'shining upon the disintegrating body of the slain monster.',
              '?',
              'Whats that on the floor?',
              Image(url='the_orb.jpg', width=700, height=None),
              '<br>',
              Button(text='Pick it up', url='/the_end'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))

assert_equal(
 the_end(State(name='Young Witch', items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0), Item(name='Health Potion', quantity=0, health=5, damage=0), Item(name='Knife', quantity=1, health=0, damage=0)], health=34, damage=9, status=Status(is_monsters=True, monsters=[]), updates=Updates(routes='ending', is_hidden=False))),
 Page(state=State(name='Young Witch',
                 items=[Item(name='Invisibility Potion', quantity=1, health=0, damage=0),
                        Item(name='Health Potion', quantity=0, health=5, damage=0),
                        Item(name='Knife', quantity=1, health=0, damage=0)],
                 health=34,
                 damage=9,
                 status=Status(is_monsters=True, monsters=[]),
                 updates=Updates(routes='ending', is_hidden=False)),
     content=['✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.',
              '<br>',
              'You reach for the item on the ground, holding it up in the sunlight for a better look.',
              'The small sphere is only slightly bigger than a marble and feels smooth to the touch.',
              'However, it glows a brilliant variety of colors,',
              'swirling together, reminiscent of the cosmos in the starry night sky.',
              'It kinda looks like that orb you broke earlier.',
              'The orb glows brighter for a moment,',
              'and outside your window, you see the last of the monsters slip away into the treeline.',
              "You don't know why the monster had this, but you definitely feel like you should keep it.",
              'If nothing else, it at least seems to keep other creatures off your property.',
              'You place the orb in a little jewlery box and place it on the mantle above your fireplace.',
              'For your own sanity (and physical well-being),',
              "you'll be careful not to break this one.",
              Image(url='the_end.png', width=800, height=None),
              '<br>',
              Button(text="Guess we'll have to see about that", url='/win_screen'),
              '<br>',
              '✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.✧˖°.']))
