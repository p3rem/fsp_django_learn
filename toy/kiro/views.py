
import email
from django.shortcuts import render , redirect
from django.http import HttpResponse, FileResponse
from kiro.models import *
import requests
import os 
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def send_email(request):
    send_mail(
        'Welcome to Kiro App',
        'Thank you for registering with Kiro App. We are excited to have you on board!',
        settings.EMAIL_HOST_USER,
        ['ppp046959@gmail.com'],  # Replace with actual recipient email
        fail_silently=False,
    )
    return HttpResponse("Email sent successfully!")


def test(request):
    return HttpResponse("This is a test view in kiro app.")

def test2(request):
    return HttpResponse("testing 2 view in kiro app.")

def index(request):

    email = request.session.get('email', None)
    return render(request, 'index.html', {'email': email})

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    # If user already logged in, redirect to index
    if 'email' in request.session:
        return redirect('/kiro/index')
    return render(request, 'login.html')

def login_check(request):
    error = None
    email = request.GET.get('email', '')
    password = request.GET.get('password', '')
    
    users = user.objects.filter(email=email, password=password)
    
    if users.exists():
        request.session['email'] = email
        return redirect('/kiro/index')
    else:
        error = "Invalid email or password"
    
    return render(request, 'login.html', {'error': error})

def add(request):
    return render(request, 'add.html')

def sum(request):
    a1= int(request.GET['a1'])
    a2= int(request.GET['a2'])
    res= a1 + a2
    return HttpResponse(f"The sum of {a1} and {a2} is {res}.")
def evenorodd(request):
    return render(request, 'evenorodd.html')

def eoo(request):
    n = int(request.GET['n'])
    if n % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    return HttpResponse(f'the number {n} is {result}.')
def fibonacci(request):
    return render(request, 'fibonacci.html')

def fibo(request):
    a1 = int(request.GET['a1'])
    fib_sequence = []
    a, b = 0, 1
    for _ in range(a1):
        fib_sequence.append(a)
        a, b = b, a + b
    return HttpResponse(f'The Fibonacci sequence up to {a1} terms is: {fib_sequence}.')
def calculator(request):
    result = None

    if request.method == 'GET' and 'operation' in request.GET:
        try:
            a1 = int(request.GET.get('a1'))
            a2 = int(request.GET.get('a2'))
            operation = request.GET.get('operation')

            if operation == 'addc':
                result = a1 + a2

            elif operation == 'subtractc':
                result = a1 - a2

            elif operation == 'multiplyc':
                result = a1 * a2

            elif operation == 'dividec':
                if a2 == 0:
                    result = "Division by zero error"
                else:
                    result = a1 / a2

        except (TypeError, ValueError):
            result = "Invalid input"

    return render(request, 'calculator.html', {'result': result})

def insert(request):
    return render(request, 'insert.html')

def ins(request):
    if request.GET.get('a1'):
        u = user()
        u.name = request.GET.get('a1')
        u.email = request.GET.get('a2')
        u.password = request.GET.get('a3')
        u.phno = request.GET.get('a4')
        u.age = request.GET.get('a5')
        u.save()
    return render(request, 'insert.html')

def student_input(request):
    return render(request, 'student.html')
    
def student_entry(request):
    if request.GET.get('b1'):
        s = student()
        s.first_name = request.GET.get('b1')
        s.last_name = request.GET.get('b2')
        s.address = request.GET.get('b3')
        s.pincode = request.GET.get('b4')
        s.city = request.GET.get('b5')
        s.state = request.GET.get('b6')                
        s.father_name = request.GET.get('b7')
        s.mother_name = request.GET.get('b8')
        s.phno = request.GET.get('b9')
        s.emailid = request.GET.get('b10')
        s.adhaar_no = request.GET.get('b11')
        s.save()
    
    return render(request, 'student.html')

def show(request):
    if 'email' not in request.session:
        return redirect('/kiro/login')
    u = user.objects.all()
    return render(request, 'show.html', {'u': u})

def delta(request, id):
    if 'email' not in request.session:
        return redirect('/kiro/login')
    u = user.objects.get(id=id)
    u.delete()
    return redirect('../show')

def edit(request,id):
    if 'email' not in request.session:
        return redirect('/kiro/login')
    u=user.objects.get(id=id)
    return render(request,'edit.html',{'u':u})

def upd(request,id):
    if 'email' not in request.session:
        return redirect('/kiro/login')
    u = user.objects.get(id=id)
    params = request.POST if request.method == 'POST' else request.GET
    u.name = params.get('a1', u.name)
    u.email = params.get('a2', u.email)
    u.password = params.get('a3', u.password)
    u.phno = params.get('a4', u.phno)
    u.age = params.get('a5', u.age)
    u.save()
    return redirect('../show')

def ed(request,id):
    if 'email' not in request.session:
        return redirect('/kiro/login')
    s = student.objects.get(id=id)
    return render(request, 'ed.html', {'s': s})

def update(request,id):
    if 'email' not in request.session:
        return redirect('/kiro/login')
    s = student.objects.get(id=id)
    params = request.POST if request.method == 'POST' else request.GET
    s.first_name = params.get('b1', s.first_name)
    s.last_name = params.get('b2', s.last_name)
    s.address = params.get('b3', s.address)
    s.pincode = params.get('b4', s.pincode)
    s.city = params.get('b5', s.city)
    s.state = params.get('b6', s.state)
    s.father_name = params.get('b7', s.father_name)
    s.mother_name = params.get('b8', s.mother_name)
    s.phno = params.get('b9', s.phno)
    s.emailid = params.get('b10', s.emailid)
    s.adhaar_no = params.get('b11', s.adhaar_no)
    s.save()
    return redirect('../show_student')

