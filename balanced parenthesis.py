def isEqual(opening,closing):
    if( opening == '(' and closing == ')' ):
        return True;
    elif ( opening == '[' and closing == ']' ):
        return True;
    elif ( opening == '{' and closing == '}' ):
        return True;
    return False;


def balanced_parenthesis(exp):
    """
    Args: 
    exp: expression to be evaluated
    """
    stack = []
    for i in range(0 , len(exp)):
        if (exp[i] == '(' or exp[i] == '{' or exp[i] == '['):
            stack.insert(0,exp[i])
            print(stack)
        elif (exp[i] == ')' or exp[i] == '}' or exp[i] == ']'):
            if(stack == [] or isEqual(stack[0] , exp[i]) == False ):
                return False
            else:
                stack.pop(0)
            print(stack)
    return stack == []



