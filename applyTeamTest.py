import requests

header ={
	"authorization": "0c302f37495640524a036c58053346ba31981ae9",
	"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15"
}


def apply(name, cardNumber):
	applyData = {
	"pName": name,
	"gender": 1,
	"country": 344,
	"identType": 2,
	"identCard": cardNumber,
	"birthDate": "1993-06-03",
	"phone": "15811540164",
	"email": "x@b.am",
	"bloodType": "A",
	"province": "上海市",
	"city": "黄浦区",
	"Address": "ceshi",
    "clothesSize": "XXL",
	"emergency": "dd",
	"emergencyPhone": "15811540163",
	"job": 1,
	"education": 1,
	"income": "5万以内",
    "matchEventID": "5233590237812791",
	"teamID": "5234610124832434",
	"runnerSource": 2
	}
	applyUrl = "https://saas-user-gw.mararun.com/v1/application/apply"
	try:
		request = requests.post(url = applyUrl, headers=header,data = applyData)
		print("status_code = %s" %request.status_code)
		print(request.json())
	except Exception as e:
		print(e)

for i in range(10,32):
	print("i=",i)
	name = "testName"+ str(i)
	cardNumber = i
	apply(name, cardNumber)
	print("-----------------")










