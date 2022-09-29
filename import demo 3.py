import arcade
my_window = arcade.open_window(1200, 800, "First Window Demo")
arcade.set_background_color(arcade.color.AERO_BLUE)
arcade.start_render()
arcade.draw_circle_filled(600, 400, 200,
arcade.color.YELLOW_ORANGE)
arcade.draw_circle_filled(520, 430, 50,
arcade.color.WHITE)
arcade.draw_circle_filled(680, 430, 50,
arcade.color.WHITE)
arcade.draw_circle_filled(520,430,22,
arcade.color.BLACK)
arcade.draw_circle_filled(680,430,22,
arcade.color.BLACK)
arcade.draw_rectangle_filled(600,381,350,50,
arcade.color.YELLOW_ORANGE)
arcade.draw_parabola_filled(480,150,720,200,
arcade.color.BLACK,180)
arcade.draw_parabola_outline(380,300,500,60,arcade.color.LIGHT_BLUE,40,50)
arcade.draw_parabola_outline(380,300,500,60,arcade.color.LIGHT_BLUE,40,230)
arcade.draw_rectangle_filled(430,350,140,40,
arcade.color.LIGHT_BLUE,130)
arcade.finish_render()
arcade.run()