import os

##########   WRITING FILE OUT   ##########
#open file to write
to_write_file_pointer = open('to_read_write.txt', 'w+')
#FOR: number in range from 1 to 10, write the number and a new line to our file
for number in range(1, 10):
    #write number to file (with a new line)
    to_write_file_pointer.write("{0}\n".format(number))
#create a list of letters to output to our file
letters = ['a', 'b', 'c', 'd', 'e']
#FOR: letter in letters from a to e, write letter and a new line to our file
for letter in letters:
    #write letter to file (with a new line)
    to_write_file_pointer.write("{0}\n".format(letter))
#close file
#to_write_file_pointer.close()
to_write_file_pointer.seek(0)
readhw = to_write_file_pointer.read()
##########   READING FILE IN   ##########
#open file to read
#to_read_file_pointer = open('to_read.txt', 'r')
#FOR: line in to_read_file_pointer, read and print each line
#for line in to_read_file_pointer:
    #print line
    #print("Line: {0}".format(line))
toHW1 = open('output.txt', 'w+')
toHW1.write(readhw)
#close file
to_write_file_pointer.close()
#uncomment line below to remove file after reading
#os.remove('to_read.txt')
#ALL DONE!

