from pynput.keyboard import Listener

def capturar(tecla):
    tecla = str(tecla)
    print(tecla)
    
with Listener(on_press=capturar) as l:
    l.join()
    