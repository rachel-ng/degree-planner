# degree-planner

oh man i really spent like 4 hours writing this huh 

## terminal usage

```
$ python classes.py [requirements fulfilled] [hardness] [output file] [comparison] [writing intensive]
```

#### comparison (optional)

`>=` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **\[default]** &nbsp;&nbsp; i.e. 2 or more

`==` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i.e. exactly 1

`-` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for use with [writing intensive option](#writing-intensive) uses the **\[default]** `>=`


#### writing intensive (optional)

`WI` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; writing intensives only

`-WI` &nbsp;&nbsp;&nbsp;&nbsp; no writing intensives


### examples

```
$ python classes.py 2 4 out.txt
```

classes that fulfill 1 requirement
```
$ python classes.py 1 4 out.txt == 
```

writing intensive classes that fulfill 2 or more requirements 
```
$ python classes.py 2 4 out.txt - WI           // lazy way
$ python classes.py 2 4 out.txt >= WI
```

non-writing intensive classes that fulfill 1 requirement
```
$ python classes.py 1 4 out.txt == -WI
```
