# sql-type_language
Implementation of an sql type language with python



**Here is an example code:**


mem=Table('student', srid=[int], name=[str], marks=[int])

mem.addrow([1,'siddharth',94])

mem.addrow([2,'dhiman',90])

mem.addrow([3,'chirag',92])

mem.addrow([4,'parth',65])

mem.addcol('age', int, [17,17,17,17])

mem.col_operations('+','srid','marks','age')

mem.col_operations('*','srid','marks','age')

mem.select()

mem.edit('parth','name','suman')

mem.select()
