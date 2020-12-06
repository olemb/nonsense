# Compile Hello World into C macro Brainfudge.
hello = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
instructions = {
    '+': 'I',    # increment
    '-': 'D',    # decrement
    '>': 'R',    # right
    '<': 'L',    # left
    '.': 'P',    # put
    ',': 'G',    # get
    '[': 'W',    # while
    ']': 'E',    # end
}

print('#include "bf.h"')
print('B', end=' ')
for char in hello:
    print(instructions[char], end=' ')
print('E')
