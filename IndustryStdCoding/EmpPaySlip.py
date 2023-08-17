#Program to generate an Emp Payslip - accepting empno, empname, basicsal

while(True):
    empno = int(input("Enter Employee number(200 - 500): "))
    if(empno<=500) and (empno>=200):
        break
    print("{} is invalid Employee Number, try again..")
#Employee Name
empname = input("Enter Employee Name")

#Basic Salary
while(True):
    basicsal = int(input("Enter Employee Basic Salary: "))
    if(basicsal>=10000):
        da = (basicsal/10)*100
        ta = (basicsal/15)*100
        cca = (basicsal/2)*100
        ma = (basicsal/2)*100
        hra = (basicsal/12)*100
        gpf = (basicsal/2)*100
        lic = (basicsal/1)*100
    else:
        if(0 < basicsal < 10000):
            da = (basicsal / 8) * 100
            ta = (basicsal / 9) * 100
            cca = (basicsal / 2) * 100
            ma = (basicsal / 1) * 100
            hra = (basicsal / 8) * 100
            gpf = (basicsal / 1) * 100
            lic = (basicsal / 1) * 100

# calculation
totalsal = basicsal + da + ta + cca + ma + hra - gpf + lic
