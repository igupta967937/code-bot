from .template import make_templates



templates = {
        'C0103': make_templates('should pay attention to the naming convention for the %s %s. In Python, there are naming conventions for the different types such as for constants, variables and classes. For example, constants should be all in capital letters and variables and classes should start with a capital letter.', 'violated the naming convention for the %s name %s. You should change it according to the conventions: Constants should be in capitals, class and variables names should follow the CapWords convention.', [0, 2]),
        'C0111': make_templates('should specify what a %s does. This so-called documentation string includes for example the command line syntax, environment variables and files. You use triple quotes to start and end the description. Doc strings are convenient as they allow to be inspected by the programmer at run time.', 'should remember to include docstrings to document what your %s does. Using docstrings will save you time and troubleshooting.', [1]),
        'C0301': make_templates('should limit the line length to a maximum of 79 characters according to the Python conventions. The limits are chosen to avoid wrapping in editors with the window width set to 80. Wrapping disrupts the visual structure of the code and makes it more difficult to understand.', 'exceeded the recommended line length of 79 characters. For flowing long blocks of text with fewer structural restrictions such as docstrings or comments, the line length should be limited to 72 characters.', []),
        'C0202': make_templates('should have cls as first name in your class method %s. The cls name is used to easily differentiate class methods from instance methods, which use self as the first argument to instance methods.', 'should use cls for the first argument to your class method %s. ', [2]),
        'C0303': make_templates('used one or more whitespace characters directly before the line end character. Do not write string literals that rely on trailing whitespace. Such trailing whitespace is visually indistinguishable and some editors will trim them.', 'wrote a trailing whitespace, which is in general not recommended', []),
        'C0304': make_templates('forgot to include a final newline. While Python interpreters typically do not require line end characters on the last line, other programs processing Python source files may do. Therefore, it is simply good practice to have it.', 'you forgot to include line end characters on the last line.', []),
        'C0321': make_templates('have more than one statement on the same line. Python syntax does permit more than one statement on a line, separated by a semicolon. However, limiting each line to one statement makes it easier for a human to follow a program\'s logic when reading through it.', 'used more than one statement on a single line, which is not recommended.', []),
        'E0001': make_templates('wrote code that cannot be understood by the computer.', 'have a syntax error!', []),
        'E0213': make_templates('should have self as first name for your method. This is nothing more than a convention: the name self has absolutely no special meaning to Python. Note however that by not following the convention your code may be less readable to other Python programmers.', 'should call fhe first argument of the instance method ''self''. ', []),
        'E0601': make_templates('accessed a local variable before you assigned it. Check again in your code where the assignment happens or if at all.', 'accessed a local variable before its assignment.', []),
        'E0602': make_templates('used the variable %s that is undefined. Always assign a variable before accessing it. Remember that you just have to use the equal sign to assign a value to a variable.', 'included an undefined variable named %s.', [2]),
        'E0104': make_templates('wrote a "return" that is outside of its function. You might have to change the indentation of the return statement.', 'used a return statement outside of a function.', []),
        'E0107': make_templates('have used an operator which does not exist in Python. Remember that for example the operators -- and ++ cannot be used in Python. Use += or -= instead!', 'used a non-existent operator, possibly a wrong pre-, post-increment or decrement operator.', []),
        'E1102': make_templates('accessed a non-callable object.','accessed a non-callable object', []),
        'E0211': make_templates('should use ''self'' as the first argument to instance methods and ''cls'' as first argument to class methods. The first argument of a method in Python must always be the object on which the method is invoked.', 'forgot to define an argument for a method. Remember that the first argument is always the bound instance.', []),
        'W0104': make_templates('included a statement which does not seem to have an effect. Maybe you did not finish writing in this line or you wanted to put a comment here.', 'used a statement which does not seem to have an effect', []),
        'W0301': make_templates('ended a statement by a semicolon, which is not necessary. Semicolons are not necessary in Python unless you are putting more than one statement in a line - that is not recommended anyway.', 'included an unnecessary semicolon.', []),
        'W0312': make_templates('should pay attention to the number of tabulations or spaces. Maybe you mixed tabs and spaces. Python interprets tabs and spaces differently, so consistent indentation is critical to the correct interpretation of blocks in Python syntax.', 'used an indent that is not consistent with the indent-string option. By default, indent-string is set to four spaces.', []),
        'W0613': make_templates('used an argument that is not used in the body of its function or method. Either use the argument or delete it in order to solve this error.', 'included an unused argument', []),

                 }
