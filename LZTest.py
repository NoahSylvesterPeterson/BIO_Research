from LZCompression import *
from Noise import *

def main(n, startLen, EndLen):
    f = open("Tests_With_Crossed_as_Joint.csv", "w")

    s1 = randomBinary(startLen)
    s2 = randomBinary(startLen)
    add_amount = (EndLen-startLen)//n
    if add_amount<1:
        add_amount = 1
    f.write("length of strings, compression ratio of s1, compression ratio of s2, mutual compression ratio, mutual compression ratio zipped, mutual compression ratio crossed, Compression Ratio half crossed, s1, s2 \n")
    for i in range(n):
        oupt = []
        oupt.append(str(len(s1)))
        oupt.append(str(lzCompression_ratio(s1)))
        oupt.append(str(lzCompression_ratio(s2)))
        oupt.append(str(Mutual_Compression_ratio(s1,s2)))
        oupt.append(str(Mutual_Compression_ratio(s1,s2, zip= True)))
        oupt.append(str(Mutual_Compression_Crossed(s1,s2)))
        oupt.append(str(Mutual_Compression_ratio(s1,s2)))
        oupt.append(s1)
        oupt.append(s2)
        f.write(",".join(oupt) + "\n")
        s1 += randomBinary(add_amount)
        s2 += randomBinary(add_amount)

    f.close()


def main2(n, startLen, EndLen):
    f = open("Tests_With_Crossed_as_Joint.csv", "w")

    s1 = randomBinary(startLen)
    s2 = randomBinary(startLen)
    add_amount = (EndLen-startLen)//n
    if add_amount<1:
        add_amount = 1
    f.write("length of strings, compression ratio of s1, compression ratio of s2, joint compression,Mutual compression ratio, s1, s2 \n")
    for i in range(n):
        oupt = []
        oupt.append(str(len(s1)))
        oupt.append(str(lzCompression_ratio(s1)))
        oupt.append(str(lzCompression_ratio(s2)))
        oupt.append(str(lzCompression_ratio(s1+s2)))
        #s12 = zipper(s1,s2)
        #oupt.append(str(lzCompression_ratio(s12)))
        oupt.append(str(Mutual_Compression_ratio1(s1,s2)))
        #oupt.append(str(Mutual_Compression_ratio(s1,s2, zip= True)))
        oupt.append(s1)
        oupt.append(s2)
        f.write(",".join(oupt) + "\n")
        s1 += randomBinary(add_amount)
        s2 += randomBinary(add_amount)

    f.close()


def CrossedPropertyTest1(n, startLen, EndLen):
    f = open("CrossedPropertyTest.csv", "w")

    s1 = randomBinary(startLen)
    s2 = randomBinary(startLen)
    add_amount = (EndLen-startLen)//n
    if add_amount<1:
        add_amount = 1
    f.write("length of strings, compression ratio of s1, compression ratio of s2 , joint compression , Mutual compression crossed(s1:s1), Mutual compression crossed(s2:s2), Mutual compression crossed(s1:s2), Mutual compression crossed(s1:s2), s1, s2 \n")
    for i in range(n):
        oupt = []
        oupt.append(str(len(s1)))
        oupt.append(str(lzCompression_ratio(s1)))
        oupt.append(str(lzCompression_ratio(s2)))
        oupt.append(str(lzCompression_ratio(s1+s2)))
        oupt.append(str(Mutual_Compression_Crossed(s1,s1)))
        oupt.append(str(Mutual_Compression_Crossed(s1,s2)))
        oupt.append(str(Mutual_Compression_Crossed(s1,s2)))
        oupt.append(str(Mutual_Compression_Crossed(s2,s1)))
        oupt.append(s1)
        oupt.append(s2)
        f.write(",".join(oupt) + "\n")
        s1 += randomBinary(add_amount)
        s2 += randomBinary(add_amount)

    f.close()

