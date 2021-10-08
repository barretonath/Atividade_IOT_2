import paho.mqtt.client as mqtt #informação importada
import json #informação importada

client = mqtt.Client(client_id='sub-py') #classe

client.connect('localhost', port=1883) #porta padrão
client.subscribe('casa/sala/lampada/1') #objetos

print("Subscriber connected!") #exibir mensagem dizendo que subscriber conectou

def on_message_callback(client, userdata, message): #verifica se chega mensagem
    msg = json.loads(message.payload.decode('utf-8')) #lê mensagem em formato json e realiza conversão para python
    if(msg["status"] == True): #Se valor for verdadeiro, liga pino do raspberry / arduino
        print("Pino X ligado") #exibe mensagem dizendo que o pino foi ligado
    elif(msg["status"] == False):#se valor for falso, desliga pino do raspberry / arduino
        print("Pino X desligado") #exibe mensagem dizendo que o pino foi desligado


client.on_message = on_message_callback #verifica se chega mensagem

client.loop_forever() #verifica em loop infinito
