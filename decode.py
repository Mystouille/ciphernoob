import binascii
synthese = [-0.29,0.31,0.456,999,0.94,-0.68,-0.57,-0.063,0.187,-0.37,-0.58,999,1.05,-0.140,0.298,0.243,-0.62,-0.084,1.02,999,0.412,-0.61,0.0290,1.24,-0.19,-0.19,0.60,-0.28,1.07,0.53,0.7,999,0.8,0.52,-0.260,0.6,0.51,-0.50,0.84,-0.53,-0.27,-0.0146,-0.79,-0.48,-0.411,0.4,-0.29,0.186,999,-0.080,0.275,-0.237,-1.80,-0.144,0.209,-0.044,-1.06,999,-0.64,1.0,-0.53,0.69,0.64,0.59,-0.290,0.470,-0.84,0.211,999,999,999,1.90,1.1,-2.02,999,0.302,-0.28,999,-1.14,0.200,0.59,0.154,0.81,-0.22,-1.31,-0.043,0.025,999,-0.16,-0.024,0.342,0.57,-0.19,0.170,-0.244,-0.55,-0.80,0.62,-0.50,0.59,0.61,0.66,-1.0,-0.12,0.61,-0.95,0.1,999,999,-0.24,-0.80,-1.950962968186587E-4,999,0.94,-0.99,0.410,-0.35,0.25,-0.179,999,-0.130,-0.57,-0.319,999,-0.69,-0.036,0.380,0.64,0.116,999,-0.81,0.7,-0.30,-1.62,-0.087,1.14,0.69,-0.27,-1.37,0.168,-0.60,999,-0.2,-0.,-0.130,0.91,0.87,-0.27,-1.06,0.79,-0.37,-0.66,-0.74,0.42,-0.067,-0.3,0.234,-0.38,-0.219,1.43,-0.203,999,-1.09,-0.33,0.28,1.64,0.077,1.05,-0.3,-0.165,-0.53,1.82,0.446,0.281,-0.429,-0.72,0.56,-1.2,999,0.247,0.229,-0.82,0.56,-1.1,-0.357,-0.234,-1.04,0.188,-0.117,0.251,0.7,-0.0,0.50,-0.323,0.216,-0.50,-0.48,-0.289,999,-1.8,999,0.18,0.41,-0.075,999,-0.53,0.205,0.18,1.36,0.65,0.156,0.96,1.06,0.108,0.83,-0.181,-0.47,1.0,-0.225,999,-0.58,0.281,999,0.66,999,1.04,-0.2,0.13,0.68,1.21,0.70,999,-0.78,0.294,-1.53,999,-0.60,0.491,0.325,999,0.9,-0.345,0.0220,1.5,0.246,-0.224,-0.18,1.24,-1.15,0.425,-1.41,-0.0267,0.247,999,0.022,-0.489,0.126,0.299,-0.46,-0.9,999,0.83,-0.110,-0.075,999,0.2,-0.0455,0.227,-0.65,-0.89,0.175,1.3,0.07,0.51,999,0.063,-0.96,1.3,-0.13,999,0.95,-0.64,999,0.189,-0.88,999,-0.56,-0.48,-0.0223,-0.40,0.093,0.77,-0.27,999,-0.66,999,-0.59,0.248,-1.30,1.11,0.291,-1.15,999,0.70,-0.37,0.31,999,0.19,-0.436,0.213,999,-0.27,-0.91,0.102,0.30,999,0.71,-0.83,-0.15,0.44,-0.35,999,-0.79,-0.25,-0.385,-1.97,0.071,-0.93,0.50,-0.076,-0.66,-0.172,0.252,-0.1,0.83,-0.51,-0.156,-0.118,0.290,0.396,0.84,1.40,-0.076,-0.049,-0.51,-0.0565,0.141,0.439,-1.11,0.82,-0.164,1.02,0.8,999,0.75,-0.326,0.26,0.36,0.073,0.249,0.4,0.35,-0.6,0.126,0.0114,999,0.0189,-0.461,0.47,0.370,0.10,0.230,1.875,0.8,0.64,0.240,0.59,0.291,0.13,-1.12,-0.402,-0.311,-0.7,-0.66,-0.81,0.33,0.101,999,0.35,-0.29,-1.02,0.38,-1.89,0.86,0.2,0.73,-0.65,0.398,-0.51,-0.97,0.253,-0.116,999,0.213,0.,-0.66,-0.283,0.41,1.15,-0.70,0.32,1.05,-0.66,-0.17,-0.012,0.65,-0.84,0.286,1.13,0.362,-0.091,0.84,0.66,0.417,0.183,0.,-0.71,1.78,-0.277,999,0.59,0.66,0.0124,0.15,0.196,-0.70,-0.28,-0.95,-0.175,-0.412,-0.22,1.42,0.7,0.63,999,-0.55,0.240,0.37,-0.92,-0.64,-0.124,999,0.10,0.93,0.28,-1.3,0.242,1.55,-0.406,999,-0.74,0.033,-0.45,999,-1.03,999,-0.82,0.066,-0.52,-0.7,-0.133,-0.93,-0.0029,0.0177,0.8,2.1,0.65,-0.098,-0.265,-0.66,0.212,0.075,999,-0.76,0.143,-0.077,0.38,0.4,-0.6,-1.34,-0.0256,0.70,0.3,0.92,0.0167,-0.6,-0.080,0.61,0.52,-1.02,1.88,999,-0.62,-0.50,999,0.7,-0.30,0.54,0.122,0.46,-0.61,0.93,0.60,-0.00633,0.85,-0.378,-0.474,0.224,-0.083,0.62,0.175,0.35,-0.36,-0.83,-0.9,0.226,0.35,999,1.,0.34,-0.58,-1.54,-1.02,0.0178,-0.048,-0.53,-0.486,-0.27,0.018,-0.82,-0.70,0.90,-1.14,-0.327,-0.22,-1.27,0.188,999,-0.8,-0.78,0.62,0.323,-0.109,0.37,-0.348,0.072,999,-0.53,1.17,-1.38,0.62,-0.353,999,0.33,-0.66,0.4,-0.45,-0.439,0.00431,0.338,0.212,-0.72,999,-0.09,0.58,0.55,999,-0.160,0.090,-0.07,1.24,-0.384,0.0560,-0.7,-1.19,-0.4,999,1.23,-0.188,-0.264,0.58,-0.27,-0.97,0.99,-0.073,0.1,-0.261,-0.43,0.88,-0.26,0.303,0.153,-0.51,0.441,1.50,-0.049,-0.177,-1.53,-0.98,-0.420,-0.47,0.51,0.383,-0.73,0.6,1.11,0.91,-0.40,999,0.14,0.32,-0.83,999,-0.84,-0.60,0.377,-0.23,-0.28,-0.34,0.5,-0.0485,-0.474,1.0,0.61,999,0.9,-0.40,-0.5,0.450,999]
syntheseUB = 2.15
syntheseLB = -syntheseUB
syntheseAccuracy = 0.01

