"""
Ortholinear Purple Owl v1.0 KMK Build
"""

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

# =============================================================
# Keyboard Physical Configuration
keyboard.diode_orientation = DiodeOrientation.COL2ROW     ## направление от столбца к строке (от анода к катоду)
keyboard.col_pins = (
    board.GP0,  # col-1 (left)
    board.GP1,
    board.GP2,
    board.GP3,     
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,  # col-14 (right)
)
keyboard.row_pins = (   
    board.GP18,  # row-1 (top)
    board.GP19,
    board.GP20,
    board.GP21,
    board.GP22,  # row-5 (bottom)   
)
keyboard.coord_mapping = [
    0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
    28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
    42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,
                    60, 61, 62,     64, 65,
]

# =============================================================
# Extensions
layers_ext = Layers()

keyboard.modules = [layers_ext]

# =============================================================
# Keymap
_______ = KC.TRNS
XXXXXXX = KC.NO

# Layers
LFN = KC.MO(1)
RFN = KC.MO(2)


keyboard.keymap = [
    [   # Base
        KC.ESC,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.MINUS,  KC.EQUAL,  KC.DEL,  
        KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.LBRC,   KC.RBRC,   KC.BSLS,
        KC.LCTL,  KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,   KC.UP,     KC.ENT,
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.LEFT,   KC.DOWN,   KC.RGHT,
                                                LFN,      KC.LGUI,  KC.SPC,             KC.RALT,  RFN,    
    ],
    [   # Left FN
        KC.TILD,   KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,   KC.F12,  KC.BSPC,
        KC.CAPS,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  KC.GRV,   _______,  _______,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
                                                _______,  _______,  _______,            _______,  _______,
    ],
    [   # Right FN
        KC.TILD,  KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,   KC.F12,   KC.BSPC,
        KC.CAPS,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  KC.GRV,   _______,  _______,
        _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
                                                _______,  _______,  _______,            _______,  _______,
    ],

]

if __name__ == '__main__':
    keyboard.go()
