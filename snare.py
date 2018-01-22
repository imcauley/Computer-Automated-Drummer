import instrument

class Snare(instrument.Instrument):
  def __init__(self):
    instrument.Instrument.__init__(self)
    self.sound = 38
    self.duration = 0.25
    self.quarter = 4
    self.offset = 2
    self.play_chance = 60
