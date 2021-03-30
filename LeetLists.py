class LeetLists:
	"""leetspeak to wordlists"""
	def __init__(self):
		self.maps = [{
			"0" : "o",
			"1" : "i",
			"2" : "z",
			"3" : "e",
			"4" : "a",
			"5" : "s",
			"6" : "b",
			"7" : "t",
			"8" : "b",
			"9" : "g",
			"!" : "i",
			"@" : "a",
			"#" : "h",
			"$" : "s",
			"%" : "x",
			"&" : "e",
			"(" : "c",
			"~" : "n",
			"[" : "c",
			"|" : "i"
		},
		{
			"1" : "l",
			"2" : "r",
			"4" : "h",
			"7" : "l",
			"9" : "q",
			"!" : "l",
			"&" : "g",
			"|" : "l"
		}]

	def check_string(self, chk, li):
		"""Check if a compensated string is in a list"""
		if not isinstance(chk, str):
			raise TypeError("arg1 must be a str")
		if not isinstance(li, list):
			raise TypeError("arg2 must be a list of str")
		for i in li:
			if not isinstance(i, str):
				raise TypeError("arg2 must be a list of str")

		for i in range(len(li)):
			li[i] = li[i].lower()
		chk = chk.lower()
		chk = chk.replace(" ","")
		
		if chk in li:
			return True

		sl = list(chk)

		mapIndex, iterable = -1, -1
		for _ in range(len(self.maps) + 1):
			for stringIndex in range(len(sl)):
				if stringIndex > iterable:
					for mi in range(len(self.maps)):
						if sl[stringIndex] in self.maps[mi]:
							placeholder = sl[stringIndex]
							sl[stringIndex] = self.maps[mi].get(sl[stringIndex])
							for item in li:
								if item in "".join(sl):
									return True
							sl[stringIndex] = placeholder
					if mapIndex != -1 and sl[stringIndex] in self.maps[mapIndex]:
						sl[stringIndex] = self.maps[mapIndex].get(sl[stringIndex])
					iterable += 1
			if mapIndex != -1 and sl[stringIndex] in self.maps[mapIndex]:
				sl[stringIndex] = self.maps[mapIndex].get(sl[stringIndex])
			iterable = -1
			mapIndex += 1

		return False