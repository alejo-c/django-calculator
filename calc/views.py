from django.shortcuts import render

# Create your views here.
def calculator(request):
	operations = {
		'add': lambda x, y: x + y,
		'sub': lambda x, y: x - y,
		'mul': lambda x, y: x * y,
		'div': lambda x, y: x / y if y != 0 else None
	}

	if request.method == 'GET':
		return render(request, 'calc/calculator.html')
	
	num1 = float(request.POST['num1'])
	num2 = float(request.POST['num2'])
	operation = request.POST['operation']
	
	result = operations[operation](num1, num2)
	
	return render(request, 'calc/calculator.html', {'result': result})
	