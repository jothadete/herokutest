## REST-API mit Flask
Nach dem Artikel auf Codeburst von Leon Wee: www.codeburst.io/@leonweecs

1. virtualenv venv
2. source venv/bin/activate (deaktivieren mit deactivate)
3. git init
4. Repository auf Github angelegt.
5. pip install flask-restful
6. Code erstellt.
7. API läuft. Die URL ist jeweils "user/XYZ" - vgl. die Zeile 82 - add_resource an dieser Adresse.
8. touch requirements.txt
9. pip freeze > requirements.txt
10. git add -A, dann git commit -m ""
11. git remote add origin git@github.com:jothadete/rest-api-test.git
12. git push -u origin master


Test mit Postman lokal:
python app.py
Postman: GET 127.0.0.1:5000/user/Nicholas


13. runtime.txt - Python und Version angeben.
14. uWSGI nicht lokal installiert, aber in requirements.txt aufnehmen.
15. uwsgi.ini - Port - Der Port wird von Heroku gelesen - $(Port), Masterprozess, Module - hier wird das Module (app.py) und die Variable angegeben (app).
16. Procfile - Welche "Dyno"? Hier vom Typ "web". Welcher Prozess? Hier z. B. Python - hier aber uWSGI-Prozess, dieser startet dann Flask.
