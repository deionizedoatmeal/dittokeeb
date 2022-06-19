# written summer '22 by ian k. bania
# to edit key layout, search for "EDIT KEYBOARD LAYERS HERE"
# to use a microcontroller, search for "ADD CUSTOM CODE HERE"
# to change neopixel colors, search for "EDIT LED COLORS HERE"
# HBD!

import board
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# the number of columns and rows in the scan matrix
COLUMNS = 12
ROWS = 4

# define with pins on the RP2040 are used for those columns/rows,
# allow 50 milisecs to debounce and define polarity of scan metrix diodes
keys = keypad.KeyMatrix(
        row_pins=(
            board.GP1, 
            board.GP2, 
            board.GP3, 
            board.GP4, 
            board.GP5
        ),
        column_pins=(
            board.GP6, 
            board.GP7, 
            board.GP8, 
            board.GP9, 
            board.GP10, 
            board.GP11, 
            board.GP12, 
            board.GP13, 
            board.GP14, 
            board.GP15, 
            board.GP16 
        ),
        interval=0.050,
        columns_to_anodes = False
)

kbd = Keyboard(usb_hid.devices)

# EDIT KEYBOARD LAYERS HERE
# create a keycode dictionary including modifier state and keycodes
keymap = {(0): (0, Keycode.ESCAPE),
    # top row keys, left to right
    (1): (0, Keycode.Q),
    (2): (0, Keycode.W),
    (3): (0, Keycode.E),
    (4): (0, Keycode.R),
    (5): (0, Keycode.T),
    (6): (0, Keycode.Y),
    (7): (0, Keycode.U),
    (8): (0, Keycode.I),
    (9): (0, Keycode.O),
    (10): (0, Keycode.P),
    (11): (0, Keycode.BACKSPACE),
    # 2nd row keys, left to right
    (12): (0, Keycode.TAB),
    (13): (0, Keycode.A),
    (14): (0, Keycode.S),
    (15): (0, Keycode.D),
    (16): (0, Keycode.F),
    (17): (0, Keycode.G),
    (18): (0, Keycode.H),
    (19): (0, Keycode.J),
    (20): (0, Keycode.K),
    (21): (0, Keycode.L),
    (22): (0, Keycode.ENTER),
    # 3rd row keys, left to right
    (23): (1, Keycode.LEFT_SHIFT),
    (24): (0, Keycode.Z),
    (25): (0, Keycode.X),
    (26): (0, Keycode.C),
    (27): (0, Keycode.V),
    (28): (0, Keycode.B),
    (29): (0, Keycode.N),
    (30): (0, Keycode.M),
    (31): (0, Keycode.PERIOD),
    (32): (1, Keycode.RIGHT_SHIFT),
    (33): (2, Keycode.APPLICATION),
    # bottom row keys, left to right
    (34): (0, Keycode.LEFT_CONTROL),
    (35): (0, Keycode.WINDOWS),
    (36): (0, Keycode.LEFT_ALT),
    (37): (0, Keycode.SPACEBAR),
    (38): (0, Keycode.RIGHT_ALT),
    (39): (0, Keycode.RIGHT_CONTROL)
}

