import re

# Função para detectar uma expressão formada somente por dígitos
def digit(exp):
    i=0
    while i < len(exp):
        if (exp[i] >= '0' and exp[i] <= '9'):
            i+=1
        else: 
            return False
    return True

# Função para detectar uma expressão formada somente por letras
def alpha(exp):
    i = 0
    while i < len(exp):
        if (exp[i] >= 'a' and exp[i] <= 'z') or (exp[i] >= 'A' and exp[i] <= 'Z'):
            i += 1
        else: 
            return False
    return True

# Função para detectar uma expressão formada somente caractres alfanuméricos
def alphadigit(exp):
    i = 0
    while i < len(exp):
        if (exp[i] >= 'a' and exp[i] <= 'z') or (exp[i] >= 'A' and exp[i] <= 'Z') or (exp[i] >= '0' and exp[i] <= '9'):
            i += 1
        else: 
            return False
    return True

def lexer(input_string):
    tokens = []
    index = 0
    length = len(input_string)

    while index < length:
        char = input_string[index]

        if alpha(char):
            # Início de uma variável (palavra)
            word = ""
            while index < length:
                if char == '*' or char== '+' or char== '=' or char== ')' or char=='(' or char == '¬':  
                    break
                if input_string[index:index+2] == '->' or input_string[index:index+3] == '<->' or input_string[index:index+2] == '\\\\':
                    break
                else:
                    word += char
                index += 1
                if index < length:
                    char = input_string[index]
                if char.isspace():
                    index+=1
                    break
            i = 0
            while i < len(word):
                if not alphadigit(word[i]):
                    raise ValueError(f"Error: {word} variável com caractere especial. Utilize espaços entre variáveis e caracteres especiais")
                i+=1
            if len(word)>100:
                raise ValueError("Error: Variável com mais de 100 caracteres")
           
            if word == "True":
                tokens.append(('true_boolean', word))
            elif word == "False":
                tokens.append(('false_boolean', word))
            else:
                tokens.append(('identifier', word))
        elif digit(char):
            # Início de um número
            num = ""
            while index < length and alphadigit(char):
                num += char
                index += 1
                if index < length:
                    char = input_string[index] 
            i = 0
            while i < len(num):
                if not digit(num[i]):
                    raise ValueError(f"Error: {num} variável não pode iniciar com número")
                i+=1

            tokens.append(('number', num))
        elif char == '(':
            tokens.append(('left_paren', char))
            index += 1
        elif char == ')':
            tokens.append(('right_paren', char))
            index += 1
        elif char == '+':
            tokens.append(('or_operator', char))
            index += 1
        elif char == '*':
            tokens.append(('and_operator', char))
            index += 1
        elif input_string[index:index+2] == '->':
            tokens.append(('implies_op', '->'))
            index += 2
        elif input_string[index:index+3] == '<->':
            tokens.append(('iff_operator', '<->'))
            index += 3
        elif char == '¬':
            tokens.append(('not_operator', char))
            index += 1
        elif char == '=':
            tokens.append(('equal_operator', char))
            index += 1
        elif input_string[index:index+2] == '\\\\':
            while index < length and input_string[index] != '\n':
                index += 1   
        elif not char.isalnum() and not char.isspace():
            tokens.append(('UNKNOWN', char))  
            index += 1
        elif char.isspace():
            index+=1
    return tokens

def process_input(input_data):
    # Remover comentários da entrada apenas para exibição 
    expression = re.sub(r'\\.*', '', input_data)

    expression = expression.strip()

    return expression, lexer(input_data)

