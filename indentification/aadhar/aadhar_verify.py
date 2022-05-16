import requests
import json

url = "https://kyc-api.aadhaarkyc.io/api/v1/aadhaar-v2/generate-otp"

payload = json.dumps({
  "id_number": "GIVEN_AADHAAR_NUMBER"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer YOUR_TOKEN'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

url = "https://kyc-api.aadhaarkyc.io/api/v1/aadhaar-v2/submit-otp"

payload = json.dumps({
  "client_id": "GENERATED_CLIENT_ID",
  "otp": "708768"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)