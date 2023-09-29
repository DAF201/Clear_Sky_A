
LOGIN = b'^<clearsky><head><ver>v\d\.\d\.\d<ver><id>([0-9a-zA-Z_ ]{2,16})<id><secret>([0-9a-zA-Z_+-=?`~!@#$%^&*]{6,16})<secret><head><clearsky>$'

LOGOUT = b'^<clearsky><tail><id>([0-9a-zA-Z_ ]{2,16})<id><secret>([0-9a-zA-Z_+-=?`~!@#$%^&*]{6,16})<secret><tail><clearsky>$'
