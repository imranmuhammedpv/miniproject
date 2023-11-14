from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import auth
from .models import bank
# Create your views here.
def homebank(request):
    return render(request,'HOME.html')

def regbank(request):
    if request.method=='POST':
        name=request.POST['name']
        acc_no=int(request.POST['acc_no'])
        phno=int(request.POST['phno'])
        amount=int(request.POST['amount'])
        if amount<1000:
            context={
                'message':'minimum balance 1000'
            }
            return render(request,'bank.html',context)
        else:
         try:
            data=bank.objects.create(name=name,acc_no=acc_no,phno=phno,amount=amount)
            data.save()
            context={
                'message2':'account created successfully'
            }
            return render(request,'bank.html',context)
         except Exception:
            context={
                'message':'account number alreadt exists'
            }
            return render(request,'bank.hyml',context)
    else:
        return render(request,'bank.html',)



def log(request):
    if request.method =='POST':
        name=request.POST['name']
        acc_no=request.POST['acc-no']
        data10=bank.objects.get(acc_no=acc_no)
        if data10 is not None:
            data10=auth.login(request,data10)
            return render(request,'profile.html',{'data11':data10})
    else:
        return render(request,'log.html')



#def profile(request):
    #if 'acc_no' in request.session:
        #acc_no=request.session['acc_no']
        #if request.method =='GET':
            #data15=bank.objects.filter(acc_no=acc_no).all()
            #return render(request,'profile.html',{'data16':data15})
def balance(request):
    if request.method=='POST':
        acc_no=request.POST['acc_no']
        data17=bank.objects.get(acc_no=acc_no)
        return render(request,'balance.html',context={'data18':data17.amount,'message':'balance Amount is','balance':balance})
    else:
        return render(request,'balance.html')
def deposit(request):
    if request.method=='POST':
        acc_no=request.POST['acc_no']
        deposit=int(request.POST['deposit'])
        data20=bank.objects.get(acc_no=acc_no)
        data20.amount=data20.amount+deposit
        data20.save()
        return render(request,'deposit.html',context={'rs':'RS','deposit':deposit,'d':'deposited'})
    else:
        return render(request,'deposit.html')

def withdraw(request):
    if request.method=='POST':
      acc_no=request.POST['acc_no']
      withdraw=int(request.POST['withdraw'])
      data23=bank.objects.get(acc_no=acc_no)
      data23.amount=data23.amount-withdraw
      data23.save()
      return render(request,'withdraw.html',context={'message':'withdrawn','rs':'RS','withdraw':withdraw})
    else:
        return render(request,'withdraw.html')