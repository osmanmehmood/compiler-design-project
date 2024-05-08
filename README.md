# Arithmetic Expression Parser

This repository contains a Python program for parsing arithmetic expressions using a Lexical Analyzer and an LR(1) Parser.

## Overview

The program consists of two main components:

1. **Lexical Analyzer:** Responsible for tokenizing input arithmetic expressions into tokens such as numbers, operators, and parentheses.
2. **LR(1) Parser:** Parses the tokenized input using LR(1) parsing technique, ensuring correct expression syntax.

## Usage

1. **Tokenization**: Input an arithmetic expression, and the program will tokenize it using the Lexical Analyzer.
2. **Lexical Analysis**: Displays the tokens generated by the Lexical Analyzer.
3. **Parsing**: Parses the tokenized input using the LR(1) Parser and generates a parse tree.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/osmanmehmood/compiler-design-project.git
    ```

2. Navigate to the directory:

    ```bash
    cd arithmetic-expression-parser
    ```

3. Run the program:

    ```bash
    python main.py
    ```

## Example

```python
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
