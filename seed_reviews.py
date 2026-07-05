import urllib.request
import json
import ssl

url = 'https://script.google.com/macros/s/AKfycbyVB3O9B-yKMPjmQDCyOXas08J1YWEpoajfxRuvw5_Vt8NGstVctH3oaWAWHKdEuuU7/exec'

reviews = [
    { "name": "Sarah & Mike", "country": "United Kingdom", "text": "Traveling with Andy was the highlight of our trip. His knowledge of the local history and secret spots made our adventure truly exceptional." },
    { "name": "James Doe", "country": "Australia", "text": "We saw 3 leopards in Yala thanks to Andy's eagle eyes! He arranged everything perfectly and we just had to sit back and enjoy." },
    { "name": "Anna Lindström", "country": "Sweden", "text": "The train ride to Ella was magical. Andy took care of our tickets months in advance. Best guide we've ever had on any of our travels!" },
    { "name": "Paul Thompson", "country": "Canada", "text": "Our family of 5 had an incredible time. Andy was so patient with the kids and customized everything to our pace. Highly recommended." },
    { "name": "Tour Group CHN251", "country": "China", "text": "Excellent service! The guide was highly praised for being extremely patient and attentive. We were very satisfied with the meals. The vehicle was comfortable, clean, and tidy, and the flower welcome ceremony was a beautiful touch." }
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for r in reviews:
    data = json.dumps(r).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    req.add_header('Content-Type', 'text/plain;charset=utf-8')
    try:
        response = urllib.request.urlopen(req, context=ctx)
        print(f"Posted {r['name']}: {response.read().decode('utf-8')}")
    except Exception as e:
        print(f"Failed to post {r['name']}: {e}")
