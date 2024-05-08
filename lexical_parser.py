import re

class ArithmeticParser:
    def __init__(self):
        self.tokens = []
        self.current_token_idx = 0

    def tokenize_input(self, input_str):
        # Regular expressions to match numbers, operators, and parentheses
        number_pattern = r'\d+(\.\d+)?'
        operator_pattern = r'[+\-*/]'
        parenthesis_pattern = r'[()]'

        # Compile regular expressions
        number_regex = re.compile(number_pattern)
        operator_regex = re.compile(operator_pattern)
        parenthesis_regex = re.compile(parenthesis_pattern)

        # Tokenize input string
        while input_str:
            # Skip whitespace
            if input_str[0].isspace():
                input_str = input_str[1:]
                continue
            
            # Match numbers
            if number_match := number_regex.match(input_str):
                self.tokens.append(('NUMBER', float(number_match.group(0))))
                input_str = input_str[number_match.end():]
                continue
            
            # Match operators
            if operator_match := operator_regex.match(input_str):
                self.tokens.append(('OPERATOR', operator_match.group(0)))
                input_str = input_str[1:]
                continue
            
            # Match parentheses
            if parenthesis_match := parenthesis_regex.match(input_str):
                self.tokens.append(('PARENTHESIS', parenthesis_match.group(0)))
                input_str = input_str[1:]
                continue
            
            # If none of the patterns matched, raise an error
            raise ValueError("Invalid input")

    def accept_input(self):
        while True:
            try:
                user_input = input("Enter an arithmetic expression: ")
                self.tokenize_input(user_input)
                break
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid arithmetic expression.")

        print("Input tokens:", self.tokens)

    # Parsing methods
    def parse_expression(self):
        result = self.parse_term()
        while self.current_token_idx < len(self.tokens):
            token_type, token_value = self.tokens[self.current_token_idx]
            if token_type == 'OPERATOR' and token_value in ['+', '-']:
                self.current_token_idx += 1
                right = self.parse_term()
                if token_value == '+':
                    result += right
                else:
                    result -= right
            else:
                break
        return result

    def parse_term(self):
        result = self.parse_factor()
        while self.current_token_idx < len(self.tokens):
            token_type, token_value = self.tokens[self.current_token_idx]
            if token_type == 'OPERATOR' and token_value in ['*', '/']:
                self.current_token_idx += 1
                right = self.parse_factor()
                if token_value == '*':
                    result *= right
                else:
                    result /= right
            else:
                break
        return result

    def parse_factor(self):
        token_type, token_value = self.tokens[self.current_token_idx]
        if token_type == 'NUMBER':
            self.current_token_idx += 1
            return token_value
        elif token_type == 'PARENTHESIS' and token_value == '(':
            self.current_token_idx += 1
            result = self.parse_expression()
            if self.current_token_idx >= len(self.tokens) or self.tokens[self.current_token_idx][0] != 'PARENTHESIS' or self.tokens[self.current_token_idx][1] != ')':
                raise ValueError("Mismatched parentheses")
            self.current_token_idx += 1
            return result
        else:
            raise ValueError("Invalid factor")

# Create an instance of the ArithmeticParser class
parser = ArithmeticParser()

# Accept input from the user and tokenize it
parser.accept_input()

# Parse the input tokens
try:
    result = parser.parse_expression()
    print("Result:", result)
except ValueError as e:
    print(f"Parsing Error: {e}")
