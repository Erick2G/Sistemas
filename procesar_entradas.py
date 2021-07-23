
silabas =[
	['a'],
	['b'],
	['c'],
	['d'],
	['e'],
	['f'],
	['g'],
	['h'],
	['i'],
	['j'],
	['k'],
	['l'],
	['m'],
	['n'],
	['o'],
	['p'],
	['q'],
	['r'],
	['s'],
	['t'],
	['u'],
	['v'],
	['w'],
	['x'],
	['y'],
	['z'],
	['ñ']

]


silabas =[
	['que','ent','nte','con','est','ado','par','en','de','er','es','ue','la','ra','os'],
	['los','era','ien','men','per','sta','nt','te','ar','qu','el','ta','do','co'],
	['ara','por','una','ion','ant','tra','erp','re','as','on','an','to','lo','st','un'],
	['nto','ció','aci','las','com','ste','or','ad','ie','se','ci','al','pa','na','güe','güi'],
	['res','ier','ten','dos','des','ver','ido','ada','ro','no','me','in','ho','ca','cu'],
	['e','a','o','s','n','r','i'],
	['l','d','t','u','c','m'],
	['p','b','h','q','y','v','g'],
	['ó','í','f','j','z','á','é','ñ','x','k'],

	#end spanish -----------------
	['the','and','ang','her,','you','ver','was','th','he','an','er','in','re','nd','ou'],
	['hat','for','not','thi','tha','his','en','on','ed','to','it','at','ha','ve'],
	['ent','ion','ith','ere','wit','all','eve','as','or','hi','ar','te','es','ng','is'],
	['oul','uld','tio','ter','had','hen','st','le','al','ti','se','ea','wa','me'],
	['era','are','hin','our','sho','ted','ome','but','nt','ne','cu','ca'],
	['e','t','a','o','n','i','h'],
	['s','r','l','d','u','c'],
	['m','w','y','f','g','p','b'],
	['k','j','x','q','z'],

	#end english ------------------
	['ich','ein','der','sch','die','und','che','en','er','ch','de','ei','ie','in','te'],
	['cht','den','hen','ine','ten','ung','ge','un','nd','ic','es','be','he','st'],
	['hen','nde','lic','ver','sie','ste','nen','ne','an','re','se','di','sc','au','ng'],
	['eit','ber','ter','nge','das','ach','si','le','da','it','ht','el','li'],
	['and','ers','ren','ere','nic','ist','sic','ben','auf','lle','abe','end','mit','men','sei','sen','ige','aus','nte','ese'],
	['e','n','i','r','s','t','a'],
	['d','h','u','l','c','g'],
	['m','o','b','w','f','k','z'],
	['v','p','ü','ä','ö','j','x','y','q']
	#end german xD
]


def estructuraSilaba(palabra):
	entradas = [int(0)]*27

	for g in range(len(silabas)):
		for i in range(len(silabas[g])):
			if silabas[g][i] in palabra:
				entradas[g]+=1

	return entradas

