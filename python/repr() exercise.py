Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> today = datetime.datetime.now()
>>> today
datetime.datetime(2017, 8, 23, 13, 33, 10, 651454)
>>> repr(today)
'datetime.datetime(2017, 8, 23, 13, 33, 10, 651454)'
>>> str(today)
'2017-08-23 13:33:10.651454'
>>> eval(today)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    eval(today)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> 
