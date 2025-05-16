from abc import ABC, abstractmethod

class Client(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_discount(self):
        pass

class RegularClient(Client):
    def get_discount(self):
        return 5

class VIPClient(Client):
    def get_discount(self):
        return 15

def show_client_info(client):
    print(f"{client.name} получает скидку {client.get_discount()}%.")

clients = [
    RegularClient("Айгуль"),
    VIPClient("Нурлан"),
    RegularClient("Элина")
]

for c in clients:
    show_client_info(c)
