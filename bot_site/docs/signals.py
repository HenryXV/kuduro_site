from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from docs.models import Command, Usage, Option, Example, Alias

@receiver(post_save)
@receiver(post_delete)
def update_json_file(sender, **kwargs):

    list_of_models = ['Command', 'Alias']
    if sender.__name__ in list_of_models:

        import json
        commands_list = list()

        for command in Command.objects.all():

            id = command.id

            u = [u.command_usage for u in Usage.objects.filter(command=id)]
            o = [o.command_option for o in Option.objects.filter(command=id)]
            e = [e.command_example for e in Example.objects.filter(command=id)]
            a = [a.command_alias for a in Alias.objects.filter(command=id)]

            commands_list.append({'category': command.command_category.category_name,
            'name': command.command_name,
            'info': command.command_info, 'usage': u, 'options': o, 'examples': e, 'aliases': a})

        with open('docs/static/docs/json/data.json', 'w') as file:
            json.dump(commands_list, file, indent=4)
