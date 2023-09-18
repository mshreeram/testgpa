from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Marks, Profile
from django.contrib import messages
from django.contrib.auth.models import User, auth

lst = [{"id": 0, "name": "delete me", "credit": 3, "grade": 10}]
curr = 0
def index(req):
  if req.method == "POST":
    name = req.POST["subName"]
    credit = float(req.POST["credit"])
    grade = int(req.POST["grade"])
    global curr
    curr = curr + 1
    curr_sub_score = {
      "id": curr,
      "name": name,
      "credit": credit,
      "grade": grade
    }

    lst.append(curr_sub_score)
    total = 0
    credsum = 0
    gpa = 0
    for i in range(0, len(lst)):
      total = total + (lst[i]["credit"] * lst[i]["grade"])

    for i in range(0, len(lst)):
      credsum = credsum + lst[i]["credit"]

    gpa = total / credsum
    return render(req, 'index.html', {"lst": lst, "gpa": gpa} )
  
  else:
    total = 0
    credsum = 0
    gpa = 0
    for i in range(0, len(lst)):
      total = total + (lst[i]["credit"] * lst[i]["grade"])

    for i in range(0, len(lst)):
      credsum = credsum + lst[i]["credit"]

    if credsum == 0:
      credsum = 1
    
    gpa = total / credsum
    return render(req, 'index.html', {"lst": lst, "gpa": gpa})
    

def dashboard(req):
  current_user = req.user
  if req.user.is_authenticated:
    prof = Profile.objects.filter(factor = current_user.username)
    user_first_name = req.user.first_name
    print(user_first_name)
    # targetgpa = float(prof[0].targetgpa)
    nosc = int(prof[0].nosc)

    lst = [prof[0].Sem1, prof[0].Sem2, prof[0].Sem3, prof[0].Sem4, prof[0].Sem5, prof[0].Sem6, prof[0].Sem7, prof[0].Sem8]

    creds = [19.5, 19.5, 21.5, 21.5, 21.5, 21.5, 23, 12]

    sum = 0
    cred_sum = 0
    for i in range(0, nosc):
      sum = sum + (lst[i] * creds[i])
      cred_sum = cred_sum + creds[i]
    total = sum / cred_sum

    try:
        while True:
            lst.remove(0)
    except ValueError:
        pass


    return render(req, "dashboard.html", { "user_first_name": user_first_name,"nosc": nosc, "lst": lst, "size": range(0, nosc), "total": round(total, 2)})
  else:
    return redirect("login")

def register(req):
  if req.method == "POST":
    first_name = req.POST["first_name"]
    last_name = req.POST["last_name"]
    username = req.POST["username"]
    email = req.POST["email"]
    password1 = req.POST["password1"]
    password2 = req.POST["password2"]
    if password1 == password2:
      if User.objects.filter(username=username).exists():
        messages.info(req, "Username already taken")
      elif User.objects.filter(email=email).exists():
        messages.info(req, "email already taken")
      else:
        user = User.objects.create_user(username= username, password= password1, first_name= first_name, last_name= last_name, email= email)
        user.save()
        messages.info(req, "User created successfully")
        return redirect("/login")
    else:
      messages.info(req, "password not matched")
    return redirect("register")
  else:
    return render(req, "register.html")
  
def login(req):
  if req.method == "POST":
    username = req.POST["username"]
    password = req.POST["password"]
    user = auth.authenticate(username= username, password= password)

    if user is not None:
      auth.login(req, user)
      try:
        current_user = req.user
        prof = Profile.objects.filter(factor = current_user.username)
        targetgpa = float(prof[0].targetgpa)
        return redirect("/dashboard")
      except:
        return redirect("/profile")
    else:
      messages.info(req, "invalid credintails")
      return redirect("login")

  else:
    if req.user.is_authenticated:
      return redirect("/dashboard")
    return render(req, "login.html")
  
def logout(req):
  auth.logout(req)
  return redirect("/")

def delete(req):
  if req.method == 'POST':
    sub_id = int(req.POST['sub_id'])
    for i in range(0, len(lst)):
      if (lst[i]["id"] == sub_id):
        lst.remove(lst[i])
        break
    return redirect("../")
  
def profile(req):
  current_user = req.user
  nosc = Profile.objects.filter(factor = current_user.username)
  if nosc:
    context = int(nosc[0].nosc)
  else:
    context = 0
  return render(req, "profile.html", {"nosc": range(1, context + 1), })

def addTarget(req):
  if req.method == "POST":
    # targetgpa = float(req.POST["target-gpa"])
    nosc = float(req.POST["no-sem-completed"])
    obj = Profile()
    obj.factor = req.user.username
    # obj.targetgpa = targetgpa
    obj.nosc = nosc
    obj.save()
    return redirect("../addSem")

def addSem(req):
  sems = []
  current_user = req.user
  prof = Profile.objects.filter(factor = current_user.username)

  # targetgpa = float(prof[0].targetgpa)
  nosc = int(prof[0].nosc)
  curr_prof = Profile()
  if req.method == "POST":
    current_user = req.user
    prof = Profile.objects.filter(factor = current_user.username)
    curr_prof.factor = current_user.username

    # targetgpa = float(prof[0].targetgpa)
    nosc = int(prof[0].nosc)

    # curr_prof.targetgpa = targetgpa
    curr_prof.nosc = nosc

    if prof:
      prof = int(prof[0].nosc)
    for i in range(1, prof + 1):
      sems.append(float(req.POST["sem" + str(i)]))
    

    sems_len = len(sems)
    i = 0
    if i < sems_len:
      curr_prof.Sem1 = sems[0]
      i = i + 1

    if i < sems_len:
      curr_prof.Sem2 = sems[1]
      i = i + 1

    if i < sems_len:
      curr_prof.Sem3 = sems[2]
      i = i + 1

    if i < sems_len:
      curr_prof.Sem4 = sems[3]
      i = i + 1

    if i < sems_len:
      curr_prof.Sem5 = sems[4]
      i = i + 1

    if i < sems_len:
      curr_prof.Sem6 = sems[5]
      i = i + 1

    if i < sems_len:
      curr_prof.Sem7 = sems[6]
      i = i + 1

    if i < sems_len:
      curr_prof.Sem8 = sems[7]

    curr_prof.save()
    return redirect("../../dashboard")
  else:
    return render(req, "addSem.html", {"nosc": range(1, nosc + 1)})


