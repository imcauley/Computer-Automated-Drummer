import instrument

class Kick(instrument.Instrument):
  def __init__(self):
    instrument.Instrument.__init__(self)
    self.sound = 36
    self.duration = 0.25
    self.quarter = 4
    self.play_chance = 90
