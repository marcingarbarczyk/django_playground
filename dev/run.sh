mkdir -p data/elasticsearch
if ! [ -O ./data/elasticsearch ]; then sudo chown -R ${USER} ./data/elasticsearch; fi
docker compose down && docker compose up -d

echo "First init (y)?" &&
	read choice
	if  [ "$choice" = "Y" ] || [ "$choice" = "y" ]
	then
	    docker exec -it django-playground bash -c "python manage.py createsuperuser"
	    docker exec -it django-playground python manage.py seed blog --number=1000
	    docker exec -it django-playground python manage.py seed books --number=1000
	    docker exec -it django-playground python manage.py seed shop --number=1000
	fi