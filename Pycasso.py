'''
PYCASSO PROJECT (4pts)
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Upload both your code and a screenshot of your art.
'''
import arcade

arcade.open_window(700, 400, "Jonathan Reischel")
arcade.set_background_color((86, 125, 40))
arcade.start_render()

for i in range(0, 700, 70):
    arcade.draw_line(i, 0, i, 700, arcade.color.WHITE, 4,)

# University of Oregon logo
arcade.draw_text("O", 200, 150, arcade.color.YELLOW, 100, 300, "center", "times new roman")
arcade.draw_text("University of Oregon", 200, 100, arcade.color.YELLOW, 25)

# 50 yard line
arcade.draw_text("50", 72, 10, arcade.color.WHITE, 30, 300, "right")
arcade.draw_text("50", 72, 360, arcade.color.WHITE, 30, 300, "right")

# 40 yard line
arcade.draw_text("40", 142, 10, arcade.color.WHITE, 30, 300, "right")
arcade.draw_text("40", 142, 360, arcade.color.WHITE, 30, 300, "right")
arcade.draw_text("40", 2, 10, arcade.color.WHITE, 30, 300, "right")
arcade.draw_text("40", 2, 360, arcade.color.WHITE, 30, 300, "right")

# 30 yard line
arcade.draw_text("30", 212, 10, arcade.color.WHITE, 30, 300, "right")
arcade.draw_text("30", 212, 360, arcade.color.WHITE, 30, 300, "right")
arcade.draw_text("30", -70, 10, arcade.color.WHITE, 30, 300, "right")
arcade.draw_text("30", -70, 360, arcade.color.WHITE, 30, 300, "right")

# 20 yard line
arcade.draw_text("20", 282, 10, arcade.color.WHITE, 30, 300, "right")
arcade.draw_text("20", 282, 360, arcade.color.WHITE, 30, 300, "right")
arcade.draw_text("20", -139, 10, arcade.color.WHITE, 30, 300, "right")
arcade.draw_text("20", -139, 360, arcade.color.WHITE, 30, 300, "right")

# 10 yard line
arcade.draw_text("10", 352, 10, arcade.color.WHITE, 30, 300, "right")
arcade.draw_text("10", 352, 360, arcade.color.WHITE, 30, 300, "right")
arcade.draw_text("10", -206, 10, arcade.color.WHITE, 30, 300, "right")
arcade.draw_text("10", -206, 360, arcade.color.WHITE, 30, 300, "right")

arcade.finish_render()
arcade.run()




