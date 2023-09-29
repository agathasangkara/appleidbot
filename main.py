try:
	import random, string
	import requests as r, sys, json
except Exception as e:
	print(e)

class Apple:
	
	def __init__(self):
		
		self.x = r.Session()
	
	def apple_service(self):
		ip = self.x.get("http://ip-api.com/json")
		print(f" IP Addres : {ip.json()['query']} | {ip.json()['city']}")
		ua = f"Music/4.8 Android/13 model/XiaomiRedmiNote{random.randint(1111,9999)} build/1676435016 (dt:66)"
		nama = random.choice([line.rstrip('\n') for line in open('username.txt')]).replace(" ","").lower()
		email = input(' Email : ')
		
		while True:
			initial = self.x.get("https://auth.tv.apple.com/auth/v1/liteReplayProtection/initializeSession", headers={"x-apple-store-front":"143476-2,8","user-agent":f"{ua}","content-type":"application/json","cookie":"geo=ID;dslang=GB-EN;site=GBR"})
			if "pageUUID" in initial.text:
				wr = initial.headers.get("set-cookie").split("wosid-replay=")[1].split(";")[0]
				page = initial.json()["pageUUID"]
			else:
				sys.exit(" Your IP Address Blocked Apple inc")
			
			pod = self.x.get("https://buy.tv.apple.com/account/pod", headers={"x-apple-store-front":"143476-2,8","User-Agent":f"{ua}","content-type":"application/json","cookie":f"geo=ID;dslang=GB-EN;site=GBR;wosid-replay={wr}"}).headers.get('set-cookie').split("itspod=")[1].split(';')[0]
			create = self.x.get("https://buy.tv.apple.com/account/restricted/create/options?restrictedAccountType=restrictedEmailOptimizedWeb", headers={"x-apple-store-front":"143476-2,8","User-Agent":f"{ua}","content-type":"application/json","cookie":f"geo=ID;dslang=GB-EN;site=GBR;wosid-replay={wr};itspod={pod}"})
			if "pageUUID" in create.text:
				pagec = create.json()["pageUUID"]
				ws = create.headers.get('set-cookie').split("wosid-lite=")[1].split(";")[0]
			else:
				sys.exit(f" Create Page error")
			
			createone = self.x.post("https://buy.tv.apple.com/WebObjects/MZFinance.woa/wa/validateAccountFieldsSrv", data=f"storefront=IDN&context=create&acAccountName={email}&acAccountPassword=%40Sangkara123&marketing=1&restrictedAccountType=restrictedEmailOptimizedWeb&addressOfficialCountryCode=IDN&paymentMethodType=None&pageUUID={pagec}&accountType=email&email={email}", headers={"x-apple-store-front":"143476-2,8","User-Agent":f"{ua}","content-type":"application/x-www-form-urlencoded;charset=UTF-8","cookie":f"geo=ID;dslang=GB-EN;site=GBR;wosid-replay={wr};itspod={pod};wosid-lite={ws}"})
			if "pageUUID" in createone.text:
				pageo = createone.json()["pageUUID"]
				ns = createone.headers.get("set-cookie").split("ns-mzf-inst=")[1].split(";")[0]
				mzf = createone.headers.get("set-cookie").split("mzf_in=")[1].split(";")[0]
				break
			else:
				continue
			
			createtwo = self.x.post("https://buy.tv.apple.com/WebObjects/MZFinance.woa/wa/validateAccountFieldsSrv", data=f"storefront=IDN&context=create&firstName=Aga&lastName=Maker&birthDay=19&birthMonth=01&birthYear=1999&acAccountName={email}&acAccountPassword=%40Sangkara123&marketing=1&restrictedAccountType=restrictedEmailOptimizedWeb&addressOfficialCountryCode=IDN&paymentMethodType=None&pageUUID={pagec}&agreedToTerms=1&accountType=email&email={email}", headers={"x-apple-store-front":"143476-2,8","User-Agent":f"{ua}","content-type":"application/x-www-form-urlencoded;charset=UTF-8","cookie":f"ns-mzf-inst={ns}; mzf_in={mzf}; dslang=GB-EN; site=GBR; wosid-replay={wr}; itspod={pod}; wosid-lite={ws}"})
			if "pageUUID" in createtwo:
				paget = createtwo.json()["pageUUID"]
				break
			else:
				continue
			
		send = self.x.post("https://buy.tv.apple.com/WebObjects/MZFinance.woa/wa/generateEmailConfirmationCodeSrv", json={"email":email}, headers={"x-apple-store-front":"143476-2,8","User-Agent":f"{ua}","content-type":"application/json","cookie":f"ns-mzf-inst={ns}; mzf_in={mzf}; dslang=GB-EN; site=GBR; wosid-replay={wr}; itspod={pod}; wosid-lite={ws}"})
		if "clientToken" in send.text:
			print(f" True sending Code email")
			client = send.json()["clientToken"]
		else:
			sys.exit(f" False sending Code email")
		
		
		otp = input(" OTP : ")
		
		verify = self.x.post("https://buy.tv.apple.com/WebObjects/MZFinance.woa/wa/validateEmailConfirmationCodeSrv", json={"email":email,"secretCode":otp,"clientToken":client}, headers={"x-apple-store-front":"143476-2,8","User-Agent":f"{ua}","content-type":"application/json","cookie":f"ns-mzf-inst={ns}; mzf_in={mzf}; dslang=GB-EN; site=GBR; wosid-replay={wr}; itspod={pod}; wosid-lite={ws}"})
		pagev = verify.json()["pageUUID"]
		create = self.x.post("https://buy.tv.apple.com/WebObjects/MZFinance.woa/wa/createAccountSrv?isTVPlus=true", data=f"storefront=IDN&context=create&firstName=Aga&lastName=Maker&birthDay=19&birthMonth=01&birthYear=1999&acAccountName={email}&acAccountPassword=%40Sangkara123&marketing=1&restrictedAccountType=restrictedEmailOptimizedWeb&addressOfficialCountryCode=IDN&paymentMethodType=None&pageUUID={pagev}&agreedToTerms=1&accountType=email&email={email}&secretCode={otp}&clientToken={client}&webCreate=true", headers={"x-apple-store-front":"143476-2,8","User-Agent":f"{ua}","content-type":"application/x-www-form-urlencoded;charset=UTF-8","cookie":f"ns-mzf-inst={ns}; mzf_in={mzf}; dslang=GB-EN; site=GBR; wosid-replay={wr}; itspod={pod}; wosid-lite={ws}"})
		print(create.text)
		
Apple().apple_service()
