#!/usr/bin/env python
# -*- coding: utf-8 -*-
# usage: ./chord_list.py | sort | less
import sys
import itertools

from chord import Chord


MAX_FRET = 4

tunings = {
    'guitar': ['E', 'A', 'D', 'G', 'B', 'E'],
    'ukulele': ['G', 'C', 'E', 'A']
}

tuning = tunings['ukulele']
if len(sys.argv) > 1 and sys.argv[1] == 'guitar':
    tuning = tunings['guitar']

# Print all finger positions from 0 to max fret for identified chords.
for finger_postions in itertools.product(range(0, MAX_FRET + 1), repeat=len(tuning)):
    c = Chord(finger_postions, tuning)
    if not c.root_note:
        continue

    pos = ','.join(map(str, finger_postions))
    print('{}\t{}'.format(c.name, pos))
