import socket as st



class Network:
    def __init__(self):
        self.client = st.socket(st.AF_INET, st.SOCK_STREAM)
        self.server = "100.115.92.203"#"100.115.92.203""10.158.1.100"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        
        
    def getPos(self):
        return self.pos
        
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
        
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except st.error as e:
            print(e)