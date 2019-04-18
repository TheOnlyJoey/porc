Shenanigans BeardComb - Analyzer
================================


Shenanigans BeardComb - Analyzer is based on the work from Python Open Room Correction (PORC)
Required Python dependencies:

    1) Python 3.6
    2) Scientific Python: SciPy, Numpy, & Matplotlib
    3) UI: kivy, kivy-garden (graph, matplotlib)

Measurement
===========

One needs to measure the log-frequency impulse response of your speakers with a 
calibrated Electret Measurement Microphone, e.g. Dayton Audio EMM-6. Software 
such as Room EQ Wizard (REQ), Holm Impulse, or Arta may be used for this purpose:
http://www.hometheatershack.com/roomeq/

Usage
=====

# When using GUI

In development.
Options include loading audio files, real time microphone capture, EQ preset export, png captures and mic/speaker/room preset files.


# When not using GUI

main.py [-h] [--mixed] [-t FILE] [-n NTAPS] [-o OPFORMAT] input_file output_file

    python3 main.py -t tact30f.txt -n 6144 -o bin l48.wav leq48.bin

Use the -h flag for help!

Target Response
===============

The default target curve for PORC is flat. Included in the data directory are a number 
of target curves. Experiment to suit your listening preferences. Use the [-t] flag to load a target
file.

One may also target a flat curve, and then use separate parametric equalization for bass boosting
and other pschoaccoustic preferences. 

For further reference, the B&K House Curve is a good place to start. Read "Relevant loudspeaker 
tests in studios in Hi-Fi dealers' demo rooms in the home etc.," Figure 5:
http://www.bksv.com/doc/17-197.pdf

Mixed-Phase Compensation
==============

To use mixed-phase compensation, one needs to specify the [--mixed] flag. One also needs to modify
the Room Impulse Response (RIR) to remove leading silence (zeros) before the main impulse. You can
easily do this with Audacity or REQ.

Example:

	python3 main.py --mixed -t tact30f.txt -n 6144 -o bin l48.wav leq48.wav
	
Have some patience with this method. The convolution takes a few CPU cycles.

PC Convolution
==============

Suggestions:

Windows (foobar2000 convolver)
Linux (jconvolver w/ jcgui & Jack)

You may need to merge left and right channels into a single stereo .wav 

    sox -M le148.wav req48.wav equalizer.wav


OpenDRC Convolution
===================

Use -o bin flag to set binary 32bit IEEE floating point mono file format output for OpenDRC.