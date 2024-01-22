import arcade
Fly = 1.9*260
Hoist = 260
Union_Fly = .76*260
Union_Hoist = .5385*260
arcade.open_window(Fly, Hoist, "Flag Art")
arcade.set_background_color((255, 255, 255))
arcade.start_render()
for i in range(0, Hoist, 010): # 010 is a place holder usure of what to put there
    arcade.draw_line(0, i, Fly, i, (191, 10, 48), size) # size is a place holder usure of how to dimension the flag
arcade.draw_lrtb_rectangle_filled(0, Union_Fly, 260, Union_Hoist, (0, 40, 104))
arcade.finish_render()
arcade.run()

