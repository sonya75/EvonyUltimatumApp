from evony import *
import time
import os
import sys
import json
import requests
import random
from actionfactory.builder import *
from actionfactory.quest import *
from actionfactory.items import *
from threading import Thread
def createacc(server,mailguy,declarewar,proxy='',proxytype='HTTP',useclient=None,timeout=30,callback=None):
	try:
		def tth(infiunw):
			return
		declarewar=declarewar.strip().split(';')
		chnum=random.randint(0,(len(declarewar)-1))
		declarewar=declarewar[chnum].split(',')
		declarewar=int(declarewar[0])+int(declarewar[1])*800
		if proxy.count(':')!=1:
			proxyhost=''
			proxyport=0
			useproxy=False
		else:
			useproxy=True
			proxyhost=proxy.split(':')[0]
			proxyport=int(proxy.split(':')[-1])
		if useclient==None:
			x=Client(server,setproxy=useproxy,proxyhost=proxyhost,proxyport=proxyport,proxytype=proxytype,callback=tth,timeout=timeout)
		else:
			x=useclient
		fatalerror=None
		y=x.registernewplayer()
		callback("|9|9")
		builder=Builder(x)
		castleid=y['data']['player']['castles'][0]['id']
		fieldid=y['data']['player']['castles'][0]['fieldId']
		quest=Quest(x,castleid)
		items=Item(x,castleid)
		x.client.sendmessage('common.addToFavorites',{})
		res=x.responsehandler('common.addToFavorites')
		quest.completequest(226)
		builder.createbuilding(castleid,0,1)
		builder.upgradebuilding(castleid,0,1,1)
		quest.completequest(1)
		items.useitem('player.box.present.2')
		quest.completequest(2)
		quest.completequest(535)
		builder.createbuilding(castleid,1,21)
		time.sleep(1)
		builder.createbuilding(castleid,2,29)
		time.sleep(2)
		builder.createbuilding(castleid,1001,7)
		quest.completequest(15)
		builder.createbuilding(castleid,1002,4)
		quest.completequest(16)
		builder.createbuilding(castleid,1003,5)
		quest.completequest(17)
		builder.createbuilding(castleid,1004,6)
		quest.completequest(18)
		time.sleep(2)
		x.client.sendmessage('interior.modifyCommenceRate',{'ironrate':100,'foodrate':100,'stonerate':100,'woodrate':100,'castleId':castleid})
		res=x.responsehandler('interior.modifyCommenceRate')
		quest.completequest(19)
		quest.completequest(80)
		quest.completequest(86)
		x.client.sendmessage('interior.modifyTaxRate',{'castleId':castleid,'tax':20})
		res=x.responsehandler('interior.modifyTaxRate')
		quest.completequest(20)
		x.client.sendmessage('city.modifyCastleName',{'castleId':castleid,'name':'NO','logUrl':'images/icon/cityLogo/citylogo_01.png'})
		res=x.responsehandler('city.modifyCastleName')
		quest.completequest(21)
		x.client.sendmessage('city.modifyFlag',{'newFlag':'JO'})
		res=x.responsehandler('city.modifyFlag')
		builder.createbuilding(castleid,3,23)
		builder.speedup(castleid,'consume.2.a',3)
		quest.completequest(22)
		builder.upgradebuilding(castleid,1002,4,1)
		quest.completequest(23)
		quest.completequest(138)
		builder.createbuilding(castleid,4,3)
		builder.speedup(castleid,'consume.2.a',4)
		quest.completequest(139)
		builder.createbuilding(castleid,5,1)
		builder.upgradebuilding(castleid,5,1,1)
		builder.createbuilding(castleid,6,1)
		builder.upgradebuilding(castleid,6,1,1)
		builder.createbuilding(castleid,7,1)
		builder.upgradebuilding(castleid,7,1,1)
		ddf=False
		quest.special()
		x.client.sendmessage('interior.taxation',{'typeId':3,'castleId':castleid})
		res=x.responsehandler('interior.taxation')
		quest.completequest(12)
		quest.completequest(155)
		builder.upgradebuilding(castleid,-1)
		builder.speedup(castleid,'consume.2.a',-1)
		builder.speedup(castleid,'consume.2.a',-1)
		quest.completequest(26)
		quest.completequest(194)
		quest.completequest(214)
		items.useitem('player.box.gambling.3')
		quest.completequest(223)
		builder.createbuilding(castleid,8,25)
		builder.speedup(castleid,'consume.2.a',8)
		quest.completequest(35)
		quest.completequest(210)
		builder.createbuilding(castleid,9,2)
		quest.completequest(87)
		x.client.sendmessage('mail.sendMail',{'username':mailguy,'content':'Hey','title':'Hi'})
		res=x.responsehandler('mail.sendMail')
		quest.completequest(78)
		quest.completequest(87)
		quest.completequest(79)
		quest.completequest(87)
		builder.createbuilding(castleid,10,27)
		quest.completequest(81)
		quest.completequest(87)
		builder.upgradebuilding(castleid,1004,6,1)
		builder.upgradebuilding(castleid,1004)
		builder.speedup(castleid,'consume.2.a',1004)
		builder.createbuilding(castleid,11,22)
		quest.completequest(111)
		builder.upgradebuilding(castleid,11)
		builder.speedup(castleid,'consume.2.a',11)
		time.sleep(2)
		builder.createbuilding(castleid,12,26)
		builder.speedup(castleid,'consume.2.a',12)
		quest.completequest(112)
		builder.upgradebuilding(castleid,1003,5,1)
		time.sleep(2)
		builder.createbuilding(castleid,-2,32)
		builder.speedup(castleid,'consume.2.a',-2)
		builder.speedup(castleid,'consume.2.a',-2)
		quest.completequest(240)
		quest.completequest(113)
		quest.completequest(184)
		x.client.sendmessage('shop.getBuyResourceInfo',{'castleId':castleid})
		res=x.responsehandler('shop.getBuyResourceInfo')
		x.client.sendmessage('shop.buyResource',{'castleId':castleid,'stoneUse': 0, 'foodUse': 0, 'woodUse': 5, 'ironUse': 0})
		res=x.responsehandler('shop.buyResource')
		builder.upgradebuilding(castleid,-1)
		builder.speedup(castleid,'consume.2.b',-1)
		quest.completequest(241)
		quest.completequest(27)
		quest.completequest(211)
		builder.createbuilding(castleid,13,30)
		builder.speedup(castleid,'consume.2.b',13)
		quest.completequest(145)
		quest.completequest(581,wait=False)
		quest.completequest(582,wait=False)
		x.client.sendmessage('trade.newTrade',{'castleId':castleid,'price':'0.9','tradeType':0,'amount':20000,'resType':2})
		amount=0
		idlist=[]
		while amount<20000:
			res=x.responsehandler('server.TransingTradeUpdate',checkok=False)
			tramount=res['data']['bean']['amount']
			trid=res['data']['bean']['id']
			if trid in idlist:
				continue
			idlist.append(trid)
			amount+=tramount
			if tramount>=10000:
				break
			if amount>=20000:
				raise
		x.client.sendmessage('trade.speedUpTrans',{'itemId':'consume.transaction.1','castleId':castleid,'transingTradeId':trid})
		res=x.responsehandler('trade.speedUpTrans')
		time.sleep(5)
		builder.upgradebuilding(castleid,-2)
		builder.speedup(castleid,'consume.2.b',-2)
		quest.completequest(114)
		items.useitem('player.box.present.4')
		items.useitem('player.box.special.1')
		quest.completequest(536)
		quest.completequest(97)
		quest.completequest(199)
		quest.completequest(215)
		quest.completequest(216)
		quest.completequest(185)
		x.client.sendmessage('trade.newTrade',{'castleId':castleid,'price':'1','tradeType':0,'amount':70000,'resType':2})
		amount=0
		while amount<70000:
			res=x.responsehandler('server.TransingTradeUpdate',checkok=False)
			tramount=res['data']['bean']['amount']
			trid=res['data']['bean']['id']
			if trid in idlist:
				continue
			idlist.append(trid)
			amount+=tramount
			if tramount>=30000:
				break
			if amount>=70000:
				raise
		x.client.sendmessage('trade.speedUpTrans',{'itemId':'consume.transaction.1','castleId':castleid,'transingTradeId':trid})
		res=x.responsehandler('trade.speedUpTrans')
		time.sleep(5)
		builder.upgradebuilding(castleid,-2)
		builder.speedup(castleid,'consume.2.b.1',-2)
		quest.completequest(115)
		quest.completequest(186)
		builder.upgradebuilding(castleid,-1)
		builder.speedup(castleid,'consume.2.b.1',-1)
		quest.completequest(28)
		quest.completequest(195)
		builder.upgradebuilding(castleid,-1)
		builder.speedup(castleid,'consume.2.b',-1)
		builder.speedup(castleid,'consume.2.b',-1)
		builder.speedup(castleid,'consume.2.b',-1)
		builder.speedup(castleid,'consume.2.b',-1)
		quest.completequest(29)
		quest.completequest(209)
		items.buyitem('player.trick.jbqy')
		x.client.sendmessage('shop.useTrickItem',{'itemId':'player.trick.jbqy', 'armyid': 0, 'castleId': fieldid})
		res=x.responsehandler('shop.useTrickItem')
		quest.completequest(212)
		quest.completequest(552)
		items.buyitem('player.trick.bxez')
		x.client.sendmessage('shop.useTrickItem',{'itemId':'player.trick.bxez','armyid':0,'castleId':declarewar})
		fatalerror="You have possibly entered a invalid co-ordinate to declare war on."
		res=x.responsehandler('shop.useTrickItem')
		fatalerror=None
		quest.completequest(553)
		time.sleep(2)
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
		callback("8|||FINISH|"+str(chnum))
		return x
	except:
		try:
			x.close()
			del x
		except:
			pass
		return
