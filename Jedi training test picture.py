# Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
# BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
# The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
import arcade
arcade.open_window(500, 400, "213639")
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
for i in range(0, 500, 20):
    arcade.draw_line(i, 0, i, 500, arcade.color.BLACK, 1)
for i in range(0, 500, 20):
    arcade.draw_line(0, i, 500, i, arcade.color.BLACK, 1)
arcade.draw_arc_filled(400, 300, 125, 125, arcade.color.YELLOW, 0, 0) # 0, 0 is a place holder unsure how to find angle
arcade.finish_render()
arcade.run()
