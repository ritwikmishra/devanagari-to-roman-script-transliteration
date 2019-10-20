# devanagari-to-roman-script-transliteration
Python scipt to convert &lt;text written in devnagri script> TO &lt;text in roman/english script>

## USE
Open terminal
```
git clone https://github.com/ritwikmishra/devanagari-to-roman-script-transliteration.git
cd devanagari-to-roman-script-transliteration
python3 createDict.py
python3 runTransliteration.py sample
```

## COMPARISON
The comparison is taken for the following sample file:
```
ऋत्विक ने ये टूल बनाया है। ये python language में लिखा गया है।
राज! अगर ये तुझसे प्यार करती है तो ये पलट के देखेगी, पलट, पलट।
लंदन पहूँच गए, एक महीना कैसे गुज़रा, पता ही नहीं चला।
मैं चाहती हूं कि मेरी बेटी मुझे जाने।
मम्मा! मैं ये आठ चिठ्ठियां आप के पास छोड़ कर जा रही हूं।
अरे राजेश! यहां आओ यार, ये जो तुम्हारे ससुर जी हैं न, बड़े दिलचस्प इंसान हैं।
आपको बजाना- वजाना भी आता है, सिर्फ पोज़ लेकर खड़े हैं।
```

### Output of [Sheetal](https://github.com/sheetalgiri/devanagari-to-roman-script)
```
ritwika ne ye tula banaayaa hai। ye python language mem likhaa gayaa hai।
raaja! agara ye tujhase pyaara karati hai to ye palata ke dekhegi, palata, palata।
lumdana pahuncha gae, eka mahinaa kaise guja़raa, pataa hi nahim chalaa।
maim chaahati hum ki meri beti mujhe jaane।
mammaa! maim ye atha chiththiyaam apa ke paasa chhoda़ kara jaa rahi hum।
are raajesa! yahaam ao yaara, ye jo tumhaare sasura ji haim na, baड़e dilachaspa imsaana haim।
apako bajaanaa- wajaanaa bhi ataa hai, sirpha poज़ lekara khaड़e haim।
```

### Output of [Pandey](https://pandey.github.io/posts/transliterate-devanagari-to-latin.html)
```
r̥tvika ne ye ṭūla banāyā hai. ye python language meṃ likhā gayā hai. rāja! agara ye tujhase pyāra karatī hai to ye palaṭa ke dekhegī, palaṭa, palaṭa. laṃdana pahūṃca gae, eka mahīnā kaise guzarā, patā hī nahīṃ calā. maiṃ cāhatī hūṃ ki merī beṭī mujhe jāne. mammā! maiṃ ye āṭha ciṭhṭhiyāṃ āpa ke pāsa choṛa kara jā rahī hūṃ. are rājeśa! yahāṃ āo yāra, ye jo tumhāre sasura jī haiṃ na, bae dilacaspa iṃsāna haiṃ. āpako bajānā- vajānā bhī ātā hai, sirpha poa lekara khae haiṃ.
```

### Output of my method
```
ritvik ne ye tool banaya hai. ye python language men likha gaya hai.
raj! agar ye tujhse pyar karati hai to ye palat ke dekhegi, palat, palat.
lndan pahoonch ge, ek mahina kaise guzara, pata hi nahin chala.
main chahati hoon ki meri beti mujhe jane.
mamma! main ye aath chiththiyan aap ke pas chhor kar ja rahi hoon.
are rajesh! yahan aao yar, ye jo tumhare sasur ji hain n, bare dilachasp insan hain.
aapako bajana- vajana bhi aata hai, sirph poz lekar khare hain.
```

## Cite

### In footnote
```Code available on bit.ly/2pFG5g8```

### Bibtex
```
@misc{Ritwik2019,
  author = {Mishra, Ritwik},
  title = {devanagari-to-roman-script-transliteration},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/ritwikmishra/devanagari-to-roman-script-transliteration}},
}
```