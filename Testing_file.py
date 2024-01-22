import arcade
SH = 600
SW = 600
arcade.open_window(SW, SH, "Star Wars Art")
arcade.set_background_color((255, 255, 255))
arcade.start_render()
# Draw stuff
arcade.draw_lrtb_rectangle_filled(200, 300, 400, 300,arcade.color.AIR_FORCE_BLUE)
arcade.draw_rectangle_filled(SW/2, SH/2, 300, 50, (0, 255, 0, 150))
arcade.draw_rectangle_outline(SW/2, SH/2, 300, 50, (0, 0, 0), 2)
arcade.draw_point(300, 300, arcade.color.AFRICAN_VIOLET, 10)
arcade.draw_line(0, 0, SW, SH, (0, 0, 255), 2)

# Draw Lines
for i in range(0, SW, 10):
    arcade.draw_line(i, 0, i, SH, (255, 0, 0), 1)
# Draw circle
arcade.draw_circle_filled(100, 100, 30, arcade.color.ANTIQUE_BRASS, 45)

# Draw ellipse
arcade.draw_ellipse_filled(400, 400, 300, 60, (0, 255, 0), 45)

# Creating text on drawing
arcade.draw_text("Jedi vs. Sith", 300, 300, arcade.color.BLACK, 16, 300,
"right", "times new roman", True, True,)

# To draw snowman in for loop
radius = 50
y = 50
for i in range(3):
    arcade.draw_circle_filled(100, y, radius, arcade.color.BLUE)
    y = y+1.8*radius
    radius *= .8

# Draw fence
for x_offset in range(0,610,20):
     arcade.draw_rectangle_filled(0+x_offset,60,10,30,arcade.color.WHITE)

# Draw rails
arcade.draw_rectangle_filled(300, 67, 600, 5, arcade.color.WHITE)
arcade.draw_rectangle_filled(300, 52, 600, 5, arcade.color.WHITE)
arcade.finish_render()



arcade.run()
