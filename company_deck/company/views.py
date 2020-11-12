from django.shortcuts import render,redirect

# Create your views here.
from django.template import RequestContext
from django.http import HttpResponse
from company.models import Employ_Form, Employ_Form2, Employ_Form3, Review, Job

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from django.views import generic

from django.db.models import Q # new

from company.forms import UserForm 

from django.contrib.auth import authenticate, login, logout  #for user authentication
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages



class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "index.html"

class HomePageView(generic.TemplateView):
    model = Review
    template_name = 'company_review.html'

class SearchResultsView(generic.ListView):
    model = Review
    context_object_name ='reviews'
    template_name = 'search_production.html'

    
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Review.objects.filter(
            Q(name__icontains=query) | Q(location__icontains=query)
        )
        return object_list


class PageView(generic.TemplateView):
    model = Job
    template_name = 'job_search.html'

class ResultsView(generic.ListView):
    model = Job
    context_object_name ='jobs'
    template_name = 'job_production.html'

    
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Job.objects.filter(
            Q(name__icontains=query) | Q(location__icontains=query)
        )
        return object_list





def index (request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        
        if user_form.is_valid(): 
            user = user_form.save()
            user.set_password(user.password) 
            user.save()
            user = user_form.cleaned_data.get('username')
            messages.success(request, "Successful! Explore now  "  +   user)

            registered = True 
            return job_search(request)
        else:
            print (user_form.errors) 

    else:
        user_form = UserForm()


    return render(request, 'index.html',{'user_form':user_form}) 





def user_sign_in (request):
    if request.method == "POST":           
        username = request.POST['username']                             #get user name and password from the user input
        password = request.POST['password']

        user = authenticate(username=username, password=password) #to validate the information in the database
        
        if user is not None: #user present in database
            print ("hello") 
            if user.is_active:
                login(request, user)
                # return about(request)
                return job_search(request)
            else:
                return HttpResponse("Your Rango account is disabled")
        else:
            print ("Invalid login details: {0}, {1}".format(username,password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'sign_in.html',{})    


# def logoutUser(request):
    # return render(request, 'index.html')


def forget (request):
    return render(request, 'forget.html')

def employer_page (request):
    return render(request, 'employer_page.html')

def job_search (request):
    data=Employ_Form.objects.all()
    data2=Employ_Form2.objects.all()
    data3=Employ_Form3.objects.all()  
    return render(request, 'job_search.html', {'data': data, 'data2': data2, 'data3': data3})

def employ_form (request):
    if request.method  == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        copname = request.POST['copname']
        jobtitle = request.POST['jobtitle']
        location = request.POST['location']
        print(fname, lname, phone, email, copname, jobtitle, location)
        ins = Employ_Form(fname=fname, lname=lname, phone=phone, email=email, copname=copname, jobtitle=jobtitle, location=location)
        ins.save()
        print("the data has been written to db")
        return render(request,'employ_form2.html',)
    
    return render(request, 'employ_form.html')

def employ_form2 (request):
    if request.method  == "POST":
        
        
        my_population = request.POST['my_population'],
        job = request.POST['job'],
        employment = request.POST['employment'],
        contract = request.POST['contract'],
        ins = Employ_Form2(my_population = my_population, job=job, employment=employment, contract=contract)
        ins.save()
        print("the data has been stored into database")
        return render (request,'employ_form3.html')
        
    return render(request, 'employ_form2.html') 

def employ_form3 (request):
    if request.method  == "POST":
            
        rangeo = request.POST['rangeo'],
        amount1 = request.POST['amount1'],
        amount2= request.POST['amount2'],
        per = request.POST['per'],
        comment = request.POST['comment'],
        print("hello")
        ins = Employ_Form3(rangeo= rangeo, amount1=amount1, amount2= amount2, per = per, comment=comment)
        ins.save()
        print("data")
        return render (request, 'employer_page.html')
      
    return render(request, 'employ_form3.html')
    


def company_review (request):
    return render(request, 'company_review.html')

