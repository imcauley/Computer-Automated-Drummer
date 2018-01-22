import instrument

class Clap(instrument.Instrument):
  def __init__(self):
    instrument.Instrument.__init__(self)
    self.sound = 39
    self.quarter = 4
    self.offset = 3
    self.play_chance = 33
