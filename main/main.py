import numpy as np
import re
from calculeNumerique.calcule import Calcule
from calculeNumerique.transformsSubroutines import transformsSubroutines

# DYNAMICALLY NUMPY ARRAY UNDEFINITED
ARRAYS = np.empty((), dtype= np.chararray, order='F')
ARRAYHEXA = np.empty((15, 3), dtype= np.chararray, order='F')
basis_string="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# ARRAY HEXA USING FOR ALL HEXA, OCTA, DUAL YIN 0 YANG 1
hexa_string="123456789ABCDEF"
octa_string="12345678"
binary_string="01"

# PROGRAM TO TRANFORM A STRING CHAR USER IN POSITIONAL  DECIMAL
# AND POSITIONAL DECIMAL IN CHOISIS BASES 2,8 OR 16
# AUTHOR : NICOLAS DAVERSA
# MAIL CONTRIBUTORS : NICOLAVERSA@LIBERO.IT

obj_Class=Calcule()
obj_Transforms=transformsSubroutines()

def main():

	i=0

	listGeneralDim=[]

	# ENTER STRING
	userString=enterStringUser()

	# ENTER BASES FROM USER
	# strBases=outputBases(askingBases())


	# DEFINE DIMENTION OF ARRAY
	# TODO
	obj_Class.buildinList(userString, listGeneralDim)
	obj_Class.buildinList(basis_string, listGeneralDim)
	obj_Class.buildinList(hexa_string, listGeneralDim)

	# RESIZE TO DYNAMICAL ARRAY A MIMIMAL USED (iDim, 15, 10) RANK
	ARRAYSTRING = obj_Class.resizeUndimentionalArray(listGeneralDim, ARRAYS)

	tempListHexa=[hexa_string, octa_string, binary_string]

	# ASSIGNEMENT HEXA,OCTA,DOUAL YIN 0 YANG 1 TO ARRAYH
	obj_Class.calculeHexaToArray(tempListHexa, ARRAYHEXA)

	# ASSIGNEMENT BASIS TO ARRAYS
	obj_Class.calculeBasisToArray(basis_string, ARRAYSTRING)

	# ASSIGNEMENT ENTERED_STRING TO ARRAYS
	obj_Class.calculeEnteredToArray(userString, ARRAYSTRING)

	# CALCULE zone 51

	# characterIndividual=obj_Class.outputCharString(0,userString)

	obj_Class.convertAlphaToDecimal(ARRAYSTRING)


	# ASSIGNEMENT FROM DECIMAL TO HEXA,OCTA,DUAL
	# HERE DUMMY ARGUMENT OF CHOIX IN HEXA,OCTA,DUAL
	obj_Class.tranformDecimalToHexa(ARRAYSTRING,ARRAYHEXA)

	listArray = []
	# OUTPUT HEXA IN STRING
	listArray = obj_Class.outputOfMatrixForMortels(listArray, ARRAYSTRING)

	userInt = obj_Transforms.trasformStringToInt(decalageCyrpto(len(listArray)))

	listCrypted=[]

	# CYPTAGE ELEMENTS
	listCrypted=obj_Class.cryptoElementSuliman(userInt, listArray, ARRAYHEXA)
	print(listCrypted)

#ENDDEFMAIN


def enterStringUser():

	bol=True

	while(bol==True):

		var = input("Please enter something alphanumerique WITHOUT special char: ")

		if(bool(re.search("^(?=.*[a-zA-Z ])[A-Za-z0-9 ]+$",var)) or
				re.search("^(?=.*[0-9 ])[A-Za-z0-9 ]+$",var)):
			print("OK YOU STRING IS GOOD , BIENVENU dans zone 51 , A BORD D'UN NAVIRE EXTRATERRESTRE \n"
				  "ANCIENT VIMANA POUR FAIRE DE LA RETROINGENIERIER EXACTEMENT COMME BOB LAZAR ET E. SNODWEN : \n"
				  "Elément 115 (applications d’antigravité) \n"
				  "https://www.dailymotion.com/video/x18q4bp \n"
				  "https://www.youtube.com/watch?v=ypHNy2-JC-Q")
			bol=False
			return var
		else:
			print("YOU STRING IS WRONG: warning re-enter string")
		#ENDIF

	# END WHILE

#END enter




def decalageCyrpto(lenListArray: int)->str:


	varInt=input("Please enter le KEY DECALAGE DE CRYPTAGE CESAER ENTRE 1 ET " +
				 str(lenListArray-1) + "\n")

	return varInt

# END DECALAGE


# SUROUTINE QUESTIONS BASES
def outputBases(varBases: str) -> str:

	# SWITCH
	match varBases:
		case "hexa":
			return "16"
	match varBases:
		case "binary":
			return "2"
	match varBases:
		case "octa":
			return "8"
	# END SFICTH

	return None

# END FUNCTION

def askingBases()->str:
	varBases = input("Please enter le BASES OF CONVERTION STRING \n"
					 "hexa -> BASE 16 \n"
					 "binary -> BASE 2 \n"
					 "octa -> BASE 8 \n")
	return varBases
# END FONCTION








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	main()
# END IF