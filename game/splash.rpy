
init python:
    
    import os

    try:os.mkdir("C:/Mango")
    except:pass

    try:os.mkdir(config.basedir + "/test")
    except:pass



init python:

    splashMessage = "Game By Mango \nEngine: Ren'py"


style splashText:

    properties gui.text_properties()
    language gui.language

image splashWarning = ParameterizedText(style="splashText", xalign=0.5, yalign=0.5)    


label splashscreen:
 
    






    $ splashMessages = splashMessage

    
    show white
    show splashWarning "[splashMessages]" + "[renpy.version_only]" with Dissolve(2.5)
    pause 2.5
    hide splashWarning with Dissolve(2.5)      

    
    show splashWarning "本游戏目前还是未完成版本,后续将会有新的东西出现\n请留意后续的更新" with Dissolve(2.5)
    pause 3.5
    hide splashWarning with Dissolve(2.5) 


    

    if persistent.nogame == True:


        jump select_game 



    #show splashWarning "StoryBased:???????" with Dissolve(2.5)
    #pause 2.5
    #hide splashWarning with Dissolve(2.5)    

    pause 2.0




    return














label before_main_menu:

    $ config.window_title = config.name + " " + "标题界面"