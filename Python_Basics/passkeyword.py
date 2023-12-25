# The pass keyword represents a null operation in Python. 
# It is generally used for the purpose of filling up empty blocks of code which may execute during runtime but has yet to be written.
# Without the pass statement in the following code,
# we may run into some errors during code execution.
def myEmptyFunc():
   # do nothing
   pass
myEmptyFunc()    # nothing happens
## Without the pass keyword
# File "<stdin>", line 3
# IndentationError: expected an indented block
