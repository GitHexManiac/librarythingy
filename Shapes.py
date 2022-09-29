import arcade
my_window = arcade.open_window(1000, 800, "Lot's of shapes")
arcade.set_background_color(arcade.color.AUREOLIN)
arcade.start_render()
#_________________________________________________________
arcade.draw_line_strip([(20,30), (90,180), (160,30), (10,120), (170,120),(20,30)],arcade.color.YELLOW_ORANGE, 5)

arcade.draw_lrtb_rectangle_outline(520, 620, 550, 250, arcade.color.ARMY_GREEN)
arcade.draw_lrtb_rectangle_filled(720, 820, 550, 250, arcade.color.BYZANTIUM)

arcade.draw_xywh_rectangle_outline(600,50,100,300, arcade.color.HONOLULU_BLUE, 7)
arcade.draw_xywh_rectangle_outline(500,100,400,100, arcade.color.HONEYDEW, 20)

arcade.draw_circle_filled(350, 700, 300, arcade.color.PURPLE_HEART)
arcade.draw_circle_outline(350,700, 300, arcade.color.PAOLO_VERONESE_GREEN, 10)

arcade.draw_triangle_filled(500,500, 700,500, 600, 400, arcade.color.UROBILIN)
arcade.draw_triangle_filled(500,300, 700,300, 600, 400, arcade.color.AUROMETALSAURUS)

arcade.draw_arc_filled( 100, 300, 100,100,arcade.color.BLACK_LEATHER_JACKET,60,330)
arcade.draw_arc_filled( 200, 400, 100,100, arcade.color.BLANCHED_ALMOND,60.555, 330)
#_________________________________________________________
arcade.finish_render()
arcade.run()

