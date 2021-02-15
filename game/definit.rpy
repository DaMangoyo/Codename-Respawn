
#define config.developer = False

init python:
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)



default persistent.prologue_intro = True

default persistent.chapter = 0



default persistent.prologue_clear = False
default persistent.chapter_select = True



init python:
    
    area_enemies_total = 100
    area_enemies_truename_total = 480



    enemies_left = area_enemies_total
    enemies_truename_left = area_enemies_truename_total 
    
    area8_total_enemies = 40
    area8_total_enemies_truename = 120
    area9_total_enemies = 16
    area9_total_enemies_truename = 120
    area10_total_enemies = 30
    area10_total_enemies_truename = 120
    area11_total_enemies = 14
    area11_total_enemies_truename = 120
    area12_total_enemies = 0
    area12_total_enemies_truename = 0