# # define the shift layer of the keyboard
# keymap_shift = {
#     # top row keys, left to right
#     (0): (0, Keycode.ESCAPE),
#     (1): (0, Keycode.Q),
#     (2): (0, Keycode.W),
#     (3): (0, Keycode.E),
#     (4): (0, Keycode.R),
#     (5): (0, Keycode.T),
#     (6): (0, Keycode.Y),
#     (7): (0, Keycode.U),
#     (8): (0, Keycode.I),
#     (9): (0, Keycode.O),
#     (10): (0, Keycode.P),
#     (11): (0, Keycode.BACKSPACE),
#     # 2nd row keys, left to right
#     (12): (0, Keycode.TAB),
#     (13): (0, Keycode.A),
#     (14): (0, Keycode.S),
#     (15): (0, Keycode.D),
#     (16): (0, Keycode.F),
#     (17): (0, Keycode.G),
#     (18): (0, Keycode.H),
#     (19): (0, Keycode.J),
#     (20): (0, Keycode.K),
#     (21): (0, Keycode.L),
#     (22): (0, Keycode.ENTER),
#     # 3rd row keys, left to right
#     (23): (1, Keycode.LEFT_SHIFT),
#     (24): (0, Keycode.Z),
#     (25): (0, Keycode.X),
#     (26): (0, Keycode.C),
#     (27): (0, Keycode.V),
#     (28): (0, Keycode.B),
#     (29): (0, Keycode.N),
#     (30): (0, Keycode.M),
#     (31): (0, Keycode.PERIOD),
#     (32): (1, Keycode.RIGHT_SHIFT),
#     (33): (2, Keycode.FN),
#     # bottom row keys, left to right
#     (34): (0, Keycode.LEFT_CONTROL),
#     (35): (0, Keycode.WINDOWS),
#     (36): (0, Keycode.LEFT_ALT),
#     (37): (0, Keycode.SPACEBAR),
#     (38): (0, Keycode.RIGHT_ALT),
#     (39): (0, Keycode.RIGHT_CONTROL)
# }

# # define the Fn layer of the keyboard
# keymap_fn = {
#     # top row keys, left to right
#     (0): (0, Keycode.GRAVE_ACCENT),
#     (1): (0, Keycode.ONE),
#     (2): (0, Keycode.TWO),
#     (3): (0, Keycode.THREE),
#     (4): (0, Keycode.FOUR),
#     (5): (0, Keycode.FIVE),
#     (6): (0, Keycode.SIX),
#     (7): (0, Keycode.SEVEN),
#     (8): (0, Keycode.EIGHT),
#     (9): (0, Keycode.NINE),
#     (10): (0, Keycode.ZERO),
#     (11): (0, Keycode.EQUALS),
#     # 2nd row keys, left to right
#     (12): (0, Keycode.CAPS_LOCK),
#     (13): (0, Keycode.A),
#     (14): (0, Keycode.UP_ARROW),
#     (15): (0, Keycode.D),
#     (16): (0, Keycode.F),
#     (17): (0, Keycode.G),
#     (18): (0, Keycode.MINUS),
#     (19): (0, Keycode.LEFT_BRACKET),
#     (20): (0, Keycode.RIGHT_BRACKET),
#     (21): (0, Keycode.FORWARD_SLASH),
#     (22): (0, Keycode.BACK_SLASH),
#     # 3rd row keys, left to right
#     (23): (1, Keycode.LEFT_SHIFT),
#     (24): (0, Keycode.LEFT_ARROW),
#     (25): (0, Keycode.DOWN_ARROW),
#     (26): (0, Keycode.RIGHT_ARROW),
#     (26): (0, Keycode.V),
#     (28): (0, Keycode.SEMICOLON),
#     (29): (0, Keycode.APOSTROPHE),
#     (30): (0, Keycode.COMMA),
#     (31): (0, Keycode.PERIOD),
#     (32): (1, Keycode.RIGHT_SHIFT),
#     (33): (2, Keycode.FN),
#     # bottom row keys, left to right
#     (34): (0, Keycode.LEFT_CONTROL),
#     (35): (0, Keycode.WINDOWS),
#     (36): (0, Keycode.LEFT_ALT),
#     (37): (0, Keycode.SPACEBAR),
#     (38): (0, Keycode.RIGHT_ALT),
#     (39): (0, Keycode.RIGHT_CONTROL)
# }

