from math import floor, log2

def lzEncoderAdvanced(s, input_alphabet = [0,1]):
    """ s = input string
        input_aplhabet = alphabet used for sting s, defalted to binary
        input_dictionary = optional starting dictionary different from just the alphabet
        output_dictionary = boolian, if true the encoder with output a tuple of the encoded string and the final state of the dictionary
    Takes in string S and outputs and ancoded sring"""
    encode_length = length_for_binary(len(input_alphabet)) # set the inital encoding lenght to accomidate the inital alphabet

    dic = MakeBinaryDictionary(input_alphabet) # make the inital dictionary using the inital alphabet

    oupt = [dic[s[0]]] # inital encoding must be what we initaly have in the dictionary for the first charicter in s
    i=1
    curr = s[0] #current string which we are looking at
    while i < len(s):
        old = curr 
        curr += s[i]
        
        if not curr in dic.keys(): #if the value is not in the current dictionary then we have to add it, otherwise we just need to keep adding to curr
            if length_for_binary(len(dic)) > encode_length: #Check if we need to update the dictionary to have larger binary strings
                encode_length = length_for_binary(len(dic))
                for j in range(len(dic)): #set all dictionary values to account for increased length of binary string
                    dic[list(dic.keys())[j]] = makeBinary_fixed(j,encode_length)
                dic[curr] = makeBinary_fixed(len(dic),encode_length) #update dictionary to include new value

            else:
                dic[curr] = makeBinary_fixed(len(dic),encode_length)#update dictionary to include new value
            curr = curr[-1] #change current so it is just the newest charicter
            oupt.append(dic[old])# Add the the encoding for the value that we did know
            
        i +=1

    oupt.append(dic[curr])# retreve the last part of the sequence
    return(oupt[1:])




def length_for_binary(n):
    """retunrs the lenght a binary string would need to be to encode the number n"""
    if log2(n) % 1 == 0:
        return(floor(log2(n)))
    else:
        return(floor(log2(n))+1)

def MakeBinaryDictionary(lst):
    """lst =  input alphabet
    Generates starting dictionary with lst as the keys and associated binary stings as the values"""
    if len(lst) == 0: # if our input alphabet is the empty set then we can just return an empty dictionary
        return({})

    l = length_for_binary(len(lst)) # set the length of all the binary strings to be 
    oupt = {}
    for i in range(len(lst)):
        oupt[str(lst[i])] = makeBinary_fixed(i,l) # for each value in the input alphabet make a dictionary entry and a corrisponding binary string
    return(oupt)

def makeBinary_fixed(n,l):
    """returns a string representing an integer n in binary of length l 
    Note: """
    rem = n
    oupt = ""
    for i in range(l):
        if rem >= 2**(l-i-1):
            oupt += "1"
            rem -= 2**(l-i-1)
        else:
            oupt += "0"
    return(oupt)







def lzEncoderAdvanced(s, input_alphabet = [0,1], input_dictionary = False, output_dictionary = False):
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