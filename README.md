# degree-planner

oh man i really spent ~like 4 hours writing this huh~ ~way too long~ far too long on this huh

<sup>you will need `pandas`, `bs4` `(beautifulsoup4)`</sup>

***NOTE**&nbsp;&nbsp;&nbsp; not all classes are available at all times* 



## terminal usage

<sub>follow the [installation instructions](#installation) if needed </sub>

```
(venv) $ python classes.py [reqs_fulfill] [hardness] [output] [comp] [writing_intensive]
```

```

CODE 10100 - Not A Real Class	['requirements', 'it', 'fulfills']
http://catalog.hunter.cuny.edu/preview_course_nopop.php?catoid=LINK&coid=TO_COURSE_DESCRIPTION

GERMN 24100 - German Fairy Tales in Translation (W)	['fcc_creative', 'plurdiv_d', 'WI']
http://catalog.hunter.cuny.edu/preview_course_nopop.php?catoid=39&coid=108730
 
```

please also look at the ***[requirements fulfilled](#requirements-fulfilled)*** and ***[scraping courses](#scraping-courses)*** sections as well for more accurate info on your situation and on the courses! 


<sup>[some examples of terminal usage below &or;](#examples)<sup>



#### requirements fulfilled (required)

\# of requirements the classes fulfill  
<sub>*can be adjusted with [comparison (optional)](#comparison-optional)*</sub>

**NOTE**
- does not include [writing intensives](#writing-intensive-optional)
- *you can not "double dip" with requirements i.e.*

  ```
  SPAN 26900 - Spanish American Women’s Literature and Cinema (W)    ['plurdiv_a', 'plurdiv_c', 'WI']
  http://catalog.hunter.cuny.edu/preview_course_nopop.php?catoid=39&coid=109908
  ```
  
  this "fulfills" `plurdiv_a` and `plurdiv_c` and it is a writing intensive class  
  *but it only fulfills **1 (one)** of the **plurdiv (pluralism and diversity) requirements**, **not both***


#### hardness (required)

*will not go above the hardness you put i.e.*  
`4` will give you all classes **below** 400-level  
<sub>*not affected by the [comparison (optional)](#comparison-optional) used*</sub>

100-, 200-level courses — lower div courses 

300-, 400-level courses — upper div courses 

500-, 600-, 700-level courses — graduate courses


#### output file (required)

writes to `output/file_name.txt`


#### comparison (optional)

this only affects the \# of requirements considered fulfilled and does not include [writing intensives](#writing-intensive-optional)

`>=` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **\[default]** &nbsp;&nbsp; i.e. 2 or more

`==` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i.e. exactly 1

`-` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for use with [writing intensive option](#writing-intensive-optional), uses the  &nbsp; **\[default]** &nbsp;&nbsp; `>=`


#### writing intensive (optional)

<sub>not included in the number of requirements</sub>


`WI` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; writing intensives only

`-WI` &nbsp;&nbsp;&nbsp;&nbsp; no writing intensives



### [requirements](data/) fulfilled 

```
fcc_creative
plurdiv_d
```

add [requirements](data/) you've fulfilled to [taken.txt](user/taken.txt)

*check [degreeworks](https://degreeworks.cuny.edu/) for everything, put them **exactly** as they correspond to the file names in **[requirements](data/) excluding the file extension*** 

`rc_whatever` required core  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `rc_eng_comp`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `rc_sci`  

`fcc_whatever` flexible common core  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `fcc_creative`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `fcc_ind`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `fcc_us`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `fcc_world`  

`plurdiv_x` pluralism and diversity  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `plurdiv_a`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `plurdiv_b`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `plurdiv_c`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `plurdiv_d`  


### scraping courses

gets the names + a link to the course description 

```
(venv) $ python scrape.py 
```


## installation 

1. activate your virtual environment (make it if you don't have one)

 ```
 $ python3 -m venv venv
 $ . path/to/venv/bin/activate
 ```

2. upgrade `pip` and install the dependencies using `requirements.txt`

 ```
 (venv) $ pip install --upgrade pip
 (venv) $ pip install -r requirements.txt
 ```

3. you're ready to go! 



## examples

#### basic

```
(venv) $ python classes.py 2 4 out.txt
```


#### classes that fulfill 1 requirement
```
(venv) $ python classes.py 1 4 out.txt == 
```


#### writing intensive classes that fulfill 2 or more requirements 
```
(venv) $ python classes.py 2 4 out.txt - WI           // lazy way
(venv) $ python classes.py 2 4 out.txt >= WI
```


#### non-writing intensive classes that fulfill 1 requirement
```
(venv) $ python classes.py 1 4 out.txt == -WI
```
