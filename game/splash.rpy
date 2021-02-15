





label splashscreen:

    if persistent.prologue_intro == True:
        call prologue from _call_prologue
    else:
        pass 


label before_main_menu:

    $ config.window_title = config.name   #  + (" ") + config.version

    return
