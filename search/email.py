import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
class email:
    def __init__(self,fro,to,msg,subject):
        self.fro = fro
        self.to = to
        self.msg = msg
        self.subject = subject

        #Dont tough 
        self.api_key = 'c9de1d29fd0a0b3a6b506584254fac51'
        self.api_secret = '1e687abdeb4d565ba62d61592330ae3e'
    def test_email(self):
        try:
            self.to
            msg = MIMEMultipart()

            msg['From'] = self.fro 
            msg['To'] = self.to
            msg['Subject'] = "Test de conexão"

            body = str(self.msg)

            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('in-v3.mailjet.com', 587)
            server.starttls()
            server.login(self.api_key,self.api_secret)
            text = msg.as_string()
            server.sendmail(self.fro, self.to, text)
            server.quit()
            print('\nEmail enviado com sucesso!')
            return(True)
        except BaseException as ex:
            st = "\nErro ao enviar email:   " + ex
            raise st

            """ Experimental 
            Load json templates and replace <Atribute> for values

            """
    def get_templates(self,name,params):
        #Mensages should be and array for each line
        #Params must be an dict
        import json
        #Some  BS tests
        if (type(params) != type(dict())): return(False)

        local = './templates/email/'+ str(name) + '.json'
        try:
            with open(local) as tp:
                mensage = str()
                temp = json.loads(tp.read())
                for x in params:
                    param_str = '<'+str(x) + '>'
                    temp['msg'] = str(temp['msg']).replace(param_str,params[x])
                #Parsing dict into an array
                for y in temp['msg']:
                    mensage =+ str(y)
                self.msg = mensage
                self.subject = temp['subject']
        except BaseException as ex:
            raise ex
        return(temp)

    #Basicly the same stuff as the first one
    def send_email(self):

        try:
            self.to
            msg = MIMEMultipart()

            msg['From'] = self.fro 
            msg['To'] = self.to
            msg['Subject'] = self.subject
            body = str(self.msg)

            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('in-v3.mailjet.com', 587)
            server.starttls()
            server.login(self.api_key,self.api_secret)
            text = msg.as_string()
            server.sendmail(self.fro, self.to, text)
            server.quit()
            print('\nEmail enviado com sucesso!')
            self.print()
            return(True)
        except BaseException as ex:
            raise ex

    def print(self):
        print(self.fro)
        print(self.to)
        print(self.msg)
        print(self.subject)