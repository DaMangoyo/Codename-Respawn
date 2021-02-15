# 这是重改的脚本,已经支持中文输入
label my_status:
    $ quick_menu = True
    scene black

    label EnterFirstMyName:
        $ player = renpy.input("给自己起个名字吧(支持中文)")
        $ player = player.strip()
        if player == "":
            "名字不能为空"
            jump EnterFirstMyName
        elif player == "Mango":
            $ player = "Mango" 

        return        

    label EnterMyBirthDay:
        $ mybirthday = renpy.input("生日",allow="1234567890",length=4) 
        $ mybirthday = mybirthday.strip()
        if mybirthday == "":
            "生日不能为空"
            jump EnterMyBirthDay

        return     

    label EnterMyAge:
        $ age = renpy.input("年龄?",allow="1234567890",length=2) 
        $ age = age.strip()
        if age == "":
            "年龄不能为空"
            jump EnterMyAge

        return    

    label SelectMyGender:
        menu SelectGender:
            "选择性别(你没得选)"
            "男":
                $ gender = "男"

        return         

    label MyGameID:
        $ gameid = renpy.input("我自己在游戏里面的ID")
        $ gameid = gameid.strip()
        if gameid == "":
            "不能为空"

            jump MyGameID                 
                 

    
    return


        
