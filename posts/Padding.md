<!-- 
.. link: 
.. description: 
.. tags: bash
.. date: 2014-12-12
.. title: Padding
.. slug: Padding
-->

Ok, it's the n-th time I search how to pad numbers in bash.    
I'll take a note here:

```bash
i=5
printf "%03d\n" $i
005
```

Something similar in Python and Go:

```python
t = "test-"
t.ljust(10, '0') # rjust for right padding

'test-00000'
```

```go
// LeftPad returns the string padded filling remaining left spaces to `length` with `pad`.
import "log"
import "strings"

func LeftPad(str, pad string, length int) string {
	var repeat int
	if (length-len(str))%len(pad) != 0 {
		log.Fatal("Can't pad ", str, " with ", pad, " to length ", length)
	} else {
		repeat = (length - len(str)) / len(pad)
	}
	return strings.Repeat(pad, repeat) + str
}
```

It is also possible to do this with `fmt` but you still need to compute the number 
of char if you want to maintain the total number of printed char.
