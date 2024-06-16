import requests
import tkinter

response = requests.get(url='https://api.kanye.rest/')
response.raise_for_status()
# print(response.json()['quote'])

window = tkinter.Tk()
window.title('Kanye Rest!!')
window.config(pady=20, padx=20)
canvas = tkinter.Canvas(window, width=450, height=600)
bg = tkinter.PhotoImage(file='background.png')
canvas.create_image(225, 225, image=bg)
kanye = tkinter.PhotoImage(file='kanye.png')
canvas.create_image(225, 500, image=kanye)
canvas_quote = canvas.create_text(225, 225, text=response.json()['quote'],
                                  font=('Arial', 20, 'bold'), fill='white', width=270)
canvas.pack()
window.mainloop()
