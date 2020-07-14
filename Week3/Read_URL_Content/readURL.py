import urllib.request
import webbrowser
#To opent the URL in webBrowser 
webbrowser.open('http://www.google.com')

#To read the content of the URL, it will read it as html code
with urllib.request.urlopen("http://www.google.com") as url:
    url_read= url.read()
    print(url_read)
    
#To save the image on the URL    
image_url = 'https://data.whicdn.com/images/221672809/original.jpg' #the image on the web
save_name = 'my_image.jpg' #local name to be saved
urllib.request.urlretrieve(image_url, save_name)
