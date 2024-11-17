import re
"""
Write a function called replace_all that takes as arguments a pattern string,
 a replacement string, and two filenames.
 It should read the first file and write the contents into
 the second file (creating it if necessary).
 If the pattern string appears anywhere in the contents,
  it should be replaced with the replacement string.
"""
def replace_all(p_string, r_string, file1):
    with open(p_string, 'r'), open(r_string,'r'):
        pass

def replace_all_v1(pattern, replacement, source_file, output_file):
    source_file = open(source_file,'r')
    output_file = open(output_file,'w')
    text = re.sub(pattern, replacement, source_file.read())
    output_file.write(text)
    source_file.close()
    output_file.close()

def replace_all_v2(str_pattern,str_replace, file1,file2):
    with open(file1,'r') as fp1, open(file2, 'w') as fp2:
        fp2.write(re.sub(str_pattern,str_replace,fp1.read() ))

def main():
    replace_all_v2(r'photos',
                   'images',
                   'photos/notes.txt'
                   ,'photos/output.txt')

if __name__=='__main__':
    main()
