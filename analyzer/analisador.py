import re

def lexer(input_string):
    tokens = []
    index = 0
    length = len(input_string)

    while index < length:
        char = input_string[index]

        # Ignorar espaços em branco e quebras de linha
        if char.isspace():
            index += 1
            continue

        if char.isalpha():
            # Início de uma variável (palavra)
            word = ""
            while index < length and (char.isalnum() or char == '_'):
                word += char
                index += 1
                if index < length:
                    char = input_string[index]
            
            if word == "True":
                tokens.append(('TRUE_BOOLEAN', word))
            elif word == "False":
                tokens.append(('FALSE_BOOLEAN', word))
            else:
                tokens.append(('VAR', word))
        elif char.isdigit():
            # Início de um número
            num = ""
            while index < length and char.isdigit():
                num += char
                index += 1
                if index < length:
                    char = input_string[index]
            tokens.append(('NUM', num))
        elif char == '(':
            tokens.append(('LPAREN', char))
            index += 1
        elif char == ')':
            tokens.append(('RPAREN', char))
            index += 1
        elif char == '+':
            tokens.append(('OR', char))
            index += 1
        elif char == '*':
            tokens.append(('AND', char))
            index += 1
        elif input_string[index:index+2] == '->':
            tokens.append(('IMPLIES', '->'))
            index += 2
        elif input_string[index:index+3] == '<->':
            tokens.append(('IFF', '<->'))
            index += 3
        elif char == '¬':
            tokens.append(('NOT', char))
            index += 1
        elif char == '=':
            tokens.append(('EQUAL', char))
            index += 1
        else:
            tokens.append(('UNKNOWN', char))  # Token para caracteres desconhecidos
        index += 1

    return tokens

def process_input(input_data):
    # Remover comentários da entrada
    input_data = re.sub(r'\\.*', '', input_data)

    # Encontrar a expressão da entrada (ignorando comentários)
    expression = ""
    lines = input_data.split('\n')
    for line in lines:
        expression += line

    # Remover espaços em branco extras
    expression = expression.strip()

    return expression, lexer(input_data)
