# Tests

## Resources

[Pickling](https://pythontips.com/2013/08/02/what-is-pickle-in-python/ "Python Tips")

## Terminology

```python
import pickle
```

Pickling is a way to convert
a python object (list, dict, etc.)
into a character stream

The idea is that this character stream
contains all the information necessary
to reconstruct the object in another python script

pickle has two main methods

- dump()
  The first one is dump,
  which dumps an object to a file object

- load()
  and the second one is load,
  which loads an object from a file object

```python
import pickle

a = ['test value','test value 2','test value 3']
a
['test value','test value 2','test value 3']

file_Name = "testfile"
# open the file for writing
fileObject = open(file_Name,'wb')

# this writes the object a to the
# file named 'testfile'
pickle.dump(a,fileObject)

# here we close the fileObject
fileObject.close()
# we open the file for reading
fileObject = open(file_Name,'r')
# load the object from the file into var b
b = pickle.load(fileObject)
b
['test value','test value 2','test value 3']
a==b
True
```
