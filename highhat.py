import instrument

class Highhat(instrument.Instrument):
  def __init__(self):
    instrument.Instrument.__init__(self)
    self.sound = 44
    self.duration = 0.25
    self.quarter = 1
    self.play_chance = 90
