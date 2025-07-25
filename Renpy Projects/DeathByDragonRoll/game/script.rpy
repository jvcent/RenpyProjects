﻿# The script of the game goes in this file.

init python:
    from renpy.display import im

# Define scaled images to fit the window
init:
    # Scale all images to fill the screen
    image bg restaurant_front = im.Scale("images/backgrounds/restaurant-outside-front.jpg", config.screen_width, config.screen_height)
    image bg sushi_bar = im.Scale("images/backgrounds/sushi-bar.webp", config.screen_width, config.screen_height)
    image bg kitchen_angle = im.Scale("images/backgrounds/kitchen-angle.jpg", config.screen_width, config.screen_height)
    
    # Equipment images - scaled to appropriate size
    image equipment evidence_swab idle = im.Scale("images/equipment/evidence_swab.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment evidence_swab hover = im.Scale("images/equipment/evidence_swab.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment evidence_swab selected = im.Scale("images/equipment/evidence_swab-kit.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    
    image equipment fingerprint_kit idle = im.Scale("images/equipment/fingerprint-kit.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment fingerprint_kit hover = im.Scale("images/equipment/fingerprint-kit.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment fingerprint_kit selected = im.Scale("images/equipment/fingerprint-kit.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    
    image equipment gauze idle = im.Scale("images/equipment/gauze.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment gauze hover = im.Scale("images/equipment/gauze.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment gauze selected = im.Scale("images/equipment/gauze.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    
    image equipment phadebas idle = im.Scale("images/equipment/phadebas.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment phadebas hover = im.Scale("images/equipment/phadebas.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment phadebas selected = im.Scale("images/equipment/phadebas.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    
    image equipment pippette idle = im.Scale("images/equipment/pippette.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment pippette hover = im.Scale("images/equipment/pippette.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment pippette selected = im.Scale("images/equipment/pippette.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    
    image equipment evidence_folder idle = im.Scale("images/equipment/evidence_folder.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment evidence_folder hover = im.Scale("images/equipment/evidence_folder.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment evidence_folder selected = im.Scale("images/equipment/evidence_folder.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    
    image equipment scissors idle = im.Scale("images/equipment/scissors.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment scissors hover = im.Scale("images/equipment/scissors.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment scissors selected = im.Scale("images/equipment/scissors.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    
    image equipment specimen_collection idle = im.Scale("images/equipment/specimen_collection.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment specimen_collection hover = im.Scale("images/equipment/specimen_collection.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment specimen_collection selected = im.Scale("images/equipment/specimen_collection.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    
    # Evidence images - normal versions (scaled to 1/3 size)
    # Restaurant evidence
    image evidence chopsticks idle = im.FactorScale("images/evidence/chopsticks.png", 0.33)
    image evidence soySauce idle = im.FactorScale("images/evidence/soySauce.png", 0.33)
    image evidence courseMenu idle = im.FactorScale("images/evidence/courseMenu.png", 0.33)
    image evidence sushi idle = im.FactorScale("images/evidence/sushi.png", 0.33)
    
    # Kitchen evidence
    image evidence knife idle = im.FactorScale("images/evidence/knife.png", 0.33)
    image evidence fishFilet idle = im.FactorScale("images/evidence/fishFilet.png", 0.33)
    image evidence notebook idle = im.FactorScale("images/evidence/notebook.png", 0.33)
    
    # Evidence images - hover versions with yellow highlight (scaled to 1/3 size)
    # Restaurant evidence
    image evidence chopsticks hover = im.FactorScale(im.MatrixColor("images/evidence/chopsticks.png", im.matrix.colorize("#FFFF00", "#FFFFFF")), 0.33)
    image evidence soySauce hover = im.FactorScale(im.MatrixColor("images/evidence/soySauce.png", im.matrix.colorize("#FFFF00", "#FFFFFF")), 0.33)
    image evidence courseMenu hover = im.FactorScale(im.MatrixColor("images/evidence/courseMenu.png", im.matrix.colorize("#FFFF00", "#FFFFFF")), 0.33)
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
    
# Now scales to 80% of screen width and 25% of screen height
    xsize int(config.screen_width * 0.8)
    ysize int(config.screen_height * 0.25)

    # Paddings tuned for the new size - adjusted to move text lower
    left_padding   400
    right_padding  120
    top_padding    250   # Increased to push text down
    bottom_padding  30   # Decreased to keep overall space balanced

style nina_say_what:
    color       "#FFFFFF"
    size        22         # slightly smaller for better fit
    text_align  0.5
    xsize       int(config.screen_width * 0.4)  # Further reduced from 0.5 to 0.4 for even narrower text
    yalign      0.6        # Position text slightly lower in the textbox

# Define our characters
define nina = Character(
    None,
    window_style="nina_say_window",
    what_style="nina_say_what",
    window_xalign=0.5,
    window_yalign=0.75,  # Moved slightly higher on screen
)

define kenji = Character("Chef Kenji", color="#e74c3c")
define aiko = Character("Sous-Chef Aiko", color="#9b59b6")
define detective = Character("You (Detective)", color="#2980b9")

# Define inventory and evidence variables
default inventory = []
default clues_found = 0
default questioned_kenji = False
default questioned_aiko = False

# Equipment variables
default selected_equipment = None
default examining_evidence = None  # Tracks which evidence item is being examined
default equipment_list = ["evidence_swab", "fingerprint_kit", "gauze", "phadebas", "scissors", "specimen_collection", "pippette", "evidence_folder"]

# Evidence collection tracking
default evidence_collected = {
    "chopsticks": False,
    "soySauce": False,
    "courseMenu": False,
    "sushi": False,
    "knife": False,
    "fishFilet": False,
    "notebook": False,
}

# Evidence-equipment requirements mapping
default evidence_requirements = {
    "chopsticks": "evidence_folder",
    "soySauce": "pippette",
    "courseMenu": "evidence_folder",
    "sushi": "specimen_collection",
    "knife": "evidence_folder",
    "fishFilet": "specimen_collection",
    "notebook": "evidence_folder"
}

# Screen for displaying "Press space to continue" prompt
screen continue_prompt():
    frame:
        xalign 0.5
        yalign 0.98
        padding (15, 8)
        background "#00000080"
        
        text "Press SPACE to continue to next scene" style "continue_text"
    
    # Add key event to detect space bar
    key "K_SPACE" action Return(True)

# Style for continue prompt text
style continue_text:
    color "#FFFFFF"
    size 22
    outlines [(1, "#000000", 0, 0)]
    text_align 0.5
    
# Style for equipment headers
style equipment_header:
    color "#FFCC00"
    size 18
    bold True
    text_align 0.5
    outlines [(1, "#000000", 0, 0)]
    xalign 0.5

# Styles for evidence text
style evidence_text:
    color "#FFFFFF"
    size 30
    outlines [(2, "#000000", 0, 0)]
    text_align 0.5
    xalign 0.5

# Style for evidence headers
style evidence_header:
    color "#FFCC00"
    size 36
    bold True
    outlines [(2, "#000000", 0, 0)]
    text_align 0.5
    xalign 0.5

# Transforms for equipment panel animations
transform slide_in_left:
    xpos -300
    easein 0.5 xpos 0

transform slide_in_right:
    xpos config.screen_width + 300  # Start outside of the screen
    easein 0.5 xpos 1.0  # Slide to the right edge of the screen (using relative positioning)

transform pulse:
    alpha 1.0
    linear 0.5 alpha 0.7
    linear 0.5 alpha 1.0
    repeat

# Equipment selection screen - displays equipment on both sides of the screen (4 on each side)
screen equipment_selection():
    # Only show when an evidence item is being examined
    if examining_evidence:
        # Split equipment list into two groups (4 items each)
        python:
            left_equipment = equipment_list[:4]  # First four items
            right_equipment = equipment_list[4:] # Last four items
            required_equipment = evidence_requirements.get(examining_evidence, "")
            
        # Left side equipment toolbar - appears with a slide animation
        frame:
            xalign 0.0
            yalign 0.5
            xsize int(config.screen_width * 0.15)
            ysize config.screen_height
            background "#00000080"
            at slide_in_left
                
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                
                for item in left_equipment:
                    # Only highlight selected equipment, no hint for required equipment
                    $ frame_bg = "#00FF0080" if selected_equipment == item else None
                    
                    frame:
                        # Use green background for selected equipment
                        background frame_bg
                        padding (10, 10)
                        margin (5, 5)
                        xalign 0.5
                        
                        vbox:
                            spacing 5
                            xalign 0.5
                            
                            imagebutton:
                                idle "equipment " + item + " idle"
                                hover "equipment " + item + " idle"
                                action SetVariable("selected_equipment", item)
                                xalign 0.5
                                at transform:
                                    on idle:
                                        linear 0.2 alpha 1.0
                                    on hover:
                                        linear 0.2 alpha 0.8
        
        # Right side equipment toolbar - appears with a slide animation
        frame:
            xanchor 1.0  # Right edge of the frame
            xpos 1.0  # Position at the right edge of the screen
            yalign 0.5
            xsize int(config.screen_width * 0.15)
            ysize config.screen_height
            background "#00000080"
            at slide_in_right
                
            vbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                
                for item in right_equipment:
                    # Only highlight selected equipment, no hint for required equipment
                    $ frame_bg = "#00FF0080" if selected_equipment == item else None
                    
                    frame:
                        # Use green background only for selected equipment
                        background frame_bg
                        padding (10, 10)
                        margin (5, 5)
                        xalign 0.5
                        
                        vbox:
                            spacing 5
                            xalign 0.5
                            
                            imagebutton:
                                idle "equipment " + item + " idle"
                                hover "equipment " + item + " idle"
                                action SetVariable("selected_equipment", item)
                                xalign 0.5
                                at transform:
                                    on idle:
                                        linear 0.2 alpha 1.0
                                    on hover:
                                        linear 0.2 alpha 0.8

# Screen for displaying clickable evidence items
screen evidence_items(items):
    # Ensure evidence items are positioned within the visible center area
    for item_name, pos in items:
        if not evidence_collected[item_name]:
            # Use a different action based on whether this item is being examined
            if examining_evidence == item_name:
                # Check if the correct equipment is selected
                $ can_collect = selected_equipment == evidence_requirements[item_name]
                
                imagebutton:
                    auto "evidence " + item_name + " %s"
                    xalign pos[0]  # Use xalign instead of absolute position
                    yalign pos[1]  # Use yalign instead of absolute position
                    focus_mask True
                    
                    # When examined and equipment selected, handle collection
                    if can_collect:
                        action [SetDict(evidence_collected, item_name, True), 
                                Function(add_to_inventory, item_name), 
                                Show("evidence_collected", item=item_name),
                                SetVariable("examining_evidence", None),
                                SetVariable("selected_equipment", None)]
                    else:
                        # If equipment is wrong, show feedback
                        action Show("wrong_equipment", item=item_name, required_equipment=evidence_requirements[item_name])
            else:
                # Initial click to start examining this evidence
                imagebutton:
                    auto "evidence " + item_name + " %s"
                    xalign pos[0]
                    yalign pos[1]
                    focus_mask True
                    action [SetVariable("examining_evidence", item_name),
                            Show("examination_message", item=item_name)]

# Screen for displaying evidence collection message
screen evidence_collected(item):
    modal False  # Changed to not block other interactions
    frame:
        xalign 0.5
        yalign 0.3
        padding (25, 25)
        margin (50, 50)
        background "#00000080"
        vbox:
            spacing 15
            xalign 0.5
            
            text "Evidence Collected!" style "evidence_header"
            null height 10
            text item.replace("_", " ").title() style "evidence_text"
            text "Added to your inventory." style "evidence_text"
            null height 5
            if selected_equipment:
                text "Used equipment: " + selected_equipment.replace("_", " ").title() style "evidence_text"
    timer 1.5 action Hide("evidence_collected")  # Shorter timer so it doesn't block for too long

# Screen for displaying wrong equipment message
screen wrong_equipment(item, required_equipment):
    modal False  # Changed to not block other interactions
    frame:
        xalign 0.5
        yalign 0.3
        padding (25, 25)
        margin (50, 50)
        background "#AA0000AA"
        vbox:
            spacing 15
            xalign 0.5
            
            text "Wrong Equipment!" style "evidence_header"
            null height 10
            text "Cannot collect " + item.replace("_", " ").title() + "!" style "evidence_text"
            null height 5
            if selected_equipment:
                text "Current tool: " + selected_equipment.replace("_", " ").title() style "evidence_text"
                # Removed the hint about which equipment to use
            else:
                text "You need to select the appropriate equipment first." style "evidence_text"
    timer 2.0 action Hide("wrong_equipment")  # Shorter timer

init python:
    def add_to_inventory(item):
        if item not in inventory:
            inventory.append(item)
            global clues_found
            clues_found += 1

# New evidence collection label to handle investigation scenes properly
label evidence_collection_scene(evidence_items):
    # Reset variables at the beginning of each scene
    $ selected_equipment = None
    $ examining_evidence = None
    
    # Show evidence items, hint and continue prompt
    show screen evidence_items(evidence_items)
    show screen equipment_selection()  # This will only display when examining_evidence is set
    show screen investigation_hint()
    show screen cancel_examination()  # Cancel button only appears when examining_evidence is set
    show screen continue_prompt
    
    # Wait for space bar to be pressed
    $ proceed = False
    while not proceed:
        $ proceed = renpy.call_screen("continue_prompt")
        $ renpy.pause(0.1)  # Short pause to prevent CPU usage spike
    
    # Hide screens before returning
    hide screen equipment_selection
    hide screen evidence_items
    hide screen investigation_hint
    hide screen cancel_examination
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
    nina "Remember to select the appropriate forensic equipment from the sides of the screen when examining any evidence."
    nina "Your forensic toolkit is ready, start your investigation here!"

    # Define positions for evidence items in the restaurant scene
    # Format: (evidence_name, (xalign, yalign)) using values 0.0-1.0
    $ restaurant_evidence = [
        ("chopsticks", (0.40, 0.63)),   # Left side - moved down
        ("soySauce", (0.52, 0.54)),     # Center-left - moved to the left
        ("courseMenu", (0.15, 0.83)),   # Center-right - moved down and right
        ("sushi", (0.44, 0.55))         # Right side - moved down and to the right
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
    nina "Remember to select the right forensic tools for each piece of evidence. The wrong tool won't work!"
    
    # Define positions for evidence items in the kitchen scene
    # Format: (evidence_name, (xalign, yalign)) using values 0.0-1.0
    $ kitchen_evidence = [
        ("knife", (0.6, 0.6)),        # Right side - unchanged
        ("fishFilet", (0.45, 0.58)),  # Center - moved down a little
        ("notebook", (0.5, 0.85))     # Bottom center - moved further down
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
        
        # Create a dictionary mapping evidence to equipment used
        evidence_equipment_used = {}
        for item in inventory:
            evidence_equipment_used[item] = evidence_requirements[item]
    
    nina "You've found [clues_found] pieces of evidence: [evidence_list]."
    
    # Show what equipment was used for each piece of evidence
    if len(inventory) > 0:
        nina "You made good use of your forensic toolkit."
        nina "Let me show you all the evidence you've collected."
        
        # Show the visual evidence summary screen
        call screen evidence_summary()
    
    nina "This case will still require careful laboratory work to determine exactly what caused the victim's death."
    nina "This concludes the initial crime scene assessment. The evidence has been documented and collected for laboratory analysis."
    nina "Feel free to return to the lab to continue your investigation."


    # This ends the game.
    return

# Screen for displaying hints during investigation
screen investigation_hint():
    frame:
        xalign 0.5
        yalign 0.05
        padding (15, 8)
        background "#00000080"
        
        # Different hints based on investigation state
        if examining_evidence:
            $ evidence_name = examining_evidence.replace("_", " ").title()
            text "Examining: [evidence_name] - Select the appropriate tool to collect this evidence":
                size 22
                color "#FFCC00"
                outlines [(1, "#000000", 0, 0)]
                text_align 0.5
                xalign 0.5
        else:
            $ hint_message = renpy.random.choice([
                "Click on items of interest to examine them.",
                "Look carefully for evidence around the scene.",
                "Investigate the scene to find all evidence."
            ])
            text hint_message:
                size 22
                color "#FFFFFF"
                outlines [(1, "#000000", 0, 0)]
                text_align 0.5
                xalign 0.5

# Screen for displaying examination message when evidence is first clicked
screen examination_message(item):
    modal False  # Changed to non-modal so player can interact with other elements
    frame:
        xalign 0.5
        yalign 0.3
        padding (25, 25)
        margin (50, 50)
        background "#000080AA" # Dark blue background
        vbox:
            spacing 15
            xalign 0.5
            
            text "Evidence Found!" style "evidence_header"
            null height 10
            
            # Custom descriptions for each evidence item
            if item == "chopsticks":
                text "You found chopsticks with potential fingerprints." style "evidence_text"
                text "Select the appropriate tool to collect this evidence." style "evidence_text"
            elif item == "soySauce":
                text "This soy sauce bottle looks suspicious." style "evidence_text"
                text "Select the appropriate tool to collect a sample." style "evidence_text"
            elif item == "courseMenu":
                text "The menu has some unknown stains." style "evidence_text"
                text "Select the appropriate tool to collect this evidence." style "evidence_text"
            elif item == "sushi":
                text "The half-eaten sushi roll needs to be examined." style "evidence_text"
                text "Select the appropriate tool to collect a sample." style "evidence_text"
            elif item == "knife":
                text "This knife may have been used to prepare the food." style "evidence_text"
                text "Select the appropriate tool to check for prints." style "evidence_text"
            elif item == "fishFilet":
                text "The fish filet needs to be sampled." style "evidence_text"
                text "Select the appropriate tool to collect this evidence." style "evidence_text"
            elif item == "notebook":
                text "A notebook with faded writing needs analysis." style "evidence_text"
                text "Select the appropriate tool to reveal the contents." style "evidence_text"
            else:
                text "You found evidence: [item]" style "evidence_text"
                text "Select the appropriate tool to collect it." style "evidence_text"
    
    # Automatically close the message after a short delay
    timer 2.0 action Hide("examination_message")
                
# Style for confirm buttons
style confirm_button:
    background "#004080"
    hover_background "#0060A0"
    padding (20, 10)
    xalign 0.5
    
style confirm_button_text:
    color "#FFFFFF"
    hover_color "#FFFF00"
    size 22
    xalign 0.5
    text_align 0.5

# Cancel examination button - appears when examining evidence
screen cancel_examination():
    if examining_evidence:
        frame:
            xalign 0.5
            yalign 0.95
            padding (15, 8)
            background "#800000AA"
            
            textbutton "Cancel Examination":
                style "cancel_button"
                action SetVariable("examining_evidence", None)

# Style for cancel button
style cancel_button:
    background "#800000"
    hover_background "#A00000"
    padding (20, 10)
    xalign 0.5
    
style cancel_button_text:
    color "#FFFFFF"
    hover_color "#FFFF00"
    size 22
    xalign 0.5
    text_align 0.5

# Screen to display all collected evidence at the end
screen evidence_summary():
    modal True
    
    # Background overlay
    add "#000000CC"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize int(config.screen_width * 0.8)
        ysize int(config.screen_height * 0.8)
        background "#000040AA"
        padding (40, 40)
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "Evidence Collected" style "evidence_header"
            null height 10
            
            # Grid to display evidence images - calculate columns based on number of items
            $ grid_columns = min(4, max(2, len(inventory)))  # At least 2, at most 4 columns
            grid grid_columns len(inventory) // grid_columns + (1 if len(inventory) % grid_columns else 0):
                spacing 30
                xalign 0.5
                
                for item in inventory:
                    frame:
                        background "#00000080"
                        padding (10, 10)
                        xsize 250
                        
                        vbox:
                            spacing 10
                            xalign 0.5
                            
                            # Show the evidence image
                            add "evidence " + item + " idle" xalign 0.5
                            
                            # Show evidence name
                            text item.replace("_", " ").title():
                                color "#FFFFFF" 
                                size 24 
                                xalign 0.5 
                                text_align 0.5
                                outlines [(1, "#000000", 0, 0)]
                            
                            # Show equipment used
                            text "Collected with:":
                                color "#FFCC00" 
                                size 18 
                                xalign 0.5 
                                text_align 0.5
                                outlines [(1, "#000000", 0, 0)]
                                
                            text evidence_requirements[item].replace("_", " ").title():
                                color "#88CCFF" 
                                size 18 
                                xalign 0.5 
                                text_align 0.5
                                outlines [(1, "#000000", 0, 0)]
            
            null height 30
            
            # Continue button
            frame:
                background "#004080"
                hover_background "#0060A0"
                padding (30, 15)
                xalign 0.5
                
                textbutton "Continue":
                    text_style "continue_button_text"
                    action Hide("evidence_summary")

style continue_button_text:
    color "#FFFFFF"
    hover_color "#FFCC00"
    size 28
    outlines [(1, "#000000", 0, 0)]
    xalign 0.5
    text_align 0.5

# Label for showing evidence summary - can be called from other parts of the game if needed
label show_evidence_summary:
    if len(inventory) > 0:
        call screen evidence_summary()
    else:
        nina "You haven't collected any evidence yet."
    return
