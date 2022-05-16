import requests
import json

url = "https://aadhaar-number-verification.p.rapidapi.com/Uidverifywebsvcv1/Getcaptcha"

payload = "clientid=111&txn_id=985656&method=getcaptcha"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Host": "aadhaar-number-verification.p.rapidapi.com",
	"X-RapidAPI-Key": "755b5f6b31msh0a57b80698ace6ep116191jsne5929616c853"
}

response = requests.request("POST", url, data=payload, headers=headers)
response = json.loads(response.text)

captchastr = response['Succeeded']["Captcha_Details"]['captchaBase64String']
captchaID = response['Succeeded']["Captcha_Details"]['captchaTxnId']
print(captchastr, captchaID)


url = "https://aadhaar-number-verification.p.rapidapi.com/Uidverifywebsvcv1/Uidverify"

payload = r"captchaValue=TK6HXq&captchaTxnId=58p5MxkQrNFp&method=uidvalidate&clientid=111&txn_id=4545533&consent=Y&uidnumber=%3CREQUIRED%3E"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Host": "aadhaar-number-verification.p.rapidapi.com",
	"X-RapidAPI-Key": "755b5f6b31msh0a57b80698ace6ep116191jsne5929616c853"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)