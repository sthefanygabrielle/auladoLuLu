import paho.mqtt.client as mqtt
def ao_conectar (client, userdata,flags, rc):
    print ("nos conectamos com o seguinte codigo de resultado {}". format (str(rc)))

def ao_receber(client,userdata, msg):
    print("{} --- {}".format(msg.topic, str(msg.payload)))

cliente= mqtt.Client()
cliente.on_connect= ao_conectar
cliente.on_message = ao_receber
cliente.connect("broker.hivemq.com",1883, 60)
cliente.subscribe("aula3c")
cliente.loop_forever()
