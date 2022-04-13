from django.shortcuts import render
from .models import Product , Orders
from math import ceil
from django.http import HttpResponse

# Create your views here.

#importing for makeup
#Importing Dependencies
import cv2  #image processing and vivion tasks
import numpy as np
import dlib 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg #display image

def index(request):
    allProds = Product.objects.all  
    params = {'allProds':allProds}
    return render(request,'index.html',params)

def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'prodview.html', {'product':product[0]})

def TryNow(request , myid):
    
    
    cap = cv2.VideoCapture(0)
   # col= 'hot pink '
    product = Product.objects.filter(id=myid)
    col = product[0].color_code
    print(col)
    colors = dict({'red':(39,37,205),'hot red':(31,18,183),'firebrick4':(26,26,139),'firebrick3':(38,38,205),
                'deep red':(14,13,124),"raspberry":(92,11,227),"cherry":(45,4,210),"cerise":(99,49,222),
                "marsla":(112,113,181)})
        
    #print(colors)

    #print(colors.get(col)) 



    #Lipstick filter
    cam= cv2.VideoCapture(0)  #Aquiring Webcam

    detector= dlib.get_frontal_face_detector()
    predictor= dlib.shape_predictor(r'C:\Users\Owner\shape_predictor_68_face_landmarks.dat')



    mouthCoord=[]
    while True:
        _,frame= cam.read()
        if frame is None:
          break
        frame= cv2.flip(frame,1)
        frameC= frame.copy()
        F= frame.copy()
        grayFrame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)     #Converting image to grayscale format
        
        faces= detector(grayFrame)   
        for face in faces:
            
            mouthCoord=[]
            landmark= predictor(grayFrame,face)   #predicting 68 landmarks 
            for i in range(48,68):              #printing landmarks of lips
                x= landmark.part(i).x
                y= landmark.part(i).y
                #cv2.circle(frame,(x,y),1,(0,255,0),-1)
                mouthCoord.append([x,y])
                
            poly1=np.array(mouthCoord[:12], np.int32).reshape((-1,1,2))  #reshaping
            poly2=np.array(mouthCoord[12:], np.int32).reshape((-1,1,2))
            yewala= cv2.fillPoly(frameC, [poly1,poly2],colors.get(col))       #filing colour
            cv2.addWeighted(yewala, 0.4, frame, 0.6 , 0, frame)


        cv2.imshow('Final', frame)
        cv2.imshow('Original',F)

        key= cv2.waitKey(1)
        if key== 27:
            break
            
    cam.release()
    cv2.destroyAllWindows()

    product = Product.objects.filter(id=myid)
    return render(request, 'prodview.html', {'product':product[0]})

def BuyView(request , myid):
 
    product = Product.objects.filter(id=myid)
    return render(request,'buy.html',{'product':product[0]})


def checkout(request):
    if request.method=="POST":
        prodId = request.POST.get('prodId', '')
        print(prodId)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(prodId =prodId, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        
        return render(request, 'thankYou.html')

def AboutUs(request):
    return render(request,'about_us.html')

def ContactUs(request):
    return render(request,'contact_us.html')
