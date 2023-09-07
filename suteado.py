import requests

class SuteAddress():

    def __init__(self,SessionHash=None):
        self.headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
        self.hash = SessionHash

    def get_csrf(self,session=None):
        if session == None:
            session = requests.Session()
        cookie = {"cookie_sessionhash":self.hash}
        response = session.get(f"https://m.kuku.lu/index.php",headers=self.headers,cookies=cookie)
        return response.cookies.get_dict()["cookie_csrf_token"]

    def create_Mail(self,domain,address=None):
        session = requests.Session()
        csrf_token = self.get_csrf(session)
        if address == None:
            address = ""
        if domain == None:
            domain = ""
        response = session.get(f"https://m.kuku.lu/index.php?action=addMailAddrByManual&nopost=1&by_system=1&t=&csrf_token_check={csrf_token}&newdomain={domain}&newuser={address}&recaptcha_token=&_=",
                               headers=self.headers,data=None,cookies={"cookie_sessionhash":self.hash})
        data = response.text
        return data
    
    def get_AllAddress(self):
        response = requests.get("https://m.kuku.lu/index._addrlist.php?&t=&nopost=1&_=",
        headers=self.headers,cookies={"cookie_sessionhash":self.hash})
        data = response.text.split('Data("')
        mail_list = []
        for count in data:
            mail_list.append(count.split('")')[0])
        mail_list.pop(0)
        if mail_list == []:
            raise ValueError("SessionHashが間違っています。")
        return mail_list
    
    def get_mailbox(self,amount:int):
        response = requests.get("https://m.kuku.lu/recv._ajax.php?&&nopost=1&csrf_token_check=&csrf_subtoken_check=&_=",
                                headers=self.headers,cookies={"cookie_sessionhash":self.hash})
        data = response.text
        keys = []
        numbers = data.split('mailnumlist = "')[1].split('"')[0].split(",")
        if len(numbers) <= amount:
            amount = len(numbers)
        else:
            for count in range(len(numbers)-amount):
                numbers.pop()
        for count in range(amount):
            count = count + 1
            keys.append(data.split("openMailData('")[count].split("',")[1].replace(" '",""))
        mails = {}
        for counter in range(count):
            counter = counter
            num = numbers[counter]
            key = keys[counter]
            data = {
            "num": num,
            "key": key,
            "noscroll": "1"}
            response = requests.post("https://m.kuku.lu/smphone.app.recv.view.php",
                                 headers=self.headers,data=data,cookies={"cookie_sessionhash":self.hash})
            title = response.text.split('<div class="full" style="flex-grow:100;">\r\n\t\t\t\t\t')[1].split("\t\t")[0]
            content = response.text.split('<div style="height:fit-content;">')[1].split("</script>")[0].replace('<div dir="auto">',"").replace("\r","").replace("<div>","").replace("</div>","").replace("\t","").replace("</a>","").replace("\n","")
            mails[f"title{counter+1}"] = title
            mails[f"content{counter+1}"] = content
        return mails
