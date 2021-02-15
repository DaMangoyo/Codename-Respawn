screen story_menu:
    
    tag menu

    use game_menu(_("故事")):

        hbox:
            textbutton "故事开始" xalign 0.5 yalign 0.5 action Start()   
            textbutton "第一章终章-最后的留言(仅供预览)" xalign 0.5 yalign 0.5 action Start("chfinal_message")     



screen story_select:
    
    tag menu

    use game_menu(_("故事")):

        hbox:
            textbutton "序章(上下部分)" xalign 0.5 yalign 0.5 action Start()  
            textbutton "第一章:最开始的冒险生涯" xalign 0.5 yalign 0.5 action NullAction()             


screen extra_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()


            