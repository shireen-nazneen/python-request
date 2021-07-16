import requests
import json
result=requests.get("http://saral.navgurukul.org/api/courses")
data_1=(result.json())
def writingfile(fileName,var1):
    with open(fileName,"w")as f:
        json.dump(var1,f,indent=4)
        return f
def courses_1():
    count=1
    for course in data_1["availableCourses"]:
        print(count,course["name"],course["id"])
        count+=1
    select_course=int(input("select the course no---:"))
    print(data_1["availableCourses"][select_course-1]["name"])
    select_course_id=(data_1["availableCourses"][select_course-1]["id"])
    result2=requests.get("http://saral.navgurukul.org/api/courses/"+str(select_course_id)+"/exercises")
    data_2=result2.json()
    calling_writing_file=writingfile("ng_data2.json",data_2)
    b=[]
    count3=1
    for  perent in data_2["data"]:
        print(count3,perent["name"])
        b.append(perent["slug"])
        count3=count3+1
        for child in perent["childExercises"]:
            print("     ",count3,child["name"])
            b.append(child["slug"])
            count3+=1
    select_slug=int(input("enter slug-----:"))
    result3=requests.get("http://saral.navgurukul.org/api/courses/"+str(select_course_id)+"/exercise/getBySlug?slug="+str(b[select_slug-1]))
    r=result3.json()       
    slug1=writingfile("slug.json",r)
    print("-------------------")
    print("content",r["content"])                                                                    
courses_1()

