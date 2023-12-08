from django.db import migrations

list_comics = [{"title": "Shaman King", "author": "Hiroyuki Takei"}, {"title": "Naruto", "author": "Masashi Kishimoto"},
               {"title": "Death Note", "author": "Tsugumi Ohba"}, {"title": "One Punch Man", "author": "ONE"}]
def import_data(app, _):
    Comics = app.get_model("comics", "Comics")
    for comics in list_comics:
        Comics.objects.create(title=comics["title"], author=comics["author"])


class Migration(migrations.Migration):
    dependencies = [
        ("comics", "0001_initial"),
    ]

    operations = [migrations.RunPython(import_data, migrations.RunPython.noop)]
