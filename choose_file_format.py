import reading_file_name
file_list = reading_file_name.file_list_1

for i in range(len(file_list)):
    if 'pdf' in file_list[i]:
        print('This file is pdf format.')
    elif 'xlsx' in file_list[i]:
        print('this file is excel format.')
    elif 'pptx' in file_list[i]:
        print('this file is pptx format.')
    elif 'docx' in file_list[i]:
        print('this file is docx format.')
    else:
        print('Sorry, I cannot read this file.{}'.format(file_list[i]))