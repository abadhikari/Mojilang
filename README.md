# Mojilang 👻

Mojilang (EmojiLanguage 😉) is a simple interpreted programming language that utilizes emojis and is built from scratch with a custom lexer, parser, and interpreter. 
My goal with Mojilang was to learn the basic inner workings of a programming language while also making a fun goofy programming language using emojis for common programming constructs like variables, loops, and conditionals.
It's currently written in Python which will be terribly slow but I wanted/E to create a quick prototype before deciding if I wanted to sink weeks into creating it in C 😮‍💨.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Syntax Overview](#syntax)
  - [Syntax Rolodex](#syntax-rolodex-)
- [How It Works](#how-it-works)
  - [Lexer](#lexer)
  - [Parser](#parser)
  - [Interpreter](#interpreter)
- [License](#license)

## Features
- 🙈 Emoji-based syntax
- 😤 Custom lexer, parser, and interpreter
- 🦍 Basic programming features: variables, loops, conditionals, and functions
- 🗿 Proper operation precedence handling
- 😮‍💨 Block scoping
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
   python -m mojilang.mojilang path/to/your/file.moji

## Syntax
Mojilang uses emojis to represent common programming constructs. Below is an overview of the syntax:

1. **Variables**
 
Define variables using the 🥸 emoji, followed by the variable name, the assignment emoji ✍️, a value, and semicolon (all statements must end in a semicolon):
```
🥸 variable ✍️ 5;
```
Can also use '=' instead of ✍️ and it's valid but it's less fun 😩.
```
🥸 variable = 5;
```

2. Print Statements
The 🗣️ emoji is used for printing output:
```
🗣️("Hello, World!");
```

Parentheses are optional in prints so the following will also work:
```
🗣️"Hello, World!";
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
The 🔁 emoji is used for loops, 💥 is for break, and 🤓 is for continue, ☝️is for greater ('>' also works).
```
🥸 i ✍️ 10;
🔁(i ☝️ 0) {
    🗣️(i);
    i ✍️ i ➖ 1;
}
🗣️("Blast off!");
```

5. **Functions**
The 🛠️ emoji is used for functions, 🥸 is used for the parameters, 🫡 is used for return, and 👀 is used to call the function. 
```
🛠 sum(🥸 num1, 🥸 num2) {
  🫡 num1 ➕ num2;
}

🗣️(👀sum(1, 2) ➕ 2);
```

6. **Example**

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

### Syntax Rolodex ###

#### Variables: 

| Operation | Emoji | Description |
|-----------|-------|-------------|
| variable  | 🥸    | Dynamically typed variable |

#### Math Operators:

| Operation | Emoji/Symbol | Description |
|-----------|--------------|-------------|
| add       | ➕ or '+'     | Add two numbers |
| subtract  | ➖ or '-'     | Subtract two numbers |
| multiply  | ✖️ or '*'    | Multiply two numbers |
| divide    | ➗ or '/'     | Divide two numbers |
| modulus   | 🍕 or  '%'   | Leftover slice (modulus) |
| exponent  | 🥕 or '^'    | Exponent (caret symbol in some languages) |

#### Control Flow:

| Operation | Emoji/Symbol   | Description                                      |
|-----------|----------------|--------------------------------------------------|
| if        | 🤔             | If condition                                     |
| else      | 💅             | Else condition                                   |
| true      | 😤             | True value                                       |
| false     | 😔             | False value                                      |
| and       | and            | Sticking with English                            |
| or        | or             | Sticking with English                            |
| !         | 🙅‍ or '!'     | Not operation                                    |
| =         | ✍️ or '='      | Assignment                                       |
| ==        | 🤝 or '=='     | Equals comparison                                |
| !=        | 🙅‍🤝 or '!='  | Not equals comparison                            |
| \>        | ☝️ or '>'      | Greater than                                     |
| <         | 👇  or '<'     | Less than                                        |
| \>=       | ☝️🤝  or '>='  | Greater than or equal                            |
| <=        | 👇🤝   or '<=' | Less than or equal                               |
| loop      | 🔁             | Single loop for both for and while (like Golang) |
| break     | 💥             | Break out of the loop                            |
| continue  | 🤓             | Skip to next iteration in the loop              |


#### Functions:

| Operation     | Emoji | Description       |
|---------------|-------|-------------------|
| function      | 🛠    | Define a function |
| return        | 🫡    | Return a value    |
| function call | 👀    | Call a function   |

#### Input/Output:

| Operation | Emoji | Description |
|-----------|-------|-------------|
| input     | 🖊    | Take user input |
| print     | 🗣    | Output a value to the console |

#### Error Handling:

| Operation | Emoji | Description |
|-----------|-------|-------------|
| error     | 🤯    | An error occurred |
| throw     | 🤮    | Throw (up) an error |

#### Comments:

| Operation | Emoji | Description |
|-----------|-------|-------------|
| comment   | 🧐    | Add a comment |

## How It Works
Mojilang consists of three main components: the lexer, parser, and interpreter.

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
The parser takes the tokens produced by the lexer and organizes them into an Abstract Syntax Tree (AST) using the rescursive descent parsing algorithm. The AST is a hierarchical structure that represents the syntactical structure of the Mojilang program.

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
