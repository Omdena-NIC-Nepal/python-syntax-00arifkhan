def format_string(name, age):
    return(f"My name is {name} and I am {age} years old")
 

def conditional_check(number):
    num = number
    if num>10:
        return("Greater")
    elif num==10:
        return("Equal")
    else:
        return("Lesser")
 
def loop_sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return(sum)

def list_operations(numbers):
    sum=0
    for i in numbers:
        sum+=i
    maximum=max(numbers)
    minimum=min(numbers)
    return(sum,maximum,minimum)


def dict_operations(students_dict):
    student=[key for key, value in students_dict.items() if values>80]
    return(student)
 

def set_operations(list1, list2):
    common_element=(a for a in list1 if a in list2)
    return(set(common_element))
 

def arithmetic_ops(a, b):
    ret={"sum":a+b,"difference":a-b,"product":a*b,"quotient":a/b}
    return(ret)
  

def logical_ops(x, y):
    a=x and y
    b=x or y
    c=not x
    return({"and":a,"or":b,"not_x":c})
   

def bitwise_ops(a, b):
    return({"and":a & b,"or":a | b,"xor": a ^ b})
    

