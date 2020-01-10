#f = open('test.txt', 'r') #1st argument: name, 2nd argument: mode

#Using a context manager, which automatically closes files once used
#with open('passport_photo.jpg', 'rb') as rf:
#    with open('passport_photo_copy.jpg', 'wb') as wf:   #'b' denotes binary file
#        for line in rf:
#            wf.write(line)
    #for line in f:
    #    print(line, end="")
    #size_to_read = 10

    #f_contents = f.read(size_to_read)
    #print(f_contents, end="*")

    #f.seek(0)

    #f_contents = f.read(size_to_read)
    #print(f_contents)

    #while len(f_contents) > 0:
    #    print(f_contents, end="*")
    #    f_contents = f.read(size_to_read)

#print(f.name)
#f.close()

#must close the file

chunk_size = 4096

with open('passport_photo.jpg', 'rb') as rf:
    with open('passport_photo_copy.jpg', 'wb') as wf:   #'b' denotes binary file
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size) #Prevent infinite loop





#with open('test_2.txt', 'w') as f:
#   f.write('Test') - Marking as 'w' will overrite the file if it exists, 'a' will append it
#   pass

#with open('test_2.txt', 'w') as f:
#    f.write('Test') #Marking as 'w' will overrite the file if it exists, 'a' will append it