def Crossed2PropertyTest(n, startLen, EndLen):
    f = open("Crossed2PropertyTest.csv", "w")

    s1 = randomBinary(startLen)
    s2 = randomBinary(startLen)
    add_amount = (EndLen-startLen)//n
    if add_amount<1:
        add_amount = 1
    f.write("length of strings, compression ratio of s1, compression ratio of s2 , joint compression , Mutual compression crossed2(s1:s1), Mutual compression crossed2(s2:s2), Mutual compression crossed2(s1:s2), Mutual compression crossed2(s2:s1), s1, s2 \n")
    for i in range(n):
        oupt = []
        oupt.append(str(len(s1)))
        oupt.append(str(lzCompression_ratio(s1)))
        oupt.append(str(lzCompression_ratio(s2)))
        oupt.append(str(lzCompression_ratio(s1+s2)))
        oupt.append(str(Mutual_Compression_Crossed2(s1,s1)))
        oupt.append(str(Mutual_Compression_Crossed2(s2,s2)))
        oupt.append(str(Mutual_Compression_Crossed2(s1,s2)))
        oupt.append(str(Mutual_Compression_Crossed2(s2,s1)))
        oupt.append(s1)
        oupt.append(s2)
        f.write(",".join(oupt) + "\n")
        s1 += randomBinary(add_amount)
        s2 += randomBinary(add_amount)

    f.close()



def main3(n, startLen, EndLen):
    f = open("Tests_10_4-2.csv", "w")

    s1 = randomBinary(startLen)
    s2 = randomBinary(startLen)
    add_amount = (EndLen-startLen)//n
    if add_amount<1:
        add_amount = 1
    f.write("length of strings, compression ratio of s1, compression ratio of s2, Mutual compression ratio, Mutual Compresison ratio zipped, Mutual compression ratio with crossed as joint, mutual compression ratio #4, s1, s2 \n")
    for i in range(n):
        oupt = []
        oupt.append(str(len(s1)))
        oupt.append(str(lzCompression_ratio(s1)))
        oupt.append(str(lzCompression_ratio(s2)))
        oupt.append(str(Mutual_Compression_ratio(s1,s2)))
        oupt.append(str(Mutual_Compression_ratio(s1,s2, zip= True)))
        oupt.append(str(Mutual_Compression_ratio1(s1,s2)))
        oupt.append(str(Mutual_Compression_ratio2(s1,s2)))
        oupt.append(s1)
        oupt.append(s2)
        f.write(",".join(oupt) + "\n")
        s1 += randomBinary(add_amount)
        s2 += randomBinary(add_amount)

    f.close()


def ConditiononalCompression_tests(n, startLen, EndLen):
    f = open("ConditiononalCompression_tests.csv", "w")

    s1 = randomBinary(startLen)
    s2 = randomBinary(startLen)
    add_amount = (EndLen-startLen)//n
    if add_amount<1:
        add_amount = 1
    f.write("length of strings, compression ratio of s1, compression ratio of s2, Conditional_Comrpession(s1 s1), Conditional_Comrpession(s2 s2), Conditional_Comrpession(s1 s2), Conditional_Comrpession(s2 s1), Conditional_Comrpession(s1 0s), Conditional_Comrpession(s2 0s), s1, s2 \n")
    for i in range(n):
        oupt = []
        oupt.append(str(len(s1)))
        oupt.append(str(lzCompression_ratio(s1)))
        oupt.append(str(lzCompression_ratio(s2)))
        oupt.append(str(Conditional_Comrpession(s1,s1)))
        oupt.append(str(Conditional_Comrpession(s2,s2)))
        oupt.append(str(Conditional_Comrpession(s1,s2)))
        oupt.append(str(Conditional_Comrpession(s2,s1)))
        oupt.append(str(Conditional_Comrpession(s1,"0"*len(s1))))
        oupt.append(str(Conditional_Comrpession(s2,"0"*len(s2))))
        oupt.append(s1)
        oupt.append(s2)
        f.write(",".join(oupt) + "\n")
        s1 += randomBinary(add_amount)
        s2 += randomBinary(add_amount)

    f.close()



