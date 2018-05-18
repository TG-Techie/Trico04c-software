from staging.disp import disp, backlite as back_light, colorst

disp.fill(colorst(0,0,255))
disp.text(0,0,"ABCDEFGHIJKLMNOPQRSTU")
disp.text(0,8,"VWXYZ0123456789().")
disp.text(0,16,'"S,;:@#$%^&*-_+=`~')
disp.text(0,50,"ROB A.", size = 3)
disp.round_rect(0,0,50,50,15,0)
disp.round_rect(60,10,40,20,5,colorst(180,255,180))
