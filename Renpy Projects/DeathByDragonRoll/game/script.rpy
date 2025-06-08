# The script of the game goes in this file.

init python:
    from renpy.display import im

# Define scaled images to fit the window
init:
    # Scale all images to fill the screen
    image bg restaurant_front = im.Scale("images/backgrounds/restaurant-outside-front.jpg", config.screen_width, config.screen_height)
    image bg sushi_bar = im.Scale("images/backgrounds/sushi-bar.webp", config.screen_width, config.screen_height)
    image bg kitchen_angle = im.Scale("images/backgrounds/kitchen-angle.jpg", config.screen_width, config.screen_height)
    
    # Evidence images - normal versions (scaled to 1/3 size)
    # Restaurant evidence
    image evidence chopsticks idle = im.FactorScale("images/evidence/chopsticks.png", 0.33)
    image evidence soySauce idle = im.FactorScale("images/evidence/soySauce.png", 0.33)
    image evidence menuTilt idle = im.FactorScale("images/evidence/menuTilt.png", 0.33)
    image evidence sushi idle = im.FactorScale("images/evidence/sushi.png", 0.33)
    
    # Kitchen evidence
    image evidence knife idle = im.FactorScale("images/evidence/knife.png", 0.33)
    image evidence fishFilet idle = im.FactorScale("images/evidence/fishFilet.png", 0.33)
    image evidence notebook idle = im.FactorScale("images/evidence/notebook.png", 0.33)
    
    # Evidence images - hover versions with yellow highlight (scaled to 1/3 size)
    # Restaurant evidence
    image evidence chopsticks hover = im.FactorScale(im.MatrixColor("images/evidence/chopsticks.png", im.matrix.colorize("#FFFF00", "#FFFFFF")), 0.33)
    image evidence soySauce hover = im.FactorScale(im.MatrixColor("images/evidence/soySauce.png", im.matrix.colorize("#FFFF00", "#FFFFFF")), 0.33)
    image evidence menuTilt hover = im.FactorScale(im.MatrixColor("images/evidence/menuTilt.png", im.matrix.colorize("#FFFF00", "#FFFFFF")), 0.33)
    image evidence sushi hover = im.FactorScale(im.MatrixColor("images/evidence/sushi.png", im.matrix.colorize("#FFFF00", "#FFFFFF")), 0.33)
    
    # Kitchen evidence
    image evidence knife hover = im.FactorScale(im.MatrixColor("images/evidence/knife.png", im.matrix.colorize("#FFFF00", "#FFFFFF")), 0.33)
    image evidence fishFilet hover = im.FactorScale(im.MatrixColor("images/evidence/fishFilet.png", im.matrix.colorize("#FFFF00", "#FFFFFF")), 0.33)
    image evidence notebook hover = im.FactorScale(im.MatrixColor("images/evidence/notebook.png", im.matrix.colorize("#FFFF00", "#FFFFFF")), 0.33)

    # Define character images (you'll need to add these files later)
    image kenji normal = "images/characters/kenji_normal.png" 
    image aiko normal = "images/characters/aiko_normal.png"

# Define styles for Nina's dialogue
# this is the bubble itself
style nina_say_window:
    background "images/interface/nina_dialogue.png"
    xalign 0.5
    yalign 0.8

    # carve out exactly the region you want text to appear in.
    # adjust these until the "hole" in your speech‐bubble matches your image.
    left_padding  385   # push text in from the left edge of the bubble
    right_padding 200   # push text in from the right edge
    top_padding   230   # push text down from the top
    bottom_padding 120  # push text up from the bottom

# this is the text inside that carved‐out region
style nina_say_what:
    color       "#FFFFFF"
    size        28
    text_align  0.5    # center each line
    xsize       900 

# Define our characters
define nina = Character(
    None,
    window_style="nina_say_window",
    what_style="nina_say_what",
    window_xalign=0.5,
    window_yalign=0.8,
)

define kenji = Character("Chef Kenji", color="#e74c3c")
define aiko = Character("Sous-Chef Aiko", color="#9b59b6")
define detective = Character("You (Detective)", color="#2980b9")

# Define inventory and evidence variables
default inventory = []
default clues_found = 0
default questioned_kenji = False
default questioned_aiko = False

# Evidence collection tracking
default evidence_collected = {
    "chopsticks": False,
    "soySauce": False,
    "menuTilt": False,
    "sushi": False,
    "knife": False,
    "fishFilet": False,
    "notebook": False,
}

# Screen for displaying "Press space to continue" prompt
screen continue_prompt():
    frame:
        xalign 0.98
        yalign 0.98
        padding (10, 5)
        background "#00000080"
        
        text "Press SPACE to continue" style "continue_text"
    
    # Add key event to detect space bar
    key "K_SPACE" action Return(True)