def ConditiononalCompression_Noise_Test(n, startLen, EndLen):
    f = open("ConditiononalCompression_Noise_Test1.csv", "w")

    Os = "0"*startLen
    ls = "1"*startLen
    add_amount = (EndLen-startLen)//n
    if add_amount<1:
        add_amount = 1
    f.write("length of strings, Conditional_Comrpession(0s 0s), Conditional_Comrpession(1s 0s), Conditional_Comrpession(2s 0s), Conditional_Comrpession(5s 0s), Conditional_Comrpession(10s 0s), Conditional_Comrpession(50s 0s) \n")
    for i in range(n):
        s2 = Distortion1(2,Os)
        s5 = Distortion1(5,Os)
        s10 = Distortion1(10,Os)
        s50 = Distortion1(50,Os)
        oupt = []
        oupt.append(str(len(Os)))
        oupt.append(str(Conditional_Comrpession(Os, Os)))
        oupt.append(str(Conditional_Comrpession(ls, Os)))
        oupt.append(str(Conditional_Comrpession(s2, Os)))
        oupt.append(str(Conditional_Comrpession(s5, Os)))
        oupt.append(str(Conditional_Comrpession(s10, Os)))
        oupt.append(str(Conditional_Comrpession(s50, Os)))
        f.write(",".join(oupt) + "\n")
        Os += "0"*add_amount
        ls += "1"*add_amount

    f.close()



def Def1_Noise_Test(n, startLen, EndLen):
    f = open("Def1_Noise_Test1.csv", "w")

    Os = "0"*startLen
    ls = "1"*startLen
    add_amount = (EndLen-startLen)//n
    if add_amount<1:
        add_amount = 1
    f.write("length of strings, Mutual_Compression_ratio(0s 0s), Mutual_Compression_ratio(1s 0s), Mutual_Compression_ratio(2s 0s), Mutual_Compression_ratio(5s 0s), Mutual_Compression_ratio(10s 0s), Mutual_Compression_ratio(50s 0s) \n")
    for i in range(n):
        s2 = Distortion1(2,Os)
        s5 = Distortion1(5,Os)
        s10 = Distortion1(10,Os)
        s50 = Distortion1(50,Os)
        oupt = []
        oupt.append(str(len(Os)))
        oupt.append(str(Mutual_Compression_ratio(Os, Os)))
        oupt.append(str(Mutual_Compression_ratio(ls, Os)))
        oupt.append(str(Mutual_Compression_ratio(s2, Os)))
        oupt.append(str(Mutual_Compression_ratio(s5, Os)))
        oupt.append(str(Mutual_Compression_ratio(s10, Os)))
        oupt.append(str(Mutual_Compression_ratio(s50, Os)))
        f.write(",".join(oupt) + "\n")
        Os += "0"*add_amount
        ls += "1"*add_amount

    f.close()

def Def1_Zipped_Noise_Test_StartwithKB2(n, startLen, EndLen):
    f = open("Def1_Zipped_Noise_Test_StartwithCHAMP2.csv", "w")
    adds = "".join(K_BalancedAphabet(2))*4
    f.write("length of strings, ")
    f.write("lzCompression_ratio(s), ")
    ss = ["s10","s20","s30","s40","s50","s60","s70","s80","s90"]
    fss = ["lzCompression_ratio","Mutual_Compression_ratio","Conditional_Comrpession","Mutual_Compression_ratio2","Mutual_Compression_ratio_Crossed"]
    for fs in fss:
        for s in ss:
            f.write(fs+"("+s+"), ")
    f.write("\n")
    
    sss = ["","","","","","","","",""]
    fss = [Mutual_Compression_ratio,Conditional_Comrpession,Mutual_Compression_ratio2,Mutual_Compression_ratio_Crossed]
    s = ""
    for i in range(n):
        s += adds
        for i in range(9):
            sss[i] += Distortion2(0.1*(i+1),adds)
        oupt = []
        oupt.append(str(len(s)))
        oupt.append(str(lzCompression_ratio(s)))
        for ss in sss:
            oupt.append(str(lzCompression_ratio(ss)))
        for fs in fss:
            for ss in sss:
                oupt.append(str(fs(ss,s)))
        f.write(",".join(oupt) + "\n")

    f.close()

Def1_Zipped_Noise_Test_StartwithKB2(500, 10,10000)