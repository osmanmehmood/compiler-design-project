import re
 
class LexicalAnalyzer:
    def _init_(self):
        pass
 
    def tokenize(self, input_str):
        # Regular expressions for token patterns
        patterns = [
            (r'\d+(\.\d+)?', 'NUMBER'),   # Match numbers
            (r'[+\-*/]', 'OPERATOR'),      # Match operators
            (r'[()]', 'PARENTHESIS'),      # Match parentheses
            (r'\s+', None),                # Match whitespace (to be ignored)
            (r'\/\/.*', None)              # Match comments (to be ignored)
        ]
 
        tokens = []
        while input_str:
            for pattern, token_type in patterns:
                regex = re.compile(pattern)
                match = regex.match(input_str)
                if match:
                    if token_type:  # If token type is not None (i.e., not whitespace or comment)
                        tokens.append((token_type, match.group(0)))
                    input_str = input_str[match.end():]
                    break
            else:
                raise ValueError("Invalid input")
        return tokens
 
class LRParser:
    def _init_(self):
        self.tokens = []
        self.current_token_index = 0
 
    def parse(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.parse_expression()
 
    def parse_expression(self):
        self.parse_term()
        while self.current_token_index < len(self.tokens):
            token_type, token_value = self.tokens[self.current_token_index]
            if token_type == 'OPERATOR':
                self.current_token_index += 1
                self.parse_term()
            elif token_type == 'PARENTHESIS' and token_value == ')':
                break
            else:
                raise SyntaxError("Invalid expression")
 
    def parse_term(self):
        token_type, token_value = self.tokens[self.current_token_index]
        if token_type == 'NUMBER':
            print(f"Number: {token_value}")  # Print number token
            self.current_token_index += 1
        elif token_type == 'PARENTHESIS' and token_value == '(':
            print("(")  # Print opening parenthesis token
            self.current_token_index += 1
            self.parse_expression()
            if self.current_token_index >= len(self.tokens) or self.tokens[self.current_token_index][1] != ')':
                raise SyntaxError("Mismatched parentheses")
            self.current_token_index += 1
            print(")")  # Print closing parenthesis token
        else:
            raise SyntaxError("Invalid term")
 
# Example usage:
user_input = input("Enter an arithmetic expression: ")
 
# Tokenization
lexer = LexicalAnalyzer()
tokens = lexer.tokenize(user_input)
print("Tokenization:")
print(tokens)
 
# Lexical Analysis
print("\nLexical Analysis:")
for token in tokens:
    print(token)
 
# Parsing
print("\nParse Tree (LR(1) Parsing):")
parser = LRParser()
parser.parse(tokens)
