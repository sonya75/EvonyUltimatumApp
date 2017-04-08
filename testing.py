from evony import *
import time
import os
import sys
import json
import requests
from actionfactory.builder import *
from actionfactory.quest import *
from actionfactory.items import *
from threading import Thread
def createacc(server,mailguy,declarewar,proxy='',proxytype='HTTP',useclient=None,timeout=30,callback=None):
	declarewar=declarewar.strip().split(',')
	declarewar=int(declarewar[0])+int(declarewar[1])*800
	callback("PROGRESSREPORT0")
	if proxy.count(':')!=1:
		proxyhost=''
		proxyport=0
		useproxy=False
	else:
		useproxy=True
		proxyhost=proxy.split(':')[0]
		proxyport=int(proxy.split(':')[-1])
	if useclient==None:
		x=Client(server,setproxy=useproxy,proxyhost=proxyhost,proxyport=proxyport,proxytype=proxytype,callback=callback,timeout=timeout)
	else:
		x=useclient
	fatalerror=None
	callback("PROGRESSREPORT1")
	y=x.registernewplayer()
	callback("|9|9")
	callback("PROGRESSREPORT1")
	builder=Builder(x)
	callback("PROGRESSREPORT2")
	castleid=y['data']['player']['castles'][0]['id']
	callback("PROGRESSREPORT2")
	fieldid=y['data']['player']['castles'][0]['fieldId']
	callback("PROGRESSREPORT3")
	quest=Quest(x,castleid)
	callback("PROGRESSREPORT3")
	items=Item(x,castleid)
	callback("PROGRESSREPORT4")
	x.client.sendmessage('common.addToFavorites',{})
	callback("PROGRESSREPORT4")
	res=x.responsehandler('common.addToFavorites')
	callback("PROGRESSREPORT5")
	quest.completequest(226)
	callback("PROGRESSREPORT5")
	builder.createbuilding(castleid,0,1)
	callback("PROGRESSREPORT6")
	builder.upgradebuilding(castleid,0,1,1)
	callback("PROGRESSREPORT6")
	quest.completequest(1)
	callback("PROGRESSREPORT7")
	items.useitem('player.box.present.2')
	callback("PROGRESSREPORT7")
	quest.completequest(2)
	callback("PROGRESSREPORT8")
	quest.completequest(535)
	callback("PROGRESSREPORT8")
	builder.createbuilding(castleid,1,21)
	callback("PROGRESSREPORT9")
	time.sleep(1)
	callback("PROGRESSREPORT9")
	builder.createbuilding(castleid,2,29)
	callback("PROGRESSREPORT10")
	time.sleep(2)
	callback("PROGRESSREPORT10")
	builder.createbuilding(castleid,1001,7)
	callback("PROGRESSREPORT11")
	quest.completequest(15)
	callback("PROGRESSREPORT11")
	builder.createbuilding(castleid,1002,4)
	callback("PROGRESSREPORT11")
	quest.completequest(16)
	callback("PROGRESSREPORT12")
	builder.createbuilding(castleid,1003,5)
	callback("PROGRESSREPORT12")
	quest.completequest(17)
	callback("PROGRESSREPORT13")
	builder.createbuilding(castleid,1004,6)
	callback("PROGRESSREPORT13")
	quest.completequest(18)
	callback("PROGRESSREPORT14")
	time.sleep(2)
	callback("PROGRESSREPORT14")
	x.client.sendmessage('interior.modifyCommenceRate',{'ironrate':100,'foodrate':100,'stonerate':100,'woodrate':100,'castleId':castleid})
	callback("PROGRESSREPORT15")
	res=x.responsehandler('interior.modifyCommenceRate')
	callback("PROGRESSREPORT15")
	quest.completequest(19)
	callback("PROGRESSREPORT16")
	quest.completequest(80)
	callback("PROGRESSREPORT16")
	quest.completequest(86)
	callback("PROGRESSREPORT17")
	x.client.sendmessage('interior.modifyTaxRate',{'castleId':castleid,'tax':20})
	callback("PROGRESSREPORT17")
	res=x.responsehandler('interior.modifyTaxRate')
	callback("PROGRESSREPORT18")
	quest.completequest(20)
	callback("PROGRESSREPORT18")
	x.client.sendmessage('city.modifyCastleName',{'castleId':castleid,'name':'NO','logUrl':'images/icon/cityLogo/citylogo_01.png'})
	callback("PROGRESSREPORT19")
	res=x.responsehandler('city.modifyCastleName')
	callback("PROGRESSREPORT19")
	quest.completequest(21)
	callback("PROGRESSREPORT20")
	x.client.sendmessage('city.modifyFlag',{'newFlag':'JO'})
	callback("PROGRESSREPORT20")
	res=x.responsehandler('city.modifyFlag')
	callback("PROGRESSREPORT21")
	builder.createbuilding(castleid,3,23)
	callback("PROGRESSREPORT21")
	builder.speedup(castleid,'consume.2.a',3)
	callback("PROGRESSREPORT22")
	quest.completequest(22)
	callback("PROGRESSREPORT22")
	builder.upgradebuilding(castleid,1002,4,1)
	callback("PROGRESSREPORT22")
	quest.completequest(23)
	callback("PROGRESSREPORT23")
	quest.completequest(138)
	callback("PROGRESSREPORT23")
	builder.createbuilding(castleid,4,3)
	callback("PROGRESSREPORT24")
	builder.speedup(castleid,'consume.2.a',4)
	callback("PROGRESSREPORT24")
	quest.completequest(139)
	callback("PROGRESSREPORT25")
	builder.createbuilding(castleid,5,1)
	callback("PROGRESSREPORT25")
	builder.upgradebuilding(castleid,5,1,1)
	callback("PROGRESSREPORT26")
	builder.createbuilding(castleid,6,1)
	callback("PROGRESSREPORT26")
	builder.upgradebuilding(castleid,6,1,1)
	callback("PROGRESSREPORT27")
	builder.createbuilding(castleid,7,1)
	callback("PROGRESSREPORT27")
	builder.upgradebuilding(castleid,7,1,1)
	callback("PROGRESSREPORT28")
	ddf=False
	callback("PROGRESSREPORT28")
	quest.special()
	callback("PROGRESSREPORT29")
	x.client.sendmessage('interior.taxation',{'typeId':3,'castleId':castleid})
	callback("PROGRESSREPORT29")
	res=x.responsehandler('interior.taxation')
	callback("PROGRESSREPORT30")
	quest.completequest(12)
	callback("PROGRESSREPORT30")
	quest.completequest(155)
	callback("PROGRESSREPORT31")
	builder.upgradebuilding(castleid,-1)
	callback("PROGRESSREPORT31")
	builder.speedup(castleid,'consume.2.a',-1)
	callback("PROGRESSREPORT32")
	builder.speedup(castleid,'consume.2.a',-1)
	callback("PROGRESSREPORT32")
	quest.completequest(26)
	callback("PROGRESSREPORT33")
	quest.completequest(194)
	callback("PROGRESSREPORT33")
	quest.completequest(214)
	callback("PROGRESSREPORT33")
	items.useitem('player.box.gambling.3')
	callback("PROGRESSREPORT34")
	quest.completequest(223)
	callback("PROGRESSREPORT34")
	builder.createbuilding(castleid,8,25)
	callback("PROGRESSREPORT35")
	builder.speedup(castleid,'consume.2.a',8)
	callback("PROGRESSREPORT35")
	quest.completequest(35)
	callback("PROGRESSREPORT36")
	quest.completequest(210)
	callback("PROGRESSREPORT36")
	builder.createbuilding(castleid,9,2)
	callback("PROGRESSREPORT37")
	quest.completequest(87)
	callback("PROGRESSREPORT37")
	x.client.sendmessage('mail.sendMail',{'username':mailguy,'content':'Hey','title':'Hi'})
	callback("PROGRESSREPORT38")
	res=x.responsehandler('mail.sendMail')
	callback("PROGRESSREPORT38")
	quest.completequest(78)
	callback("PROGRESSREPORT39")
	quest.completequest(87)
	callback("PROGRESSREPORT40")
	quest.completequest(79)
	callback("PROGRESSREPORT41")
	quest.completequest(87)
	callback("PROGRESSREPORT41")
	builder.createbuilding(castleid,10,27)
	callback("PROGRESSREPORT42")
	quest.completequest(81)
	callback("PROGRESSREPORT42")
	quest.completequest(87)
	callback("PROGRESSREPORT43")
	builder.upgradebuilding(castleid,1004,6,1)
	callback("PROGRESSREPORT43")
	builder.upgradebuilding(castleid,1004)
	callback("PROGRESSREPORT44")
	builder.speedup(castleid,'consume.2.a',1004)
	callback("PROGRESSREPORT44")
	builder.createbuilding(castleid,11,22)
	callback("PROGRESSREPORT44")
	quest.completequest(111)
	callback("PROGRESSREPORT45")
	builder.upgradebuilding(castleid,11)
	callback("PROGRESSREPORT45")
	builder.speedup(castleid,'consume.2.a',11)
	callback("PROGRESSREPORT46")
	time.sleep(2)
	callback("PROGRESSREPORT46")
	builder.createbuilding(castleid,12,26)
	callback("PROGRESSREPORT47")
	builder.speedup(castleid,'consume.2.a',12)
	callback("PROGRESSREPORT47")
	quest.completequest(112)
	callback("PROGRESSREPORT48")
	builder.upgradebuilding(castleid,1003,5,1)
	callback("PROGRESSREPORT48")
	time.sleep(2)
	callback("PROGRESSREPORT49")
	builder.createbuilding(castleid,-2,32)
	callback("PROGRESSREPORT49")
	builder.speedup(castleid,'consume.2.a',-2)
	callback("PROGRESSREPORT50")
	builder.speedup(castleid,'consume.2.a',-2)
	callback("PROGRESSREPORT50")
	quest.completequest(240)
	callback("PROGRESSREPORT51")
	quest.completequest(113)
	callback("PROGRESSREPORT51")
	quest.completequest(184)
	callback("PROGRESSREPORT52")
	x.client.sendmessage('shop.getBuyResourceInfo',{'castleId':castleid})
	callback("PROGRESSREPORT82")
	res=x.responsehandler('shop.getBuyResourceInfo')
	callback("PROGRESSREPORT82")
	x.client.sendmessage('shop.buyResource',{'castleId':castleid,'stoneUse': 0, 'foodUse': 0, 'woodUse': 5, 'ironUse': 0})
	callback("PROGRESSREPORT83")
	res=x.responsehandler('shop.buyResource')
	builder.upgradebuilding(castleid,-1)
	callback("PROGRESSREPORT52")
	builder.speedup(castleid,'consume.2.b',-1)
	callback("PROGRESSREPORT53")
	quest.completequest(241)
	callback("PROGRESSREPORT53")
	quest.completequest(27)
	callback("PROGRESSREPORT54")
	quest.completequest(211)
	callback("PROGRESSREPORT54")
	builder.createbuilding(castleid,13,30)
	callback("PROGRESSREPORT55")
	builder.speedup(castleid,'consume.2.b',13)
	callback("PROGRESSREPORT55")
	quest.completequest(145)
	callback("PROGRESSREPORT56")
	quest.completequest(581,wait=False)
	callback("PROGRESSREPORT56")
	quest.completequest(582,wait=False)
	callback("PROGRESSREPORT56")
	x.client.sendmessage('trade.newTrade',{'castleId':castleid,'price':'1','tradeType':0,'amount':20000,'resType':2})
	callback("PROGRESSREPORT57")
	amount=0
	callback("PROGRESSREPORT57")
	idlist=[]
	callback("PROGRESSREPORT58")
	while amount<20000:
		callback("PROGRESSREPORT58")
		res=x.responsehandler('server.TransingTradeUpdate',checkok=False)
		callback("PROGRESSREPORT59")
		tramount=res['data']['bean']['amount']
		callback("PROGRESSREPORT59")
		trid=res['data']['bean']['id']
		callback("PROGRESSREPORT60")
		if trid in idlist:
			callback("PROGRESSREPORT60")
			continue
		callback("PROGRESSREPORT61")
		idlist.append(trid)
		callback("PROGRESSREPORT61")
		amount+=tramount
		callback("PROGRESSREPORT62")
		if tramount>=10000:
			callback("PROGRESSREPORT62")
			break
		callback("PROGRESSREPORT63")
		if amount>=20000:
			callback("PROGRESSREPORT63")
			raise
	callback("PROGRESSREPORT64")
	x.client.sendmessage('trade.speedUpTrans',{'itemId':'consume.transaction.1','castleId':castleid,'transingTradeId':trid})
	callback("PROGRESSREPORT64")
	res=x.responsehandler('trade.speedUpTrans')
	callback("PROGRESSREPORT65")
	time.sleep(5)
	callback("PROGRESSREPORT65")
	builder.upgradebuilding(castleid,-2)
	callback("PROGRESSREPORT66")
	builder.speedup(castleid,'consume.2.b',-2)
	callback("PROGRESSREPORT66")
	quest.completequest(114)
	callback("PROGRESSREPORT67")
	items.useitem('player.box.present.4')
	callback("PROGRESSREPORT67")
	items.useitem('player.box.special.1')
	callback("PROGRESSREPORT67")
	quest.completequest(536)
	callback("PROGRESSREPORT68")
	quest.completequest(97)
	callback("PROGRESSREPORT68")
	quest.completequest(199)
	callback("PROGRESSREPORT69")
	quest.completequest(215)
	callback("PROGRESSREPORT69")
	quest.completequest(216)
	callback("PROGRESSREPORT70")
	quest.completequest(185)
	callback("PROGRESSREPORT71")
	x.client.sendmessage('trade.newTrade',{'castleId':castleid,'price':'1','tradeType':0,'amount':70000,'resType':2})
	callback("PROGRESSREPORT72")
	amount=0
	callback("PROGRESSREPORT72")
	while amount<70000:
		callback("PROGRESSREPORT73")
		res=x.responsehandler('server.TransingTradeUpdate',checkok=False)
		callback("PROGRESSREPORT73")
		tramount=res['data']['bean']['amount']
		callback("PROGRESSREPORT74")
		trid=res['data']['bean']['id']
		callback("PROGRESSREPORT74")
		if trid in idlist:
			callback("PROGRESSREPORT75")
			continue
		callback("PROGRESSREPORT75")
		idlist.append(trid)
		callback("PROGRESSREPORT76")
		amount+=tramount
		callback("PROGRESSREPORT76")
		if tramount>=30000:
			callback("PROGRESSREPORT77")
			break
		callback("PROGRESSREPORT77")
		if amount>=70000:
			callback("PROGRESSREPORT78")
			raise
	callback("PROGRESSREPORT78")
	x.client.sendmessage('trade.speedUpTrans',{'itemId':'consume.transaction.1','castleId':castleid,'transingTradeId':trid})
	callback("PROGRESSREPORT78")
	res=x.responsehandler('trade.speedUpTrans')
	callback("PROGRESSREPORT79")
	time.sleep(5)
	callback("PROGRESSREPORT79")
	builder.upgradebuilding(castleid,-2)
	callback("PROGRESSREPORT80")
	builder.speedup(castleid,'consume.2.b.1',-2)
	callback("PROGRESSREPORT80")
	quest.completequest(115)
	callback("PROGRESSREPORT81")
	quest.completequest(186)
	callback("PROGRESSREPORT81")
	builder.upgradebuilding(castleid,-1)
	callback("PROGRESSREPORT84")
	builder.speedup(castleid,'consume.2.b.1',-1)
	callback("PROGRESSREPORT84")
	quest.completequest(28)
	callback("PROGRESSREPORT85")
	quest.completequest(195)
	callback("PROGRESSREPORT85")
	builder.upgradebuilding(castleid,-1)
	callback("PROGRESSREPORT86")
	builder.speedup(castleid,'consume.2.b',-1)
	callback("PROGRESSREPORT86")
	builder.speedup(castleid,'consume.2.b',-1)
	callback("PROGRESSREPORT87")
	builder.speedup(castleid,'consume.2.b',-1)
	callback("PROGRESSREPORT87")
	builder.speedup(castleid,'consume.2.b',-1)
	callback("PROGRESSREPORT88")
	quest.completequest(29)
	callback("PROGRESSREPORT88")
	quest.completequest(209)
	callback("PROGRESSREPORT89")
	items.buyitem('player.trick.jbqy')
	callback("PROGRESSREPORT89")
	x.client.sendmessage('shop.useTrickItem',{'itemId':'player.trick.jbqy', 'armyid': 0, 'castleId': fieldid})
	callback("PROGRESSREPORT89")
	res=x.responsehandler('shop.useTrickItem')
	callback("PROGRESSREPORT90")
	quest.completequest(212)
	callback("PROGRESSREPORT90")
	quest.completequest(552)
	callback("PROGRESSREPORT91")
	items.buyitem('player.trick.bxez')
	callback("PROGRESSREPORT91")
	x.client.sendmessage('shop.useTrickItem',{'itemId':'player.trick.bxez','armyid':0,'castleId':declarewar})
	fatalerror="You have possibly entered a invalid co-ordinate to declare war on."
	callback("PROGRESSREPORT92")
	res=x.responsehandler('shop.useTrickItem')
	fatalerror=None
	callback("PROGRESSREPORT92")
	quest.completequest(553)
	callback("PROGRESSREPORT93")
	time.sleep(2)
	callback("PROGRESSREPORT93")
	builder.upgradebuilding(castleid,2)
	builder.speedup(castleid,'free.speed',2)
	builder.upgradebuilding(castleid,2)
	builder.speedup(castleid,'consume.2.a',2)
	builder.upgradebuilding(castleid,2)
	builder.speedup(castleid,'consume.2.a',2)
	builder.speedup(castleid,'consume.2.a',2)
	builder.upgradebuilding(castleid,2)
	builder.speedup(castleid,'consume.2.b',2)
	builder.upgradebuilding(castleid,10)
	builder.speedup(castleid,'consume.2.a',10)
	builder.upgradebuilding(castleid,10)
	builder.speedup(castleid,'consume.2.b',10)
	builder.upgradebuilding(castleid,10)
	builder.speedup(castleid,'consume.2.b',10)
	allid=[]
	x.client.sendmessage('hero.getHerosListFromTavern',{'castleId':castleid})
	res=x.responsehandler('hero.getHerosListFromTavern')
	idf=res['data']['heros'][0]['name']
	x.client.sendmessage('hero.hireHero',{'heroName':idf,'castleId':castleid})
	res=x.responsehandler('server.HeroUpdate',checkok=False)
	df=res['data']['hero']['id']
	allid.append(df)
	x.client.sendmessage('hero.getHerosListFromTavern',{'castleId':castleid})
	res=x.responsehandler('hero.getHerosListFromTavern')
	idf=res['data']['heros'][0]['name']
	x.client.sendmessage('hero.hireHero',{'heroName':idf,'castleId':castleid})
	res=x.responsehandler('server.HeroUpdate',checkok=False)
	df=res['data']['hero']['id']
	allid.append(df)
	x.client.sendmessage('hero.getHerosListFromTavern',{'castleId':castleid})
	res=x.responsehandler('hero.getHerosListFromTavern')
	idf=res['data']['heros'][0]['name']
	x.client.sendmessage('hero.hireHero',{'heroName':idf,'castleId':castleid})
	res=x.responsehandler('server.HeroUpdate',checkok=False)
	df=res['data']['hero']['id']
	allid.append(df)
	x.client.sendmessage('hero.getHerosListFromTavern',{'castleId':castleid})
	res=x.responsehandler('hero.getHerosListFromTavern')
	idf=res['data']['heros'][0]['name']
	x.client.sendmessage('hero.hireHero',{'heroName':idf,'castleId':castleid})
	res=x.responsehandler('server.HeroUpdate',checkok=False)
	df=res['data']['hero']['id']
	allid.append(df)
	for j in allid:
		x.client.sendmessage('army.newArmy',{'castleId': castleid, 'newArmyBean': {'missionType': 5, 'resource': {'food': 0, 'stone': 0, 'wood': 0, 'gold': 0, 'iron': 0}, 'troops': {'catapult': 0, 'pikemen': 0, 'scouter': 0, 'peasants': 1, 'batteringRam': 0, 'carriage': 0, 'archer': 0, 'militia': 0, 'lightCavalry': 0, 'heavyCavalry': 0, 'ballista': 0, 'swordsmen': 0}, 'restTime': 0, 'backAfterConstruct': False, 'useFlag': False, 'heroId': j, 'useItem': False, 'targetPoint':declarewar}})
	for j in allid:
		res=x.responsehandler('army.newArmy')
def f(x):
	print(x)
createacc('na59','Kritter',"470,367",callback=f)