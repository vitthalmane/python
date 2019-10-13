from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import EmpData

# Create your views here.
def EmpReg(request):
    return render(request,"EmployeeData/registration.html")

    
def DisplayEmpData(request):
    all_Emp_data=EmpData.objects.all()
        #return HttpResponse("Success")
    return render(request,"EmployeeData/EmployeesData.html",{'Emp_savedData':all_Emp_data})
    

def SaveEmpData(request):
    #if (request.method=='POST'):
    empName=request.POST.get('emp_name','NA')
    emailadd=request.POST.get('email','NA')
    phoneNo=request.POST.get('mob_no','00')
    department=request.POST.get('department','NA')
        
    if(request.POST.get('department','NA')==""):
        department="NA"
    print(empName,emailadd,phoneNo,department)
    obj=EmpData(Emp_name=empName,Emp_email=emailadd,Emp_phonNO=phoneNo,Emp_dept=department)
    obj.save()
    
       
    request.method=="GET"
    
        #return HttpResponse("Success")
    all_Emp_data=EmpData.objects.all()
    return redirect(DisplayEmpData)
    #return render(request,"EmployeeData/EmployeesData.html",{'Emp_savedData':all_Emp_data})

    

