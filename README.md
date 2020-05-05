# degree-planner

oh man i really spent ~like 4 hours writing this huh~ way too long on this huh


## terminal usage

```
$ python classes.py [reqs_fulfill] [hardness] [output] [comp] [writing_intensive]

```

<sup>[some examples below &or;](#examples)<sup>


### to re-scrape the course names, etc. 

```
$ python scrape.py 
```

### add requirements you've filled to [taken.txt](user/taken.txt)

```
fcc_creative
plurdiv_d
```

`rc` required core 
`fcc` flexible common core 
`plurdiv_x` pluralism and diversity x (check [degreeworks](https://degreeworks.cuny.edu/) for your letters)


#### requirements fulfilled (required)
\# of requirements the classes fulfill


#### hardness (required)

*will not go above this the hardness you put i.e. `4` will give you all classes below 400* 

100-, 200-level courses — lower div courses 

300-, 400-level courses — upper div courses 

500-, 600-, 700-level courses — graduate courses


#### output file (required)

writes to `output/file_name.txt`


<!--
#### fulfilled requirements file (optional)

file name or &nbsp;&nbsp; `-` &nbsp;&nbsp; for none

reads from `user/file_name.txt`
-->


#### comparison (optional)

`>=` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **\[default]** &nbsp;&nbsp; i.e. 2 or more

`==` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i.e. exactly 1

`-` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for use with [writing intensive option](#writing-intensive), uses the  &nbsp; **\[default]** &nbsp;&nbsp; `>=`


#### writing intensive (optional)

`WI` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; writing intensives only

`-WI` &nbsp;&nbsp;&nbsp;&nbsp; no writing intensives



### examples

#### basic

```
$ python classes.py 2 4 out.txt
```


#### classes that fulfill 1 requirement
```
$ python classes.py 1 4 out.txt == 
```


#### writing intensive classes that fulfill 2 or more requirements 
```
$ python classes.py 2 4 out.txt - WI           // lazy way
$ python classes.py 2 4 out.txt >= WI
```


#### non-writing intensive classes that fulfill 1 requirement
```
$ python classes.py 1 4 out.txt == -WI
```

<!-- 
#### [ignore this] non-writing intensive classes that fulfill 2 requirements not in [taken.txt](user/taken.txt)
```
$ python classes.py 2 4 out.txt taken.txt == -WI
```
-->
