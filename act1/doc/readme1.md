=====================
tache
=====================
Turtlesim est configuré par une vitesse fixe
La vitesse est fixé dans un fichier config/vitesse.yaml cette valeur sera chargé dans le fichier launch/fixedVelocity.launch qui sera par la suite utiliser par un script python scr/fixedVelocity.py

Démarrage
============
ouvrir 2 terminales :

terminale 1 :
  roscore
terminale 2 :
  cd ~/act1
  build: catkin_make
  source: source devel/setup.bash
  cd /src/tache
  roslaunch tache fixedVelocity.launch
  rosrun tache fixedVelocity.py

