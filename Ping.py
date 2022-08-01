from pythonping import ping
import time
import json

List = json.loads(open('Ping.Servers').read()) #Change Ping.Servers to where you have it in the public_html place/folder

while True:
    time.sleep(3)
    Servers = 0
    SText = ''
    Text = ''
    for Continent in List:
        #print('## '+Continent+' ##\n\n') #Debuging
        Text = Text+'## '+Continent+' ##\n\n'
        for Place in List[Continent]:
            PText = '# Servers in '+Place[0]+' ('+Place[1]+'):\n'
            for Server in Place[3]:
                Servers = Servers+1
                try:
                    Pping = ping(Server[0], timeout=1, count=1)
                    Line = str(Pping).split('\n')[0]
                    Time = Line.split('bytes in ')[1].strip()
                    SText = SText+Time+'\n'
                    PText = PText+'Server in '+Server[2]+' [ONLINE]:\nPing Time: '+Time+'\nServer Domain: '+Server[1]+'\nServer IP: '+Server[0]+'\n\n'
                except:
                    SText = SText+'#\n'
                    PText = PText+'Server in '+Server[2]+' [OFFLINE or TIMEOUT]:\nPing Time: NULL\nServer Domain: '+Server[1]+'\nServer IP: '+Server[0]+'\n\n'

            #print(PText) #Debuging
            Text = Text+PText
    SText = SText+'##'
    F = open('Ping.Data', 'w') #Change Ping.Data to where you have it in the public_html place/folder
    F.write(Text)
    F.close()
    F2 = open('Server.Data', 'w')  #Change Server.Data to when you have it in the public_html place/folder
    F2.write(SText)
    F2.close()