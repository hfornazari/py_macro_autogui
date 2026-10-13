
import tkinter as tk
from tkinter import ttk
import threading,time,json,os
import pyautogui
from pynput import mouse, keyboard
from pynput.mouse import Button
from pynput.keyboard import Key

MACRO='macros/default.json'
recording=False
stop_play=False
events=[]
last_time=0
IGNORE={'Key.f6','Key.f8','Key.f9','Key.f10','Key.esc'}

root=tk.Tk(); root.title('Macro Recorder'); root.geometry('800x550'); root.attributes('-topmost',True)
rep=tk.StringVar(value='10')
intervalo=tk.StringVar(value='1')
mousepos=tk.StringVar(value='Mouse Pos: X=0 Y=0')

bar=ttk.Frame(root); bar.pack(fill='x')
ttk.Label(bar,textvariable=mousepos).pack(side='left',padx=5)
ttk.Label(bar,text='Repetições').pack(side='left')
ttk.Entry(bar,textvariable=rep,width=6).pack(side='left')
ttk.Label(bar,text='Intervalo').pack(side='left')
ttk.Entry(bar,textvariable=intervalo,width=6).pack(side='left')

log=tk.Text(root)
log.pack(fill='both',expand=True)

def addlog(m):
 log.insert('end',m+'\n'); log.see('end'); root.update_idletasks()

def update_mouse():
 x,y=pyautogui.position(); mousepos.set(f'Mouse Pos: X={x} Y={y}'); root.after(100,update_mouse)

def delay():
 global last_time
 t=time.time(); d=0 if last_time==0 else round(t-last_time,3); last_time=t; return d

class Rec:
 def on_click(self,x,y,button,pressed):
  if recording and pressed:
   events.append({'type':'click','delay':delay(),'x':x,'y':y,'button':'left' if button==Button.left else 'right'})
   addlog(f'CAPTURADO CLICK({x},{y})')
 def on_press(self,key):
  global recording
  if str(key) in IGNORE: return
  if recording:
   try:k=key.char
   except:k=str(key)
   events.append({'type':'key','delay':delay(),'key':k})
   addlog(f'CAPTURADA KEY({k})')
rec=Rec()

def start_record():
 global recording,events,last_time
 events=[]; last_time=0; recording=True
 addlog('=== GRAVACAO INICIADA ===')
 threading.Thread(target=record_thread,daemon=True).start()

def record_thread():
 ml=mouse.Listener(on_click=rec.on_click)
 kl=keyboard.Listener(on_press=rec.on_press)
 ml.start(); kl.start(); kl.join(); ml.stop()

def stop_record():
 global recording
 recording=False
 json.dump(events,open(MACRO,'w',encoding='utf-8'),indent=2)
 addlog(f'=== GRAVACAO FINALIZADA: {len(events)} EVENTOS ===')

def stop_exec():
 global stop_play
 stop_play=True; addlog('*** EXECUCAO INTERROMPIDA ***')

def play(): threading.Thread(target=play_thread,daemon=True).start()

def play_thread():
 global stop_play
 stop_play=False
 data=json.load(open(MACRO,'r',encoding='utf-8'))
 for r in range(int(rep.get())):
  addlog(f'-- CICLO {r+1}/{rep.get()} --')
  for i,e in enumerate(data,1):
   if stop_play:return
   time.sleep(e.get('delay',0))
   if e['type']=='click':
    addlog(f'LINHA {i}: CLICK({e["x"]},{e["y"]})')
    pyautogui.moveTo(e['x'],e['y'])
    if e['button']=='right': pyautogui.rightClick()
    else: pyautogui.click()
   else:
    addlog(f'LINHA {i}: KEY({e["key"]})')
    k=e['key']
    try:
      if k=='Key.enter': pyautogui.press('enter')
      elif k=='Key.tab': pyautogui.press('tab')
      elif k=='Key.space': pyautogui.press('space')
      elif len(str(k))==1: pyautogui.press(k)
    except: pass
  time.sleep(float(intervalo.get()))
 addlog('=== EXECUCAO CONCLUIDA ===')

keyboard.GlobalHotKeys({'<f6>':start_record,'<f8>':stop_record,'<f9>':play,'<f10>':stop_exec}).start()
root.bind('<Escape>',lambda e: os._exit(0))
update_mouse()
root.mainloop()
