import webbrowser
import threading
def url():
    webbrowser.open("http://127.0.0.1:2000")

print ("abrir pagina")
abrir = threading.Thread(target=url)
abrir.start()