def show_student(request):
    if 'email' not in request.session:
        return redirect('/kiro/login')
    s = student.objects.all()
    return render(request, 'show_student.html', {'s': s})

def sdel(request, id):
    if 'email' not in request.session:
        return redirect('/kiro/login')
    s = student.objects.get(id=id)
    s.delete()
    return redirect('../show_student')

def search(request):
    return render(request, 'search.html')

def ser(request):
    a=request.GET['s1']
    s=student.objects.filter(dept=a)

def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect('/kiro/index')

def log(request):
    error = None
    a = request.GET.get('a1', '')
    n = request.GET.get('a2', '')
    
    if a and n:
        if user.objects.filter(email=a, password=n).exists():
            u = user.objects.filter(email=a, password=n).first()
            x = {'name': u.name, 'email': u.email}
            request.session['aec'] = x
            return render(request, 'show.html')
        else:
            error = "Invalid email or password"
    
    return render(request, 'log.html', {'error': error})

def pfile(request):
    return render(request, 'upload.html')

def is_valid_file_upload(file):
    """
    Validates that the uploaded file is either a PDF or an image.
    Returns tuple (is_valid, error_message)
    """

    allowed_mimes = [
        'application/pdf',  
        'image/jpeg',      
        'image/png',       
        'image/gif',    
        'image/webp',    
        'image/bmp',       
        'image/tiff'        
    ]
    
    allowed_extensions = ['.pdf', '.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.tiff']
    
    
    if file.content_type not in allowed_mimes:
        return False, "Invalid file type. Only PDF and image files are allowed"
    
    
    file_name = str(file.name).lower()
    if not any(file_name.endswith(ext) for ext in allowed_extensions):
        return False, "Invalid file extension. Only PDF and image files are allowed"
    
    return True, None

def handle_uploaded_file(file, filename):
    if not os.path.exists('kiro/static/upload/'):
        os.mkdir('kiro/static/upload/')
    with open('kiro/static/upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def upload(request):
    error = None
    if request.method == 'POST' and 'a2' in request.FILES:
        uploaded_file = request.FILES['a2']
        
    
        is_valid, error_msg = is_valid_file_upload(uploaded_file)
        
        if not is_valid:
            error = error_msg
            return render(request, 'upload.html', {'error': error})
        
        handle_uploaded_file(uploaded_file, str(uploaded_file))
        url = "upload/" + str(uploaded_file)
        u = picfile()
        u.fname = request.POST.get('a1', '')
        u.furl = url
        u.save()
        return redirect('../show_upload')
    
    return render(request, 'upload.html', {'error': error})

def show_upload(request):
    files = picfile.objects.all()
    return render(request, 'show_upload.html', {'files': files})

def download_file(request, file_id):
    try:
        file_obj = picfile.objects.get(id=file_id)
        # Get the full file path from Django's storage
        file_path = file_obj.furl.path
        
        if os.path.exists(file_path):
            response = FileResponse(open(file_path, 'rb'), as_attachment=True)
            response['Content-Disposition'] = f'attachment; filename="{file_obj.fname}"'
            return response
        else:
            return HttpResponse("File not found", status=404)
    except picfile.DoesNotExist:
        return HttpResponse("File record not found", status=404)
    except Exception as e:
        return HttpResponse(f"Error downloading file: {str(e)}", status=500)


def weather_view(request):
    city=request.GET.get('city','Kolkata') 
    api_key='55a5b4e1ae3fc66a14c425550f70544a'
    url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response=requests.get(url)
    data=response.json()
    weather_data={
        'city':city,
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'temp_min':data['main']['temp_min'],
        'temp_max':data['main']['temp_max'],
        'pressure':data['main']['pressure'],
        'sea_level':data['main']['sea_level'],
        'ground_level':data['main']['ground_level'],
        'main':data['weather'][0]['main'],
        'description':data['weather'][0]['description'],
        'icon':data['weather'][0]['icon'],
        'country': data['sys']['country'],
        'sunrise': data['sys']['sunrise'],
        'sunset':data['sys']['sunset'],
        'coordinates': data['coord'],
        'weather': data['weather'],
        'wind': data['wind'],
        'clouds': data['clouds'],
        'feels_like':data['main']['feels_like'], 
        'visibilty':data['visibility'],
        'sys':data['sys'],
        'timezone':data['timezone'],
        'name':data['name'],
        'cod':data['cod'],

        # {"coord":{"lon":86.9833,"lat":23.6833},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"base":"stations","main":{"temp":24.82,"feels_like":24.19,"temp_min":24.82,"temp_max":24.82,"pressure":1017,"humidity":32,"sea_level":1017,"grnd_level":1002},"visibility":10000,"wind":{"speed":2.98,"deg":333,"gust":3.34},"clouds":{"all":0},"dt":1768974385,"sys":{"type":1,"id":9144,"country":"IN","sunrise":1768956951,"sunset":1768996217},"timezone":19800,"id":1278314,"name":"Asansol","cod":200}
    }

    return render(request,'weather.html',weather_data)

class reactview(APIView):
    serializer_class=ReactSerializer
    def get(self,request):
        stu=student.objects.all()
        serializer=ReactSerializer(stu,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

class UserListView(APIView):
    def get(self, request):
        users = user.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    def delete(self, request, pk):
        try:
            user_obj = user.objects.get(pk=pk)
            user_obj.delete()
            return Response({'message': 'User deleted successfully'}, status=204)
        except user.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

