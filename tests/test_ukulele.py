#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from os.path import dirname

sys.path.append(dirname(dirname(__file__)))
from chord import Chord


tuning = ['G', 'C', 'E', 'A']

# Ukulele specific tests
c = Chord([0, 0, 0, 3], tuning)
c7 = Chord([0, 0, 0, 1], tuning)
cdim7 = Chord([2, 3, 2, 3], tuning)
caug = Chord([1, 0, 0, 3], tuning)
c9 = Chord([0, 0, 0, 5], tuning)
c9alt = Chord([0, 2, 0, 3], tuning)
dm = Chord([2, 2, 1, 0], tuning)
f = Chord([2, 0, 1, 0], tuning)
gm = Chord([0, 2, 3, 1], tuning)

assert c.notes == ['G', 'C', 'E', 'C']
assert dm.notes == ['A', 'D', 'F', 'A']
assert f.notes == ['A', 'C', 'F', 'A']
assert gm.notes == ['G', 'D', 'G', 'A#']

assert c.chord_type == ''
assert c7.chord_type == '7'
assert cdim7.chord_type == 'dim7'
assert caug.chord_type == 'aug'
assert c9.chord_type == '9'
assert c9alt.chord_type == '9'
assert dm.chord_type == 'm'
assert f.chord_type == ''
assert gm.chord_type == 'm'

assert c.root_note == 'C'
assert c7.root_note == 'C'
assert dm.root_note == 'D'
assert f.root_note == 'F'
assert gm.root_note == 'G'

# Do not assert root tone of a "dim7" because there are four equally
# valid roots. Similarly there are 3 equally valid root notes for "aug".
assert c9.root_note == 'C'
assert c9alt.root_note == 'C'