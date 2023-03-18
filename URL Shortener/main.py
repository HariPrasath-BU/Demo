from tkinter import *
import pyperclip
import requests
import sys
import traceback
import urllib
global URL,url
global link
global res



window = Tk()
window.title("URL SHORTENER")
bg = PhotoImage(file = "BG.png")
window.iconbitmap(r'icon.ico')
window.geometry('800x450')
label1 = Label( window, image = bg)
label1.place(x = 0, y = 0)


empty_label= Label(window)
empty_label.grid(column = 0, row = 0 ,  padx=50, pady =30)
intro = Label(window, text="URL SHORTENER",font=('Times New Roman',32),bg='#008081')
intro.grid(column = 3, row = 1 , padx=50, pady =10)

link_url= pyperclip.paste()

url_in = Label(window, text="Enter the Url BWLOW ",font=('Times New Roman',20),bg='#008081')
url_in.grid(column = 3,row = 2, padx=10, pady =10)
input_url = StringVar()
input_url.set(link_url)
input_url1 = Entry(window,textvariable = input_url,width=50)
input_url1.grid(column = 3,row = 3,padx=10, pady =10)

def clicked():
    window.destroy()
Shorten = Button (window, text="Shorten" , command = clicked)
Shorten.grid(column = 3,row = 4,padx=10, pady =10)
window.mainloop()

class UrlShortenTinyurl:
    URL = "http://tinyurl.com/api-create.php"

    def shorten(self, url_long):
        try:

            url = self.URL + "?" \
                + urllib.parse.urlencode({"url": url_long})
            res = requests.get(url)
            print("STATUS CODE:", res.status_code)
            print("   LONG URL:", url_long)
            print("  SHORT URL:", res.text)
            window2 = Tk()
            window2.title("URL SHORTENER")
            bg = PhotoImage(file = "BG.png")
            window2.iconbitmap(r'icon.ico')
            window2.geometry('800x450')
            label2 = Label( window2, image = bg)
            label2.place(x = 0, y = 0)

            empty_label2= Label(window2)
            empty_label2.grid(column = 0, row = 0 ,  padx=50, pady =30)
            intro2 = Label(window2, text="URL SHORTENER",font=('Times New Roman',32),bg='#008081')
            intro2.grid(column = 3, row = 1 , padx=50, pady =10)

            url_out = Label(window2, text="The Shortened Url IS BELOW ",font=('Times New Roman',20),bg='#008081')
            url_out.grid(column = 3,row = 2, padx=10, pady =10)
            result = Label(window2,text = res.text,font=('Times New Roman',20),width=25,bg='#008081')
            result.grid(column = 3,row = 3, padx=10, pady =10)
            window2.mainloop()
        except Exception as e:
            raise


if __name__ == '__main__':
    url_long = "https://www.mk-mode.com/octopress/2018/02/25/python-napier-computation/"
    try:
        obj = UrlShortenTinyurl()
        obj.shorten(url_long)
    except Exception as e:
        traceback.print_exc()
