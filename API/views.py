
from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from django.conf import settings


@api_view(['GET'])
def costOPT(request):
    try:
        if request.method == 'GET':

            St_A = int(request.GET.get('Stock_A', default = 0))
            St_B = int(request.GET.get('Stock_B', default = 0))
            St_C = int(request.GET.get('Stock_C', default = 0))
            St_D = int(request.GET.get('Stock_D', default = 0))
            St_E = int(request.GET.get('Stock_E', default = 0))
            St_F = int(request.GET.get('Stock_F', default = 0))
            St_G = int(request.GET.get('Stock_G', default = 0))
            St_H = int(request.GET.get('Stock_H', default = 0))
            St_I = int(request.GET.get('Stock_I', default = 0))

            if(St_A<0) or (St_B<0) or (St_C<0) or (St_D<0) or (St_E<0) or (St_F<0) or (St_G<0) or (St_H<0) or (St_I<0):
                raise ValueError

            x = (3*St_A+2*St_B+8*St_C) # x is weight of C1
            y = (12*St_D+25*St_E+15*St_F) #y is weight of C2
            z = (0.5*St_G+1*St_H+2*St_I)  # z is weight of C3

            if x > 5:
                m = ( 10 + ((x-5)//5)*8 )
                if (((x-5)%5)>0):
                    m = m+8
                else:
                    m = m 
            else:
                m = 10
            # m is the total cost/unit for C1

            if y > 5:
                n = ( 10 + ((y-5)//5)*8 )
                if (((y-5)%5)>0):
                    n = n+8
                else:
                    n = n    
            else:
                n = 10
            # n is the total cost/unit for C2
                
            if z > 5:
                o = ( 10 + ((z-5)//5)*8 )
                if (((z-5)%5)>0):
                    o = o+8
                else:
                    o = o 
            else:
                o = 10
            # o is the total cost/unit for C3

            
            if (x > 0) and (y == 0) and (z == 0):
                cost = 3*m
                return JsonResponse("Minimum cost of transporation is: "+str(cost)+" Rupee",safe=False)  

            elif (x==0) and (y>0) and (z==0):
                cost = 2.5*n
                return JsonResponse("Minimum cost of transporation is: "+str(cost)+" Rupee",safe=False)  

            elif (x==0) and (y==0) and (z>0):
                cost = 2*o
                return JsonResponse("Minimum cost of transporation is: "+str(cost)+" Rupee",safe=False)  

            elif (x>0) and (y>0) and (z==0):
                a = 3*m + 25+ 2.5*n                 #C1-L1-C2-L1
                b = 4*m + 2.5*(m+n)                 #C1-C2-L1
                c = 2.5*n + 30 + 3*m                #C2-L1-C1-L1
                d = 4*n + 3*(m+n)                   #C2-C1-L1
                cost = min(a,b,c,d)
                return JsonResponse("Minimum cost of transporation is: "+str(cost)+" Rupee",safe=False)  

            elif (x==0) and (y>0) and (z>0):
                a = 2.5*n + 20 + 2*o                #C2-L1-C3-L1
                b = 3*n + 2*(n+o)                   #C2-C3-L1
                c = 2*o +25+ 2.5*n                  #C3-L1-C2-L1
                d = 3*o + 2.5*(n+o)                 #C3-C2-L1
                cost = min(a,b,c,d)
                return JsonResponse("Minimum cost of transporation is: "+str(cost)+" Rupee",safe=False)  

            elif (x>0) and (y==0) and (z>0):
                a = 3*m + 20 + 2*o                  #C1-L1-C3-L1
                b = 5*m + 2*(m+o)                   #C1-C3-L1
                c = 2*o + 30 + 3*m                  #C3-L1-C1-L1
                d = 5*o + 3*(m+o)                   #C3-C1-L1
                cost = min(a,b,c,d)
                return JsonResponse("Minimum cost of transporation is: "+str(cost)+" Rupee",safe=False)

            elif (x>0) and (y>0) and (z>0):
                a = 4*m + 3*(m+n) + 2*(m+n+o)                 #C1-C2-C3-L1
                b = 5*m + 3*(m+o) + 2.5*(m+n+o)             #C1-C3-C2-L1
                c = 4*m + 2.5*(m+n) + 20 + 2*o              #C1-C2-L1-C3-L1
                d = 5*m + 2*(m+o) + 25 + 2.5*n              #C1-C3-L1-C2-L1
                e = 3*m + 25 + 3*n + 2*(n+o)                #C1-L1-C2-C3-L1
                f = 3*m + 20 + 3*o + 2.5*(n+o)              #C1-L1-C3-C2-L1
                g = 3*m + 25 + 2.5*n + 20 + 2*o             #C1-L1-C2-L1-C3-L1
                h = 3*m + 20 + 2*o + 25 + 2.5*n             #C1-L1-C3-L1-C2-L1
                i = 4*n + 5*(m+n) + 2*(m+n+o)               #C2-C1-C3-L1
                j = 3*n + 5*(n+o) + 3*(m+n+o)               #C2-C3-C1-L1
                k = 4*n + 3*(m+n) + 20 + 2*o                #C2-C1-L1-C3-L1
                l = 3*n + 2*(n+o) + 30 + 3*m                #C2-C3-L1-C1-L1
                m2 = 2.5*n + 30 + 5*m + 2*(m+o)             #C2-L1-C1-C3-L1 
                n2 = 2.5*n + 20 + 5*o + 3*(m+o)             #C2-L1-C3-C1-L1
                o2 = 2.5*n + 20 + 2*o + 30 + 3*m            #C2-L1-C3-L1-C1-L1
                p = 2.5*n + 30 + 3*m + 20 + 2*o             #C2-L1-C1-L1-C3-L1
                q = 3*o + 4*(o+n) + 3*(o+n+m)               #C3-C2-C1-L1
                r = 5*o + 4*(o+m) + 2.5*(o+m+n)             #C3-C1-C2-L1
                s = 3*o + 2.5*(o+n) + 30 + 3*m               #C3-C2-L1-C1-L1
                t = 5*o + 3*(o+m) + 25 + 2.5*n              #C3-C1-L1-C2-L1
                u = 2*o + 25 + 4*n + 3*(n+m)                #C3-L1-C2-C1-L1
                v = 2*o + 30 + 4*m + 2.5*(m+n)               #C3-L1-C1-C2-L1
                w = 2*o + 25 + 2.5*n + 30 + 3*m               #C3-L1-C2-L1-C1-L1
                x2 = 2*o + 30 + 3*m + 25 + 2.5*n            #C3-L1-C1-L1-C2-L1
                cost = min(a,b,c,d,e,f,g,h,i,j,k,l,m2,n2,o2,p,q,r,s,t,u,v,w,x2)
                return JsonResponse("Minimum cost of transporation is: "+str(cost)+" Rupee",safe=False)


             
                                
            else:
                cost = 0   
                return JsonResponse("PLease select a valid amount of Stock",safe=False)        

        
    except ValueError as e1:
         return Response("Please enter a non string, postive whole number value of Stock",status.HTTP_400_BAD_REQUEST)
       
    except Exception as e:
        print(str(e))
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
