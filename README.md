## download
git clone https://lab.ssafy.com/vacanter/final_pjt.git .<br>

## back
cd final-pjt-back<br>
pip install -r requirements.txt<br>
```	
pip install pillow
pip install pilkit
pip install django-imagekit
pip install jellyfish
pip install -U scikit-learn
```
python manage.py makemigrations<br>
python manage.py migrate<br>
python manage.py loaddata movies.json actors.json genres.json<br>
python manage.py runserver<br>

## front
cd final-pjt-front<br>
npm i<br>
npm run serve<br>
<br>
