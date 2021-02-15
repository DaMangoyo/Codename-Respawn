# 游戏的脚本可置于此文件中。

# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    show screen exp_and_gold_screen

    
    if persistent.chapter == 0:
        call chapter0_1 

        call enemy_appear 

        call chapter0_2 

        call enemy_appear 

        call chapter0_end 
             
    
        

    # 此处为游戏结尾。

    return

label level_up(target_label=""):

    if player_level < player_maxlevel:

        if player_level == 1 and player_exp >= level_exp:
            python:
                player_level += 1
                nextlevel_exp = 75
                player_maxhp += level_maxhp
                player_hp += level_hp
                player_atk += level_atk
                player_def += level_def

            "恭喜升级!\nMango 等级:[player_level]"

        if player_level == 2 and player_exp >= level_exp:
            python:
                player_level += 1
                level_exp = 255
                player_maxhp += (level_maxhp + 60)
                player_hp += (level_hp + 60)
                player_atk += (level_atk + 5)
                player_def += (level_def + 5)

            "恭喜升级!\nMango 等级:[player_level]"    

        if player_level == 3 and player_exp >= level_exp:
            python:
                player_level += 1
                level_exp = 498
                player_maxhp += (level_maxhp + 90)
                player_hp += (level_hp + 90)
                player_atk += (level_atk + 8)
                player_def += (level_def + 8)

            "恭喜升级!\nMango 等级:[player_level]"    

        if player_level == 4 and player_exp >= level_exp:
            python:
                player_level += 1
                level_exp = 688
                player_maxhp += 150
                player_hp += 150
                player_atk += 12
                player_def += 12   

            "恭喜升级!\nMango 等级:[player_level]"   

        else:
            pass 

    "下个等级所需经验:[nextlevel_exp]"


    
    jump expression target_label