#function takes in a list 
#returns all the items in onew string with commas


list = []



def comma(list):
    whole_string = ""
    for i in range(len(list)):
        if i == len(list)-1:
            whole_string = whole_string + "and " + str(list[i])
        else:
            whole_string += str(list[i]) +  "," + " "
    if whole_string =="":
        return "Empty List"
    else:
        return whole_string

print(comma(list))
