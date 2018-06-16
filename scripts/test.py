import warnings
import pandas as pd
from jazzElements.chord import Chord
from jazzElements.note import Note
from jazzElements.scale import Scale
from jazzElements.progression import Progression
from jazzElements.annotate import annGraph


prg = Progression('|C|F|D7|G7|C|')
prg.annotate()
prg.plot()
print(prg.ann.ann)

"""
todo: fix bar separation
todo: some cadPos arent right e.g. My romance chord 3
"""
"""
Harmonic Analysis of the chord progression
Args:
    key: force a given key (str)

Following WalkThatBass:
http://www.thejazzpianosite.com/jazz-piano-lessons/jazz-chord-progressions/how-to-analyse-a-chord-progression-harmonic-analysis/

Level 1:
- Find the most represented key
- Annotate chords using this key
Level 2:
- Annotate Function: (PD,D,T)
- Annotate Second Level Chords
    Everything before PD-D-T is a Tonic Prolongation (prolongs the tonic without a cadence)
    They can be Substitutions, or Quick Passing Chords
- Look for non-diatonic chords:
    Long period (>1bar): Modulation
    Short Period (.5-1 bar): Passing Chord | Borrowed Chord | Secondary Dominant

Improvisation:
- first level: We can use the relevant mode under each chord, but we change scale all the time
- or in the second level: We use the functionally important chords
then we can go into crazy stuff i.e. side slipping, cycled patterns, chromatic runs etc...
"""
"""
    - Tritone substitution: we can replace a dom7 by a dom7 that is 6halfSteps above the root   
    - Tritone substitution is good on II-V-I because it provides a chromatic root movement   
      e.g. Dm7–G7–CM7 -> Dm7–D♭7–CM gives a downward walking bass   
"""

self=Progression('Misty')
self.annotate(reduce=False)
self.plot('kbd')



ann=annGraph(self.chords)
ann.annotate(reduce=False)
ann.plot()

# The Following should give I IV V/V V I
# fn: T S D D T
# https://www.semanticscholar.org/paper/HarmTrace-%3A-Automatic-functional-harmonic-analysis-Remco/257c1b75d56c7a13975ea0f000a9ba4ff833cd6c/figure/0
# prg = Progression('|C|F|D7|G7|C|')
# prg.annotate()
# prg.plot()
# print(prg.ann.ann)


# PRACTICAL ANALYSIS
# In addition to IIm7-V7-Is created through secondary dominants, many tunes are made up of IIm7-V7-Is with different key centres that may appear to be entirely random or may be related logically:
# Misty: key centres in bridge move down a semitone then a major 3rd
# Autumn Leaves: key centres Bb – Gm (major to relative minor)
# Giant Steps: (key centres move up in major 3rds)


# todo: Not all chords quality can be resolved:



# for c in Chord.chrLst:
#     print(Chord('C' + c).name + '  ' + Chord('C' + c).quality)

# prg=Progression('My Romance')
# prg.annotate(method='graph',model='majKostka',reduce=False)
#
# self=annGraph(prg.chords)
# self.annotate(reduce=False)
# self.plot()






