"""


Dimmer switch, 0+ lightbulbs
Table: Brightness of lightbulbs
Light Switch |
Dimmer Level | 5 Watt | 10 Watt | 20 Watt
------------------------------------------

 5           | 0      | 0       | 0 - >  0%
10           | 2.5    | 5       | 10 - > 50%
15           | 5      | 10      | 20 -> 100%

At level '0' is out of range so get error -1
At level '5'  is at 0% capacity of Watt potency, in brightness
At level '6'  is at 10% capacity of Watt potency, in brightness
At level '10' is at 50% capacity of Watt potency, in brightness
At level '11' is at 60% capacity of Watt potency, in brightness
At level '13' is at 80% capacity of Watt potency, in brightness
At level '14' is at 90% capacity of Watt potency, in brightness
At level '15' is at 100% capacity of Watt potency, in brightness
At level '20' is out of range so get error -1
At each level -> increase 10% per unit
"""

MIN_LEVEL = 5
MAX_LEVEL = 15


class Bulb:
	def __init__(self, bulb_id=0, watt=0):
		self.bulb_id = bulb_id
		self.watt = watt
		self.brightness = 0


class DimmerSwitch:
	def __init__(self, min_level=MIN_LEVEL, max_level=MAX_LEVEL):
		self.min_level = min_level
		self.max_level = max_level
		self.bulbs = {}

	def get_brightness(self, curr_level, bulb):
		brightness = - 1
		# If curr_level in range
		if self.min_level <= curr_level <= self.max_level:
			if curr_level <= self.min_level:
				brightness = 0
			else:
				brightness = (curr_level - self.min_level) / (self.max_level - self.min_level) * bulb.watt

		# Store brightness value in object
		bulb.brightness = brightness
		self.bulbs[bulb.bulb_id] = brightness
		return brightness

	def print_bulbs_brightness(self, bulbs, levels):
		for lvl in levels:
			print("Brightness for diff bulbs with Dimmer Switch at Level '" + str(lvl) + "'")
			for bulb in bulbs:
				self.get_brightness(lvl, bulb)
			print(self.bulbs)


bulbs_lst = [Bulb(1, 1), Bulb(2, 2), Bulb(5, 5), Bulb(8, 8), Bulb(9, 9), Bulb(10, 10), Bulb(11, 11), Bulb(12, 12),
			 Bulb(14, 14), Bulb(15, 15), Bulb(16, 16), Bulb(20, 20)]

levels_lst = [0, 5, 6, 10, 11, 13, 14, 15, 20]
dimmer = DimmerSwitch()

dimmer.print_bulbs_brightness(bulbs_lst, levels_lst)
