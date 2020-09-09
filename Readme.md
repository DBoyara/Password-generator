###### Simple password generator.

You can use it:

`git clone https://github.com/DBoyara/Password-generator.git`

`cd Password-generator`

And you can start without params:

`python gener_pass.py`

Have a result in console:

`Your strong password n1"7gBB2(GnJcQ with 14 symbols`

But you can use the following parameters:

_-u Required number of uppercase characters, **default=5**_

_-l The required number of lowercase characters, **default=4**_

_-n The required number of digits, **default=3**_

_-s Required number of special characters, **default=2**_

For example:

`python gener_pass.py -u 5 -l 1 -n 8 -s 5`

`Your strong password (174"SYE7p1V08V&>!9 with 19 symbols`

You can also pass an optional argument:

`python gener_pass.py -o`

`python gener_pass.py -u 5 -l 1 -n 8 -s 5 -o`

And get only the password, like here example:

`g"F1#JjFlX9Hk9`

`R!*S05:808$LZ"x8Z78`