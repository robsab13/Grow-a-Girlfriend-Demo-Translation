
init python:

    def get_available_translations():
        tl_path = os.path.join(renpy.config.gamedir, "tl")
        available_translations = []
        if os.path.isdir(tl_path):
            for folder_name in os.listdir(tl_path):
                # Exclude "None" folder and any hidden files
                if folder_name != "None" and not folder_name.startswith('.'):
                    available_translations.append(folder_name)
        return available_translations



translate russian style default:
    font "NotoSans-Regular.ttf"

translate russian style choice_button_text:
    font "NotoSans-Regular.ttf"

translate russian style input:
    font "NotoSans-Regular.ttf"

translate russian style check_button_text:
    font "NotoSans-Regular.ttf"

translate russian style button_text:
    font "NotoSans-Regular.ttf"

translate russian style say_label:
    size 30

translate russian style radio:
    font "NotoSans-Regular.ttf"

translate russian style navigation_button_text:
    font "NotoSans-Regular.ttf"

translate russian style radio_button_text:
    font "NotoSans-Regular.ttf"

translate russian style confirm_button_text:
    font "NotoSans-Regular.ttf"

translate russian python:
    gui.text_font = "NotoSans-Regular.ttf"
    gui.system_font = "NotoSans-Regular.ttf"
    gui.interface_text_font = "NotoSans-Regular.ttf"
    gui.name_text_font = "NotoSans-Regular.ttf"
    
    gui.name_text_size = 10
    gui.interface_text_size = 45
    gui.text_size = 30
    gui.label_text_size = 45
    gui.notify_text_size = 24
    gui.title_text_size = 75


screen change_language:
    tag menu
    add "gui/main_menu_items/menu_bg_scroll.png" at scroll
    imagebutton:
        xpos 0 ypos 0
        idle "gui/main_menu_items/gallery_arrow_idle.png"
        hover "gui/main_menu_items/gallery_arrow_hover.png"
        action ShowMenu("main_menu")
        focus_mask True
    vbox:
        xalign 0.5 yalign 0.3
        style_prefix "radio"
        # label ("Languages")
        text "{color=#4a3138}English button:"
        imagebutton:
            xoffset 30
            idle "images/sprites/affection/affection min_good.png"
            action Language(None)
        
        spacing 20

        for lang in get_available_translations():
            textbutton (f"{lang.capitalize()}") action [Language(lang)]

    text "{color=#4a3138}I suggest you translate screens.rpy first so you can navigate the game, otherwise menu options will be blank.\nTip: Hold Shift and R while in game to reload all your scripts! Handy for quick testing!":
        xpos 0.1 ypos 0.8

