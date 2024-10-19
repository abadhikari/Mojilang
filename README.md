# Mojilang 👻

Mojilang (EmojiLanguage 😉) is a simple programming language that utilizes emojis and is built from scratch with a custom lexer, parser, and interpreter. 
My goal with Mojilang was to learn the basic inner workings of a programming language while also making a fun goofy programming language using emojis for common programming constructs like variables, loops, and conditionals.
It's currently written in Python which will be terribly slow but I wanted/E to create a quick prototype before deciding if I wanted to sink weeks into creating it in C 😮‍💨.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Syntax](#syntax)
- [Example](#example)
- [How It Works](#how-it-works)
  - [Lexer](#lexer)
  - [Parser](#parser)
  - [Interpreter](#interpreter)
- [License](#license)

## Features
- 🙈 Emoji-based syntax
- 😤 Custom lexer, parser, and interpreter
- 🦍 Basic programming features: variables, loops, conditionals, and functions
- 🗣️ Built-in `print` functionality

## Installation
To run Mojilang, you’ll need Python 3.6+ installed on your machine. You can clone this repository and run the interpreter directly.

1. Clone the repository:
   ```bash
   git clone https://github.com/abadhikari/Mojilang.git
   ```

## Usage
To run an Mojilang program, follow these steps:

1. Write your Mojilang code in a `.moji` file using the emoji-based syntax.

2. Run the interpreter on your `.moji` file using the following command from the project root directory:
   ```bash
   python -m main.py path/to/your/file.moji

## Syntax
Mojilang uses emojis to represent common programming constructs. Below is an overview of the syntax:

1. **Variables**
 
Define variables using the 🥸 emoji, followed by the variable name, the assignment emoji ✍️, a value, and semicolon (all statements must end in a semicolon):
```
🥸 variable ✍️ 5;
```

2. Print Statements
The 🗣️ emoji is used for printing output:
```
🗣️("Hello, World!");
```

3. **If Statements**

The 🤔 emoji is used for if statements, 🙈 is used for else if, 💅 is used for else, 😤 is the equivalent of true while 😔 is the equivalent of false. 
```
🤔(😤) {
    🗣️("This is true.");
} 💅 {
    🗣️("This is false.");
}
```

4. **Loops**
The 🔁 emoji is used for loops, 💥 is for break, and 🤓 is for continue. 
```
🥸 i ✍️ 10;
🔁(i ☝️ 0) {
    🗣️(i);
    i ✍️ i ➖ 1;
}
🗣️("Blast off!");
```

5. **Example**

Here's an example utilizing several constructs from above:
```
🥸 age ✍️ 20;
🤔(age ☝️ 21) {
    🗣️("You can drink 😤!");
} 🙈(age 🤝 20) {
    🗣️("You're so close but you still can't drink 😩!");
} 💅 {
    🗣️("You can't drink 😔!");
}
```

## How It Works
Mojilang consists of three main components: the lexer, parser, and interpreter.

**Lexer**: Converts the raw source code into tokens.
**Parser**: Takes the tokens and organizes them into an Abstract Syntax Tree (AST) using the rescursive descent parsing algorithm.
**Interpreter**: Walks through the AST and executes the program by evaluating each node, handling expressions, statements, etc.

### Lexer
The lexer is responsible for converting raw source code into a list of tokens. A token is a logic unit of the code, such as a number, an operator, or a keyword. The lexer scans each character of the source code and converts them into tokens.

For example:
```
🥸 variable ✍️ 5;
```
This is converted by the lexer into the following tokens:

* VAR (🥸)
* IDENTIFIER (variable)
* EQUAL (✍️)
* NUMBER (5)
* SEMI_COLON (;)

### Parser
The parser takes the tokens produced by the lexer and organizes them into an Abstract Syntax Tree (AST). The AST is a hierarchical structure that represents the syntactical structure of the Mojilang program.

For example:

```
🥸 variable ✍️ 5 ➕ 3;
```

This is parsed into an AST node representing an assignment of the value 5 + 3 to the variable variable which would look like

```
AssignmentNode
 ├── VariableNode ("variable")
 └── AdditionNode
     ├── NumberLiteralNode (5)
     └── NumberLiteralNode (3)
```

The parser ensures that the syntax of the program is correct. If any syntax violations occur (such as missing semicolons or invalid expressions), then the parser raises a SyntaxExceptoin.

### Interpreter
The interpreter is responsible for executing the Abstract Syntax Tree (AST) generated by the parser. The interpreter evaluates each node of the AST, executing statements and expressions in the correct order.
Currently, it's very simple since all it has to do is run evaluate method of the root node 😉.

For example:

```
🥸 x ✍️ 10 ➕ 20;
🗣️(x);
```
The interpreter will:

1. Evaluate 10 + 20 and assign the result (30) to x.
1. Print the value of x to the console (resulting in 30 being displayed).
The interpreter handles all the logic and operations defined by Mojilang, such as variable assignments, conditionals, loops, and function calls (these are still in-progress).

## License
This project is licensed under the MIT License - see the LICENSE file for details.
