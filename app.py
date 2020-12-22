import json

from flask import Flask,render_template
from flask import request
from flask import jsonify

import requests as http

app = Flask(__name__)

states = {
"Andhra Pradesh":"आंध्र प्रदेश",
"Arunachal Pradesh":"अरुणाचल प्रदेश",
"Assam":"असम",
"Bihar":"बिहार",
"Chhattisgarh":"छत्तीसगढ़",
"Goa":"गोवा",
"Gujarat":"गुजरात",
"Haryana":"हरियाणा",
"Himachal Pradesh":"हिमाचल प्रदेश",
"Jammu and Kashmir":"जम्मू और कश्मीर",
"Jharkhand":"झारखंड",
"Karnataka":"कर्नाटक",
"Kerala":"केरल",
"Madhya Pradesh":"मध्य प्रदेश",
"Maharashtra":"महाराष्ट्र",
"Manipur":"मणिपुर",
"Meghalaya":"मेघालय",
"Mizoram":"मिजोरम",
"Nagaland":"नगालैंड",
"Odisha":"ओडिशा",
"Punjab":"पंजाब",
"Rajasthan":"राजस्थान",
"Sikkim":"सिक्किम",
"Tamil Nadu":"तमिलनाडु",
"Telangana":"तेलंगाना",
"Tripura":"त्रिपुरा",
"Uttar Pradesh":"उत्तर प्रदेश",
"Uttarakhand":"उत्तराखंड",
"West Bengal":"पश्चिम बंगाल",
"Andaman and Nicobar Islands": "अंडमान व नोकोबार द्वीप समूह",
"Chandigarh":"चंडीगढ़",
"Dadra and Nagar Haveli" : "दादरा और नगर हवेली",
"Daman and Diu":"दमन और दीव",
"Lakshadweep":"लक्षद्वीप",
"Delhi":"दिल्ली",
"Puducherry":"पुडुचेरी"}

@app.route('/')
def hi():
    API_KEY = '579b464db66ec23bdd00000188e8cbf7c0f1426c45b312eb9ce4f6c5'
    offset = 0
    limit = 10
    # date = '1-10-2020'
    state = 'Uttar Pradesh'
    url = 'https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key={}&filters[state]={}&format=json&offset={}&limit={}'.format(API_KEY,state,offset,limit)
    # url2 = 'https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key={}&format=json&offset={}&limit={}'.format(API_KEY,offset,limit)

    args = request.args
    for k, v in args.items():
        print(f"{k}:{v}")

    if "state" in args:
        state = args['state']
    response = http.get(url)
    # print(response.text)
    # print("sdsdsddsds")
    return json.loads(response.text)
    # return render_template("filter.html")