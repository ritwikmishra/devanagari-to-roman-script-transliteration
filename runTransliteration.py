# -*- coding: utf-8 -*-
import csv
import sys

# unicode conversion
# 'फ़'.encode('utf-8') --> b'\xe0\xa4\xab\xe0\xa4\xbc'
# (b'\xe0\xa4\xab\xe0\xa4\xbc').decode() --> 'फ़'

# ''.join(f'\\u{ord(char):04X}' for char in 'फ़') --> \u092B\u093C
# print('\u092B\u093C') --> फ़
# '\\u092B\\u093C'.encode().decode('unicode_escape') --> फ़

def transliterate(eng_text, vowels, consonants):
	content = eng_text

	# if ज्ञ appears in beginning then [gy], otherwise gya
	# if क्ष appears in beginning then sh, otherwise [ksh]
	# square brackets means default value

	content = content.replace('ज़','ज़').replace('ड़','ड़').replace('फ़','फ़') # replacing combinations with single character
	content = content.replace('क\u093C','\u0958').replace('\u0916\u093C','ख़').replace('\u0917\u093C','ग़').replace('\u0922\u093C','ढ़').replace('य\u093C','\u095F')

	# --------------- shwa sound addition ---------------
	content2 = ''
	i = 0
	while i < len(content):
		if content[i] == '\u094D':
			# since we are already covering halants below, entering this loop will be very rare
			# we will enter it when there is 
			# <hindi-cons><halant><hindi-cons><halant><hindi-cons>
			#     -3         -2       -1        i^        +1
			# example: ???
			# let us preserve the halant
			content2+=content[i]
		elif i+1 < len(content):
			if content[i+1] == '\u094D': # halant
				if i+3 < len(content):
					if content[i] in consonants.keys() and content[i+3] in consonants.keys():
						# <hindi-cons><halant><hindi-cons><hindi-cons>
						#   i^           +1       +2         +3
						# example: prashn
						content2 = content2 + content[i]+content[i+1]+content[i+2]+'a'
					else:
						# <hindi-cons><halant><hindi-cons><not-hindi-cons>
						#   i^           +1       +2         +3
						# here <not-hindi-cons> can mean hindi-vowel or a punctuation mark or whitespace
						# example: pyaar
						content2 = content2 + content[i]+content[i+1]+content[i+2]
					i+=2
				elif i+2 < len(content):
					# <hindi-cons><halant><hindi-cons><end-of-seq>
					#   i^           +1       +2         +3
					# example: jashn
					content2 = content2 + content[i]+content[i+1]+content[i+2]
					i+=2
				else:
					# <hindi-cons><halant><end-of-seq>
					#   i^           +1       +2      
					# a rare word which is ending with a hindi consonant having a halant
					# example: ??
					# let us preserve the halant
					content2 = content2 + content[i]+content[i+1]
					i+=1
			else:
				if content[i] in consonants.keys() and content[i+1] in consonants.keys():
					if i == 0:
						# <beg-of-seq><hindi-cons><hindi-cons>
						#      -1          i^           +1       
						# example: हर --> har
						content2 = content2 + content[i]+'a'
					elif content[i-1] in [' ','\n','\t',':']:
						# <sep><hindi-cons><hindi-cons>
						#   -1    i^           +1       
						# new word starts after <sep>
						# <sep> can be whitespace or new line 
						# example: _हर --> har
						content2 = content2 + content[i]+'a'
					elif content[i-1] in vowels.keys() or content[i-1] in consonants.keys():
						if i+2 == len(content) or content[i+2] not in vowels.keys():
							# <hindi-vow or hindi-cons><hindi-cons><hindi-cons><eos or not-hindi-vow>
							#            -1                  ^i           +1            +2
							# example: अमल --> amal , विमल --> vimal
							# example: कमल --> kamal
							content2 = content2 + content[i]+'a'
						else:
							# <hindi-vow or hindi-cons><hindi-cons><hindi-cons><hindi-vow>
							#            -1                  ^i           +1       +2
							# example: अमली --> amli , विमला --> vimla
							# example: कमला --> kamla
							content2 = content2 + content[i]
					else:
						# we assume <sep>
						# example: #बज --> #baj
						content2 = content2 + content[i]+'a'


						
				else:
					if content[i+1] == 'ा':
						if i+2 < len(content):
							if content[i+2] in consonants.keys() or content[i+2] == 'ँ':
								# <hindi-cons><sound-of-A><hindi-cons or chandra-bindu>
								#   i^           +1          +2
								# example: हार --> haar, चाँद --> chaand
								content2 = content2 + content[i]+'a'
							else:
								# <hindi-cons><sound-of-A><not-hindi-cons>
								#   i^           +1          +2
								# here <not-hindi-cons> can mean hindi-vowel or a punctuation mark or whitespace
								# example: गया --> gaya , मनाओ --> manao
								content2+=content[i]
						else:
							# <hindi-cons><sound-of-A><end-of-seq>
							#   i^           +1           +2
							# example: का --> ka
							content2+=content[i]

					elif content[i+1] == 'ं':
						if i+2 < len(content):
							if content[i] in consonants.keys() and content[i+2] in consonants.keys():
								# <hindi-cons><sound-n><hindi-cons>
								#   i^           +1       +2
								# example: छंद --> chhand
								content2 = content2 + content[i]+'a'
							else:
								# <hindi-cons><sound-n><not-hindi-cons>
								#   i^           +1       +2
								# here <not-hindi-cons> can mean hindi-vowel or a punctuation mark or whitespace
								# example: 
								content2 = content2 + content[i]

						else:
							# <hindi-cons><sound-n><end-of-seq>
							#   i^           +1       +2
							# example: मैं --> main
							content2 = content2 + content[i]

					else:
						# <hindi-cons><hindi-vow>
						#   i^           +1       
						# example: से --> se
						content2+=content[i]
		else:
			content2+=content[i]
		i+=1
	content = content2
	# ---------------------------------------------------

	# print(content)

	for vk in vowels.keys():
		content = content.replace(vk,vowels[vk])

	for ck in consonants.keys():
		if ck in content[:len(ck)]: # consonant in the beginning
			content = '^'+content
		# a character appears in the beginning of a word if
		# 1) if the word is the first word of the text
		# 2) if the word has any of the following before it: <whitespace> ' ' <tab> '\t' <new-line> '\n'
		if ck == 'ज्ञ':
			content = content.replace('^'+ck,consonants[ck]+'a')
			content = content.replace(' '+ck,' '+consonants[ck]+'a')
			content = content.replace('\t'+ck,'\t'+consonants[ck]+'a')
			content = content.replace('\n'+ck,'\n'+consonants[ck]+'a')
		elif ck == 'क्ष':
			content = content.replace('^'+ck,consonants[ck][1:])
			content = content.replace(' '+ck,' '+consonants[ck][1:])
			content = content.replace('\t'+ck,'\t'+consonants[ck][1:])
			content = content.replace('\n'+ck,'\n'+consonants[ck][1:])
		if '^' == content[0]:
			content = content[1:]
		content = content.replace(ck,consonants[ck])

	content = content.replace('\u094D','') # removing all halants
	content = content.replace('।','.') # removing all purn viraam

	return content