# # define the Fn + shift layer of the keyboard
# keymap_fnshift = {
#     # top row keys, left to right
#     (0): (0, Keycode.TILDA),
#     (1): (0, Keycode.ECLAIM),
#     (2): (0, Keycode.AT),
#     (3): (0, Keycode.POUND),
#     (4): (0, Keycode.DOLLAR),
#     (5): (0, Keycode.PERCENT),
#     (6): (0, Keycode.ASCIICIRCUM),
#     (7): (0, Keycode.AMPERSAND),
#     (8): (0, Keycode.ASTERICKS),
#     (9): (0, Keycode.LEFT_PAREN),
#     (10): (0, Keycode.RIGHT_PAREN),
#     (11): (0, Keycode.PLUS),
#     # 2nd row keys, left to right
#     (12): (0, Keycode.CAPS_LOCK),
#     (13): (0, Keycode.A),
#     (14): (0, Keycode.UP_ARROW),
#     (15): (0, Keycode.D),
#     (16): (0, Keycode.F),
#     (17): (0, Keycode.G),
#     (18): (0, Keycode.UNDERSCORE),
#     (19): (0, Keycode.LEFT_BRACE),
#     (20): (0, Keycode.RIGHT_BRACE),
#     (21): (0, Keycode.QUESTION),
#     (22): (0, Keycode.BAR),
#     # 3rd row keys, left to right
#     (23): (1, Keycode.LEFT_SHIFT),
#     (24): (0, Keycode.LEFT_ARROW),
#     (25): (0, Keycode.DOWN_ARROW),
#     (26): (0, Keycode.RIGHT_ARROW),
#     (26): (0, Keycode.V),
#     (28): (0, Keycode.COLON),
#     (29): (0, Keycode.QUOTE),
#     (30): (0, Keycode.COMMA),
#     (31): (0, Keycode.PERIOD),
#     (32): (1, Keycode.RIGHT_SHIFT),
#     (33): (2, Keycode.FN),
#     # bottom row keys, left to right
#     (34): (0, Keycode.LEFT_CONTROL),
#     (35): (0, Keycode.WINDOWS),
#     (36): (0, Keycode.LEFT_ALT),
#     (37): (0, Keycode.SPACEBAR),
#     (38): (0, Keycode.RIGHT_ALT),
#     (39): (0, Keycode.RIGHT_CONTROL)
# }

# shift -> 1
# fn -> 2
# set up boolean flags to use with modifier keys
shift_mod = False 
fn_mod = False

# main loop, runs continuously when rp2040 is powered
# steps 0) through 4) control the keyboard, add any custom code to step 5)
while True:
    # 0) CHECK ALL THE KEYS FOR AN EVENT (KEY PRESS)
    event = keys.events.get()
    
    # 1) IF A KEY IS PRESSED
    if event and event.pressed:
        # 2) CHECK FOR MODIFIER KEYS
        # take the number of the key being pressed (event.key_number)
        # used that as the index for the keymap dictionary
        # retrieve the first element (i.e. [0]) from that dictionary entry
        # check to see if the key pressed is a shift key
        if keymap[event.key_number][0] == 1:
            shift_mod = True 
        # check to see if the key pressed is a fn key
        if keymap[event.key_number][0] == 2:
            fn_mod = True

        # 3) PRINT THE KEY BASED ON MODIFIER STATUS
        # 3a) no modifiers pressed
        if shift_mod == False and fn_mod == False:
            # simply print the key that is being pressed
            kbd.press(keymap[event.key_number][1])

        # 3b) shift pressed
        if shift_mod == True and fn_mod == False:
            # use the correct layer dictionary (i.e. keymap_shift)
            kbd.press(Keycode.SHIFT, keymap_shift[event.key_number][1])

        # 3c) Fn pressed
        if shift_mod == False and fn_mod == True:
            kbd.press(keymap_fn[event.key_number][1])

        # 3d) both pressed
        if shift_mod == True and fn_mod == True:
            kbd.press(Keycode.SHIFT, keymap_fnshift[event.key_number][1])

    # 4) CHECK FOR MODIFIER KEYS BEING RELEASED
    elif event and event.released:
        # reset boolean correspodning to that modifier key
        if keymap[event.key_number][0] == 1:
            shift_mod = False 
        if keymap[event.key_number][0] == 2:
            fn_mod = False 

        # and send the release signal
        kbd.release(keymap[event.key_number][1])


    # 5) ADD ANY CUSTOM CODE USING NEOPIXELS OR GPIO PINS 17-29 HERE!
    # ADD CUSTOM CODE HERE
    # note that if your code has errors and cannot run, your keyboard will not work either
    # best to only use microcontroller functionaity when you have a second keyboard avaliable

