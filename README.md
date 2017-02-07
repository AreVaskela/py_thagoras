# py_thagoras
pythonskripti, joka muuttaa input tiedoston jalkoina olevat luvut metreiksi ja laskee hypotenuusan

Tehty python 2.7.x:llä ja kun python on PATHissa, niin ajoon shellistä "python .\pythagoras.py input.tiedosto output.tiedosto"

Tehtävänanto oli näin, näkyy paremmin tekstieditorissa:

Make a program, which reads from an input file length of legs (A and B) of a right-angled triangle. 
Calculate length of the hypotenuse using Pythagoras’s law (hypotenuse² = legA² + LegB²). Name 
of the input and output file is given as command line arguments.

Constrains:
•Lengths in the input file are foots (1 foot = 0.3048 meters)
•All lengths in the output file must be in meters.
•Number of the rows in the input file varies and overall length of the file is not limited.
•An operation system has not been chosen yet, so application must be implemented so, that it is as easy to port as possible
•Format of the input file is:
legA LegB
5.91 4.51
5.10 6.82

•Format of the output file must be:
legA legB hypotenuse
30.48 30.48 43.1052
•Rows in the output file must be arranged according to the hypotenuse in ascending order.
