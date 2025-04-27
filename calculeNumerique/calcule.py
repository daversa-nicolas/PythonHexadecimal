import re

import numpy
import numpy as np

from calculeNumerique.transformsSubroutines import transformsSubroutines

class Calcule:

	# OBJETS CLASS GENERAL
	obj_ClassTransforms = transformsSubroutines()

	# 1EME DIM IS THE RECORDS  ARRAYSTRING CORRESPONDANCE ALPHA 0_RANK _DECIMAL 1_RANK OF 2EME DIM  OUTPUT 3EME DIM TO HEXA CONVERTION
	def calculeBasisToArray(self, basisString, ARRAYS) -> None:

		i=0
		while(i<len(basisString)):

			match=bool(re.search("[a-zA-Z]", basisString[i]))

			#re.search("hi", "abcdefghijkl")
			if (match):

				# ORIGINAL STRING 0 DIM  OF 36 CHARS
				ARRAYS[i][0][0]=basisString[i]
				# NUMBER ASSOCIATED 1 DIM
				ARRAYS[i][1][0]=i+1
				# CONVERTED CHAR IN HEXA i 2 j - 3 DIM

			else:

				ARRAYS[i][0][0]=basisString[i]
				ARRAYS[i][1][0]=basisString[i]

			# END IF

			i = i + 1

		# END WHILE

		#self.listGeneralDim.append(len(basisString))

		return None

	# END DEF

	# ORIGINAL STRING HEXA,OCTA,DOUAL YIN 0 YANG 1 : TAO TO CHING
	# ASSIGNEMENT STRING TO ARRAY DUAL, OCTA, HEXA
	def calculeHexaToArray(self, tempListOfHexas: list,
						   ARRAYH: numpy.chararray) -> None :

		print(tempListOfHexas)

		i=0

		while (i < len(tempListOfHexas)):

			j=0

			while (j < len(tempListOfHexas[i])):

				# ORIGINAL STRING HEXA,OCTA,DOUAL YIN 0 YANG 1 : TAO TO CHING
				# tempListHexa = [hexa_string, octa_string, binary_string]
				# IF bases is 2,8 and 16
				# 16 is hexa so index 0
				# 8 is Octa SO INDEX 1
				# 2 IS DUAL YIN YANG SO 2
				# ASSING TO ARRAYH
				ARRAYH[j][i] = tempListOfHexas[i][j]

				j = j + 1

			# END INNER DO LOOP _ 2

			i = i + 1

		# END DO LOOP _1

		#self.listGeneralDim.append(len(stringHexa))

		return None

	#ENDCALCULE

	# ASSIGNEMENT OF ENTERED STRING TO 2_RANK OF 2EME DIM ARRAYS
	def calculeEnteredToArray(self, stringEnteredNoUpper, ARRAYS) -> None :

		stringEntered = self.obj_ClassTransforms.renderMaj(
			self.obj_ClassTransforms.renderNoSpaces(stringEnteredNoUpper)
		)

		i=0
		while(i<len(stringEntered)):
			ARRAYS[i][2][0]=stringEntered[i]
			i=i+1
		#END WHILE

		#self.listGeneralDim.append(len(stringEntered))

		return None

	#END calculeEntered

	# BUILDING LIST TEMP OF DIM MAX (iDimMax,5,10)
	def buildinList(self, strDim: int, listTempDim) -> None :

		listTempDim.append(len(strDim))

	# END SUBROUTINE

	# SUBROUTINE TO RESIZE UNSIZE ARRAY
	def resizeUndimentionalArray(self, listTempDim, ARRAYS: np.chararray) -> np.chararray:

		maxDim: int=0
		print(maxDim)

		ARRAYS = np.empty((self.dimMaximalEntered(listTempDim), 5, 10), dtype=np.chararray, order='F')

		return ARRAYS

	# END SUBROUTINE

	# FUNCTION TO OUTPUT MINIMAL DIMENSION OF RESIZE ARRAY
	def dimMaximalEntered(self, listGeneralDim: list) -> int:

		# TODO TESITNG
		# print(listGeneralDim)

		return max(listGeneralDim)

	# END FUCNTION


	def convertAlphaToDecimal(self, ARRAYS):

		# obj_calcule = Calcule()

		i=0
		# print(ARRAYS.shape)

		type(ARRAYS)

		#bool= (not (re.search("^[!@#$%&*()_+=|<>?{}\\[\\]~-]+$", vari.decode('utf-8')))
		#	  and vari!='')

		# ITERATION AT LEAST ONE ONCE NOT POSSIBLE IN PYTHON AS FORTRAN, JAVA OR LISP, SO NEED TO
		# FUNCTION verifyElement THAT IS TRUE RETURN AT FIRST END REVERIFIED TO EACH ITERATION AT THE AND OF LOOP
		verifyElement=self.functionIsEmptySpecial(i, (ARRAYS[i][2][0]),
															 ARRAYS)
		# REFACTORING OF PROGRAM
		self.iEmeAlphaMatchTable(i, verifyElement, ARRAYS)

		return None

	# END CONVERT

	def iEmeAlphaMatchTable(self, i: int, verifyElement: bool,
							ARRAYS: np.chararray) -> None:

		while (verifyElement):
			# POUR EXEMPLE ADZ1
			# ENTERED ADZ1 ASSOCIATED STRING 2 DIM
			# ALPHA ASSOCIATED 0 DIM
			# ARRAYS[i][0][0] = basisString[i]
			# NUMBER ASSOCIATED 1 DIM FOR BASIS
			# ARRAYS[i][1][0] = i + 1
			# ALPHA ENTERED ASSIGNED IN 2 DIM FOR ENTERED
			# ARRAYS[i][2][0]
			# ALPHA ENTERED TO DECIMAL POSITION ASSIGNED IN 3 DIM
			# ARRAYS[i][3][0]

			j = 0

			verifyElement = self.functionIsEmptySpecial(j, (ARRAYS[j][0][0]),
														ARRAYS)
			# REFACTORING OF PROGRAM
			self.iemeAlphaMatchJemeDecimal(i, j, verifyElement, ARRAYS)

			i = i + 1
			verifyElement = self.functionIsEmptySpecial(i, (ARRAYS[i][2][0]),
														ARRAYS)

		# END WHILE DO ... INNER LOOP 2

		return None

	# END IEMEALPHAMATCH

	# VERIFY THE CONVERTION THE ALPHA ENTRY TO DECIMAL OUTPUT
	# TRANSFORM ALPHA ENTRY TO POSITION
	def iemeAlphaMatchJemeDecimal(self, iEme: int, jEme: int, verifyElement: bool,
								  ARRAYS: np.chararray) -> None:

		while(verifyElement):

			if (ARRAYS[jEme][0][0]==ARRAYS[iEme][2][0]):

				# IN THE SAME MATRIX EXTRATERRESTRIAL VIMANAS
				# IF FOUNDED CHAR THE DECIMAL IS ASSIGNED IN 3 DIM
				ARRAYS[iEme][3][0]=ARRAYS[jEme][1][0]
				break

			#END IF

			jEme = jEme + 1
			verifyElement = self.functionIsEmptySpecial(jEme, (ARRAYS[jEme][0][0]),
														ARRAYS)

		# END WHILE DO ... INNER LOOP 1

		return None

	# END FUNCTION iemeAlphaMatchJemeDecimal


	# FUNCTION VERIFY EMPTY CHAR
	# RETURN BOOLEAN TRUE IF NOT FOUND EMPTY
	def functionIsEmptySpecial(self, emeElement: int, varElement, ARRAYS: np.chararray) -> bool:

		# TEST
		# varElement=''
		varElementBol=True


		if (varElement is None):

			varElementBol=False

		#END IF

		bool = (varElementBol and varElement != '')

		return bool

	# END FUNCTIONISEMPTY

	#
	# # EVENTUALLY TRANFORM BYTES TO STRING
	# def trasformBytesToString(self, element) -> str:
	#
	# 	if (type(element) == bytes):
	#
	# 		element = element.decode("utf-8")
	#
	# 	# END IF
	#
	# 	return element
	#
	# #END TRANSFORM

	# FONCTION THAT TRANSFORM A POSITIONAL INDEX IN listTemp TO HEXA
	def tranformDecimalToHexa(self, bases: str, ARRAYS: np.chararray, ARRAYH: np.chararray) -> None:

		# obj_calcule = Calcule()

		#TEMP LIST FOR INVERTER
		listTemp=[]
		#del listTemp[:]

		# TESTING NUMBER
		# numberDecimal = 7956
		# numberQuotient = numberDecimal // 16

		# IN THE SAME MATRIX EXTRATERRESTRIAL VIMANAS
		# IF FOUNDED CHAR THE DECIMAL IS ASSIGNED IN 3 DIM
		# ARRAYS[i][3][0] = ARRAYS[j][1][0]

		i=0

		# ITERATION AT LEAST ONE ONCE NOT POSSIBLE IN PYTHON AS FORTRAN, JAVA OR LISP, SO NEED TO
		# FUNCTION verifyElement THAT IS TRUE RETURN AT FIRST END REVERIFIED TO EACH ITERATION AT THE AND OF LOOP
		verifyElement = self.functionIsEmptySpecial(i, (ARRAYS[i][3][0]),
													ARRAYS)
		while(verifyElement):
			#self.trasformStringToInt(self.trasformByteToString(ARRAYS[i][3][0]))
			listTemp = []
			del listTemp[:]
			# self.assignementToListHexa(self.trasformStringToInt(self.trasformByteToString(ARRAYS[i][3][0])), listTemp)
			# TODO BOOLEAN
			firstRecursion=0
			decimalChar: int
			if(type(ARRAYS[i][3][0])==str):
				decimalChar=self.obj_ClassTransforms.trasformStringToInt(ARRAYS[i][3][0])
			elif(type(ARRAYS[i][3][0])==int):
				decimalChar=ARRAYS[i][3][0]

			self.assignementToListHexa(firstRecursion, self.obj_ClassTransforms.trasformStringToInt(bases),
									   decimalChar, listTemp)
			print(listTemp)
			listTemp = self.leaveNullFromList(listTemp)
			print(listTemp)
			# TODO DUMMY
			listTemp = self.listPositionalToHexa(bases, listTemp, ARRAYH)

			j=0
			while (j<len(listTemp)):

				# 3 DIM UTILISED TO ASSIGNEMENT THE j-EME ELEMENT HEXA FINAL CHAR ELEMENT TO iEME CHAR SAISI BY USER
				# THE iEME POSITIONAL HEXA IS ONE BY ONE CHAR INVERTED IN THIRDY DIMENTION
				# Z -> 26 -> TODO
				ARRAYS[i][4][j]=listTemp[len(listTemp)-1-j]
				# print(listTemp[j])

				j=j+1

			# END INNER LOOP 2

			i = i + 1
			verifyElement = self.functionIsEmptySpecial(j, (ARRAYS[i][3][0]),
														ARRAYS)

		# END LOOP 1

		return None

	# ENDTRANSFORMDECIMAL



	# RECURSIVE FUNCTION TO RETURN A LIST OF HEXA CHAR
	# THE APPLICATION IS OPEN TO EXTENSION AND CLOSED TO MODIFICATION
	# THE QUOTIENT IS ELEMENT DUMMY ARGUMENT
	def assignementToListHexa(self, i:int, bases: int, numberDec: int,
							  listTemporary: list) -> str:


		# print(listTemporary)

		obj_calcule = Calcule()
		# TODO USING BOOLEAN BETTER
		#valBolInRecurtion=valBolOutRecursion

		# print(bases)

		# TEMP LIST FOR INVERTER
		numberDecimalRest = numberDec % bases

		# TODO REFACTORING
		if (numberDec==0 and numberDecimalRest ==0):
			if(i==0):
				listTemporary.append(numberDecimalRest)
				return None
			else:
				return None
			# ENS IF
		# END IF

		listTemporary.append(numberDecimalRest)

		numberQuotient = numberDec // bases

		i=i+1

		return listTemporary.append(obj_calcule.assignementToListHexa(i, bases, numberQuotient, listTemporary))

	# END ASSIGNMENTLISTFUCNTION

	# TRANSFORM POSITIONAL TO HEXA

	def decimalRestToHexaChar(self, baseArray: int, rest: int, ARRAYH: np.chararray) -> str:
		# print(baseArray)
		# TODO REFACTORING SEQUENCY CONDITIONAL
		# IF bases is 2,8 and 16
		# 16 is hexa so index 0
		# 8 is Octa SO INDEX 1
		# 2 IS DUAL YIN YANG SO 2
		varRank=0
		if(baseArray == "16"):
			varRank=0
		elif(baseArray == "8"):
			varRank=1
		elif(baseArray == "2"):
			varRank=2
		# END IF
		# TODO TESTING WITH 16
		return ARRAYH[rest][varRank]

	# END DECIMAL

	# THE ELEMENT OF LIST IS THE POSITIONAL HEXA ORIGINAL ET NOT INVERSED
	# DUMMY ARGUMENT BASES HERE
	def listPositionalToHexa(self, baseArray: int, listTempArg: list, ARRAYH: np.chararray) -> list:

		obj_calcule = Calcule()

		i=0

		while(i<len(listTempArg)):

			# DUMMY ARGUMENT BASES HERE
			listTempArg[i]=obj_calcule.decimalRestToHexaChar(baseArray,
															 self.obj_ClassTransforms.trasformStringToInt(listTempArg[i]),
															 ARRAYH)
			# print(listTempArg)
			i = i + 1

		# END WHILE

		return(listTempArg)

	# END LISTPOSIONAL


	# ERASE EMPTY VALUE
	def leaveNullFromList(self, listTemp: list) -> list:

		filteredList=list(filter(lambda v: v is not None, listTemp))

		# OR filtered_list = list(filter(None, original_list))
		# Use remove() to Filter None Values
		#filter(lambda v: v is not None, L)
		return filteredList

	# END LEAVE


	def trasformByteToString(self, varElementByte: bytes) -> str:
		return varElementByte.decode("utf-8")
	# END tranformByteToString

	def trasformByteToInteger(self, varElementByte: bytes) -> int:
		#return int.from_bytes(varElementByte, byteorder='little', signed=False)
		return list(varElementByte)
	# END TRANFORMBYTETOINT

	def outputOfMatrixForMortels(self, arrayList: list, ARRAYS: np.chararray)->list:

		strHexa=""

		i=0

		# ITERATION AT LEAST ONE ONCE NOT POSSIBLE IN PYTHON AS FORTRAN, JAVA OR LISP, SO NEED TO
		# FUNCTION verifyElement THAT IS TRUE RETURN AT FIRST END REVERIFIED TO EACH ITERATION
		# AT THE AND OF LOOP
		verifyElement = self.functionIsEmptySpecial(i, (ARRAYS[i][3][0]),
													ARRAYS)

		while(verifyElement):

			j=0
			verifyElement = self.functionIsEmptySpecial(i, (ARRAYS[i][4][j]),
														ARRAYS)

			strHexa=""
			while (verifyElement):

				strHexa = strHexa + ARRAYS[i][4][j]
				j=j+1
				verifyElement = self.functionIsEmptySpecial(i, (ARRAYS[i][4][j]),
															ARRAYS)

			# END WHILE

			arrayList.append(strHexa)

			i=i+1
			verifyElement = self.functionIsEmptySpecial(i, (ARRAYS[i][3][0]),
													ARRAYS)

		# END WHILE

		print("ARRAY LIST OF ENTERED CHAR TRANSFORMED IN BASES CHOISIE")
		print(arrayList)

		return arrayList

	# END OUTPUT


	# CYRPTAGE FUNCTION
	def cryptoElementSuliman(self, decalageGap: int, listElements: list, ARRAYS: np.chararray) -> list:

		listCrypted=[]
		# TRY FUNCTION PREVIOUS
		i=0
		while (i < len(listElements)):

			if ((i + decalageGap) < len(listElements)):

				listCrypted.insert(i + decalageGap, listElements[i])

			else:

				listCrypted.insert(i - len(listElements) + decalageGap, listElements[i])

			# END IF

			i=i+1

		# END WHILE

		print ("THIS IS THE ARRAY LIST CRYPTED WITH : " + str(decalageGap) + " DECALAGE GAP")
		return listCrypted

	# END CRYPTO

#ENDCLASS