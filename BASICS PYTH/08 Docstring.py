# ------   Docstring are string literals the appers just below the function, method , class, or module

def table_of(n):
    # make sure to not write code here else the string below will not be docstring anymore
    '''Takes the number                                     
    And print it's table'''
    
    for i in range(1,11) :
        print(f"{n} X {i} = {n*i}")

table_of(4)
print(table_of.__doc__)             # Unlike comments it is not ignored by the interpreter , so we can acesses it by using this command  



import this          # Zen Of Python



'''PEP 8 is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.'''