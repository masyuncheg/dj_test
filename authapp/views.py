from django.shortcuts import render
import MySQLdb
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.http import JsonResponse
from django.shortcuts import render

def db_con():
    return MySQLdb.connect(host='localhost', user='maksim',passwd='1234',db='test',charset='utf8mb4')

@ensure_csrf_cookie
def auth_form_view(request):
    if request.method=='POST':

        login=request.POST.get('login')
        password=request.POST.get('password')

        if not login:
            return JsonResponse({'error':'Заполните логин.'},status=400)

        if not password:
            return JsonResponse({'error':'Заполните пароль.'},status=400)
    
        con=db_con()
        cursor=con.cursor()
        cursor.execute("SELECT * FROM users WHERE login=%s and password=%s",(login,password))
        check=cursor.fetchone()
        cursor.close()
        con.close()

        if check:
            return JsonResponse({'success':'Успешно'})
        else:
            return JsonResponse({'error':'Неверный логин или пароль'},status=400)
    
    if request.method=='GET':
        return render(request,'authapp/log.html')
    
@ensure_csrf_cookie
def reg_form_view(request):
    if request.method=='POST':
        login=request.POST.get('login')
        password=request.POST.get('password')

        if not login or not password:
            return JsonResponse({'error':'Запоните все поля'},status=400)
        

        con=db_con()
        cursor=con.cursor()
        cursor.execute("SELECT * FROM users WHERE login=%s",(login,))

        check_log=cursor.fetchone()
        if check_log:
            cursor.close()
            con.close()
            return JsonResponse({'error':'Такой логин занят'},status=400)
        
        cursor.execute("INSERT INTO users (login, password) VALUES (%s, %s)",(login, password))
        con.commit()
        cursor.close()
        con.close()
        return JsonResponse({'success':'Вы успешно зарегистрировались'})
    if request.method=='GET':
        return render(request, 'authapp/reg.html')  
            




        

    


