
#Function with output

def format_name(f_name, l_name):

    """
    Take a first and last name
    Formate ie to return the title case version
    """

    if f_name == "" or l_name == "":
        return "You didn't give the right information"
    #Google"How to convert string to Title Case in Python"
    formated_f = f_name.title()
    formated_l = l_name.title()
    return f"Result: {formated_f} {formated_l}" #the end of function

print(
    format_name(
        input("What's your first name? "), 
        input("What's your first name? ")
    )
)

def format_name(f_name, l_name):
    #Google"How to convert string to Title Case in Python"
    formated_f = f_name.title()
    formated_l = l_name.title()

    return formated_f, formated_l

print(format_name("jing", "lu"))

