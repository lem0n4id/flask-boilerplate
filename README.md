# Flask - python
This is a repo where i learn flask from scratch and build my own boilerplate code.

## Features-

1. Use of templates - *jinja2* syntax to extend from `base.html`
1. tests in `tests.py` to test your flask app. Module used- *unittest*

## File structure-

```txt
learn-flask
├─── static/
│    └─── style.css
├─── templates/
│    ├─── base.html
│    └─── index.html
├─── .gitignore
├─── app.py
├─── README.md
├─── requirements.txt
└─── test_client.py
```
<details>
          <summary>Note - This is for small applications but as you scale up, you'll need something more like:</summary>
          
```txt
learn-flask
├─── app/
│   ├─── __init__.py
│   ├─── app.py
│   ├─── templates/
│   │    ├─── base.html
│   │    ├─── index.html
│   └─── static/
│        └─── style.css
├─── tests/
│    ├─── test_client.py
├─── setup.py
├─── README.md
└─── requirements.txt
```
</details>