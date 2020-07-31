import socket as st
import pickle


class Network:
    def __init__(self):
        self.client = st.socket(st.AF_INET, st.SOCK_STREAM)
        self.server = "100.115.92.203"#"100.115.92.203""10.158.1.100"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()
        
        
    def getP(self):
        return self.p
        
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass
        
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except st.error as e:
            print(e)