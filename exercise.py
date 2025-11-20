# Build a small program that turns a fullname into its initials
# eg. make_initials("Will Smith") #=> 'W.S'

# Parameters
#    - fullname, a string (eg. "Xiao Chan")
# Returns
#    - string (eg. 'X.C')
# Side effects
#    - None
def make_initials(fullname):
    # return fullname.split(" ")[0][0] + "." + fullname.split(" ")[1][0]
    names = fullname.split(" ") # task 1

    first_name = names[0]
    first_name_char = first_name[0]

    last_name = names[1]
    last_name_char = last_name[0] # task 2
    
    return first_name_char + "." + last_name_char # task 3

# Tasks
# - split the fullname with a space #=> ['name', 'name'] DONE
# - we need to take out the first characters (looping through, accessing them or looking for capitals) DONE
# - we need to return the first characters with a "." in between DONE

print(make_initials('Will Smith'))