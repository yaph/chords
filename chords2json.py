#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Convert a chord file generated with
# python ukulele.py | sort > ukulele-chords.txt
# to json, see https://github.com/zimolzak/ukulele/

from collections import OrderedDict

import json
import click


# Use an OrderedDict so alphabetical order of chords is retained.
chords = OrderedDict()


@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def main(input, output):
    for line in input.read().splitlines():
        name, seq = line.split('\t')
        name = name.strip().replace(' ', '')
        seq = seq.strip().replace(',', '')
        chords[name] = chords.get(name, []) + [seq]

    json.dump(chords, output)


if __name__ == '__main__':
    main()
