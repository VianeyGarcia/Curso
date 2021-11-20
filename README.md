# CURSO ROS NOETIC
Objetivo
Desarrollar las capacidades necesarias para la programación de robots en ROS Noetic.



Actividades
- Generar un repositorio en su cuenta personal de GitHub.

- Subir un programa de Python con las siguientes características:

Una clase llamada Robot.
Un arreglo de cadenas representando el nombre de cada articulación del robot.
Un arreglo de flotantes representando el valor actual de cada articulación.
Una cadena con el nombre del robot.
Un variable a un objeto llamado Pose que represente la pose del robot con los valores x (posición en x), y (posición en y), z (posición en z), rxr (rotación en x en radianes), ryr (rotación en y en radianes), rzr (rotación en z radianes).
Todas las variables deben ser inicializadas con valores en el constructor para un manipulador de 5 grados de libertad más uno más llamado base (eslabón 0).
Un método llamado set_name(robot_name) para cambiar el nombre del robot
Un método llamado get_articulacion(articulacion_nombre) que devuelva el valor de la articulación articulacion_nombre.
Un método get_Pose() que devuelva el objeto Pose.
El script debe tener un punto de entrada usando if __name__ == '__main__': llamando a una función main() que pruebe las características y funciones listadas anteriormente.
