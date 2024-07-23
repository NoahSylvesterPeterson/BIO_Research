from math import floor, log2
from itertools import permutations, combinations
from random import randrange, random

def makeBinary_fixed(n,l):
    """returns a string representing an integer in binary"""
    rem = n
    oupt = ""
    for i in range(l):
        #print(2**(l-i-1))
        if rem >= 2**(l-i-1):
            oupt += "1"
            rem -= 2**(l-i-1)
        else:
            oupt += "0"
    return(oupt)
def randomBinary(n):
    """Returns random binary string of length n"""
    oupt = ""
    for i in range(n):
        oupt += str(randrange(0,2))
    return(oupt)


def randomBinary_prob(n,p):
    """Returns random binary string of length n and probiblity p that each charicter will be a zero"""
    oupt = ""
    for i in range(n):
        s = random()
        if s <= p:
            oupt += "0"
        else:
            oupt += "1"
    return(oupt)

#print(randomBinary_prob(10,0.9))

def makeBinary_fixed(n,l):
    """returns a string representing an integer in binary"""
    rem = n
    oupt = ""
    for i in range(l):
        #print(2**(l-i-1))
        if rem >= 2**(l-i-1):
            oupt += "1"
            rem -= 2**(l-i-1)
        else:
            oupt += "0"
    return(oupt)

def makeQuatrinary_fixed(n,l):
    """returns a string representing an integer in quatrinary"""
    oupt = ""
    binary = makeBinary_fixed(n,2**l)

    for i in list(range(0,len(binary),2))[::-1]:
        if binary[i-1]+binary[i] == "00":
            oupt += "0"
        elif binary[i-1]+binary[i] == "01":
            oupt += "1"
        elif binary[i-1]+binary[i] == "10":
            oupt += "2"
        else:
            oupt += "3"
    return(oupt)

def makeBinary(n):
    """returns binary string representation of n"""
    if n == 0:
        return("0")
    l = floor(log2(n)) + 1 
    rem = n
    oupt = ""
    for i in range(l):
        if rem >= 2**(l-i-1):
            oupt += "1"
            rem -= 2**(l-i-1)
        else:
            oupt += "0"

    return(oupt)

def length_for_binary(n):
    """retunrs the lenght a binary string would need to be to encode the number n"""
    if log2(n) % 1 == 0:
        return(floor(log2(n)))
    else:
        return(floor(log2(n))+1)

def MakeBinaryDictionary(lst):
    if len(lst) == 0:
        return({})
    l = length_for_binary(len(lst)) 
    oupt = {}
    for i in range(len(lst)):
        oupt[str(lst[i])] = makeBinary_fixed(i,l)
    return(oupt)


def CHAMP(n):
    oupt = ""
    i = 0
    while len(oupt)< n:
        i += 1
        for j in range(2**i):
            oupt += makeBinary_fixed(j,i)
    oupt = oupt[:n]
    return(oupt)

def CHAMP2(n):
    oupt = ""
    i = 0
    while len(oupt)< n:
        i += 1
        for j in range(4**i):
            oupt += makeQuatrinary_fixed(j,i)
    oupt = oupt[:n]
    oupt1 = ""
    oupt2 = ""
    for i in oupt:
        if i == "0":
            oupt1 += "0"
            oupt2 += "0"
        elif i == "1":
            oupt1 += "1"
            oupt2 += "0"
        elif i == "2":
            oupt1 += "0"
            oupt2 += "1"
        else:
            oupt1 += "1"
            oupt2 += "1"
    return(oupt1,oupt2)

def isInDict(s,d):
    keys = d.keys()
    for key in keys:
        if d[key] == s:
            return((True,key))
    return((False,0))


def lzEncoder(s,  input_dictionary = False, output_dictionary = False):
    """Takes in string S and outputs and ancoded sring"""
    input_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    """ s = input string
            input_aplhabet = alphabet used for sting s
            input_dictionary = optional starting dictionary different from just the alphabet
            output_dictionary = boolian, if true the encoder with output a tuple of the encoded string and the final state of the dictionary
        Takes in string S and outputs and ancoded sring"""
    encode_length = length_for_binary(len(input_alphabet))
    if not input_dictionary:
        dic = MakeBinaryDictionary(input_alphabet)
    else:
        dic = input_dictionary
    oupt = [dic[s[0]]]
    i=1
    curr = s[0]
    while i < len(s):
        old = curr
        curr += s[i]
        
        if not curr in dic.keys():
            if length_for_binary(len(dic)) > encode_length:
                encode_length = length_for_binary(len(dic))
                for j in range(len(dic)):
                    dic[list(dic.keys())[j]] = makeBinary_fixed(j,encode_length)
                dic[curr] = makeBinary_fixed(len(dic),encode_length)

            else:
                dic[curr] = makeBinary_fixed(len(dic),encode_length)
            curr = curr[-1]
            oupt.append(dic[old])
            
        i +=1

    oupt.append(dic[curr])
    if not output_dictionary:
        return(oupt[1:])
    else:
        return(oupt[1:],dic)




def lzDecoder(lst):
    dic = {0:lst[0]}
    oupt = lst[0]
    for ele in lst[1:]:
        if len(ele) > 1:
            enc = int(ele[:len(ele)-1])
            dec = dic[enc] + ele[-1]
        else:
            dec = ele
        oupt = oupt + dec
        dic[len(dic)] = dec
        #print(dic)
    return(oupt)



def zipper(s1,s2):
    oupt = ""
    i = 0
    while i < len(s1):
        oupt = oupt + s1[i]
        if i <len(s2):
            oupt = oupt + s2[i]
        i = i+ 1
    while i< len(s2):
        oupt = oupt + s2[i]
        i = i+ 1
    return(oupt)
