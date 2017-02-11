Scripts for generating ukulele and guitar chord lists used to display chord diagrams along the video lessons featured on the [GuitarStreams website](http://guitarstreams.com/).

## Usage

Create a sorted list of ukulele chords, one chord per line. Currently the ukulele is the default instrument, so no argument needs to be passed to the chord_list.py script.

    ./chord_list.py | sort | less

Create a sorted list of guitar chords, one chord per line. You need to pass guitar as a command line argument.

    ./chord_list.py guitar | sort | less

## Tests

Run tests from the root directory of the project. Currently there are only tests for the ukulele.

    python tests/test_ukulele.py

## Todos

* Generate bar and power chords for the guitar in E and A form
* Guitar chord tests
* Make MAX_FRET a command line argument with 4 as the default
* Merge chord_list.py and chords2json.py and only generate json files
* Turn guitar Chord class into function(s)

## Credits

The code for generating the chord sequences is based on [https://github.com/zimolzak/ukulele](https://github.com/zimolzak/ukulele).