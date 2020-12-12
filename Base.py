# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 16:12:36 2020

@author: jenpr
"""

"""Base is a container for possible reactions to input and other basic game actions"""

class Base(object):
  def __init__(self, name):
    self.game = None
    self.name = name
    self.verbs = {}
    self.phrases = {}
    self.vars = {}

  def flag(self, f):
    if f in self.vars:
      return self.vars[f]
    else:
      return False

  def set_flag(self, f):
    self.vars[f] = True

  def unset_flag(self, f):
    if f in self.vars:
      del self.vars[f]

  def do_say(self, s):
    self.output( s )
    return True

  def say(self, s):
    return (lambda s: lambda *args: self.do_say(s))(s)

  def do_say_on_noun(self, n, s, actor, noun, words):
    if noun != n:
      return False
    self.output( s)
    return True

  def say_on_noun(self, n, s):
    return (lambda n, s: lambda actor, noun, words: self.do_say_on_noun(n, s, actor, noun, words))(n, s)

  def say_on_self(self, s):
    return (lambda s: lambda actor, noun, words: self.do_say_on_noun(None, s, actor, noun, words))(s)

  def add_verb( self, verb, f ):
    self.verbs[' '.join(verb.split())] = f

  def get_verb( self, verb ):
    c = ' '.join(verb.split())
    if c in self.verbs:
       return self.verbs[c]
    else:
      return None

  def add_phrase(self, phrase, f, requirements = []):
    self.phrases[' '.join(phrase.split())] = (f, set(requirements))

  def get_phrase(self, phrase, things_present):
    phrase = phrase.strip()
    things_present = set(things_present)
    if not phrase in self.phrases:
      return None
    p = self.phrases[phrase]
    if things_present.issuperset(p[1]):
      return p[0]
    return None

  def output(self, text, message_type = 0):
    self.game.output(text, message_type)


# The Game: container for player, locations, robots, animals etc.
class Game(Base):
  def __init__(self, name="Undercover Agent"):
    Base.__init__(self, name)
    self.objects = {}
    self.fresh_location = False
    self.player = None
    self.locations = {}
    

  def set_name(self, name):
    self.name = name

  # add another location to the game
  def add_location(self,  location ):
    location.game = self
    self.locations[location.name] = location
    return location
