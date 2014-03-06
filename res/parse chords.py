file1 = open("chords.txt")
file2 = open("parsedchords.txt","w")

for line in file1:
    
    line = line.replace("\t"," ")
    line = line.replace("\n","")
    line = line.split(" ")
    file2.write('"' + line[0] + '"' + ": [")
    
    for i in range(1,len(line)):
        if (i != len(line)-1):
            file2.write('"' + line[i] + '"' + ", ")
        else:
            file2.write('"' + line[i] + '"')
        
    file2.write("], ")
     
file1.close()
file2.close()


