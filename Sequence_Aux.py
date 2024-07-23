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

def PIMatrix(fileName, order, MuteInfo,seqs):
    f = open(fileName,"w")
    for seq1 in order:
        line = [seq1]
        for seq2 in order:
            line.append(str(MuteInfo(seqs[seq1],seqs[seq2])))
        f.write(",".join(line))
    f.close()