vowels = {'ँ':'n',
'ं':'n',
'ः':'a',
'अ':'a',
'आ':'aa',
'इ':'i',
'ई':'ee',
'उ':'u',
'ऊ':'oo',
'ऋ':'ri',
'ए':'e',
'ऐ':'ae',
'ओ':'o',
'औ':'au',
'ा':'a',
'ि':'i',
'ी':'i',
'ु':'u',
'ू':'oo',
'ृ':'ri',
'े':'e',
'ै':'ai',
'ो':'o',
'ौ':'au'}

consonants = {
'क्ष':'ksh', # they need to be in the beginning of this dictionary because they are combinations
'त्र':'tr',
'ज्ञ':'gy',

'क':'k', 
'क़': 'q',
'ख':'kh',
'ख़':'kh',
'ग':'g', 
'ग़':'gh',
'घ':'gh', 
'ङ':'ng',

'च':'ch', 
'छ':'chh', 
'ज':'j', 
'ज़':'z',
'ज़':'z', #these two are very different, see them in unicode by 'ज़'.encode'utf-8'. You'll see.
'झ':'jh', 
'ञ':'nj', 

'ट':'t', 
'ठ':'th', 
'ड':'d', 
'ड़':'r',
'ड़':'r', #these two are very different, see them in unicode by 'ड़'.encode'utf-8'. You'll see.
'ढ':'dh', 
'ढ़':'dh',
'ण':'n', 

'त':'t', 
'थ':'th', 
'द':'d', 
'ध':'dh', 
'न':'n', 

'प':'p', 
'फ':'ph', 
'फ़':'f',
'फ़':'f', #these two फ़ are very different, see them in unicode by 'फ़'.encode'utf-8'. You'll see.
'ब':'b', 
'भ':'bh', 
'म':'m', 

'य':'y',
'य़':'y',
'र':'r', 
'ल':'l', 
'व':'v', 
'श':'sh', 

'ष':'sh', 
'स':'s', 
'ह':'h'}

file = open(sys.argv[1],'r')
content = file.read()
file.close()

str1 = transliterate(content, vowels, consonants)

print(str1)

file = open(sys.argv[1]+'OUTPUT','w')
file.write(str1.strip())
file.close()
print("DONE! Open "+sys.argv[1]+"OUTPUT")
