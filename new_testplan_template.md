### Topics covered (in the order that they appear):

* `import` statement
* Instance of class
  * creating (without parameters)
  * accessing attributes of instances
  * creating (with parameters)
  * calling methods
* Functions
  * calling (with no return)
* Dictionaries
  * indexing
* Looping
  * for-loop
* 
*

### Exploring

Serial | Useful code snippets | WHY
------ | ------- | -------
1 | `print_matrix(myGame.PLAY_AREA)`| * what `import`ing does
-------- | ------ | * creating an instance
-------- | ------ | * accessing an attribute of a class
-------- | ------ | * calling a function
2 | `print_matrix(TETRAMINO_DICT['I'])` | * better understanding of calling a function
-------- | ------ | * dictionary and indexing its elements
3 | `# print all available tetraminos` | * do it the dumb way
-------- | ------ | * use loops and do it the smart way
4 | `# print rotated tetramino` | --------
-------- | `tetramino = Tetramino('I')` | * better intuition about classes and objects and their usefulness
-------- | `tetramino.rotate_cw()` | * accessing methods of an object
-------- | ------ | * compare with the "objectless" function - `print_matrix()` above
5 | `print_matrix(tetramino.get_matrix())` | * first introduction to methods that return something
6 | `myGame.set_spawned_tetramino('I', 0, 3)` | * parameter passing in methods
-------- | ------ | * differentiate between strings and integer values
7 | `# set the active tetramino in some other position and print the matrix` | * piece together everything

### Using
* __Make participants acquainted with the "reading code" part of the programming exp__
* __Read the already created classes and functions and reuse them in the `learntris` module to pass the tests__
* __After the participant successfully passes each test, we tell them what knowledgeable insights they should have taken from the related code__

Serial | Useful code snippets | WHY
------ | ------- | -------
1 | ------- | input 'q' to quit
2 | ------- | input 'p' to print the play-area
3 | ------- | input 'I/O/L/Z/T/S/J' to set it as active tetramino
4 | ------- | input '(' to rotate tetramino clockwise
5 | ------- | 


### Creating
* __Participant needs to write/modify functions and methods in the `tetramino`, `Game` and `helper` modules and finally use them in the learntris module to pass the tests__

Serial | Useful code snippets | WHY
------ | ------- | -------
1 | ------- | ---------
