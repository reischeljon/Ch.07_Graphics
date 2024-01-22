import arcade
arcade.open_window(600, 600, "213639")
arcade.set_background_color(arcade.color.AMAZON)
arcade.start_render()

# Draw lines
for i in range(0, 600, 200):
    arcade.draw_line(i, 0, i, 600, arcade.color.BLACK, 1)
for i in range(0, 600, 200):
    arcade.draw_line(0, i, 600, i, arcade.color.BLACK, 1)

# section 1 draw the square
arcade.draw_rectangle_filled(100, 500, 50, 50, arcade.color.NEON_CARROT)
# section 1 draw the square outline
arcade.draw_rectangle_outline(100, 500, 50, 50, arcade.color.BLACK, 2)

# section 2 draw circle
arcade.draw_circle_filled(300, 500, 50, arcade.color.BRIGHT_TURQUOISE)

# section 3 pacman
arcade.draw_arc_filled(500, 500, 50, 50, arcade.color.YELLOW, -150, 150)

# section 4
p = ((100, 400), (200, 300), (100, 200), (0, 300))
arcade.draw_polygon_filled(p,arcade.color.BARBIE_PINK)

# section 5
for i in range(200, 401, 20):
    arcade.draw_line(i, 200, 200, i, arcade.color.BLACK, 1)
    arcade.draw_line(i, 400, 400, i, arcade.color.BLACK, 1)


# Section 6 flag
# arcade.draw_lrtb_rectangle_filled(401, 599, 399, 201, arcade.color.WHITE)
# for i in range(5):
#    arcade.draw_rectangle_filled(500, 230, + i * 40, 200, 20, arcade.color.RED)
# arcade.draw_rectangle_filled(450, 350, 100, 100, arcade.color.NAVY_BLUE)

# section 7 draw 5 circles
# Did not know how to loop the code
arcade.draw_circle_filled(20, 100, 20, arcade.color.BLUEBERRY, 45)
arcade.draw_circle_filled(60, 100, 20, arcade.color.BLUEBERRY, 45)
arcade.draw_circle_filled(100, 100, 20, arcade.color.BLUEBERRY, 45)
arcade.draw_circle_filled(140, 100, 20, arcade.color.BLUEBERRY, 45)
arcade.draw_circle_filled(180, 100, 20, arcade.color.BLUEBERRY, 45)

# section 8
for y in range(10, 200, 10):
    for x in range(210, 400, 10):
        arcade.draw_point(x, y, arcade.color.NEON_GREEN, 2)

# Section 9 drawing name
arcade.draw_text("Jonathan Reischel", 260, 100, arcade.color.BLACK, 12, 300,
"right", "times new roman")

arcade.finish_render()

arcade.run()