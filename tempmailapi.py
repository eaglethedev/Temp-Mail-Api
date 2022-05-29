from time import sleep
import requests
import json


r = requests.post("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
emailrep = r.text
em = emailrep.strip()
email = em.split("@")
adress = email[0]
domain = email[1]
adresss =adress.replace('["',"")
domainn =domain.replace('"]',"")
esm = emailrep.replace('"]',"")
emailver = esm.replace('["',"")

url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={adresss}&domain={domainn}"

print(f"""
Email  : {emailver}
Domain : {domainn} 
      """)
print("-"*30)
print("Waiting for new emails...")
while True:
    r = requests.get(url)
    parsed = json.loads(r.text)
    try:
        if 'id' in parsed[0]:
            for url in parsed:
                subject = url['subject']
                id = url["id"]
                
                print(f"""
Subject : {subject}
                      """)
            url2 = f"https://www.1secmail.com/api/v1/?action=readMessage&login={adresss}&domain={domainn}&id={id}"
            response = requests.get(url2)
            response.raise_for_status()
            # access JSOn content
            jsonResponse = response.json()
            for key, value in jsonResponse.items():
                test= jsonResponse["body"]
                print(test)
                break
            
            break
            
    except:
        pass


