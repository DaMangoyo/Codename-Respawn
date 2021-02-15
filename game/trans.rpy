define dissolve = Dissolve(0.25)



#Special a series of dissolves for a full scene change
define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0), #Fade to black for 1 second
    Solid("#000"), Pause(1.0), #Wait 1 second
    Solid("#000"), Dissolve(1.0), #Fade out of black for 1 second
    True])

#Fade out from black for start of a new scene
define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

#闭眼
define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])

#睁眼
define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])

#Sudden blackness
define trueblack = MultipleTransition([
    Solid("#000"), Pause(0.25),
    Solid("#000")
    ])

#Override wipeleft with a proper-looking wipe that has a nice fade to it
define wipeleft = ImageDissolve("images/wipeleft.png", 0.5, ramplen=64)

#Wipe to black, pause for .25 seconds, then wipe to the next scene (indicates the passing of time between scenes)
define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/wipeleft.png", 0.5, ramplen=64),
    True])