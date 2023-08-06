# TerminalTyping
Module for terminal type effects  

## Documentation

[argument] - required  
<argument\> - optional.  


### Typing 
A class that serves as the overarching class. To use any of the following functions, it must be defined.
```py 
import TerminalTyping

typing = TerminalTyping.Typing()
```

### Typing.ttype([word:string], <rgb:list>, <delay:float>, <instant:boolean>, <newline:boolean>) 
  
*word: What will be passed in to "type" to the terminal*

*rgb: The color of the text. [r value, g value, b value]. Defaults to black [0,0,0]*  
  
*delay: the delay between each character in seconds.*  
  
*instant: an alternative to delay=0. The full string will be passed in all at once. Defaults to false*  
  
*newline: whether or not a new line is created after the typing is done. Defaults to true.*

```py
import TerminalTyping

typing = TerminalTyping.Typing()
typing.ttype("word",[1,255,0],1,False, True)
```
