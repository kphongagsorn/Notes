substitution_cipher.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz%-.,! '
#germankey= '0123456789eihdbkalgmnodfpprcstuvwxyz%-.,! '
#key = '0123456789movsruklytpndejwxbqgiczhaf%-.,! '
#key= '0123456789zyxwvutsrqponmlkjihgfedcbaf%-.,! '
key ='0123456789abcdefghijklmnopqrstuvwxyz%-.,! '

#text = "Pxyj mb ibf jxulg ud peblt pujx VeugniVbl? Uj hbbgd dhutxjhi bmm yd ibf hbbg yj uj.  Pxyj ud peblt pujx uj? Hbbg ytyul ylm jxulg xyem yrbfj pxyj ud lbj eutxj. Vyl ibf pbeg bfj pxyj ud peblt? Uz ibf vyl, ibf mum tbbm. Tbbm hfvg! Jxud cudytn, lb anen cnlnne bz cyluji, ud y cndjutn bz jxn cbq kbkfhu, lbp cyvylj, cyludxnm. Xbpncne, jxud cyhbebfd cudujyjubl bz y ri-tbln cnqyjubl, djylmd cucuzunm ylm xyd cbpnm jb cylsfudx jxndn cnlyh ylm cuefhnlj cneaul cyltfyemult cuvn ylm cbfvxdyzult jxn cubhnljhi cuvubfd ylm cbeyvubfd cubhyjubl bz cbhujubl. Duvg bz jxn khyi bl pbemd? BG, ibfe zhyt ud exijxauv diwiti."

#text = "r_wlmg_vevm_mvvw_zm_zhxrr_gzyov"
text ="Nwh whdjwh qm uepen, T tjb fsmt tixgi jsrsh sigm gs mpzp xwqf iahxpv iw fslkt. pehgpxf qtextz_glacz_elt_neinrw_qsg_bums_dcp"
#text = "Mba Nhgiia bst Sbaeaktgusakmzwabcukmaqtvbaqukmnuaknzbi."
#Mba Nhgiia bst Sbaeaktgusakm zwabcukmaqt vbaqukmnuaknzbi.
#die flagge ist siebentausendzweihundertvierundfuenfzig.
#die flagge ist siebentausend zweihundert vierundfuenfzig.
#the flag is Seven thousand two hundred fifty-four// flag is 7254

#text ="Maq Flghg wbqm 61 ebs 85 rj iqlsz ukm wbait zwbsrcak 4 ukm 14 fi. Flaqoaqiqlasza ukm Oqlolqtblkak abkas aqwgrcsakak Tbaqas cgakiak vlk Ghtaq, Iasrcharct, Aqkgacquki ukm Qaiblk ge. Bj fuachaqak Fhbjg haeakma Flghgs sbkm bj Ghhiajabkak iqlaszaq ukm cgeak abk mukfhaqas ukm mbrctaqas Nahh ghs mgs vlk Tbaqak bk wgaqjaqak Qaiblkak. Tqltz mbasaq Gkogssukiak ibet as gurc Guskgcjak. Bj nqurctegqak Vbrtlqbg flakkak gusiawgrcsaka Flghgjgakkrcak ebs zu 14 fi, Wabercak ebs 11 fi wbaiak. Mgs Muqrcsrckbttsiawbrct maq klaqmhbrc haeakmak Tbaqa bst kbamqbiaq: Jgakkrcak aqqabrcak 12 fi, Wabercak 8 fi. Mba Flghgs bj kbamaqsrchgisgqjak Puaakshgkm sbkm iakaqahh fhabkaq, mgs Muqrcsrckbttsiawbrct maq Jgakkrcak eatqgait 8 fi, mgs maq Wabercak 6 fi. Mba Nhgiia bst Sbaeaktgusakmzwabcukmaqtvbaqukmnuaknzbi. Maq Flghg cgt eqgaukhbrc-sbheaqiqguas, wlhhbias Nahh, gk maj eab qaiahjgaszbiaq Onhaia Qaiakwgssaq wba gj Ianbamaq abkaq Akta geoaqht, ukm zwab jbt sobtzak, srcgqnak Fqghhak vaqsacaka Iqabncgakma jbt zwab Mgujak ukm mqab aktiaiakiasatztak Nbkiaqk, mba sbrc iut zuj Fhattaqk ukm Aqiqabnak vlk Zwabiak abikak. Mba Nbkiaqfuooak cgeak Ogobhhgqhabstak, mba makak mas Jaksrcak axtqaj gackhbrc sbkm. Bcqa Nuasza tqgiak abkak fqghhakhlsak Mgujak, mba zwabtak ukm mqbttak Zacak sbkm jbtabkgkmaq vaqwgrcsak, sl mgss sba jbt mak vaqsrcjlhzakak Fqghhak Zarfak aktnaqkak flakkak, uktaq makak sba cgaunbi habmak. Rcgqgftaqbstbsrca Jaqfjgha sbkm abka vlqstacakma, mukfha Kgsa ukm iqlsza Lcqak, wlqgk jgk sbact, mgss Qbarcak ukm Claqak bk sabkaj Haeak abka wbrctbia Qlhha sobahak. Maq Flghg cgt abkak bj Vaqcgahtkbs zu sabkaj Flaqoaq iqlszak Flon, massak Iacbqkjgssa qahgtbv iaqbki bst. Mgs Nahh wbhmhaeakmaq Flghgs bst vaqwbttaqtaq ghs mgs vlk Flghgs bk Jaksrcakcgkm. Jgakkrcak uktaqsrcabmak sbrc muqrc Clmaksgrf ukm Muntmquasak gk maq Equst vlk mak Wabercak, mba muqrc bcqak Eautah gun maq Egurcsabta iafakkzabrckat sbkm. Maq Eautah bst wba eab mak Wljegts (bj Iaiaksgtz zu mak Fgakiuqus) jbt kgrc uktak iaqbrctataq Lannkuki gusiastgttat. Aqwgrcsaka Jgakkrcak flakkak ebs zu 50% iqlaszaq ghs aqwgrcsaka Wabercak sabk ukm cgeak kaeak abkaq cgfbiak Fquajjuki maq Kgsa abka atwgs gkmaqa Flonnlqj."

def makeKey(alphabet):
   alphabet = list(alphabet)
   random.shuffle(alphabet)
   return ''.join(alphabet)

def encrypt(plaintext, key, alphabet):
    #keyMap = dict(zip(alphabet, germankey))
    keyMap = dict(zip(alphabet, key))
    return ''.join(keyMap.get(c.lower(), c) for c in plaintext)

def decrypt(cipher, key, alphabet):
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c.lower(), c) for c in cipher)

#cipher = encrypt(text, germankey, alphabet)
cipher = encrypt(text, key, alphabet)
print(text + "\n")
print(cipher)
#print(decrypt(cipher, key, alphabet))
#print(decrypt(cipher, germankey, alphabet))
