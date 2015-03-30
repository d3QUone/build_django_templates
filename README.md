Утилита для финальной сборки Django-шаблонов с множеством внешних подключений ```{% include "..." %}```

<hr>

Я верю, что странички моих сервисов могут отдаваться намного быстрее. 
Главная задача этой утилиты - увеличение скорости рендеринга шаблонов за счет предварительной сборки всех включеных файлов в один файл.

<hr>

<strong>Плюсы:</strong>

Быстрый рендеринг шаблона: Django открывает только один файл, в комбинации с кэшированием шаблонов (django.template.loaders.cached.Loader) получается заметный прирост скорости отдачи страниц где был 1 и больше include-tag

<hr>

<strong>Минусы:</strong>

+1 команда в командной строке при изменении шаблона

Разработка не усложнаяется - шаблоны собираются из указанных папок (приложений) и помещаются в общую папку шаблонов, что удобно при развертке

<hr>

<strong>Как использовать:</strong>

1) Заменить в шаблонах все стандартные тэги ```{% include "block.html" %}``` на новые ```[[[ "block.html" ]]]```
2) Внимательно заполнить конфиг-файл. Важно чтобы конфиг и скрипт лежали на одном уровне с корнями подключаемых папок:

```
|-project/
|---build.py
|---config.py
|.......
|---dev_templates/
|---templates/
```

3) Запустить скрипт: ```python build.py```

Структура конфиг-файла:
  
<strong>SOURCE_DIRS</strong> - список папок, из в которых будут браться шаблоны 

<strong>TARGET_FILES</strong> - полный список файлов, требующий сборки. следует указать все файлы, которые будут рендерится Джангой, только эти файлы будут перенесены в итоговую папку. Допустимо использовать файлы с пробелами в названии. Расширения - html, css, js

<strong>TARGET_DIR</strong> - директория, куда скадываются готовые файлы 

Пример конфига для рендеринга страниц из папки "example" этого репозитория (все страницы взяты из <a href="https://github.com/d3QUone/ask_kasatkin">проекат вопросов и ответов Ask-Kasatkin</a>, для которого создавалась эта утилита)

```python

# Django's standart folder-style
SOURCE_DIRS = [
	"example/core/templates/core/",
	"example/user_profile/templates/user_profile/"
]

# results will be saved here
# !!! this folder must exist !!!
TARGET_DIR = "example/templates/" 


# all files that have [[[ "file_name.html" ]]] - include tag OR must be in target dir 
TARGET_FILES = [
	"base.html",
	"core__index.html",
	"core__question_page.html",
	"user_profile__base.html"
]
```
