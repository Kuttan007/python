""" Write all content of a given file into a new file by skipping line number 5 


Given test.txt file:

line1
line2
line3
line4
line5
line6
line7



"""

with open("/tmp/test.txt", "r") as fp:

        lines = fp.readlines()


with open("/tmp/test1.txt", "w") as fp:
        count = 0
    
        for line in lines:
                count +=1

       
        if count == 4:
                continue
        else:
          
            fp.write(line)
