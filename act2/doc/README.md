act2
=====================
cette activité consiste à exécuter une patrouille, à partir d'un fichier de configuration «config. yaml » en format JSON contenant les différents points à atteindre. 
"
Turtlesim est configuré à partir d'un fichier "config.yaml" dans le repértoire "config". Ce fichier sera chargé dans le fichier launch/patrol.launch qui sera par la suite utiliser par un script python scr/patrol.py. le script parse le fichier "config.yaml" puisqu'il est sous format json .

Démarrage
============
ouvrir 3 terminales :

terminale 1 :
  $roscore
terminale 2 :
  $rosrun turtlesim turtlesim_node
terminale 3 :
  $cd ~/act2
  build: $catkin_make
  source: $source devel/setup.bash
  $cd /src/patrol/src
  $rosrun patrol patrol.py

Environnements de travail
==========================
OS : Ubuntu 14.04 Trusty ROS: Indigo
