import numpy as np
import re


from calculeNumerique.calcule import Calcule

# DYNAMICALLY NUMPY ARRAY UNDEFINITED
ARRAYS = np.empty((), dtype= np.chararray, order='F')
ARRAYHEXA = np.empty((16), dtype= np.chararray, order='F')
basis_string="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
hexa_string="123456789ABCDEF"
octa_string="12345678";
binary_string="01";



obj_Class=Calcule()



def main():

	i=0

	listGeneralDim=[];

	# ENTER STRING
	userString=enterStringUser();

	# DEFINE DIMENTION OF ARRAY
	# TODO
	obj_Class.buildinList(userString, listGeneralDim);
	obj_Class.buildinList(basis_string, listGeneralDim);
	obj_Class.buildinList(hexa_string, listGeneralDim);

	# RESIZE TO DYNAMICAL ARRAY A MIMIMAL USED (iDim, 15, 10) RANK
	ARRAYSTRING = obj_Class.resizeUndimentionalArray(listGeneralDim, ARRAYS);

	# ASSIGNEMENT HEXA TO ARRAYH
	obj_Class.calculeHexaToArray(hexa_string, ARRAYHEXA)

	# ASSIGNEMENT BASIS TO ARRAYS
	obj_Class.calculeBasisToArray(basis_string, ARRAYSTRING)

	# ASSIGNEMENT ENTERED_STRING TO ARRAYS
	obj_Class.calculeEnteredToArray(userString, ARRAYSTRING)

	# CALCULE zone 51
	decimalFounded=0;

	# characterIndividual=obj_Class.outputCharString(0,userString);

	obj_Class.convertAlphaToDecimal(ARRAYSTRING);


	# ASSIGNEMENT FROM DECIMAL TO HEXA
	obj_Class.tranformDecimalToHexa(ARRAYSTRING,ARRAYHEXA);

	listArray = [];
	# OUTPUT HEXA IN STRING
	listArray = obj_Class.outputOfMatrixForMortels(listArray, ARRAYSTRING);

	userInt = obj_Class.trasformStringToInt(decalageCyrpto(len(listArray)));

	listCrypted=[];

	# CYPTAGE ELEMENTS
	listCrypted=obj_Class.cryptoElementSuliman(userInt, listArray, ARRAYHEXA);
	print(listCrypted);

#ENDDEFMAIN


def enterStringUser():

	bol=True;

	while(bol==True):

		var = input("Please enter something alphanumerique WITHOUT special char: ")

		if(bool(re.search("^(?=.*[a-zA-Z ])[A-Za-z0-9 ]+$",var)) or
				re.search("^(?=.*[0-9 ])[A-Za-z0-9 ]+$",var)):
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




def decalageCyrpto(lenListArray: int)->int:


	varInt=input("Please enter le KEY DECALAGE DE CRYPTAGE CESAER ENTRE 1 ET " +
				 str(lenListArray-1) + "\n");

	return varInt;

# END DECALAGE


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	main()
# END IF