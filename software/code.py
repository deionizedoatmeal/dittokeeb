import board
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

COLUMNS = 12
ROWS = 4

keys = keypad.KeyMatrix(
    row_pins=(board.D4, board.A3, board.A2, board.A1, board.A0),
    column_pins=(board.D13, board.D12, board.D11, board.D10, board.D9),
    columns_to_anodes=False,
)

kbd = Keyboard(usb_hid.devices)

keycode_LUT = [
             0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11,
             12, 13, 14, 15, 16, 17, 18, 20,
             21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
             33, 34, 35, 36, 37, 38
]

# create a keycode dictionary including modifier state and keycodes
keymap = {
            # top row keys, left to right
            (0): (0, Keycode.ESCAPE),
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
            (13): (0, Keycode.A,
            (14): (0, Keycode.S),
            (15): (0, Keycode.D),
            (16): (0, Keycode.F),
            (17): (0, Keycode.G),
            (18): (0, Keycode.H),
            (19): (0, Keycode.J),
            (20): (0, Keycode.K),
            (21): (0, Keycode.L)
            (21): (0, Keycode.ENTER)

            # 3rd row keys, left to right
            (22): (1, Keycode.LEFT_SHIFT),
            (23): (0, Keycode.Z),
            (24): (0, Keycode.X),
            (25): (0, Keycode.C),
            (26): (0, Keycode.V),
            (27): (0, Keycode.B),
            (28): (0, Keycode.N),
            (29): (0, Keycode.M),
            (30): (0, Keycode.RIGHT_BRACKET),
            (31): (1, Keycode.RIGHT_SHIFT),
            (32): (4, Keycode.FN),

            # bottom row keys, left to right
            (33): (2, Keycode.LEFT_CONTROL)
            (34): (0, Keycode.WINDOWS)
            (35): (3, Keycode.LEFT_ALT)
            (36): (0, Keycode.SPACEBAR)
            (37): (3, Keycode.RIGHT_ALT)
            (38): (2, Keycode.RIGHT_CONTROL)
}

shift_mod = True
fn_mod = True
ctrl_mod = False


while True:
    key_event = keys.events.get()
    if key_event:
        if key_event.pressed:
            if keymap[keycode_LUT.index(key_event.key_number)][0] == 1:
                shift_mod = True
            elif keymap[keycode_LUT.index(key_event.key_number)][0] == 2:
                ctrl_mod = True
            if shift_mod is False and ctrl_mod is False:
                kbd.press(keymap[keycode_LUT.index(key_event.key_number)][1])
                print(keymap[keycode_LUT.index(key_event.key_number)][1])
            elif shift_mod is True and ctrl_mod is False:
                kbd.press(Keycode.SHIFT, keymap[keycode_LUT.index(key_event.key_number)][1])
                print(keymap[keycode_LUT.index(key_event.key_number)][1])
            elif shift_mod is False and ctrl_mod is True:
                kbd.press(Keycode.CONTROL, keymap[keycode_LUT.index(key_event.key_number)][1])
                print(keymap[keycode_LUT.index(key_event.key_number)][1])
            elif shift_mod is True and ctrl_mod is True:
                kbd.press(
                          Keycode.SHIFT,
                          Keycode.CONTROL,
                          keymap[keycode_LUT.index(key_event.key_number)][1]
                          )
                print(keymap[keycode_LUT.index(key_event.key_number)][1])

        if key_event.released:
            if keymap[keycode_LUT.index(key_event.key_number)][0] == 1:  # un-shift
                shift_mod = False
            elif keymap[keycode_LUT.index(key_event.key_number)][0] == 2:  # un-ctrl
                ctrl_mod = False

            kbd.release(keymap[keycode_LUT.index(key_event.key_number)][1])