# Style for continue prompt text
style continue_text:
    color "#FFFFFF"
    size 22
    outlines [(1, "#000000", 0, 0)]
    text_align 0.5

# Screen for displaying clickable evidence items
screen evidence_items(items):
    for item_name, pos in items:
        if not evidence_collected[item_name]:
            imagebutton:
                auto "evidence " + item_name + " %s"
                xpos pos[0]
                ypos pos[1]
                focus_mask True
                action [SetDict(evidence_collected, item_name, True), 
                        Function(add_to_inventory, item_name), 
                        Show("evidence_collected", item=item_name),
                        Return(None)]

# Screen for displaying evidence collection message
screen evidence_collected(item):
    modal True
    frame:
        xalign 0.5
        yalign 0.3
        padding (20, 20)
        background "#00000080"
        vbox:
            text "Evidence Collected: " + item style "evidence_text"
            text "Added to your inventory." style "evidence_text"
    timer 2.0 action Hide("evidence_collected")

init python:
    def add_to_inventory(item):
        if item not in inventory:
            inventory.append(item)
            global clues_found
            clues_found += 1

# Styles for evidence text
style evidence_text:
    color "#FFFFFF"
    size 30
    outlines [(2, "#000000", 0, 0)]
    text_align 0.5
    xalign 0.5

# New evidence collection label to handle investigation scenes properly
label evidence_collection_scene(evidence_items):
    # Show both evidence items and continue prompt
    show screen evidence_items(evidence_items)
    show screen continue_prompt
    
    # Use Ren'Py's built-in pause to wait for player interaction
    $ renpy.pause(hard=True)
    
    # Hide screens before returning
    hide screen evidence_items
    hide screen continue_prompt
    return

# The game starts here.
label start:
    
    # Introduction
    scene bg restaurant_front with fade
    
    nina "You're here! Thanks so for responding so quickly, let's get started!"
    nina "This is Sushi Asashi - one of the most celebrated sushi restaurant in the city."
    nina "A famous food critic has collapsed and passed halfway through his meal."
    nina "The restaurant has been evacuated, and emergency services have confirmed the death."
    nina "Come, let's head inside."
    
    scene bg restaurant_front with dissolve
      # Enter the restaurant - sushi bar area where victim was seated
    scene bg sushi_bar with dissolve
    
    nina "This is the main dining area where he collapsed."
    nina "His partially eaten Dragon Roll special is still on the plate."
    nina "Medical examiner's preliminary report suggests symptoms consistent with poisoning, but they need your forensic work to confirm."
    nina "Your forensic toolkit is ready, start your investigation here!"

    # Define positions for evidence items in the restaurant scene
    # Format: (evidence_name, (x_position, y_position))
    $ restaurant_evidence = [
        ("chopsticks", (620, 700)),   # Left side
        ("soySauce", (800, 600)),     # Center-left
        ("menuTilt", (220, 740)),     # Center-right
        ("sushi", (630, 590))         # Right side
    ]    # Evidence collection phase - Show evidence and prompt
    window hide
    
    # Call a custom label for handling restaurant evidence collection
    call evidence_collection_scene(restaurant_evidence)
    
    # Show Nina's dialogue again
    window show
    
    nina "Great work so far! Now let's head to the kitchen."
    
    # Hide restaurant evidence screen before changing scene
    hide screen evidence_items
      # Kitchen investigation
    scene bg kitchen_angle with dissolve
    
    nina "All food preparation is done here, be sure to look through all their equipment and ingredients."
    
    # Define positions for evidence items in the kitchen scene
    # Format: (evidence_name, (x_position, y_position))
    $ kitchen_evidence = [
        ("knife", (700, 600)),       # Left side
        ("fishFilet", (600, 450)),   # Center
        ("notebook", (800, 970))     # Right side
    ]    # Evidence collection phase - Show evidence and prompt
    window hide
    
    # Call a custom label for handling kitchen evidence collection
    call evidence_collection_scene(kitchen_evidence)
    
    # Show Nina's dialogue again
    window show
    
    nina "Good job! You're good to proceed!"

    # Hide kitchen evidence screen before ending scene
    hide screen evidence_items

    # Display collected evidence summary
    nina "Let's look at what you've collected so far."
    
    python:
        evidence_list = ", ".join(inventory)
    
    nina "You've found [clues_found] pieces of evidence: [evidence_list]."
    nina "This case will still require careful laboratory work to determine exactly what caused the victim's death."
    nina "This concludes the initial crime scene assessment. The evidence has been documented and collected for laboratory analysis."
    nina "Feel free to return to the lab to continue your investigation."


    # This ends the game.
    return
