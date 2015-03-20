# download LSL and pylsl from https://code.google.com/p/labstreaminglayer/
# Eg: ftp://sccn.ucsd.edu/pub/software/LSL/SDK/liblsl-Python-1.10.2.zip
# put in "lib" folder (same level as user.py)
import sys; sys.path.append('../lib') # help python find pylsl relative to this example program

from pylsl import StreamInlet, resolve_stream

# Use LSL protocol read PPG data stream
class ReaderLSL():
  def __init__(self, stream_type='PPG'):
    # first resolve said stream type on the network
    streams = resolve_stream('type',stream_type)
    self.nb_streams = len(streams)
    print "Detecting", self.nb_streams, stream_type, "streams"
    
    # create inlets to read from each stream
    self.inlets = []
    for stream in streams:
      self.inlets.append(StreamInlet(stream))
    
    # init list of samples
    self.samples = [] * self.nb_streams

  # retrieve samples from network
  def __call__(self):
    # get a new samples
    i=0
    for inlet in self.inlets:
      sample,timestamp = inlet.pull_sample()
      print i, "--", timestamp, sample
      i=i+1

