import random

class Instrument:
  def __init__(self):
      self.duration = 0.75
      self.volume = 100
      self.offset = 0
      self.play_chance = 100
      self.random_play = 8

  def play(self, beat):
    beat = beat * 4
    will_play = random.randint(0,100)
    if(beat % self.quarter == (0 + self.offset)):
        if(will_play < self.play_chance):
            return True

    if(random.randint(0,100) < self.random_play):
        return True

    return False
