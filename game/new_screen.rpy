screen demo_text_screen:

     text "Demo版本" size 22 xpos 0.92
     text "警告:Demo版本只提供试玩内容" size 22 xpos 0.72  ypos 0.04

screen exp_and_gold_screen:

    text "金币:[player_gold],经验:[player_exp]/[level_exp]" xpos 0.01 ypos 0.01 color "#ffffff"

screen battle_ui:

     if player_turn == True:
          imagebutton:
               xpos 0.01 ypos 0.14
               idle "battle_images/button/fight_button0.png"        
               hover "battle_images/button/fight_button1.png"
               action Return("fight")
          imagebutton:
               xpos 0.01 ypos 0.21
               idle "battle_images/button/skill_button0.png"
               hover "battle_images/button/skill_button1.png"
               action Return("skill")
          imagebutton:
               xpos 0.01 ypos 0.28
               idle "battle_images/button/act_button0.png"
               hover "battle_images/button/act_button1.png"
               action Return("act")    
          imagebutton:
               xpos 0.01 ypos 0.35
               idle "battle_images/button/item_button0.png"
               hover "battle_images/button/item_button1.png"
               action Return("item") 
          if flee_allow == True:
               imagebutton:
                    xpos 0.01 ypos 0.42
                    idle "battle_images/button/flee_button0.png"
                    hover "battle_images/button/flee_button1.png"
                    action Return("flee")
          else:
               imagebutton:
                    xpos 0.01 ypos 0.42
                    idle "battle_images/button/flee_button_default.png"
                    #hover "battle_images/button/flee_button1.png"
                    action NullAction()

     else:
          imagebutton:
               xpos 0.01 ypos 0.14
               idle "battle_images/button/fight_button_default.png"        
               action NullAction()  
          imagebutton:
               xpos 0.01 ypos 0.21
               idle "battle_images/button/skill_button_default.png"
               action NullAction()  
          imagebutton:
               xpos 0.01 ypos 0.28
               idle "battle_images/button/act_button_default.png"
               action NullAction()     
          imagebutton:
               xpos 0.01 ypos 0.35
               idle "battle_images/button/item_button_default.png"
               action NullAction()  
          imagebutton:
               xpos 0.30 ypos 0.42
               idle "battle_images/button/flee_button_default.png"
               action NullAction()          