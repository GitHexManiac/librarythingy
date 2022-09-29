import arcade
my_window = arcade.open_window(1000, 800, "Ghana Flag")
arcade.set_background_color(arcade.color.YELLOW)
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0,1000,1000,533.36, arcade.color.RED)
arcade.finish_render()
arcade.run()