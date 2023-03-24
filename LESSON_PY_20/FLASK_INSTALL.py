"""
INSTALL FLASK

mkdir flask_project
cd flask_project
mkdir .venv
pipenv shell


Виртуальное окружение активируется командойpipenv shell,
для выхода нужно выполнить exit.


Установим Flask и все необходимые зависимости.
Для этого сохраните этот список в файле requirements.txt:
Click==7.0
Flask==1.1.1
Flask-FlatPages==0.7.1
Frozen-Flask==0.15
itsdangerous==1.1.0
Jinja2==2.10.3
Markdown==3.1.1
MarkupSafe==1.1.1
Pygments==2.4.2
PyYAML==5.1.2
Werkzeug==0.16.0


Поместите файл в директорию проекта и выполните команду:

        
pipenv install -r requirements.txt

В папке content/posts будут размещаться Markdown файлы,
в templates – шаблоны, в static – CSS стили, изображения и JS-скрипты.
Весь код приложения мы напишем в файле mysite.py – сначала импортируем
нужные модули, затем определим основные параметры, после пропишем маршруты
к шаблонам и запустим сервер.
mysite.py выглядит так:

"""
import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'
 
app = Flask(__name__)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)
 
@app.route("/")
def index():
	posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
	posts.sort(key=lambda item: item['date'], reverse=True)
	return render_template('index.html', posts=posts, bigheader=True)
 
@app.route('/posts/<name>/')
def post(name):
	path = '{}/{}'.format(POST_DIR, name)
	post = flatpages.get_or_404(path)
	return render_template('post.html', post=post)
 
if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "build":
    	freezer.freeze()
	else:
    	app.run(host='127.0.0.1', port=8000, debug=True)
