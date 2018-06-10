from flask import Flask, render_template, request, redirect
import cloudinary as Cloud
import cloudinary
import cloudinary.uploader
import cloudinary.api
import requests
import os

Cloud.config.update = ({
    'cloud_name':os.environ.get('dalhousie-cloudcomputing'),
    'api_key': os.environ.get('718933552512797'),
    'api_secret': os.environ.get('CXwvYj0iw4VRrEg3djd0_wYOVAA')
})

cloudinary.config( 
  cloud_name = "dalhousie-cloudcomputing", 
  api_key = "718933552512797", 
  api_secret = "CXwvYj0iw4VRrEg3djd0_wYOVAA" 
)


app = Flask(__name__)

@app.route('/')
def main():  
    return render_template('main.html')

@app.route('/fetch_details', methods = ['POST'])
def fetch_details():
    
    def ListImages():
        dr=cloudinary.api.resources()
        list = []
        s=""
        res_len=len(dr['resources'])
        try:
            if(res_len>0):
                for x in range(res_len):
                    temp=str(x+1)+". "+dr['resources'][x]['url']
                    list.append(temp)                
                s= "\n".join(list)
                return s
        except Exception as e:
            print(e)
            return s 
    
    s= ListImages();
    
    print (s)
    
    return render_template('main.html', s=s)
    
@app.route('/delete_file', methods = ['POST']) 
def delete_file():
    
    file_name = request.form['delete_text']
    
    print (file_name)

    def Destroy(url):
        try:
            filename_url= url.split('/')[-1]
            filename=filename_url.split('.')[0]
            r=cloudinary.uploader.destroy(filename)
            print(r['result'])
            if(r['result']=='ok'):
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
    
    a = Destroy(file_name);
    
    print (a)
    
    if (a == True):
        text_message = "File deleted!"
    else:
        text_message = "Error:: File not found. File not deleted!"
    
    return render_template('main.html', text_message = text_message)

@app.route('/download_file', methods = ['POST']) 
def download_file():
    
    file_name = request.form['download_text']
    
    print (file_name)
    
    def Download(url):
        try:
            filename = url.split('/')[-1]
            r = requests.get(url, allow_redirects=True)
            if(r.status_code==200):
                open(filename, 'wb').write(r.content)
                return True
            else:
                return False
        except Exception:
            return False
    
    b = Download(file_name);
    
    print (b)
    
    if (b == True):
        text_message_2 = "File downloaded!"
    else:
        text_message_2 = "Error:: File not found. File not downloaded!"
    
    return render_template('main.html', text_message_2 = text_message_2)

if __name__ == '__main__':
    app.run()