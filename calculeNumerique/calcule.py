import re

import numpy;

from calculeNumerique.transformsSubroutines import transformsSubroutines;

class Calcule:

	# OBJETS CLASS GENERAL
	obj_ClassTransforms = transformsSubroutines();

	# GENERAL LIST FOR MINIMAL DIMENTION
	listGeneralDim=[];

	# 1EME DIM IS THE RECORDS ; ARRAYSTRING CORRESPONDANCE ALPHA 0_RANK _DECIMAL 1_RANK OF 2EME DIM ; OUTPUT 3EME DIM TO HEXA CONVERTION
	def calculeBasisToArray(self, basisString, ARRAYS) -> None:

		i=0;
		while(i<len(basisString)):

			match=bool(re.search("[a-zA-Z]", basisString[i]))

			#re.search("hi", "abcdefghijkl")
			if (match):

				# ORIGINAL STRING 0 DIM
				ARRAYS[i][0][0]=basisString[i]
				# NUMBER ASSOCIATED 1 DIM
				ARRAYS[i][1][0]=i+1
				# CONVERTED CHAR IN HEXA i 2 j - 3 DIM

			else:

				ARRAYS[i][0][0]=basisString[i]
				ARRAYS[i][1][0]=basisString[i]

			# END IF

			i = i + 1;

		# END WHILE

		self.listGeneralDim.append(len(basisString));

		return None;

	# END DEF


	def calculeHexaToArray(self, stringHexa, ARRAYH) -> None :

		i=0;
		while (i < len(stringHexa)):


			# ORIGINAL STRING
			ARRAYH[i] = stringHexa[i]
			i = i + 1;

		# END WHILE

		self.listGeneralDim.append(len(stringHexa));

		return None;

	#ENDCALCULE

	# ASSIGNEMENT OF ENTERED STRING TO 2_RANK OF 2EME DIM ARRAYS
	def calculeEnteredToArray(self, stringEnteredNoUpper, ARRAYS) -> None :

		stringEntered = self.obj_ClassTransforms.renderMaj(stringEnteredNoUpper);

		i=0;
		while(i<len(stringEntered)):
			ARRAYS[i][2][0]=stringEntered[i];
			i=i+1;
		#END WHILE

		self.listGeneralDim.append(len(stringEntered));

		return None;

	#END calculeEntered

	# FUNCTION TO OUTPUT MINIMAL DIMENSION OF RESIZE ARRAY
	def dimMinimalEntered(self, listGeneralDim: list) -> int:
		# TODO TESITNG
		return min(listGeneralDim);

	# END FUCNTION

	# SUBROUTINE RETURN VOID
	def convertAlphaToDecimal(self, ARRAYS):

		# obj_calcule = Calcule()

		i=0
		# print(ARRAYS.shape);

		type(ARRAYS);

		#bool= (not (re.search("^[!@#$%&*()_+=|<>?{}\\[\\]~-]+$", vari.decode('utf-8')))
		#	  and vari!='')

		# ITERATION AT LEAST ONE ONCE NOT POSSIBLE IN PYTHON AS FORTRAN, JAVA OR LISP, SO NEED TO
		# FUNCTION verifyElement THAT IS TRUE RETURN AT FIRST END REVERIFIED TO EACH ITERATION AT THE AND OF LOOP
		verifyElement=self.functionIsEmptySpecial(i, (ARRAYS[i][2][0]),
															 ARRAYS);
		# REFACTORING OF PROGRAM
		self.iEmeAlphaMatchTable(i, verifyElement, ARRAYS);

		# while(verifyElement):
		#
		# 	# POUR EXEMPLE ADZ1
		# 	# ENTERED ADZ1 ASSOCIATED STRING 2 DIM
		# 	# ALPHA ASSOCIATED 0 DIM
		# 	# ARRAYS[i][0][0] = basisString[i]
		# 	# NUMBER ASSOCIATED 1 DIM FOR BASIS
		# 	# ARRAYS[i][1][0] = i + 1
		# 	# NUMBER ASSIGNED IN 3 DIM FOR ENTERED
		# 	# ARRAYS[i][3][0]
		#
		# 	j=0;
		#
		# 	verifyElement=self.functionIsEmptySpecial(j, (ARRAYS[j][0][0]),
		# 											  ARRAYS);
		# 	# REFACTORING OF PROGRAM
		# 	self.iemeAlphaMatchJemeDecimal(i, j, verifyElement, ARRAYS);
		#
		# 	i = i + 1;
		# 	verifyElement=self.functionIsEmptySpecial(i, (ARRAYS[i][2][0]),
		# 											  ARRAYS);
		#
		# #END WHILE DO ... INNER LOOP 2

		return None;

	# END CONVERT

	def iEmeAlphaMatchTable(self, i: int, verifyElement: bool,
							ARRAYS: numpy.chararray) -> None:

		while (verifyElement):
			# POUR EXEMPLE ADZ1
			# ENTERED ADZ1 ASSOCIATED STRING 2 DIM
			# ALPHA ASSOCIATED 0 DIM
			# ARRAYS[i][0][0] = basisString[i]
			# NUMBER ASSOCIATED 1 DIM FOR BASIS
			# ARRAYS[i][1][0] = i + 1
			# NUMBER ASSIGNED IN 3 DIM FOR ENTERED
			# ARRAYS[i][3][0]

			j = 0;

			verifyElement = self.functionIsEmptySpecial(j, (ARRAYS[j][0][0]),
														ARRAYS);
			# REFACTORING OF PROGRAM
			self.iemeAlphaMatchJemeDecimal(i, j, verifyElement, ARRAYS);

			i = i + 1;
			verifyElement = self.functionIsEmptySpecial(i, (ARRAYS[i][2][0]),
														ARRAYS);

		# END WHILE DO ... INNER LOOP 2

		return None;

	# END IEMEALPHAMATCH

	# VERIFY THE CONVERTION THE ALPHA ENTRY TO DECIMAL OUTPUT
	def iemeAlphaMatchJemeDecimal(self, iEme: int, jEme: int, verifyElement: bool,
								  ARRAYS: numpy.chararray) -> None:

		while(verifyElement):

			if (ARRAYS[jEme][0][0]==ARRAYS[iEme][2][0]):

				# IN THE SAME MATRIX EXTRATERRESTRIAL VIMANAS
				# IF FOUNDED CHAR THE DECIMAL IS ASSIGNED IN 3 DIM
				ARRAYS[iEme][3][0]=ARRAYS[jEme][1][0];
				break;

			#END IF

			jEme = jEme + 1;
			verifyElement = self.functionIsEmptySpecial(jEme, (ARRAYS[jEme][0][0]),
														ARRAYS);

		# END WHILE DO ... INNER LOOP 1

		return None;

	# END FUNCTION iemeAlphaMatchJemeDecimal


	# FUNCTION VERIFY EMPTY OR CHAR SPECIAL
	# RETURN BOOLEAN TRUE IF NOT FOUND EMPTY OR SPECIAL
	def functionIsEmptySpecial(self, emeElement: int, varElement, ARRAYS: numpy.chararray) -> bool:
		# TEST
		# varElement='';
		varElementBol=True;


		if (varElement is None):

			varElementBol=False;

		#END IF

		# else:
		# strVar = varElement;
		# END I+F

		# IF ELEMENT IS BYTES, IT S MORE% THAN ONE CHAR PROBALBLT 99/100
		# if len(strVar) > 1:
		#
		# 	varElementBol = False;
		#
		# # END IF

		bool = (varElementBol and varElement != '')

		return bool;

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
	# 	return element;
	#
	# #END TRANSFORM

	def tranformDecimalToHexa(self, ARRAYS: numpy.chararray, ARRAYH: numpy.chararray) -> None:

		# obj_calcule = Calcule()

		#TEMP LIST FOR INVERTER
		listTemp=[];
		#del listTemp[:];

		# TESTING NUMBER
		# numberDecimal = 7956
		# numberQuotient = numberDecimal // 16;

		# IN THE SAME MATRIX EXTRATERRESTRIAL VIMANAS
		# IF FOUNDED CHAR THE DECIMAL IS ASSIGNED IN 3 DIM
		# ARRAYS[i][3][0] = ARRAYS[j][1][0];

		i=0;

		# ITERATION AT LEAST ONE ONCE NOT POSSIBLE IN PYTHON AS FORTRAN, JAVA OR LISP, SO NEED TO
		# FUNCTION verifyElement THAT IS TRUE RETURN AT FIRST END REVERIFIED TO EACH ITERATION AT THE AND OF LOOP
		verifyElement = self.functionIsEmptySpecial(i, (ARRAYS[i][3][0]),
													ARRAYS);
		while(verifyElement):
			#self.trasformStringToInt(self.trasformByteToString(ARRAYS[i][3][0]))
			listTemp = [];
			del listTemp[:];
			# self.assignementToListHexa(self.trasformStringToInt(self.trasformByteToString(ARRAYS[i][3][0])), listTemp);
			self.assignementToListHexa(self.trasformStringToInt(ARRAYS[i][3][0]), listTemp);
			# print(listTemp);
			listTemp = self.leaveNullFromList(listTemp);
			# print(listTemp);
			listTemp = self.listPositionalToHexa(listTemp, ARRAYH);

			j=0;
			while (j<len(listTemp)):

				# 3 DIM UTILISED TO ASSIGNEMENT THE j-EME ELEMENT HEXA FINAL CHAR ELEMENT TO iEME CHAR SAISI BY USER
				# Z -> 26 -> TODO
				ARRAYS[i][4][j]=listTemp[len(listTemp)-1-j];
				# print(listTemp[j]);

				j=j+1;

			# END INNER LOOP 2

			i = i + 1;
			verifyElement = self.functionIsEmptySpecial(j, (ARRAYS[i][3][0]),
														ARRAYS);

		# END LOOP 1

		return None;

	# ENDTRANSFORMDECIMAL

	# RECURSIVE FUNCTION TO RETURN A LIST OF HEXA CHAR
	# THE QUOTIENT IS ELEMENT DUMMY ARGUMENT
	def assignementToListHexa(self, numberDec: int, listTemporary: list) -> str:

		obj_calcule = Calcule();
		i=0;

		# TEMP LIST FOR INVERTER
		numberDecimalRest = numberDec % 16

		if (numberDec == 0):

			return None;

		# END IF

		listTemporary.append(numberDecimalRest)

		numberQuotient = numberDec // 16;

		return listTemporary.append(obj_calcule.assignementToListHexa(numberQuotient, listTemporary));

	# END ASSIGNMENTLISTFUCNTION

	# TRANSFORM POSITIONAL TO HEXA
	def decimalRestToHexaChar(self, rest, ARRAYH: numpy.chararray) -> str:

		return ARRAYH[rest-1];

	# END DECIMAL

	# THE ELEMENT OF LIST IS THE POSITIONAL HEXA
	def listPositionalToHexa(self, listTempArg: list, ARRAYH: numpy.chararray) -> list:

		obj_calcule = Calcule();

		i=0;

		while(i<len(listTempArg)):

			listTempArg[i]=obj_calcule.decimalRestToHexaChar(listTempArg[i], ARRAYH);
			# print(listTempArg);
			i = i + 1;

		# END WHILE

		return(listTempArg);

	# END LISTPOSIONAL


	# ERASE EMPTY VALUE
	def leaveNullFromList(self, listTemp: list) -> list:

		filteredList=list(filter(lambda v: v is not None, listTemp));

		# OR filtered_list = list(filter(None, original_list))
		# Use remove() to Filter None Values
		#filter(lambda v: v is not None, L)
		return filteredList;

	# END LEAVE


	def trasformByteToString(self, varElementByte: bytes) -> str:
		return varElementByte.decode("utf-8");
	# END tranformByteToString

	def trasformByteToInteger(self, varElementByte: bytes) -> int:
		#return int.from_bytes(varElementByte, byteorder='little', signed=False);
		return list(varElementByte);
	# END TRANFORMBYTETOINT


	def trasformStringToInt(self, varElementString: str) -> int:

		return int(varElementString);

	# END TRANFORMESTRINGTOINT


	def outputOfMatrixForMortels(self, arrayList: list, ARRAYS: numpy.chararray)->list:

		strHexa="";

		i=0;

		# ITERATION AT LEAST ONE ONCE NOT POSSIBLE IN PYTHON AS FORTRAN, JAVA OR LISP, SO NEED TO
		# FUNCTION verifyElement THAT IS TRUE RETURN AT FIRST END REVERIFIED TO EACH ITERATION AT THE AND OF LOOP
		verifyElement = self.functionIsEmptySpecial(i, (ARRAYS[i][3][0]),
													ARRAYS);

		while(verifyElement):

			j=0;
			verifyElement = self.functionIsEmptySpecial(i, (ARRAYS[i][4][j]),
														ARRAYS);

			strHexa="";
			while (verifyElement):

				strHexa = strHexa + ARRAYS[i][4][j];
				j=j+1;
				verifyElement = self.functionIsEmptySpecial(i, (ARRAYS[i][4][j]),
															ARRAYS);

			# END WHILE

			arrayList.append(strHexa);

			i=i+1;
			verifyElement = self.functionIsEmptySpecial(i, (ARRAYS[i][3][0]),
													ARRAYS);

		# END WHILE

		print(arrayList);

		return arrayList;

	# END OUTPUT


	# CYRPTAGE FUNCTION
	def cryptoElementSuliman(self, decalageGap: int, listElements: list, ARRAYS: numpy.chararray) -> list:

		listCrypted=[];
		# TRY FUNCTION PREVIOUS
		i=0;
		while (i < len(listElements)):

			if ((i + decalageGap) < len(listElements)):

				listCrypted.insert(i + decalageGap, listElements[i]);

			else:

				listCrypted.insert(i - len(listElements) + decalageGap, listElements[i]);

			# END IF

			i=i+1;

		# END WHILE

		print ("THIS IS THE ARRAY LIST CRYPTED WITH : " + str(decalageGap) + " DECALAGE GAP");
		return listCrypted;

	# END CRYPTO

#ENDCLASS