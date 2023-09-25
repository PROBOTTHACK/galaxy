from kivy.uix.relativelayout import RelativeLayout
def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
    self._keyboard = None


def on_touch_down(self, touch):
    #state_game_over = False
    #state_game_has_started = False
    if not self.state_game_over and self.state_game_has_started:
        if touch.x < self.width / 2:
            # print("<-")
            self.current_speed_x = self.SPEED_X
        else:
            # print("->")
            self.current_speed_x = -self.SPEED_X
    return super(RelativeLayout, self).on_touch_down(touch)


def on_touch_up(self, touch):
    #print("UP")
    self.current_speed_x = 0
