import re

#############----------------------------------- introducing Mylanguge :------------------------------------------

if_keyword = ['agar']
decimals_keyword =['ashar']
print_kayword =['chap']
integer_keyword=['sahih']
input_keyword=['begir']
operations = ['+', '*', '/', '=', '<', '<=', '==', '>=', '>', '!=']
delimiters = ['(', ')', '{', '}', '[', ']', ';','.' ,r'\n', r'\t']
integer_pattern = re.compile(r'[\+\-]?\d+')
decimal_pattern = re.compile(r'-?\b\d+\.\d+\b|\b\d+\.\d+e[+-]?\d+\b')
identifier_pattern = re.compile(r'[A-Za-z]+\w*')
string_pattern = re.compile(r'"[^"]*"')
comment_pattern = re.compile(r'//.*|^/\*.*\*/')


def tokenize(code):
    tokens = []
    position = 0

    while position < len(code):
        match = None

        # Matching patterns
        for pattern in [integer_pattern, decimal_pattern, string_pattern, identifier_pattern, comment_pattern]:
            match = pattern.match(code, position)
            if match:
                token = match.group(0)
                if pattern == comment_pattern:
                    token_type = 'COMMENT\n'
                elif token in if_keyword:
                    token_type = 'KEYWORD FOR IF\n'
                elif token in decimals_keyword:
                    token_type = 'KEYWORD FOR DECIMAL\n'
                elif token in input_keyword:
                    token_type = 'KEYWORD FOR INPUT\n'
                elif token in print_kayword:
                    token_type = 'KEYWORD FOR PRINT\n'
                elif token in integer_keyword:
                    token_type = 'KEYWORD FOR INTEGER\n'
                elif pattern == integer_pattern:
                    token_type = 'INTEGER NUMBER'
                elif pattern == decimal_pattern:
                    token_type = 'DECIMAL NUMBER'   
                elif pattern == string_pattern:
                    token_type = 'STRING\n'
                else:
                    token_type = 'IDENTIFIER\n'
                tokens.append((token, token_type))
                position = match.end()
                break

        if not match:
            for token in operations + delimiters:
                if code.startswith(token, position):
                    tokens.append((token, 'OPERATION\n' if token in operations else 'DELIMITER\n'))
                    position += len(token)
                    break
            else:
                position += 1

    return tokens

#------------------------------------------test here UwU :--------------------------------------------------
with open('script.txt', 'r') as file:
    code = file.read()

tokens = tokenize(code)
for token, token_type in tokens:
    print(f'{token} : {token_type}')