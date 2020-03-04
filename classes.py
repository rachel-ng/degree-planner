#!/usr/bin/python

import sys, os, copy

#print(os.listdir('.'))

def descriptions(): 
    # scraped course data -- scrape.py
    # course id, name of course, link
    fin = open(os.getcwd() + "/data/" + "courses.txt")
    course_raw = [i.replace("-","**",1).split("*") for i in fin.read().split("\n") if i != ""]
    course_desc = {i[0].split("(")[0].strip():[i[-2].strip(), "http://catalog.hunter.cuny.edu/" + i[-1]] for i in course_raw}
    fin.close()
    return course_desc


def courses_fulfill():
    files = [f for f in os.listdir(os.getcwd() + '/data') if f != "classes.py" and f != "scrape.py" and f!= "courses.txt" and f[-4:] == ".txt"] 
    names = [f[0:-4] for f in files] 
    dicts = []

    print(files)
    print("\n\n")

    cl_ind = set()
    for f in files:
        fin = open(os.getcwd() + '/data/' + f,"r")

        # clean up data 
        clean_1 = [i.replace(" ","").split("|") for i in fin.read().split("\n") if i != ""]
        clean_2 = [[i[0] + " " + k for k in i[1].split("or") if k != ""] for i in clean_1]

        # flatten list, turn into set
        cat_classes = set(item for sublist in clean_2 for item in sublist)
        
        dicts.append(cat_classes)
        cl_ind.update(cat_classes)
        
        fin.close()

    # requirements: courses that fulfill it 
    d = dict(zip(names,dicts))

    return cl_ind, d


def courses_exclude():
    fin = open(os.getcwd() + '/user/taken.txt',"r")
    classes = [i for i in fin.read().split("\n") if i!= ""] 
    return classes

def fulfillments(cl_ind, d, course_desc, excl):
    fulfills = {i:0 for i in cl_ind}
    reqs = {i:[] for i in cl_ind}
    reqs_real = {i:set() for i in cl_ind}
    lengths = {0 : 0, 1 : 0, 2 : 0, 3 : 0}
    wi = set()
    
    # number of and which specific requirements a class fulfills
    for i in d: 
        for n in d[i]:
            #fulfills[n] += 1
            if i not in excl: 
                reqs[n].append(i)
                reqs_real[n].add(i.split('plurdiv_')[0])
            if course_desc.get(n):
                if len(course_desc.get(n)[0].split("(W)")) > 1:
                    wi.add(n)
            fulfills[n] = len(reqs_real[n])
                # find the number of classes the fulfill X requirements
    for i in fulfills: 
        lengths[fulfills[i]] += 1
  
    return fulfills, {i:(reqs[i]+["WI"] if (i in wi) else reqs[i]) for i in reqs}, wi


def seek(fulfills, reqs, wi, course_desc, n, hardness, out, comp=">=", w=""):
    ok = {}

    if comp == ">=":
        if w == "WI":
            ok = {i : reqs[i] for i in fulfills if fulfills[i] >= int(n) and "WI" in reqs[i]}
        elif w == "-WI":
            ok = {i : reqs[i] for i in fulfills if fulfills[i] >= int(n) and "WI" not in reqs[i]}
        else: 
            ok = {i : reqs[i] for i in fulfills if fulfills[i] >= int(n)}

    if comp == "==":
        if w == "WI":
            ok = {i : reqs[i] for i in fulfills if fulfills[i] == int(n) and "WI" in reqs[i]}
        elif w == "-WI":
            ok = {i : reqs[i] for i in fulfills if fulfills[i] == int(n) and "WI" not in reqs[i]}
        else:
            ok = {i : reqs[i] for i in fulfills if fulfills[i] == int(n)}

    if comp == "-":
        if w == "WI":
            ok = {i : reqs[i] for i in fulfills if fulfills[i] >= int(n) and "WI" in reqs[i]}
        elif w == "-WI":
            ok = {i : reqs[i] for i in fulfills if fulfills[i] >= int(n) and "WI" not in reqs[i]}

    '''
    if fulfilled != "-":
        fin = open("user/" + fulfilled, "r")
        completed = [i for i in fin.read().split("\n") if i != ""]
        fin.close()
        
        print(completed)
        
        good = copy.deepcopy(ok) 
        for i in ok:
            print(good[i])
            for n in completed: 
                if n in ok[i]:
                    good.pop(i, None)
                    break
            print(good[i])
            print("")
    else:
    '''    

    good = copy.deepcopy(ok) 
    
    alph = sorted(good.keys())
    bb = ""

    for i in alph: 
        l = i.split(" ")
        if int(l[1][0]) < int(hardness): 
            c = ""
            l = "\n"
            alt_name_1 = i[:-2] + "00"
            alt_name_2 = i[:-2] + "XX"
            if course_desc.get(i):
                c += " - " + course_desc.get(i)[0]
                l += course_desc.get(i)[1] + "\n"
            elif i != alt_name_1 and course_desc.get(alt_name_1):
                c += " (" + alt_name_1 + ") - " + course_desc.get(alt_name_1)[0]
                l += course_desc.get(alt_name_1)[1] + "\n"
            elif i != alt_name_2 and course_desc.get(alt_name_2):
                c += " (" + alt_name_2 + ") - " + course_desc.get(alt_name_2)[0]
                l += course_desc.get(alt_name_2)[1] + "\n"

            if (course_desc.get(i)):
                bb += i + c + "\t" + str(good[i]) + l + "\n" 
                print(i + c + "\t" + str(good[i]) + l)

    f = open("output/" + out, "w")
    f.write(bb)
    f.close()


if __name__ == "__main__":
    desc = descriptions()
    ci, dct = courses_fulfill()
    excl = courses_exclude()
    fulfills, reqs, wi = fulfillments(ci, dct, desc, excl)
    seek(fulfills, reqs, wi, desc, sys.argv[1], sys.argv[2], sys.argv[3], **dict(zip(["comp","w"],sys.argv[4:])))

