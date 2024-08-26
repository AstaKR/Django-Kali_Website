from django.shortcuts import render

from django.views import View
# Create your views here.

class HomePageView(View):
    def get(self, request):

        return render(request,"html/home_page.html")
    
    def post(self,request):
        if request.method =="POST":
            name= request["name"]
            email = request["email"]
            subject= request["subject"]
            message = request["messages"]
            print(name)
        return render(request,"html/home_page.html")