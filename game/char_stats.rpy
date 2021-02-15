


# 这个参数只对主角生效
init python:
    
    player = "Mango"
    player_default = "Mango"
    player_truename = ""
    numberID = 7415380
    gameID = "Mango" #为什么要添加这个?后面你们就知道了
    gameID_default = "Mango"
    mybirthday = 0215
    mybirthday_default = 0215
    age = 17
    age_default = 17
    gender = "男"
    gender_default = "男"

    mango_channel = "黑夜下的糖果酱"
    mango_channel_old = "迷茫大芒果"

    # 预设等级
    player_level = 1
    player_maxlevel = 130
    player_ch1_final_level = 130 # 如果等级未达到130就会进入第二个结局,反之为第一个结局


    player_maxhp = 120 #1450
    player_hp = player_maxhp
    player_atk = 0 #2440
    player_def = 1 #1840
    player_speed = 0
    player_maxmp = 3000
    player_mp = player_maxmp


    player_gold = 0

    player_turn = True
    player_action = ""

    flee_allow = False

    mango_truename = ""


    
    


    player_dmg = 0
    

define mango = Character('[player]', age=17, mybirthday=0215, gender="男", gameID="Mango",numberID=7415380)      
            

                