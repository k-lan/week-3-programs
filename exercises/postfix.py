from pythonds.basic import Stack


def infix_to_postfix(infix_expr):
    """
    Convert an infix mathematical expression into an postfix expression.
    :param infix_expr: String of infix expression
    :return: original infix expression as a postfix expression
    """
    prec = {"**": 4, "//": 3, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    op_stack = Stack()  # Stack to hold operators
    postfix_list = []  # Where we will insert our postfix expression to print
    token_list = []
    tmp_str = ''
    operator_str = ''
    for ch in infix_expr:  # Convert expression into a list  3.0*5 + 4
        if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or ch in "0123456789.":
            if operator_str != '':
                token_list.append(operator_str)
                operator_str = ''
            tmp_str = tmp_str + ch
        elif ch in "*+/-":
            if tmp_str != '':
                token_list.append(tmp_str)
                tmp_str = ''
            operator_str = operator_str + ch
        elif ch in "()":
            if tmp_str != '':
                token_list.append(tmp_str)
                tmp_str = ''
            elif operator_str != '':
                token_list.append(operator_str)
                operator_str = ''
            token_list.append(ch)
    if tmp_str != '':
        token_list.append(tmp_str)
    if tmp_str != '':
        token_list.append(operator_str)

    for token in token_list:  # Go through each item in the list.
        if token not in "+-**//()":
            postfix_list.append(token)  # add expression to list, not operator
        elif token == '(':  # Notify that we'll have an operator of top priority coming up
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':  # Take the operator out of the stack and insert into our pfix list
                postfix_list.append(top_token)  # continue for as many tokens were in the ()
                top_token = op_stack.pop()
        elif token == '':
            pass
        else:
            while (not op_stack.isEmpty()) and \
                    (prec[op_stack.peek()] >= prec[token]):  # compare operator precedence, decide which goes first
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.isEmpty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)


def postfix_eval(postfix_expr):
    """
    Take postfix expression and solve it.
    :param postfix_expr: Expression to be solved.
    :return: int or float depending on which operators were used.
    """
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token not in "()+-**//":
            operand_stack.push(float(token))
        else:
            operand_2 = operand_stack.pop()
            operand_1 = operand_stack.pop()
            result = do_math(token, operand_1, operand_2)
            operand_stack.push(result)
    return operand_stack.pop()


def do_math(op, op1, op2):
    """
    :param op: Operator to perform
    :param op1: First operand
    :param op2: Second operand
    :return: Solution to the applied math
    """
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "//":
        return op1 // op2
    elif op == "**":
        return op1 ** op2
    else:
        return op1 - op2


def infix_calc(infix_exp):
    postfix = infix_to_postfix(infix_exp)
    evaluation = postfix_eval(postfix)
    return evaluation


def main():
    print(infix_calc("5 * 3 // 6.0"))
    print(infix_to_postfix("A*B+C*D"))
    print(infix_to_postfix("A**B // C"))
    print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    print(postfix_eval('7 8 + 3 2 + /'))
    print(postfix_eval('6 1.5 //'))


if __name__ == '__main__':
    main()
