# -*- coding: utf-8 -*-
# Code based on https://github.com/zimolzak/ukulele

intervals_type_map = {
    (3, 4, 5): 'm',
    (4, 3, 5): '',
    (4, 3, 3, 2): '7',
    (4, 3, 4, 1): 'maj7',
    (3, 4, 3, 2): 'm7',
    (3, 3, 6): 'dim',
    (4, 4, 4): 'aug',
    (2, 2, 3, 5): '9',
    (5, 2, 5): 'sus',
    (7, 5): '5',
    (3, 3, 3, 3): 'dim7',
    (3, 3, 4, 2): 'm7b5',
    (5, 2, 3, 2): '7sus'
}
pitches = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
pitch_count = len(pitches)


def rotate(L, n=1):
    if len(L) > 1:
        return L[n:] + L[:n]
    return L


class Chord:

    def __init__(self, finger_postions, tuning):
        self.finger_postions = finger_postions
        self.chord_type = None
        self.root_note = None

        # Determine notes from given finger positions.
        self.notes = [pitches[(pitches.index(tuning[i]) + pos) % pitch_count] for i, pos in enumerate(finger_postions)]
        unique_notes = list(set(self.notes))
        unique_notes.sort()
        interval_count = len(unique_notes)

        # Determine chord pichtes and intervals.
        chord_pitches = [pitches.index(unique_notes[i]) for i in range(interval_count)]
        intervals = []
        for i in range(interval_count):
            interval = chord_pitches[(i + 1) % interval_count] - chord_pitches[i]
            if interval < 0:
                interval += pitch_count
            intervals.append(interval)

        # Determine chord name and type.
        for _ in intervals:
            t_intervals = tuple(intervals)
            if t_intervals in intervals_type_map:
                self.chord_type = intervals_type_map[t_intervals]
                self.root_note = unique_notes[0]
                break
            intervals = rotate(intervals)
            unique_notes = rotate(unique_notes)

    @property
    def name(self):
        return '{} {}'.format(self.root_note, self.chord_type).strip()
