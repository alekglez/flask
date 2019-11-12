## Flask App Project
Blueprint for Flask App Project
###### Note: python3.7+

#### System dependencies
```
$ sudo apt install libpq-dev
```

#### Python configuration

##### Python Environment
```
$ mkvirtualenv --python=/usr/bin/python3.7 flask_project
$ workon flask_project
```

##### Install requirements
```
$ pip install -r requirements/base.txt
```

##### Execute tests
```
$ python manage.py test
```

##### Test coverage
```
$ python manage.py coverage
```

##### After the coverage execution you should see some report like that:
```
Coverage summary:

Name                                        Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------------------------
project/app.py                                 12      5      2      0    64%
project/apps/__init__.py                        2      0      0      0   100%
project/apps/core/__init__.py                   0      0      0      0   100%
project/apps/core/commons/__init__.py           0      0      0      0   100%
project/apps/core/commons/mixins.py             6      0      0      0   100%
project/apps/frontend/__init__.py               1      0      0      0   100%
project/apps/frontend/tests/__init__.py         0      0      0      0   100%
project/apps/frontend/tests/test_views.py       5      0      0      0   100%
project/apps/frontend/views.py                  5      0      0      0   100%
-----------------------------------------------------------------------------
TOTAL                                          31      5      2      0    85%
```

###### Also a folder called: "htmlcov" was created and you can open the index.html file in your browser and see the code lines that our test are covering...

##### Execute the application...
```
$ python manage.py run
```
