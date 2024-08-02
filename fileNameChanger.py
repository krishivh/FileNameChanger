import os

def rename_file(file_name):
    #see if there even is a paranthesis inside of the file name
    if '(' in file_name and ')' in file_name:
        #find the index of both of the open and closed paranthesis
        openParen = file_name.find('(')
        closeParen = file_name.find(')')
        #make a new substring that only contains the paranthesis and everything inside
        substring = file_name[openParen:closeParen+1]
        # remove the substring from the file_name
        #file_name1 representes the file_name without the paranthesis
        file_name1= file_name[:openParen] + file_name[closeParen + 1:]
        
        #find where the first period is because the parenthesis must be placed before the first period
        first_period = file_name.find('.')
        #check to see that there actually is a period
        if first_period != -1:
        
        #if there is then we want to split the parts into 
            file_name_parts = file_name1.split('.', 1)
            final_file_name = file_name_parts[0] + substring + '.' + file_name_parts[1]
        else:
            # If there is no period, append the substring to the end
            final_file_name = file_name1 + substring
        
        return final_file_name

    else:
        return file_name

#test cases before os:
# print(rename_file('file2.jpg.json'))  # Expected: 'file2.jpg.json'
# print(rename_file('file2(1)'))  # Expected: 'file2(1)'
# print(rename_file('file2.jpg.tar'))  # Expected: 'file2.jpg.tar'
# print(rename_file('(1)file2.jpg.json'))  # Expected: 'file2(1).jpg.json'
# print(rename_file('file2(2).jpg.json'))  # Expected: 'file(2).jpg.json'
# print(rename_file('file1.jpg(1).json'))  # Expected: 'file2.jpg.json'


def rename_files_in_directory(directory):
    #os.listidr(directory) will list all the files within the directory and we will for loop through every file within that directory
    for filename in os.listdir(directory):
        #create the old path by putting the directory together with the filename
        old_path = os.path.join(directory, filename)
        #create the new file name using the rename_file method created above
        new_filename = rename_file(filename)
        #rejoin the directory with the new file name
        new_path = os.path.join(directory, new_filename)
        
        #if we have not changed the name at all, we don't want to rename it just in case it messes it up
        if old_path != new_path:
            #rename the old_path with the new_path and that should rename it overall
            os.rename(old_path, new_path)

#__file__ returns the full path of the current file that it is in, in this case the python file
#os.path.realpath will get the absolute path of the file 
#os.path.dirname will get the directory where the file is and uses the absolute path file to do that
#so in the end dir_path has the active working directory of the python file
# dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()

rename_files_in_directory(cwd)

            
            