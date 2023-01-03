import re

file = open('regex_test.txt')

data = file.readlines()
file.close()

print(data)


# names = data.split('\n')
# pattern = re.compile('(?P<first_name>[A-Z][a-z]+)(?P<middle_name>[\w -]*)(?P<last_name>[A-Z][a-z]+).*\s')

for name in data:
    # match = pattern.search(name)
    # define match and store requirements
    match = re.search('(?P<first_name>[A-Z][a-z]+)(?P<middle_name>[\w -]*)(?P<last_name>[A-Z][a-z]+).*\s', name)

    if match:
         print(f"{match.group('first_name')}{match.group('middle_name')}{match.group('last_name')}")
    else:
        print('None')




# _________________________Code that didnt work:_______________________

# match = re.search('(?P<last_name>[A-Z][a-z]+), (?P<middle_name>[\w -]*)(?P<first_name>[A-Z][a-z]+).*\s(?P<handle>@[a-zA-Z\d]+$)', final)
    
    # if match:
    #     #split between groups
    #     print(f"{match.group('first_name')} {match.group('middle_name')} {match.group('last_name')} {match.group('handle')}") 
              
#     else:


# name_pat = re.compile('(?P<first_name>[A-Z][a-z]+) (?P<last_name>[A-Z][a-z]+$)')
# found = name_pat.findall(data)

# names = data.split('\n')
#print(names)
# for name in names:
#     match = name_pat.search(name)
    
#     if match:
#         print(match.group('first_name')(match.group('last_name'))) 
        
#     if re.match('[A-Z][a-z]*\s*[A-Z]*[a-z]*\s[A-Z][a-z]*', item):
#         print(' '.join(re.findall('[A-Z][a-z]*', item)))
    
#     else:
#         print('None')
        
# import re

# file = open('names.txt')

# data = file.readlines()
# file.close()

# print(data)

# for final in data:
#     #   This is where were defining:
#     match = re.search('(?P<last_name>[A-Z][a-z]+), (?P<middle_name>[\w -]*)(?P<first_name>[A-Z][a-z]+).*\s(?P<handle>@[a-zA-Z\d]+$)', final)
    
#     if match:
#         #split between groups
#         print(f"{match.group('first_name')} {match.group('middle_name')} {match.group('last_name')} {match.group('handle')}") 
              
# #     else:
# #         print('Not valid')
        
        