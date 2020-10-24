from django.shortcuts import render
from django.views import generic
import json


from .models import Command

def IndexView(request):
    return render(request, 'docs/index.html')


class CommandView(generic.ListView):
    template_name = 'docs/commands.html'
    context_object_name = 'commands_list'

    def get_queryset(self):
        #Return all commands
        return Command.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        f = open('docs/static/docs/json/data.json', 'r')
        json_data = json.load(f)
        commands_info = list(json_data)
        f.close()

        context['commands_info'] = commands_info
        return context
