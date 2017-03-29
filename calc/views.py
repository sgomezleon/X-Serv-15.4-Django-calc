from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def barra(request):

	response = 'Bienvenido a la calculadora. Introduce la operacion en la barra de direcciones'

	return HttpResponse(response)

def suma(request,op1,op2):
	
	resultado = int(op1) + int(op2)
	respuesta = 'Vamos a hacer una SUMA Me has dado un ' + str(op1) + ' y un ' + str(op2) + \
				'. El resultado es ' + str(resultado)
	return HttpResponse(respuesta)

def resta(request,op1,op2):
	
	resultado = int(op1) - int(op2)
	respuesta = 'Vamos a hacer una RESTA. Me has dado un ' + str(op1) + ' y un ' + str(op2) + \
				'. El resultado es ' + str(resultado)
	return HttpResponse(respuesta)

def multi(request,op1,op2):
	
	resultado = int(op1) * int(op2)
	respuesta = 'Vamos a hacer una MULTIPLICACION. Me has dado un ' + str(op1) + ' y un ' + str(op2) + \
				'. El resultado es ' + str(resultado)
	return HttpResponse(respuesta)

def div(request,op1,op2):
	
	resultado = int(op1) / int(op2)
	respuesta = 'Vamos a hacer una DIVISION. Me has dado un ' + str(op1) + ' y un ' + str(op2) + \
				'. El resultado es ' + str(resultado)
	return HttpResponse(respuesta)

	

	
