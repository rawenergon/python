

# MAKES SOME STRINGS

a = "Aditya Raj"
b = "Abhinav Patel"

# UPPERCASE .upper()
uppercase_my_str = a.upper()
print(uppercase_my_str)


# LOWERCASE .lower()

lowercase_my_str = a.lower()
print(lowercase_my_str)

# STRIPPING  strip()
# it removes leading and trailing whitespace.

c = ' ADITYA RAJ      '
trimmed_my_str = c.strip()
print(trimmed_my_str)

# REPLCAE .replace()

replace_my_str = b.replace('Patel' , 'Raj')
print(replace_my_str)

# SPLIT .split()

split_my_str = a.split()
print(split_my_str)

# JOINT .joint(str_name)

d_list = ['Aditya', 'Raj']

joined_my_str = ''.join(d_list)
print(joined_my_str)

# START WITH  (prefix) : Retrun boolean indicaing start with 

start_with_str = a.startswith('Aditya')
print(start_with_str)

# END WITH (suffix) : Return boolean indicating 

end_with_str = a.endswith('Raj')
print(end_with_str)

# FIND  Return index of first occurance if not then -1 

word_index = a.find('Raj')
print(word_index)

# TITLE  
# Returns a new string with the first letter of each word capitalized and the remaining letters lowercased.

x = "how computers talk"

title_case_str = x.title()
print(title_case_str)

# Capitalized 
#  Returns a new string with the first character capitalized and the other characters lowercased.

capitalized_my_str = x.capitalize()
print(capitalized_my_str)
