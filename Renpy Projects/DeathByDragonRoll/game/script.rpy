# The script of the game goes in this file.

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
    image equipment evidence_swab selected = im.Scale("images/equipment/evidence_swab.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    
    image equipment fingerprint_kit idle = im.Scale("images/equipment/fingerprint-kit.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment fingerprint_kit hover = im.Scale("images/equipment/fingerprint-kit.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment fingerprint_kit selected = im.Scale("images/equipment/fingerprint-kit.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    
    image equipment gauze idle = im.Scale("images/equipment/gauze.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment gauze hover = im.Scale("images/equipment/gauze.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment gauze selected = im.Scale("images/equipment/gauze.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    
    image equipment phadebas idle = im.Scale("images/equipment/phadebas.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment phadebas hover = im.Scale("images/equipment/phadebas.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    image equipment phadebas selected = im.Scale("images/equipment/phadebas.png", int(config.screen_width * 0.1), int(config.screen_height * 0.1))
    
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

# Equipment variables
default selected_equipment = None
default examining_evidence = None  # Tracks which evidence item is being examined
default equipment_list = ["evidence_swab", "fingerprint_kit", "gauze", "phadebas", "scissors", "specimen_collection"]

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
    "chopsticks": "fingerprint_kit",
    "soySauce": "specimen_collection",
    "courseMenu": "gauze",
    "sushi": "evidence_swab",
    "knife": "fingerprint_kit",
    "fishFilet": "scissors",
    "notebook": "phadebas"
}

# Screen for displaying "Press space to continue" prompt
screen continue_prompt():
    frame:
        xalign 0.5
        yalign 0.98
        padding (15, 8)
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

# Equipment selection screen - displays equipment on both sides of the screen
screen equipment_selection():
    # Only show when an evidence item is being examined
    if examining_evidence:
        # Split equipment list into two groups
        python:
            left_equipment = equipment_list[:3]  # First three items
            right_equipment = equipment_list[3:] # Rest of items
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
                    $ frame_bg = "#00FF0080" if selected_equipment == item else None
                    $ is_required = (item == required_equipment)
                    
                    frame:
                        # Use different colored frames to indicate states
                        background frame_bg
                        padding (10, 10)
                        margin (5, 5)
                        xalign 0.5
                        
                        # Add gold highlight for required tool
                        if is_required:
                            at pulse
                        
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
                    $ frame_bg = "#00FF0080" if selected_equipment == item else None
                    $ is_required = (item == required_equipment)
                    
                    frame:
                        # Use different colored frames to indicate states
                        background frame_bg
                        padding (10, 10)
                        margin (5, 5)
                        xalign 0.5
                        
                        # Add gold highlight for required tool
                        if is_required:
                            at pulse
                        
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
    # Calculate adjusted center area (accounting for side panels when they appear)
    $ center_offset_x = int(config.screen_width * 0.15)  # Offset from left side panel width
    
    # Ensure evidence items are positioned within the visible center area
    for item_name, pos in items:
        if not evidence_collected[item_name]:
            # Adjust position to ensure it's in the center area
            # Scale the original position based on screen width, accounting for panel widths on both sides
            $ adjusted_x = center_offset_x + int((pos[0] / 1280.0) * (config.screen_width - 2*center_offset_x))
            
            # Use a different action based on whether this item is being examined
            if examining_evidence == item_name:
                # Check if the correct equipment is selected
                $ can_collect = selected_equipment == evidence_requirements[item_name]
                
                imagebutton:
                    auto "evidence " + item_name + " %s"
                    xpos adjusted_x
                    ypos pos[1]
                    focus_mask True
                    
                    # When examined and equipment selected, handle collection
                    if can_collect:
                        action [SetDict(evidence_collected, item_name, True), 
                                Function(add_to_inventory, item_name), 
                                Show("evidence_collected", item=item_name),
                                SetVariable("examining_evidence", None),
                                SetVariable("selected_equipment", None),
                                Return(None)]
                    else:
                        # If equipment is wrong, show feedback
                        action Show("wrong_equipment", item=item_name, required_equipment=evidence_requirements[item_name])
            else:
                # Initial click to start examining this evidence
                imagebutton:
                    auto "evidence " + item_name + " %s"
                    xpos adjusted_x
                    ypos pos[1]
                    focus_mask True
                    action [SetVariable("examining_evidence", item_name),
                            Show("examination_message", item=item_name)]

# Screen for displaying evidence collection message
screen evidence_collected(item):
    modal True
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
    timer 2.5 action Hide("evidence_collected")

# Screen for displaying wrong equipment message
screen wrong_equipment(item, required_equipment):
    modal True
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
                text "You need: " + required_equipment.replace("_", " ").title() style "evidence_text" 
            else:
                text "You need to select the appropriate equipment first." style "evidence_text"
                text "Required: " + required_equipment.replace("_", " ").title() style "evidence_text"
    timer 3.5 action Hide("wrong_equipment")

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
    
    # Use Ren'Py's built-in pause to wait for player interaction
    $ renpy.pause(hard=True)
    
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
    # Format: (evidence_name, (x_position, y_position))
    $ restaurant_evidence = [
        ("chopsticks", (620, 700)),   # Left side
        ("soySauce", (800, 600)),     # Center-left
        ("courseMenu", (220, 740)),     # Center-right
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
    nina "Remember to select the right forensic tools for each piece of evidence. The wrong tool won't work!"
    
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
        
        # Create a dictionary mapping evidence to equipment used
        evidence_equipment_used = {}
        for item in inventory:
            evidence_equipment_used[item] = evidence_requirements[item]
    
    nina "You've found [clues_found] pieces of evidence: [evidence_list]."
    
    # Show what equipment was used for each piece of evidence
    if len(inventory) > 0:
        nina "You made good use of your forensic toolkit:"
        
        python:
            equipment_summary = ""
            for item in inventory:
                equip = evidence_requirements[item]
                item_formatted = item.replace("_", " ").title()
                equip_formatted = equip.replace("_", " ").title()
                equipment_summary += "- " + item_formatted + " collected with " + equip_formatted + "\n"
                
        nina "[equipment_summary]"
    
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
            $ required_tool = evidence_requirements[examining_evidence].replace("_", " ").title()
            $ evidence_name = examining_evidence.replace("_", " ").title()
            text "Examining: [evidence_name] - Choose the correct tool to collect this evidence":
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
    modal True
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
                text "Select a tool to collect this evidence." style "evidence_text"
            elif item == "soySauce":
                text "This soy sauce bottle looks suspicious." style "evidence_text"
                text "Select a tool to collect a sample." style "evidence_text"
            elif item == "courseMenu":
                text "The menu has some unknown stains." style "evidence_text"
                text "Select a tool to collect this evidence." style "evidence_text"
            elif item == "sushi":
                text "The half-eaten sushi roll needs to be examined." style "evidence_text"
                text "Select a tool to collect a sample." style "evidence_text"
            elif item == "knife":
                text "This knife may have been used to prepare the food." style "evidence_text"
                text "Select a tool to check for prints." style "evidence_text"
            elif item == "fishFilet":
                text "The fish filet needs to be sampled." style "evidence_text"
                text "Select a tool to collect this evidence." style "evidence_text"
            elif item == "notebook":
                text "A notebook with faded writing needs analysis." style "evidence_text"
                text "Select a tool to reveal the contents." style "evidence_text"
            else:
                text "You found evidence: [item]" style "evidence_text"
                text "Select a tool to collect this evidence." style "evidence_text"
            
            null height 10
            textbutton "Choose Tool":
                style "confirm_button"
                action Hide("examination_message")
                
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
