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

# 3) Your character and portrait declarations remain unchanged
define me = Character("Jon", color="#66ccff")

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

# --- Ask if the player wants more facts or to quit ---
label more_menu:
    menu:
        "Tell me another fact":
            jump fact_menu
        "No, thanks!":
            show me idle at center
            me "See you next time!"
            return
