def ReadFromFASTA(filename, Discriptor = False):
    """Reads from fasta file then outputs only the sequence as an unbroken string
        discriptor: tells funciton wheather or not to includ the discriptor """
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    discriptor = lines[0]
    lines  = lines[1:]
    
    stringSeq = "".join(lines)
    stringSeq = stringSeq.replace("\n","")
    if Discriptor:
        return((discriptor,stringSeq))
    else:
        return(stringSeq)


def ReadMultiFromFASTA(filename, Discriptor = False):
    """Reads from fasta file then outputs only the sequence as an unbroken string
        discriptor: tells funciton wheather or not to includ the discriptor """
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    if Discriptor:
        oupt = {}
    else:
        oupt = []
    
    currseq = [lines[0]]
    lines.append(">")
    for line in lines[1:]:
        if line[0] == ">":
            discriptor = currseq[0][1:-1]
            currseq = currseq[1:]
            stringSeq = "".join(currseq)
            stringSeq = stringSeq.replace("\n","")

            
            if Discriptor:
                oupt[discriptor] = stringSeq
            else:
                oupt.append(stringSeq)
            currseq = [line]
        else:
            currseq.append(line)
    return(oupt)


def WrightSequenceToFASTA(filename, Description = "", Sequence = "", lineSize = 60):
    """Prints a description and sequence to a file
    filename: String, Name of the File
    Desciption: String, discription of the file, will have \n added to it before it is printed 
    Sequence: String or list of strings, the body of what will be written
    lineSize: number of charicters on each line, i.e number of charicters befor it puts an \n. Only applicable if Sequence is a string
    
    """
    f = open(filename, "w")
    if Description != "":
        f.write(Description + "\n")
    
    if type(Sequence) == type(""):
        if not lineSize:
            f.write(Sequence)
        else:
            number_of_lines = len(Sequence) // lineSize + 1
            line_begin = 0
            line_end = lineSize
            for i in range(number_of_lines):
                line_begin = i * lineSize
                line_end = (i+1)*lineSize
                f.write(Sequence[line_begin:line_end] + "\n")
            #if line_begin < len(Sequence):
            #    f.write(Sequence[line_begin:len(Sequence)] + "\n")
    else:
        for line in Sequence:
            f.write(line + "\n")
    f.close()

def DNAtoRNA(s, upper = True, outputUpper = True, reverse = False):
    """ Converts DNA sequence to RNA sequence
    s: DNA sequence to be converted
    upper: tells function if the values it will receve will be upper case
    outputUpper: tells function if the values it returns should be upper case
    reverse: tells function to reverse the output
    """
    dic = {"A":"A", "T":"U", "G":"G", "C":"C"}
    oupt = Conversion(dic, s, upper = upper, outputUpper = upper)

    if reverse:
        return(oupt[::-1])
    else:
        return(oupt)


def RNAtoDNA(s, upper = True, outputUpper = True, reverse = False):
    """ Converts RNA sequence to DNA sequence
    s: DNA sequence to be converted
    upper: tells function if the values it will receve will be upper case
    outputUpper: tells function if the values it returns should be upper case
    reverse: tells function to reverse the output
    """
    dic = {"A":"A", "U":"T", "G":"G", "C":"C"}
    oupt = Conversion(dic, s, upper = upper, outputUpper = upper)

    if reverse:
        return(oupt[::-1])
    else:
        return(oupt)


def DNAtoDNA(s, upper = True, outputUpper = True, reverse = False):
    """ Converts DNA sequence its complement strand 
    s: DNA sequence to be converted
    upper: tells function if the values it will receve will be upper case
    outputUpper: tells function if the values it returns should be upper case
    reverse: tells function to reverse the output
    """
    dic = {"A":"T", "T":"A", "C":"G", "G":"C"}
    oupt = Conversion(dic, s, upper = upper, outputUpper = upper)

    if reverse:
        return(oupt[::-1])
    else:
        return(oupt)

def RNAtoRNA(s, upper = True, outputUpper = True, reverse = False):
    """ Converts RNA sequence its complement strand 
    s: RNA sequence to be converted
    upper: tells function if the values it will receve will be upper case
    outputUpper: tells function if the values it returns should be upper case
    reverse: tells function to reverse the output
    """
    dic = {"A":"U", "U":"A", "C":"G", "G":"C"}
    oupt = Conversion(dic, s, upper = upper, outputUpper = upper)

    if reverse:
        return(oupt[::-1])
    else:
        return(oupt)



def ReverseStrint(s):
    return(s[::-1])



def Conversion(dic, s, upper = True, outputUpper = True):
    """maps a string into a new string using a dictinary
    dic: mapping dicionary 
    s: string to be converted
    upper: tells function if the values it will receve will be upper case
    outputUpper: tells function if the values it returns should be upper case
    """
    if upper:
        s = s.upper()
    oupt = ""
    for i in s:
        oupt += dic[i]
    if not outputUpper:
        oupt = oupt.lower()
    return(oupt)





def DNAtoAA(s,upper = True, joiner = "", outputUpper = True):
        """Turns DNA sequnce into the Ameno Acid sequence
        s: input sequence
        upper: tells function wheather input string is in upper case or lowercase
        joiner: tells the function what string it should use to join the ameno acids 
        outputUpper: Tells the funciton if the output should be capitalised"""
        if not upper:
            s = s.upper()
        dic =  {
                'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
                'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
                'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
                'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
                'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
                'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
                'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
                'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
                'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
                'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
                'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
                'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
                'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
                'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
                'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
                'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'}
        oupt = []
        i1 = 0 
        while i1+3 <= len(s):
            key = s[i1:i1+3]
            AA =    dic[key]   
            if not outputUpper:
                aa = AA[0].lower()
                AA = aa+AA[1:]
            oupt.append(AA)
            i1 = i1 + 3
            
        oupt = joiner.join(oupt)
        return(oupt)
    
    
import re
def find_reading_frames(DNA, MinCodons = 100, StartCodons = ["ATG"], StopCodons = ["TAG","TAA","TGA"]):
    """
    DNA: DNA sequence we are looking at 
    MinCodons: Minimum number of codons in the sequence
    StartCodons:  list of strings, start codons
    StopCodons: list of strings, stop codons
    """
    start = "(" + "|".join(StartCodons)+")"
    stop = "|".join(StopCodons)
    patturn =  start + "((?!" + stop + ")...){" + str(MinCodons) + ",}("+stop+")"
    p = raw_s = r'{}'.format(patturn)
    pattern2 = re.compile(p)
    orf_list2 = re.finditer(pattern2,DNA)
    oupt = []
    for each in orf_list2:
        dic = {"Start Index":each.start(), "Start Coord":each.start() + 1,  "End Index":each.end(), "End Coord":each.end(), "Sequence":each.group()}
        oupt.append(dic)
    return(oupt)