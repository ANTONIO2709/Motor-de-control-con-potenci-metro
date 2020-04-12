# Motor-de-control-con-potencimetro
Motor de control con potenciómetro
En este capítulo, aprenderemos algunos conocimientos sobre el motor de AC y el motor de DC, y cómo controlar el
velocidad y dirección del motor.
En este proyecto, se utiliza un potenciómetro para controlar el motor. Cuando el potenciómetro está en la posición de punto medio,
el motor dejará de girar, y cuando está lejos de la posición media, la velocidad del motor aumenta. Cuando
potenciómetro se desplaza a extremos, la velocidad del motor alcanza el máximo. Cuando el potenciómetro
posición está en el lado diferente de la posición media, la dirección del motor es diferente.

Motor
Motor es un dispositivo que convierte la energía eléctrica en energía mecánica. El motor consta de dos partes: estator
y rotor. Cuando el motor funciona, la parte estacionaria es estator, y la parte giratoria es rotor. Stator es generalmente el
exterior del motor, y tiene terminales para conectarse a la potencia. Rotor es generalmente el eje del motor, y puede
conectar otros dispositivos mecánicos para que funcionen. El las imagenes se ven un pequeño motor de CC con dos pines.

Cuando el motor se conecte a la fuente de alimentación, girará en una dirección. Invertir la polaridad del alimentacion del 
suministro, a continuación, el motor gira en dirección opuesta.

L293D
L293D es un chip integrado con accionamiento de motor de 4 canales. Puede conducir un motor unidireccional con 4 puertos o un
motor bidireccional con 2 puertos o un motor paso a paso.
Cuando se utiliza L293D para conducir el motor de CC, por lo general hay dos tipos de conexión.
En la imagen 1 se utiliza un canal, y puede controlar la velocidad del motor a través de PWM, pero el motor puede
sólo giran en una dirección.
La imagen 2 utiliza dos canales: una onda PWM de salidas de canal y otro canal se conecta
GND, por lo que puede controlar la velocidad del motor. Cuando se intercambian estas señales de dos canales, la
dirección del motor se puede invertir, y el motor girará en sentido inverso. Esto no sólo puede
controlar la velocidad del motor, pero también puede controlar la dirección del motor.
En uso real, el motor se conecta generalmente a los canales 1 y 2, salida de diferente nivel a in1 y in2 a
controlar la dirección de rotación del motor, y salida de onda PWM al puerto Enable1 para controlar el motor
velocidad de rotación. O bien, conecte el motor al canal 3 y 4, emita un nivel diferente a in3 y a in4 para
controlar la dirección de rotación del motor y la salida de onda PWM a pin Enable2 para controlar la rotación del motor
Velocidad.

Circuito
Al conectar el circuito, preste atención  porque el motor es un componente de alta potencia, no
utilizar la potencia proporcionada por el RPi, que puede causar daños a su RPi. el circuito lógico puede ser alimentado por
RPi potencia o fuente de alimentación externa que debe tener el tierra común con RPi.
