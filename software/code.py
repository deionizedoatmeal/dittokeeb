import board
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.keys import KC, make_key
from kmk.handlers.sequences import send_string
from kmk.extensions.RGB import RGB
from kmk.extensions.rgb import AnimationModes

# neopixels are controled with KMK's RBG library, but adafruit's neopixel library works too
rgb_ext = RGB(pixel_pin=board.GP0, num_pixels=7, animation_mode=AnimationModes.SWIRL)

# using adafruit:
# import neopixel
# pixels = neopixel.NeoPixel(board.GP0, num_pixels=7, brightness=0.5)

# define the KMK keyboard object
ditto = KMKKeyboard()

# GPIO pins corresponding to columns 
ditto.col_pins = ( 
        board.GP5,
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
)

# GPIO pins corresponding to row 
ditto.row_pins = (
        board.GP1,
	    board.GP2,
	    board.GP3,
	    board.GP4
) 
 
# orientation of the diodes in the matrix
ditto.diode_orientation = DiodeOrientation.ROW2COL

layers = Layers()
ditto.modules = [layers]

# define function key for layer switching
Fn = KC.MO(2)

# run RGB annimation
ditto.extensions.append(rgb_ext)

# define keymaps for each layer
ditto.keymap = [
    # layer 0 (i.e. QWERTY)
    [KC.ESC, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC,
    KC.TAB, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.NO, KC.ENT,
    KC.LSHIFT, KC.NO, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.DOT, KC.RSHIFT, Fn,
    KC.LCTL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.SPC, KC.NO, KC.NO, KC.NO, KC.NO, KC.RALT, KC.RCTL],

    # layer 1 shift (i.e. QWERTY)
    [KC.GRAVE, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC,
    KC.TAB, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.NO, KC.ENT,
    KC.LSHIFT, KC.NO, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.RIGHT_ANGLE_BRACKET, KC.RSHIFT, Fn,
    KC.LCTL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.SPC, KC.NO, KC.NO, KC.NO, KC.NO, KC.RALT, KC.RCTL],

    # layer 2 fn (i.e. 12345)
    [KC.TILDE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.EQUAL,
    KC.CAPSLOCK, KC.A, KC.UP, KC.D, KC.F, KC.G, KC.MINUS, KC.LBRACKET, KC.RBRACKET, KC.SLASH, KC.NO,  KC.BSLASH,
    KC.LSHIFT, KC.NO, KC.LEFT, KC.DOWN, KC.RIGHT, KC.V, KC.SCOLON, KC.QUOTE, KC.COMMA, KC.RIGHT_ANGLE_BRACKET, KC.RSHIFT, Fn,
    KC.LCTL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.SPC, KC.NO, KC.NO, KC.NO, KC.NO, KC.RALT, KC.RCTL],

    # layer 3 fn + shift (i.e. !@#$%)
    [KC.TILDE, KC.EXCLAIM, KC.AT, KC.HASH, KC.DOLLAR, KC.PERCENT, KC.CIRCUMFLEX, KC.AMPERSAND, KC.ASTERISK, KC.LEFT_PAREN, KC.RIGHT_PAREN, KC.NO, KC.PLUS,
    KC.RGB_TOG, KC.A, KC.RGB_VAI, KC.D, KC.F, KC.G, KC.H, KC.LEFT_CURLY_BRACE, KC.RIGHT_CURLY_BRACE, KC.QUESTION, KC.PIPE,
    KC.LSHIFT, KC.NO, KC.Z, KC.RGB_VAD, KC.C, KC.V, KC.COLON, KC.DOUBLE_QUOTE, KC.LEFT_ANGLE_BRACKET, KC.RIGHT_ANGLE_BRACKET, KC.RSHIFT, Fn,
    KC.LCTL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.SPC, KC.NO, KC.NO, KC.NO, KC.NO, KC.RALT, KC.RCTL]
    ]

if __name__ == '__main__':
    # run the keyboard code
    ditto.go()
    
