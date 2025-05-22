init python:
    from renpy.display import im

init:
    # Scale images to exactly fill the window
    image bg kitchen = im.Scale(
        "images/kitchen.jpg",
        config.screen_width,
        config.screen_height
    )
    image bg park    = im.Scale(
        "images/park.jpg",
        config.screen_width,
        config.screen_height
    )
    image bg dojang = im.Scale(
        "images/dojang.jpg",
        config.screen_width,
        config.screen_height
    )

    # Nina's expressions
    image nina normal1 = "images/nina normal1.png"
    image nina normal2 = "images/nina normal2.png"
    image nina normal3 = "images/nina normal3.png"
    image nina thinknote1 = "images/nina thinknote1.png"
    image nina write1 = "images/nina write1.png"

# 3) Your character and portrait declarations remain unchanged
define me = Character("Jon", color="#66ccff")
define nina = Character("Nina", color="#ff99cc")

image me idle  = "images/portrait_idle.png"

# --- Start of the game ---
label start:
    scene bg kitchen
    show me idle at center

    me "Hi there! I'm Jon, and welcome to my interactive autobiography."
    me "Let me share a few interesting facts about me."

    jump fact_menu

# --- Main menu ---
label fact_menu:
    menu:
        "Where I grew up":
            scene bg park with fade
            show me idle at center
            me "I grew up in Jakarta, Indonesia. Lived there for 18 years before coming to Canada."
            jump more_menu

        "My favorite hobbies":
            scene bg kitchen with fade
            show me idle at center
            me "I'm a huge foodie! I love cooking and trying new cuisines. I also enjoy playing video games and the guitar."
            jump more_menu

        "My favourite sports":
            scene bg dojang with fade
            show me idle at center
            me "I've always played Badminton growing up, but starting high school I did competitive Taekwondo and received my black belt before leaving for University"
            jump more_menu

        "Meet a new friend":
            jump nina_intro

# --- Ask if the player wants more facts or to quit ---
label more_menu:
    menu:
        "Tell me another fact":
            jump fact_menu
        "No, thanks!":
            show me idle at center
            me "See you next time!"
            return

# --- Nina interactive scene ---
label nina_intro:
    scene bg park with fade
    show nina normal1 at center

    nina "Hi! I'm Nina. It's nice to meet you."
    nina "What would you like to talk about?"

    jump nina_convo

label nina_convo:
    menu:
        "Ask Nina about her hobbies":
            show nina normal2 at center
            nina "Oh, I love writing stories and drawing in my notebook!"
            show nina write1 at center
            nina "Sometimes I get so lost in my writing, I forget the time."
            jump nina_more
        "Compliment Nina's notebook":
            show nina thinknote1 at center
            nina "Thank you! I always carry it with me. It's full of my thoughts and doodles."
            show nina normal3 at center
            nina "Would you like to see a drawing?"
            jump nina_more
        "Say hello shyly":
            show nina normal3 at center
            nina "Hehe, you're a bit shy, aren't you? That's okay! I'm happy to chat whenever you like."
            jump nina_more

label nina_more:
    menu:
        "Ask another question":
            jump nina_convo
        "Return to main menu":
            scene bg kitchen with fade
            show me idle at center
            me "That was fun meeting Nina!"
            jump fact_menu