def _stvote(server,mailguy,declarewar,proxy=None,proxytype='HTTP',useclient=None,callback=None,checksource=None,timeout=30,totalrunning=None):
	xpo=0
	useclient=None
	while xpo!=None:
		if checksource!=None:
			if checksource.killsignal:
				break
		if useclient!=None:
			useclient.registered=False
		xpo=createacc(server,mailguy,declarewar,proxy,proxytype,useclient,timeout=timeout,callback=callback)
		useclient=xpo
	totalrunning[0]-=1
def startscout(server,mailguy,declarewar,proxy=None,proxytype='HTTP',useclient=None,callback=None,checksource=None,timeout=30,totalconn=1):
	totalrunning=[0]
	for i in range(0,totalconn):
		totalrunning[0]+=1
		Thread(target=_stvote,args=(server,mailguy,declarewar,proxy,proxytype,useclient,callback),kwargs={'checksource':checksource,'totalrunning':totalrunning,'timeout':timeout}).start()
	while True:
		if checksource!=None:
			if checksource.killsignal:
				if totalrunning[0]>0:
					time.sleep(.3)
					continue
				callback("|NOKILL|")
				del callback
				del totalrunning
				return
		if totalrunning[0]==0:
			callback("|KILL|")
			del callback
			del totalrunning
			return
		time.sleep(.3)
