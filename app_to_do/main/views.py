from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages

from . forms import CreateUserForm, TaskForm

from .models import (
	TaskModel,
)


class ErrorView(generic.TemplateView):
	template_name = "main/404.html"


class BlankView(generic.TemplateView):
	template_name = "main/blank.html"

class ButtonsView(generic.TemplateView):
	template_name = "main/buttons.html"

class CardsView(generic.TemplateView):
	template_name = "main/cards.html"

class ChartsView(generic.TemplateView):
	template_name = "main/charts.html"

class IndexView(generic.TemplateView):
	template_name = "main/index.html"

class TablesView(generic.TemplateView):
	template_name = "main/tables.html"

class UtilitiesAnimationView(generic.TemplateView):
	template_name = "main/utilities-animation.html"

class UtilitiesBorderView(generic.TemplateView):
	template_name = "main/utilities-border.html"

class UtilitiesColorView(generic.TemplateView):
	template_name = "main/utilities-color.html"

class UtilitiesOtherView(generic.TemplateView):
	template_name = "main/utilities-other.html"


def LoginView(request):
	if request.user.is_authenticated:
		return redirect("main:index")
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect("main:index")
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'main/login.html', context)


def LogoutUserView(request):
	logout(request)
	return redirect('main:login')


def RegisterView(request):
	if request.user.is_authenticated:
		return redirect("main:index")
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Se creó la cuenta para  ' + user)

				return redirect('main:login')
			

		context = {'form':form}
		return render(request, 'main/register.html', context)
		

class CreacionTareasView(generic.FormView):
	template_name = "main/creacionTareas.html"
	form_class = TaskForm


	success_url = "../creacionTareas"
	
	
	def get_queryset(self):
		return super().get_queryset()
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		lista_tareas = TaskModel.objects.all()
		
		context["lista_tareas"] = lista_tareas
		return context

	def form_valid(self, form):
		
		form.save()
		messages.success(self.request, 'Se creó de forma exitosa.')
		return super().form_valid(form)


def eliminarTareaView(request, id):
	tarea = TaskModel.objects.get(id=id)
	tarea.delete()

	return redirect("../creacionTareas")


class TareaDetailView(generic.DetailView):
	model = TaskModel
	form_class = TaskForm
	template_name = "main/edicionTareas.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		tareas = TaskModel.objects.all()
		formulario = TaskForm
		
		context["tareas"] = tareas
		context["formulario"] = formulario


		return context







"""
def lecturaEdicionTareaView(request, id):

	#CreationTareasView()

	class CreationTareasView(generic.FormView):
		template_name = "main/creacionTareas.html"
		form_class = TaskForm


		success_url = "../creacionTareas"
		
		def get_context_data(self, **kwargs):
			context = super().get_context_data(**kwargs)
			
			lista_tareas = TaskModel.objects.all()
			
			context["lista_tareas"] = lista_tareas
			return context

		def form_valid(self, form):
			
			form.save()
			messages.success(self.request, 'Se creó de forma exitosa.')
			return super().form_valid(form)
"""

"""
	tarea = TaskModel.objects.get(id=id)
	datosTarea = {
		'titulo': tarea.titulo,
		'descripcion': tarea.descripcion,
		'estado': tarea.estado,
		'cuerpo': tarea.cuerpo
	}

	return render(request, "main/edicionTareas.html", datosTarea)
"""

"""
class LecturaView(id):
	template_name = "main/cedicionTareas.html"
	form_class = TaskForm


	success_url = "../edicionTareas"
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		tarea = TaskModel.objects.get(id=id)
		
		context["tarea"] = tarea
		return context
"""


"""
class LecturaView(generic.FormView):
	template_name = "main/creacionTareas.html"
	form_class = TaskForm


	success_url = "../creacionTareas"
	
	def lecturaEdicionTareaView(request, id):
		tarea = TaskModel.objects.get(id=id)
		datosTarea = {
			'titulo': tarea.titulo,
			'descripcion': tarea.descripcion,
			'estado': tarea.estado,
			'cuerpo': tarea.cuerpo
		}
		messages.success(request, 'Se cargó COOL.')

		return render(request, "main/edicionTareas.html", datosTarea)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		
		lista_tareas = TaskModel.objects.all()
		
		context["lista_tareas"] = lista_tareas
		return context
"""