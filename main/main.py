import numpy as np
import re


from calculeNumerique.calcule import Calcule

ARRAYSTRING = np.empty((100, 5, 10), dtype= np.chararray, order='F')
ARRAYHEXA = np.empty((16), dtype= np.chararray, order='F')
basis_string="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
hexa_string="123456789ABCDEF"


obj_Class=Calcule()


def main():

	i=0

	# ASSIGNEMENT HEXA TO ARRAYH
	obj_Class.calculeHexaToArray(hexa_string, ARRAYHEXA)

	# ASSIGNEMENT BASIS TO ARRAYS
	obj_Class.calculeBasisToArray(basis_string, ARRAYSTRING)

	# ENTER STRING
	userString=enterStringUser();

	# ASSIGNEMENT ENTERED_STRING TO ARRAYS
	obj_Class.calculeEnteredToArray(userString,ARRAYSTRING)

	# CALCULE zone 51
	decimalFounded=0;

	# characterIndividual=obj_Class.outputCharString(0,userString);

	obj_Class.convertAlphaToDecimal(ARRAYSTRING);


	# ASSIGNEMENT FROM DECIMAL TO HEXA
	obj_Class.tranformDecimalToHexa(ARRAYSTRING,ARRAYHEXA);

	listArray = [];
	# OUTPUT HEXA IN STRING
	listArray = obj_Class.outputOfMatrixForMortels(listArray, ARRAYSTRING);

	print(listArray);

	userInt=decalageCyrpto();

	# CYPTAGE ELEMENTS
	# listArray=obj_Class.cryptoElementSuliman(userInt, listArray, ARRAYHEXA);



#ENDDEFMAIN


def enterStringUser():

	bol=True;

	while(bol==True):

		var = input("Please enter something alphanumerique: ")

		if(bool(re.search("^(?=.*[a-zA-Z])[A-Za-z0-9]+$",var)) or
				re.search("^(?=.*[0-9])[A-Za-z0-9]+$",var)):
			print("OK YOU STRING IS GOOD , BIENVENU dans zone 51 , A BORD D'UN NAVIRE EXTRATERRESTRE \n"
				  "ANCIENT VIMANA POUR FAIRE DE LA RETROINGENIERIER EXACTEMENT COMME BOB LAZAR ET E. SNODWEN : \n"
				  "Elément 115 (applications d’antigravité) \n"
				  "https://www.dailymotion.com/video/x18q4bp \n"
				  "https://www.youtube.com/watch?v=ypHNy2-JC-Q");
			bol=False;
			return var
		else:
			print("YOU STRING IS WRONG: warning re-enter");
		#ENDIF

	# END WHILE
#END enter




def decalageCyrpto()->int:
	varInt=input("Please enter le KEY DECALAGE DE CRYPTAGE CESAER : ");
	return varInt;
# END DECALAGE


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	main()
# END IF