#def zipper(s1,s2):
#    """Binary Zipper"""
#    oupt = ""
#    for i in range(len(s1)):
#        oupt += str(int(s1[i])*1 + int(s2[i])*2)
#    return(oupt)

def lzCompression_ratio(s):
    return(len("".join(lzEncoder(s)))/len(s))


def Mutual_Compression_ratio(s1,s2, zip = False):
    if zip:
        s12 = zipper(s1,s2)

    else:
        s12 = s1 + s2
    return(lzCompression_ratio(s1)+lzCompression_ratio(s2)-2*lzCompression_ratio(s12))

def Mutual_Compression_ratio1(s1,s2):
    return(lzCompression_ratio(s1)+lzCompression_ratio(s2)-Conditional_Comrpession(s1,s2))




def Mutual_Compression_Crossed(s1,s2):
    (s1Encoded,s1Dic) = lzEncoder(s1, input_dictionary = False, output_dictionary = True)
    (s2Encoded,s2Dic) = lzEncoder(s2,  input_dictionary = False, output_dictionary = True)

    (s1Encoded2,s1Dic2) = lzEncoder(s1,  input_dictionary = s2Dic, output_dictionary = True)
    (s2Encoded2,s2Dic2) = lzEncoder(s2,  input_dictionary = s1Dic, output_dictionary = True)

    return(
        (len("".join(s1Encoded2)) + len("".join(s2Encoded2)))/(len(s1)+len(s2))# try deviding by n instead of 2n
    )

def Mutual_Compression_ratio_Crossed(s1,s2):
    return(lzCompression_ratio(s1)+lzCompression_ratio(s2)-Mutual_Compression_Crossed(s1,s2))

def Conditional_Comrpession(s2,s1):
    (s1Encoded,s1Dic) = lzEncoder(s1, output_dictionary = True)
    (s12Encoded,s12Dic) = lzEncoder(s2, input_dictionary = s1Dic, output_dictionary = True)
    return(len("".join(s12Encoded))/ len(s1))


def Mutual_Compression_ratio_Conditional(s1,s2):
    return(lzCompression_ratio(s2)-Conditional_Comrpession(s1,s2))

#s1 = "00"*5000
#s2 = "1011"*2500
#print(Mutual_Compression_ratio2(s1,s2))

"""A = ["#","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W", "X", "Y","Z"]
s = "TOBEORNOTTOBEORTOBEORNOT"
(lst,dic) = lzEncoder(s, input_alphabet = A, output_dictionary = True)
print(dic)
for i in lst:
    for key in dic.keys():
        if dic[key] == i:
            print(key)
print(lst)
print(len("".join(lst)))"""



def doubelString(s):
    oupt = ""
    for c in s:
        oupt += c*2
    return(oupt)





#print(list(permutations([1, 2, 3])))

def K_BalancedAphabet(k):
    lst = []
    for i in range(k):
        lst.append("0")
        lst.append("1")
    oupt = []
    for i in list(permutations(lst)):
        c = "".join(i)
        if c not in oupt:
            oupt.append(c)
        
    return(oupt)

#print(K_BalancedAphabet(4))

def SigCHAMP_helper(alp,n,oupt="", lastjoin = []):
    newjoin = []
    for i in lastjoin:
        for j in alp:
            nw = i+j
            oupt += nw
            #print(oupt)
            if len(oupt) >= n:
                return(oupt)
            newjoin.append(nw)
    oupt = SigCHAMP_helper(alp,n,oupt = oupt, lastjoin = newjoin)
    return(oupt)

def SigCHAMP(alp,n):
    oupt=""
    oupt += "".join(alp)
    if len(oupt) >= n:
        return(oupt[:n])
    else:
        oupt = SigCHAMP_helper(alp,n,oupt=oupt, lastjoin = alp)
    return(oupt[:n])
s1 = randomBinary_prob(100000,0.5)





s1 = "Title: The Last StandAct I: The USS Enterprise is on a routine mission to explore a remote planet when they detect a distress signal coming from a nearby starbase. The crew responds to the call and finds that the starbase is under attack by a group of hostile aliens. Captain Kirk and the landing party beam down to assess the situation and plan a strategy to defend the starbase.Act II:As the crew fights off the invading aliens, they discover that the enemy is not just trying to conquer the starbase, but is seeking to destroy it completely. The crew realizes that this attack is part of a larger campaign by the alien race to eradicate all human colonies in the sector. Captain Kirk and his crew must not only defend the starbase but also protect the lives of the civilians who have taken refuge there.Act III:The crew works to fortify the starbase and prepare for the next wave of the enemy's attack. The tension mounts as the crew faces a seemingly insurmountable challenge. As the battle rages on, Captain Kirk orders his crew to hold their ground and protect the starbase at all costs."



#print(lzCompression_ratio(randomBinary_prob(100000,0.5), ia = [0,1]))
#print(SigCHAMP(K_BalancedAphabet(1),10000))
#s1 = SigCHAMP(K_BalancedAphabet(1),1000000)
#s1 = "0"*10000000
#print(lzCompression_ratio(s1, ia = [0,1]))
#s = CHAMP(100000)
#s2 = doubelString(s)
#s = "0"*100
#s = "10" * 10000
#print(lzCompression_ratio(s2))
#print(Mutual_Compression_Crossed2(s2,s2))
#s1 = CHAMP(1000000)
#print(lzCompression_ratio("00011011"*1000))
#print(Conditional_Comrpession(s1,"0"*100000))

#(u,w) = CHAMP2(1000000)
#print(Mutual_Compression_Crossed2(u,w))

#s1 = s2 = "0"*100000
#print(Conditional_Comrpession(s1,s2))
# for next week find plagerisum detection shenangins 
# dynamic programming way of 