import numpy

class transformsSubroutines:

	# convert message to uppercase
	def renderMaj(self, strEntered:str) -> str:

		return strEntered.upper();

	# END FUNCTION RENDERMAJ

	# leave spaces message
	def renderNoSpaces(self, strEntered:str) -> str:

		return "".join(strEntered.split());

	# END FUNCTION RENDERMAJ


	def trasformStringToInt(self, varElementString: str) -> int:

		return int(varElementString)

	# END TRANFORMESTRINGTOINT




# END CLASS