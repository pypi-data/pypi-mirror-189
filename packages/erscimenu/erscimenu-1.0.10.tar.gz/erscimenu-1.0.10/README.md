
Erscimenu
=========
Create UL LI html menu from django model queryset .

Quick start
-----------

 Add ``erscimenu`` to your INSTALLED_APPS setting like this:
```
INSTALLED_APPS = [
...,
'erscimenu' ,
]
```

2.Run ``python manage.py makemigrations`` and ``python manage.py migrate``  to create the MenuModel models.

3.add your menu with admin registered MenuModel.

4.Use this command to add menu with your views like this:

```
from erscimenu.menu import MenuClass

def index(request):
	c=MenuClass()
	return HttpResponse(c)
	
```

4.Run  ``python manage.py runserver`` Visit http://127.0.0.1:8000 to create users and its cards.


Model is like this:
------------------
```
class MenuModel(models.Model):
	title = models.CharField(max_length=100)
	css_class = models.CharField(max_length=100,null=True,blank=True)
	link = models.CharField(max_length=1000,null=True,blank=True)
	parent = models.ForeignKey("self",models.DO_NOTHING,null=True,blank=True) 
	def __str__(self):
		return self.title
```

