import numpy as np
#import scipy as sp

#data = np.loadtxt("DogData.txt")
#scipy.io.savemat("data")
def spot(dog):
	pcomp  = np.loadtxt("DogMatrix.txt")
	coeff  = np.matmul(np.transpose(pcomp[1:,0]),dog)
	rating = np.dot(coeff,pcomp[0,0])
	return rating/40



if __name__ == "__main__":
	print(spot(np.array([0.12199731211317869, 6.80409156135084e-05, 0.09506887585027701, 0.24940838665531148, 0.12121258319468693, 0.04203010739639894, 0.37021472131102023])))
	print(spot(np.array([0.12933559562628646, 0.000431463081843903, 0.06281908189197115, 0.12297435607783164, 0.09106757738233524, 0.03209377200810974, 0.5612781585677399])))
