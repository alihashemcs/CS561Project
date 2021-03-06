import sys
import math

class SigmoidUnit:
	def __init__(self,w,l):
		self._wi = []
		for i in range(len(w)):
			self._wi.insert(i,w[i])
		self._learningrate = l
		self._in = []
		self._out = 0
		
	
	def linearCombinationInputs(self,x):
		net=0
		for i in range(len(x)):
			net += self._wi[i]*x[i]
		return net
	
	def calculateOutput(self,x):
		y = self.linearCombinationInputs(x)
		y = y*(-1)
		o = math.exp(y)
		o += 1.0
		o = (1.0)/o
		self._out = o
		return o
	
	def updateWeights(self,t,x,err):
		o = calculateOutput(x)
		for i in range(len(x)):
			self._wi[i] += ( err*x[i]*self._learningrate )
		
	def calculateErrorOutputLayer(self,t):
		return (self._out)*(1-self._out)*(t-self._out)
	
	def calculateErrorHiddenLayer(self,wkh,ek):
		e = 0
		for i in range(len(wkh)):
			e += wkh[i]*ek[i]
		return e*self._out*(1-self._out)

def main():
	x = str(sys.argv[1])
	print("Testing the main() test client with command line arguments to test module.")
	print(x)
	#print(linearCombinationInputs([1,2,3],[4,5,6]))
	s = SigmoidUnit([1,1],0.5)
	#print(s.linearCombinationInputs([2,3]))
	print(s.calculateOutput([2,3]))

if __name__ == '__main__' : main()