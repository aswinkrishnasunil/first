from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse

from .models import table

from .forms import AddForm
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

def reg (request):
  if request.method == "POST":
    fname = request.POST.get('fname')
    lname = request.POST.get('lname') 
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirmpassword = request.POST.get('confirmpassword')
    gender = request.POST.get("gender")

    if confirmpassword == password :

      table(fname=fname,lname=lname,phone=phone,email=email,password=password,gender=gender).save()

      return render (request,"login.html")
    else:
      messages.error(request, 'password is not maching')
      print ("password is not same")
      return redirect ('reg')
      

  return render(request,'reg.html')

def login (request):
    return render (request,"login.html")

def loguser(request):
    if request.method== 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')
      cr = table.objects.filter(email=email, password=password)
      if cr:
        user_details=table.objects.get(email=email,password=password)
        id=user_details.id
        fname=user_details.fname
        lname=user_details.lname
        request.session['id']=id
        request.session['fname']=fname
        request.session['lname']=lname

        send_mail(
            'login',
            'Hi '+fname+ ',login sucessfully' ,
            'aswinkrishnasunil@gmail.com',
            [email],
            fail_silently=False,
)



        return redirect('wel')
      else:
        return render(request,'login.html')
    else:
        return render(request,'reg.html')



def wel (request):
  id = request.session['id']
  fname = request.session['fname']
  lname = request.session['lname']
  return render (request,'wel.html',{'id':id,'fname':fname,'lname':lname})

def view (request):
    cr = table.objects.all()
    return render (request,'view.html',{'cr':cr})

def update(request,pk):
  cr=table.objects.get(id=pk)
  form=AddForm(instance=cr)
  if request.method=="POST":
    form=AddForm(request.POST,instance=cr)
    if form.is_valid:
      form.save()
    redirect('wel')
  return render(request,"update.html",{'form':form})  
  

def delete(request,pk):
  cr = table.objects.get(id = pk)
  cr.delete()
  return redirect("view")

def detail(request,pk):
  cr = table.objects.get(id = pk)
  return render(request,"detail.html",{'cr':cr})
