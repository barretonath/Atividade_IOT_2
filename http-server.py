from http.server import BaseHTTPRequestHandler, HTTPServer #classes importadas

HOST = 'localhost' #host
PORT = 5000 #porta que receberá conexões

class MyHandler(BaseHTTPRequestHandler): #classe
    def do_GET(self): #heranças da classe
        self.send_response(200) #resposta enviada
        self.send_header("Content-type", "text/html") #formato do texto enviado
        self.end_headers() #string
        self.wfile.write(bytes("<html><head><title>AULA HTTP</title></head>","utf-8")) #escrever texto determinado
        self.wfile.write(bytes("<body>", "utf-8"))#escrever texto determinado
        self.wfile.write(bytes("<p>Servidor HTTP de exemplo.</p>", "utf-8"))#escrever texto determinado
        self.wfile.write(bytes("</body></html>", "utf-8"))#escrever texto determinado

webServer = HTTPServer((HOST,PORT), MyHandler) # recebe as variáveis
print("Servidor iniciado em http://%s:%s" % (HOST, PORT)) #exibir mensagem pra provar que servisor foi iniciado

webServer.serve_forever() #ficar rodando até receber uma requisição