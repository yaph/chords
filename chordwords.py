#!/usr/bin/env python
# -*- coding: utf-8 -*-

pitches = set('abcdefg')

with open('/usr/share/dict/words') as f:
    for line in f.read().splitlines():
        if set(line.lower()) <= pitches:
            print(line)