authorizedAsciiValues = []
#lower case chars
authorizedAsciiValues.extend(range(97,123))
authorizedAsciiValuesLimited = range(97,123)
#upper case chars
authorizedAsciiValues.extend(range(65,91))
#numbers
authorizedAsciiValues.extend(range(48,58))
#punctuation? why not!
authorizedAsciiValues.extend([33,46,58,59,63])
authorizedAsciiValues

defaultThreshold = 0.5

#different possible conversion methods
def getBit1(b, threshold):
        return "1" if b>threshold else "0"
def getBit2(b, threshold):
        return "1" if abs(b)>threshold else "0"
def getBit3(b, threshold):
    if b>0:
        return "1" if b>threshold else "0"
    else:
        return "0" if b<-threshold else "1"

conversionMethods = [getBit1,getBit2,getBit3]

def gluttonFix(byteStrList, brokenBits, asciiValues):
        #glutton heuristic to find a value of the broken bits giving a letter after conversion, flipping the heavy bits first
        #this is not an exhaustive seach
        n = int(''.join(byteStrList), 2)
        possibleValue = n
        found = False
        for idx in brokenBits:
                possibleByte = byteStrList
                possibleByte[idx] = "1"
                possibleValue = int(''.join(possibleByte), 2)
                if possibleValue in asciiValues:
                        n = possibleValue
                        found = True
                        break
                else:
                        if possibleValue < max(asciiValues):
                                byteStrList = possibleByte 
                        else:
                                possibleByte[idx] = "0"
        return n

