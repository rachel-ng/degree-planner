# degree-planner

oh man i really spent ~like 4 hours writing this huh~ way too long on this huh

***NOTE**&nbsp;&nbsp;&nbsp; not all classes are available at all times* 

## terminal usage

```
$ python classes.py [reqs_fulfill] [hardness] [output] [comp] [writing_intensive]

```

please also look at the ***[requirements fulfilled](#requirements-fulfilled)*** and ***[scraping courses](#scraping-courses)*** sections as well for more accurate info on your situation and on the courses! 


<sup>[some examples of terminal usage below &or;](#examples)<sup>


#### requirements fulfilled (required)

\# of requirements the classes fulfill
<sup>*can be adjusted with [comparison (optional)](#comparison-(optional))*</sup>

**NOTE**
- does not include [writing intensives](#writing-intensive)
- *you can not "double dip" with requirements i.e.*

  ```
  SPAN 26900 - Spanish American Women’s Literature and Cinema (W)    ['plurdiv_a', 'plurdiv_c', 'WI']
  http://catalog.hunter.cuny.edu/preview_course_nopop.php?catoid=39&coid=109908
  ```
  
  *only fulfills **1 (one)** of the **plurdiv (pluralism and diversity) requirements**, **not both***


#### hardness (required)

*will not go above the hardness you put i.e.*  
`4` will give you all classes **below** 400-level  
<sup>*it is not affected by the comparison (optional) used*</sup>

100-, 200-level courses — lower div courses 

300-, 400-level courses — upper div courses 

500-, 600-, 700-level courses — graduate courses


#### output file (required)

writes to `output/file_name.txt`


#### comparison (optional)

this only affects the \# of requirements considered fulfilled and does not include writing intensives 

`>=` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **\[default]** &nbsp;&nbsp; i.e. 2 or more

`==` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i.e. exactly 1

`-` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for use with [writing intensive option](#writing-intensive), uses the  &nbsp; **\[default]** &nbsp;&nbsp; `>=`


#### writing intensive (optional)

if you don't include this it will give you classes both with and without writing intensives &mdash; if you have a preference you'll have to include this  
<sup>not included in the number of requirements</sup>


`WI` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; writing intensives only

`-WI` &nbsp;&nbsp;&nbsp;&nbsp; no writing intensives



### [requirements](data/) fulfilled 

add [requirements](data/) you've fulfilled to [taken.txt](user/taken.txt)

*check [degreeworks](https://degreeworks.cuny.edu/) for everything, put them **exactly** as they correspond to the file names in **[requirements](data/) excluding the file extension*** 

```
rc_eng_comp
fcc_creative
plurdiv_d
```

`rc_whatever` required core (eng_comp, sci)

`fcc_whatever` flexible common core (creative, ind, us, world) 

`plurdiv_x` pluralism and diversity (a, b, c, d) 


### scraping courses

gets the names + a link to the course description 

```
$ python scrape.py 
```


## examples

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
