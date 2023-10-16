tutor = 'david john bartlett'

title = 'Mr'

dob = "30/12/1996"

job_title = "Senior Tutor"

pronouns = 'he/him'

#A
first_name = tutor[0:5]
print(first_name)

#B
last_name = tutor[11:19]
print(last_name)

#OR split the string into a list
tutor_split = tutor.split()
print(tutor_split)

#A
first_name = tutor_split[0]
#B
last_name = tutor_split[2]

#C
#reverse a string in python using [::-1]
reverse_reverse = last_name[::-1] + ' ' + first_name[::-1]
print(reverse_reverse)

#D
signature = first_name + tutor_split[1][0] + last_name
print(signature)

#E
#upper turns strings to upper case, slicing without a second number will slice to the end of the string
side_hustle = tutor_split[0][0].upper() + tutor_split[1][0].upper() + " " + tutor_split[2][0].upper() + tutor_split[2][1:]
print(side_hustle, "<<<side hustle")
#OR use .capitalize() to capitalise the first letter of a string
side_hustle2 = tutor_split[0][0].capitalize() + tutor_split[1][0].capitalize() + " " + tutor_split[2][0].capitalize() + tutor_split[2][1:]
print(side_hustle2, "<<<side hustle2")

#F
us_dob = dob[3:5] + "/" + dob[0:2] + "/" + dob[6:]
print(us_dob)

#G
slack_handle = tutor_split[0][0].upper() + tutor_split[0][1:] + "-NC"
print(slack_handle)

#H
twitter_handle = "@" + first_name[0][0] + last_name[0:4] + us_dob[0:2] + us_dob[3:5]
print(twitter_handle)

#I
formal_salutation =  title + " " + first_name[0].upper() +  " " +  last_name[0].upper() + last_name[1:]
print(formal_salutation)

#J 
email_signature = first_name.capitalize() + " " + last_name.capitalize() + " (" + pronouns + ") - " + job_title
print(email_signature)

#K
sandwich = last_name[0:4] + first_name + last_name[4:9]
print(sandwich)

#L pig_latin = Avidday Artlettbay
pig_latin = first_name[1:].capitalize() + first_name[0] + "ay " + last_name[1:].capitalize() + last_name[0] + "ay"
print(pig_latin)