def perfectFix(byteStrList, brokenBits, asciiValues):
        #recursive search   
        if not brokenBits:     
                return byteStrList
        for idx in brokenBits:
                possibleByte = byteStrList
                possibleByte[idx] = "1"
                subBrokenBits = brokenBits.copy()
                subBrokenBits = subBrokenBits.remove(idx)
                possibleByte = perfectFix(possibleByte,subBrokenBits, asciiValues)
                possibleValue = int(''.join(possibleByte), 2)
                if possibleValue in asciiValues:
                        return possibleValue
        return byteStrList

def convertSyntheseByte(byteNumList, convertion, threshold = defaultThreshold):
        #fuck yeah lambdas
        byteStrList = [(lambda x: convertion(x, threshold))(num) for num in byteNumList]
        brokenBits = []
        for idx,num in enumerate(byteNumList):
                if num<syntheseLB or num>syntheseUB:
                        brokenBits.append(idx)

        #get the represented int
        n = int(''.join(byteStrList), 2)
        return (byteStrList, n, brokenBits)

def tryFixByteIfNeeded(byteNumList, convertion, asciiValues, dichotomyAccuracy):
        #convert list of 8 synthese numbers into a list of 8 "0" or "1" strings
        byteStrList, n, brokenBits = convertSyntheseByte(byteNumList, convertion)
        byteStrListInitial = byteStrList.copy()
        for idx in brokenBits:
                byteStrListInitial[idx] = "x"
                
        initialByte = ''.join(byteStrListInitial)
        #check if we got a match
        if n in asciiValues:
                return n

        #if not, try to fix according to the brokenBits
        charFound = False
        threshold = defaultThreshold
        upperBound = syntheseUB
        lowerBound = 0
        print("start fixing "+initialByte)
        while not charFound:
                #convert according to current threshold
                byteStrList, n, temp = convertSyntheseByte(byteNumList, convertion, threshold)
                print(''.join(byteStrList)+": "+str(n)+" @ "+str(threshold))
                #maybe fix it if need be
                possibleByte = perfectFix(byteStrList.copy(),brokenBits.copy(),asciiValues)
                n = int(''.join(byteStrList), 2)
                if n in asciiValues:
                        charFound = True
                        break
                else:
                        #dichotomy search the next threshold
                        oldThreshold = threshold
                        if n > max(asciiValues):
                                lowerBound = threshold
                                threshold = (lowerBound + (upperBound-lowerBound)/2)

                        else:   
                                upperBound = threshold
                                threshold = (upperBound - (upperBound-lowerBound)/2)

                        #stop if the dichotomy moves got too small
                        if abs(oldThreshold - threshold) < dichotomyAccuracy/2:
                                break


        #Logging this stuff
        if charFound and brokenBits:
                letter = binascii.unhexlify('%x' % n).decode('ascii')
                print("found "+letter+" out of "+ ''.join(byteStrList))
        else:
                print("Failed to fix "+initialByte)
        #done!
        return n

for convertion in conversionMethods[1:2]:
        letters=[]
        ints=[]
        print(str(convertion))
        for i in range(0,int(len(synthese)/8)):
                byteIntList = []
                #get a pack of 8 bit and reverse them back into little endian format
                byteData=synthese[i*8:i*8+8][::-1]

                #Try to get a letter value from set of 8 numbers
                n = tryFixByteIfNeeded(byteData, convertion, authorizedAsciiValuesLimited, syntheseAccuracy)

                ints.append(n)
                
                try:
                        letter = binascii.unhexlify('%x' % n).decode('ascii')
                        letters.append(letter)
                except:
                        letters.append('%')
        print("".join(letters))
        print(ints)