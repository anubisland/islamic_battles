import asyncio, os, sys
import edge_tts

VOICES = { 'ar': 'ar-SA-ZariyahNeural', 'en': 'en-US-JennyNeural' }
SLOT = 'story'

BATTLES = [
  {
    "id": 1, "yearH": "٢ هـ", "yearM": "624 م", "epoch": "2 AH · 624 CE",
    "nameAr": "غَزْوَةُ بَدْرٍ الْكُبْرَى", "nameEn": "the Great Battle of Badr",
    "narratorAr": "وَقَفَ الْمُسْلِمُونَ صَفًّا وَاحِدًا كَالْبُنْيَانِ الْمَرْصُوصِ أَمَامَ جَيْشٍ يَفُوقُهُمْ ثَلَاثَةَ أَضْعَافٍ، لَكِنَّ التَّخْطِيطَ الْجُغْرَافِيَّ الْمُحْكَمَ وَالسَّيْطَرَةَ عَلَى الْمَاءِ صَنَعَا النَّصْرَ الْأَوَّلَ لِلإِسْلَامِ.",
    "narratorEn": "Muslims stood unified against a force three times their size. Masterful geographic planning and water control secured Islam's first great victory at the wells of Badr.",
    "causesAr": "اعْتِرَاضُ عِيرِ قُرَيْشٍ الْكُبْرَى الْقَادِمَةِ مِنَ الشَّامِ، وَتَصَاعُدُ التَّوَتُّرِ بَعْدَ الْهِجْرَةِ.",
    "causesEn": "Intercepting the Quraysh trade caravan from Syria amid post-Hijra escalating tensions.",
    "tacticAr": "السَّيْطَرَةُ الْكَامِلَةُ عَلَى مَصَادِرِ الْمِيَاهِ بِمَشُورَةِ الْحُبَابِ بْنِ الْمُنْذِرِ مَعَ تَشْكِيلِ صُفُوفٍ مُحْكَمَةٍ.",
    "tacticEn": "Complete water source control through Hubab ibn al-Mundhir's counsel, with tight formations.",
    "figuresAr": "الرَّسُولُ ﷺ، حَمْزَةُ بْنُ عَبْدِ الْمُطَّلِبِ، عَلِيُّ بْنُ أَبِي طَالِبٍ، الْحُبَابُ بْنُ الْمُنْذِرِ، أَبُو جَهْلٍ",
    "figuresEn": "The Prophet peace be upon him, Hamza ibn Abd al-Muttalib, Ali ibn Abi Talib, Al-Hubab ibn al-Mundhir, Abu Jahl the Quraysh commander",
    "resultsAr": "نَصْرٌ مُؤَزَّرٌ — مَقْتَلُ ٧٠ قَائِدًا مِنْ قُرَيْشٍ وَأَسْرُ ٧٠ آخَرِينَ.",
    "resultsEn": "Decisive victory — 70 Quraysh leaders killed, 70 captured. A turning point for the Islamic state.",
    "lessonsAr": ["الإِدَارَةُ اللُّوجِسْتِيَّةُ تَتَفَوَّقُ عَلَى الْكَثْرَةِ", "قِيمَةُ الشُّورَى الْمَيْدَانِيَّةِ", "الثِّقَةُ بِاللهِ تَصْنَعُ الرُّوحَ", "التَّحَكُّمُ الْجُغْرَافِيُّ حَاسِمٌ"],
    "lessonsEn": ["Logistics triumph over numbers", "Field consultation wins battles", "Faith builds unshakeable morale", "Geographic control is decisive"]
  },
  {
    "id": 2, "yearH": "٣ هـ", "yearM": "625 م", "epoch": "3 AH · 625 CE",
    "nameAr": "غَزْوَةُ أُحُدٍ", "nameEn": "the Battle of Uhud",
    "narratorAr": "صَعِدَ الرُّمَاةُ جَبَلَ عَيْنَيْنِ بِأَمْرٍ نَبَوِيٍّ صَارِمٍ أَلَّا يَبْرَحُوا مَكَانَهُمْ، لَكِنَّ اسْتِعْجَالَ الْغَنِيمَةِ فَتَحَ ثُغْرَةً اسْتِرَاتِيجِيَّةً قَلَبَتْ مَوَازِينَ الْمَعْرَكَةِ.",
    "narratorEn": "Archers held position by Prophetic order — until lure of spoils opened a fatal flank Khalid exploited.",
    "causesAr": "انْتِقَامُ قُرَيْشٍ لِهَزِيمَةِ بَدْرٍ بِجَيْشٍ ثَلَاثَةِ آلَافِ مُقَاتِلٍ.",
    "causesEn": "Quraysh revenge for Badr, mobilizing 3,000 warriors.",
    "tacticAr": "تَأْمِينُ الْعُمْقِ الدِّفَاعِيِّ بِنَشْرِ خَمْسِينَ رَامِيًا عَلَى جَبَلِ عَيْنَيْنِ لِحِمَايَةِ الظَّهْرِ.",
    "tacticEn": "Securing defensive depth by deploying 50 archers on Mount Aynayn.",
    "figuresAr": "الرَّسُولُ ﷺ، حَمْزَةُ سَيِّدُ الشُّهَدَاءِ، خَالِدُ بْنُ الْوَلِيدِ قُرَيْشٌ، عَبْدُ اللهِ بْنُ جُبَيْرٍ",
    "figuresEn": "The Prophet peace be upon him, Hamza the Lord of Martyrs, Khalid ibn al-Walid as a Quraysh commander, Abd Allah ibn Jubayr",
    "resultsAr": "اسْتِشْهَادُ ٧٠ صَحَابِيًّا مِنْهُمْ حَمْزَةُ — النَّبِيُّ ﷺ نَجَا وَالْجَيْشُ لَمْ يُبَدَّ.",
    "resultsEn": "70 companions martyred including Hamza. The Prophet peace be upon him survived unwounded and the army remained intact — a test, not a defeat.",
    "lessonsAr": ["الِالْتِزَامُ بِالْأَوَامِرِ فَرِيضَةٌ", "ثُغْرَةٌ وَاحِدَةٌ تَقْلِبُ النَّصْرَ", "الطَّمَعُ يُلْغِي الْخُطَطَ", "الثَّبَاتُ الْقِيَادِيُّ فِي الشَّدَائِدِ"],
    "lessonsEn": ["Strict obedience to orders is mandatory", "A single breach can flip a victory", "Greed cancels even perfect plans", "Steadfast leadership in hardship"]
  },
  {
    "id": 3, "yearH": "٥ هـ", "yearM": "627 م", "epoch": "5 AH · 627 CE",
    "nameAr": "غَزْوَةُ الْخَنْدَقِ", "nameEn": "the Battle of the Trench",
    "narratorAr": "عَشَرَةُ آلَافِ مُقَاتِلٍ جَاءُوا لِاسْتِئْصَالِ الْمُسْلِمِينَ فَوَقَفُوا مَذْهُولِينَ أَمَامَ أُخْدُودٍ عَمِيقٍ لَمْ تَعْرِفْهُ الْعَرَبُ قَطُّ.",
    "narratorEn": "Ten thousand warriors marched to annihilate Medina and stood frozen before a deep trench completely alien to Arabian warfare. The siege collapsed and the Confederates retreated in humiliation.",
    "causesAr": "تَحَالُفُ الْقَبَائِلِ لِاسْتِئْصَالِ الْمُسْلِمِينَ بِجَيْشٍ عَشَرَةِ آلَافِ مُقَاتِلٍ.",
    "causesEn": "Coalition mobilized 10,000 warriors to eliminate Medina.",
    "tacticAr": "الْمُفَاجَأَةُ الْهَنْدَسِيَّةُ بِحَفْرِ خَنْدَقٍ شَمَالِيٍّ بِمَشُورَةِ سَلْمَانَ الْفَارِسِيِّ.",
    "tacticEn": "A surprise defensive trench based on Salman al-Farisi's expertise.",
    "figuresAr": "الرَّسُولُ ﷺ، سَلْمَانُ الْفَارِسِيُّ، نُعَيْمُ بْنُ مَسْعُودٍ، أَبُو سُفْيَانَ",
    "figuresEn": "The Prophet peace be upon him, Salman al-Farisi who proposed the trench, Nuaym ibn Masud the diplomatic saboteur, Abu Sufyan the coalition commander",
    "resultsAr": "فَشَلُ الْحِصَارِ وَانْسِحَابُ الْأَحْزَابِ — نَصْرٌ حَاسِمٌ.",
    "resultsEn": "Siege failed — Coalition retreated. Decisive victory.",
    "lessonsAr": ["الاِسْتِفَادَةُ مِنْ عُلُومِ الْحَضَارَاتِ", "الدِّبْلُومَاسِيَّةُ تُكَمِّلُ الْقُوَّةَ", "الطَّبِيعَةُ حِصْنٌ مَنِيعٌ", "الْعَقْلُ أَقْوَى مِنَ الْعَضَلَاتِ"],
    "lessonsEn": ["Borrow military knowledge from all civilizations", "Diplomacy complements force", "Natural terrain is a fortress", "Intellect outweighs brute strength"]
  },
  {
    "id": 4, "yearH": "٧ هـ", "yearM": "628 م", "epoch": "7 AH · 628 CE",
    "nameAr": "غَزْوَةُ خَيْبَرَ", "nameEn": "the Conquest of Khaybar",
    "narratorAr": "حُمِلَتِ الرَّايَةُ بِأَمْرٍ نَبَوِيٍّ لِرَجُلٍ يُحِبُّ اللهَ وَرَسُولَهُ فَتَهَاوَتْ قِلَاعُ خَيْبَرَ الْمَنِيعَةُ.",
    "narratorEn": "The Prophet peace be upon him entrusted the banner to the true lover of Allah and His messenger and the mighty fortresses of Khaybar fell one by one before the righteous battalions.",
    "causesAr": "إِنْهَاءُ الْمُؤَامَرَاتِ الْعَسْكَرِيَّةِ وَقَطْعُ مَصَادِرِ تَمْوِيلِ الْأَحْزَابِ.",
    "causesEn": "Neutralizing conspiracies and cutting funding for anti-Muslim coalitions.",
    "tacticAr": "الْحِصَارُ الاِقْتِصَادِيُّ الْمُتَدَرِّجُ — عَزْلُ كُلِّ حِصْنٍ وَضَرْبُهُ مُنْفَرِدًا.",
    "tacticEn": "Graduated economic siege — isolating each fortress individually.",
    "figuresAr": "الرَّسُولُ ﷺ، عَلِيُّ بْنُ أَبِي طَالِبٍ، مَرْحَبٌ الْيَهُودِيُّ، صَفِيَّةُ بِنْتُ حُيَيٍّ",
    "figuresEn": "The Prophet peace be upon him, Ali ibn Abi Talib the conqueror of al-Qamus, Marhab the Jew who was slain, Safiyya bint Huyayy",
    "resultsAr": "فَتْحُ خَيْبَرَ — نِهَايَةُ الْخَطَرِ الشَّمَالِيِّ.",
    "resultsEn": "Conquest of Khaybar — end of the northern threat.",
    "lessonsAr": ["أَهَمِّيَّةُ الِاسْتِخْبَارَاتِ", "تَفْكِيكُ التَّحَالُفَاتِ", "التَّعْيِينُ الْقِيَادِيُّ الصَّحِيحُ", "الْحِصَارُ الاِقْتِصَادِيُّ سِلَاحٌ"],
    "lessonsEn": ["Good intelligence precedes victory", "Isolate fortresses then take them one by one", "Right leadership assignment matters", "Economic siege is a powerful weapon"]
  },
  {
    "id": 5, "yearH": "٨ هـ", "yearM": "629 م", "epoch": "8 AH · 629 CE",
    "nameAr": "مَعْرَكَةُ مُؤْتَةَ", "nameEn": "the Battle of Mu'tah",
    "narratorAr": "أَعَادَ خَالِدٌ تَرْتِيبَ الْجَنَاحَيْنِ فِي جَوْفِ اللَّيْلِ فَظَنَّ الرُّومُ أَنَّ مَدَدًا هَائِلًا وَصَلَ فَتَنَحَّوْا خَوْفًا.",
    "narratorEn": "Khalid reshuffled flanks at night — Byzantines believed reinforcements arrived and pulled back.",
    "causesAr": "مَقْتَلُ رَسُولِ النَّبِيِّ ﷺ عَلَى يَدِ الْغَسَّاسِنَةِ — رَدٌّ حَازِمٌ وَاجِبٌ.",
    "causesEn": "Assassination of the Prophet's envoy by the Ghassanid ruler demanded a decisive military response from Medina.",
    "tacticAr": "الْحَرْبُ النَّفْسِيَّةُ بِإِعَادَةِ هَيْكَلَةِ الْأَجْنِحَةِ لَيْلًا ثُمَّ انْسِحَابٌ تَكْتِيكِيٌّ مُنَظَّمٌ.",
    "tacticEn": "Psychological warfare: reshuffling flanks at night, masterful extraction.",
    "figuresAr": "زَيْدُ بْنُ حَارِثَةَ شَهِيدٌ، جَعْفَرُ بْنُ أَبِي طَالِبٍ شَهِيدٌ، عَبْدُ اللهِ بْنُ رَوَاحَةَ شَهِيدٌ، خَالِدُ بْنُ الْوَلِيدِ",
    "figuresEn": "Zayd ibn Haritha the first commander, Jafar ibn Abi Talib, Abd Allah ibn Rawaha, Khalid ibn al-Walid the Sword of Allah",
    "resultsAr": "اسْتِشْهَادُ الْقُوَّادِ الثَّلَاثَةِ — الْجَيْشُ عَادَ سَالِمًا.",
    "resultsEn": "Three commanders martyred, but troops returned safely.",
    "lessonsAr": ["التَّرَاجُعُ الْمُنَظَّمُ انْتِصَارٌ", "الْقِيَادَةُ تَتَكَيَّفُ مَعَ الظُّرُوفِ", "الْحَرْبُ النَّفْسِيَّةُ أَقْوَى", "الِاسْتِمْرَارِيَّةُ رَغْمَ فَقْدِ الْقَائِدِ"],
    "lessonsEn": ["An organized retreat is a strategic victory", "Leadership adapts to circumstances", "Psychological warfare surpasses spears", "Continuity despite losing the commander"]
  },
  {
    "id": 6, "yearH": "٨ هـ", "yearM": "630 م", "epoch": "8 AH · 630 CE",
    "nameAr": "غَزْوَةُ حُنَيْنٍ", "nameEn": "the Battle of Hunayn",
    "narratorAr": "أَنَا النَّبِيُّ لَا كَذِبَ أَنَا ابْنُ عَبْدِ الْمُطَّلِبِ! صَرْخَةٌ نَبَوِيَّةٌ زَلْزَلَتِ الْوَادِيَ فَأَعَادَتْ صُفُوفًا تَمَزَّقَتْ.",
    "narratorEn": "I am the Prophet no lie! A Prophetic war cry rallied shattered lines to victory.",
    "causesAr": "حَشَدَتْ قَبَائِلُ هَوَازِنَ وَثَقِيفٍ بَعْدَ فَتْحِ مَكَّةَ لِصَدِّ الْمَدِّ الإِسْلَامِيِّ.",
    "causesEn": "Hawazin and Thaqif tribes rallied to halt the Islamic advance.",
    "tacticAr": "اسْتِيعَابُ صَدْمَةِ الْكَمِينِ الْجَبَلِيِّ وَإِعَادَةُ التَّجَمُّعِ السَّرِيعِ وَالْهُجُومُ الْمُضَادُّ.",
    "tacticEn": "Absorbing the ambush, rapid regrouping, then crushing counter-offensive.",
    "figuresAr": "الرَّسُولُ ﷺ ثَبَتَ، الْعَبَّاسُ بْنُ عَبْدِ الْمُطَّلِبِ، أَبُو سُفْيَانَ بْنُ الْحَارِثِ، خَالِدُ بْنُ الْوَلِيدِ",
    "figuresEn": "The Prophet peace be upon him who held firm, Al-Abbas ibn Abd al-Muttalib, Abu Sufyan ibn al-Harith, Khalid ibn al-Walid",
    "resultsAr": "انْتِصَارٌ كَاسِحٌ — إِسْلَامُ هَوَازِنَ وَعَفْوٌ نَبَوِيٌّ كَرِيمٌ.",
    "resultsEn": "Crushing victory — Hawazin embraced Islam, captives pardoned.",
    "lessonsAr": ["لَا تَغْتَرَّ بِالْكَثْرَةِ", "الثَّبَاتُ الْقِيَادِيُّ يَصْنَعُ الْفَارِقَ", "الِانْهِيَارُ لَا يَعْنِي الْهَزِيمَةَ", "الْكَرَمُ يَكْسِبُ الْقُلُوبَ"],
    "lessonsEn": ["Never be deceived by numerical superiority", "Leadership resolve makes the difference", "Initial collapse does not mean defeat", "Generosity after victory wins hearts"]
  },
  {
    "id": 7, "yearH": "٩ هـ", "yearM": "630 م", "epoch": "9 AH · 630 CE",
    "nameAr": "غَزْوَةُ تَبُوكَ", "nameEn": "the Tabuk Expedition",
    "narratorAr": "سَارَ جَيْشُ الْعُسْرَةِ فِي هَجِيرِ الصَّيْفِ فَنَصَرَ اللهُ نَبِيَّهُ بِالرُّعْبِ فِي قُلُوبِ الرُّومِ.",
    "narratorEn": "The Army of Hardship marched through deserts — Allah cast terror into Byzantine hearts.",
    "causesAr": "تَجَمُّعُ قُوَّاتِ الرُّومِ لِضَرْبِ الدَّوْلَةِ الإِسْلَامِيَّةِ قَبْلَ اسْتِوَائِهَا.",
    "causesEn": "Byzantine forces massed to strike the Islamic state before it consolidated.",
    "tacticAr": "الرَّدْعُ الاِسْتِرَاتِيجِيُّ الْوِقَائِيُّ — نَقْلُ الْمَعْرَكَةِ إِلَى أَرَاضِي الْعَدُوِّ.",
    "tacticEn": "Preemptive deterrence — carrying the war to enemy territory.",
    "figuresAr": "الرَّسُولُ ﷺ، أَبُو بَكْرٍ أَنْفَقَ كُلَّ مَالِهِ، عُثْمَانُ جَهَّزَ الْجَيْشَ، الثَّلَاثَةُ الَّذِينَ خُلِّفُوا",
    "figuresEn": "The Prophet peace be upon him, Abu Bakr al-Siddiq who donated all his wealth, Uthman ibn Affan who equipped the army, The three companions who stayed behind",
    "resultsAr": "انْسِحَابُ الرُّومِ دُونَ قِتَالٍ — مُعَاهَدَاتُ سَلَامٍ.",
    "resultsEn": "Byzantine withdrawal without combat — peace treaties established.",
    "lessonsAr": ["الرَّدْعُ يَمْنَعُ الْحُرُوبَ", "الإِنْفَاقُ يَسْنُدُ الْعَسْكَرَ", "الْحَرْبُ النَّفْسِيَّةُ تَحْسِمُ", "الصَّبْرُ وَالتَّضْحِيَةُ سِلَاحٌ"],
    "lessonsEn": ["Deterrence prevents wars", "Financial sacrifice sustains the military", "Psychological warfare decides without bloodshed", "Patience and sacrifice are lethal weapons"]
  },
  {
    "id": 8, "yearH": "١٣ هـ", "yearM": "634 م", "epoch": "13 AH · 634 CE",
    "nameAr": "مَعْرَكَةُ الْيَرْمُوكِ", "nameEn": "the Battle of Yarmouk",
    "narratorAr": "أَعَادَ خَالِدٌ صِيَاغَةَ الْعُلُومِ الْعَسْكَرِيَّةِ بِتَكْتِيكِ الْكَرَادِيسِ لِيَهْزِمَ إِمْبَرَاطُورِيَّةً لَا تُقْهَرُ.",
    "narratorEn": "In the Syrian desert, Khalid ibn al-Walid rewrote the science of warfare with his revolutionary Karadis mobile squadron system, shattering a Byzantine empire that had stood for centuries and deemed itself unconquerable.",
    "causesAr": "رَغْبَةُ هِرَقْلَ فِي إِنْهَاءِ الْوُجُودِ الإِسْلَامِيِّ بِمِئَتَيْ أَلْفِ مُقَاتِلٍ.",
    "causesEn": "Heraclius sought to eliminate Islamic presence with 200,000 warriors.",
    "tacticAr": "نِظَامُ الْكَرَادِيسِ الثَّوْرِيُّ — عَزْلُ الْخَيَّالَةِ وَدَفْعُهُمْ نَحْوَ الْهَاوِيَةِ.",
    "tacticEn": "Revolutionary Karadis system — isolating cavalry, driving into the ravine.",
    "figuresAr": "خَالِدُ بْنُ الْوَلِيدِ، أَبُو عُبَيْدَةَ بْنُ الْجَرَّاحِ، عِكْرِمَةُ بْنُ أَبِي جَهْلٍ، هِرَقْلُ",
    "figuresEn": "Khalid ibn al-Walid the battle architect, Abu Ubayda ibn al-Jarrah, Ikrima ibn Abi Jahl, Emperor Heraclius",
    "resultsAr": "انْهِيَارٌ كَامِلٌ لِلْبِيزَنْطِيِّينَ — فَتْحُ الشَّامِ بِأَسْرِهِ.",
    "resultsEn": "Total Byzantine collapse — Syria opened for Islamic civilization.",
    "lessonsAr": ["التَّشْكِيلُ الْمَرِنُ يَتَفَوَّقُ", "الِاسْتِغْلَالُ الْعَسْكَرِيُّ لِلتَّضَارِيسِ", "عَزْلُ فُرُوعِ الْجَيْشِ", "الضَّرَبَةُ الْمُحْكَمَةُ تَحْسِمُ"],
    "lessonsEn": ["Flexible formations beat sheer mass", "Exploit terrain to maximum advantage", "Isolate enemy branches from each other", "A single well-timed blow is decisive"]
  },
  {
    "id": 9, "yearH": "١٥ هـ", "yearM": "636 م", "epoch": "15 AH · 636 CE",
    "nameAr": "مَعْرَكَةُ الْقَادِسِيَّةِ", "nameEn": "the Battle of al-Qadisiyyah",
    "narratorAr": "أَرْبَعَةُ أَيَّامٍ مِنَ الْقِتَالِ الضَّارِي غَيَّرَتِ التَّارِيخَ حَيْثُ تَحَوَّلَتْ فِيلَةُ الْفُرْسِ إِلَى نَقْمَةٍ عَلَيْهِمْ.",
    "narratorEn": "Four days of combat — Sasanian elephants were blinded and turned against their own legions.",
    "causesAr": "فَتْحُ الْعِرَاقِ وَهَدْمُ الدَّوْلَةِ السَّاسَانِيَّةِ.",
    "causesEn": "Opening Iraq and dismantling the Sasanian empire.",
    "tacticAr": "تَحْيِيدُ الْفِيلَةِ بِقَطْعِ حِبَالِهَا وَفَقْءِ عُيُونِهَا.",
    "tacticEn": "Neutralizing war elephants by cutting harnesses and blinding them.",
    "figuresAr": "سَعْدُ بْنُ أَبِي وَقَّاصٍ، الْقَعْقَاعُ بْنُ عَمْرٍو، رُسْتُمُ قُتِلَ، طُلَيْحَةُ الْأَسَدِيُّ",
    "figuresEn": "Saad ibn Abi Waqqas the commander, Al-Qaqaa ibn Amr, Rustam the Persian commander who was killed, Tulayha al-Asadi",
    "resultsAr": "مَقْتَلُ رُسْتُمَ — فَتْحُ الْمَدَائِنِ.",
    "resultsEn": "Rustam killed on the battlefield — the Persian capital Ctesiphon fell and the Sasanian empire began its final collapse after four brutal days of fighting.",
    "lessonsAr": ["تَحْيِيدُ الْقُوَّةِ الضَّارِبَةِ", "مَقْتَلُ الْقَائِدِ يُنْهِي الْمَعْرَكَةَ", "الإِبْدَاعُ يَتَفَوَّقُ", "أَيَّامٌ قَلِيلَةٌ تُقَرِّرُ قُرُونًا"],
    "lessonsEn": ["Neutralize the strike force with simple tools", "Killing the commander collapses the army", "Creativity beats tradition", "A few days determine centuries of rule"]
  },
  {
    "id": 10, "yearH": "٢١ هـ", "yearM": "642 م", "epoch": "21 AH · 642 CE",
    "nameAr": "مَعْرَكَةُ نَهَاوَنْدَ", "nameEn": "the Conquest of Conquests: Nahavand",
    "narratorAr": "أُخْرِجَ الْفُرْسُ مِنْ قِلَاعِهِمْ بِخُدْعَةِ الاِنْسِحَابِ فَكَانَتْ نَهَاوَنْدُ فَتْحَ الْفُتُوحِ.",
    "narratorEn": "Persian forces lured from fortresses — Nahavand became the Conquest of Conquests.",
    "causesAr": "الْحَشْدُ الْفَارِسِيُّ الْأَخِيرُ لِإِنْهَاءِ الْوُجُودِ الإِسْلَامِيِّ.",
    "causesEn": "The final Persian mobilization to eradicate Islamic presence.",
    "tacticAr": "شَائِعَةُ وَفَاةِ الْخَلِيفَةِ وَانْسِحَابٌ وَهْمِيٌّ ثُمَّ تَطْوِيقٌ كَامِلٌ.",
    "tacticEn": "Spreading rumors and feigning retreat then complete encirclement.",
    "figuresAr": "النُّعْمَانُ بْنُ مُقَرِّنٍ شَهِيدٌ، الْقَعْقَاعُ بْنُ عَمْرٍو، حُذَيْفَةُ بْنُ الْيَمَانِ",
    "figuresEn": "Al-Numan ibn Muqarrin who was martyred in battle, Al-Qaqaa ibn Amr, Hudhayfah ibn al-Yaman",
    "resultsAr": "نِهَايَةُ الدَّوْلَةِ السَّاسَانِيَّةِ إِلَى الْأَبَدِ.",
    "resultsEn": "Permanent end of the four hundred year Sasanian Persian empire — all of Iran and Mesopotamia opened to Islamic civilization. Truly the Conquest of Conquests.",
    "lessonsAr": ["الْقِلَاعُ تُهْزَمُ بِالِاسْتِدْرَاجِ", "الشَّائِعَةُ سِلَاحٌ حَرْبِيٌّ", "التَّضْحِيَةُ تُحَقِّقُ النَّصْرَ", "الِانْتِصَارُ الْحَاسِمُ يُنْهِي قُرُونًا"],
    "lessonsEn": ["Fortresses fall to baiting, not storming", "A directed rumour is a weapon of war", "Self-sacrifice achieves victory", "A decisive win ends centuries of conflict"]
  },
  {
    "id": 11, "yearH": "١١٤ هـ", "yearM": "732 م", "epoch": "114 AH · 732 CE",
    "nameAr": "مَعْرَكَةُ بَلَاطِ الشُّهَدَاءِ", "nameEn": "the Battle of Tours or Poitiers",
    "narratorAr": "عَلَى أَرْضِ فِرَنْسَا اسْتُشْهِدَ الْغَافِقِيُّ لِتَقِفَ عِنْدَ هَذَا الْبَلَاطِ حُدُودُ التَّمَدُّدِ الْأُمَوِيِّ.",
    "narratorEn": "On French soil, Al-Ghafiqi was martyred — Umayyad expansion halted.",
    "causesAr": "التَّمَدُّدُ الإِسْلَامِيُّ فِي أُورُوبَّا الْغَرْبِيَّةِ مُوَاجِهًا صُمُودَ الْفِرِنْجَةِ.",
    "causesEn": "Islamic expansion meeting Frankish resistance led by Charles Martel.",
    "tacticAr": "الدِّفَاعُ الْمُرَبَّعُ الصَّامِدُ فِي ظُرُوفِ إِجْهَادٍ لُوجِسْتِيٍّ.",
    "tacticEn": "Square defense amid severe logistical overextension.",
    "figuresAr": "عَبْدُ الرَّحْمَنِ الْغَافِقِيُّ شَهِيدٌ، شَارْلُ مَارْتِيلَ",
    "figuresEn": "Abd al-Rahman al-Ghafiqi who was martyred, Charles Martel the Frankish commander",
    "resultsAr": "اسْتِشْهَادُ الْغَافِقِيِّ — وَقْفُ التَّمَدُّدِ.",
    "resultsEn": "Al-Ghafiqi and his finest warriors martyred — Islamic expansion into Western Europe permanently halted at the Battle of Tours, reshaping the future of European civilization.",
    "lessonsAr": ["خَطَرُ إِثْقَالِ الإِمْدَادِ", "الْبُعْدُ يُضْعِفُ الْقُوَّةَ", "مَعْرَكَةٌ تُغَيِّرُ التَّارِيخَ", "حِمَايَةُ الْعُمْقِ الْخَلْفِيِّ"],
    "lessonsEn": ["Overextended supply lines are fatal", "Distance from the centre weakens power", "One battle can reshape European history", "Protecting the strategic rear is essential"]
  },
  {
    "id": 12, "yearH": "٤٦٣ هـ", "yearM": "1071 م", "epoch": "463 AH · 1071 CE",
    "nameAr": "مَعْرَكَةُ مَلَاذْكِرْدَ", "nameEn": "the Battle of Manzikert",
    "narratorAr": "بِثِيَابِ كَفَنِهِ قَادَ أَلْبُ أَرْسَلَانُ كَمِينَ الاِنْسِحَابِ لِيَفْتَحَ أَبْوَابَ الْأَنَاضُولِ.",
    "narratorEn": "Dressed in his burial shroud as a sign of devotion, Alp Arslan led the brilliant crescent ambush — opening the gates of Anatolia to Muslims forever and shattering Byzantine power in Asia Minor.",
    "causesAr": "رُومَانُوسُ يَسْعَى لِسَحْقِ الْقُوَّةِ السَّلْجُوقِيَّةِ.",
    "causesEn": "Romanos the fourth sought to crush the rising Seljuk power.",
    "tacticAr": "الْكَمِينُ الْهِلَالِيُّ: تَرَاجُعٌ وَهْمِيٌّ ثُمَّ إِطْبَاقُ الْأَجْنِحَةِ.",
    "tacticEn": "Crescent ambush: feigned retreat, then hidden flanks close.",
    "figuresAr": "أَلْبُ أَرْسَلَانَ بِثِيَابِ الْكَفَنِ، رُومَانُوسُ أُسِرَ",
    "figuresEn": "Sultan Alp Arslan who wore his burial shroud, Emperor Romanos the fourth who was captured",
    "resultsAr": "أَسْرُ الإِمْبَرَاطُورِ — فَتْحُ الْأَنَاضُولِ.",
    "resultsEn": "Emperor captured — Anatolia opened to Turkish civilization.",
    "lessonsAr": ["التَّرَاجُعُ يَقْلِبُ الْمَوَازِينَ", "أَسْرُ الرَّأْسِ يُنْهِي الْحَرْبَ", "الِاسْتِطْلَاعُ الضَّعِيفُ مُهْلِكٌ", "الشَّجَاعَةُ تُلْهِمُ"],
    "lessonsEn": ["A feigned retreat turns the balance", "Capturing the enemy leader ends the war", "Poor reconnaissance destroys an army", "Courage and symbolism inspire troops"]
  },
  {
    "id": 13, "yearH": "٥٨٣ هـ", "yearM": "1187 م", "epoch": "583 AH · 1187 CE",
    "nameAr": "مَعْرَكَةُ حِطِّينَ", "nameEn": "the Battle of Hattin",
    "narratorAr": "أَحَاطَتِ النِّيرَانُ بِفُرْسَانِ الصَّلِيبِ الْمُنْهَكِينَ مِنَ الْعَطَشِ فَفُتِحَ الطَّرِيقُ لِلْقُدْسِ.",
    "narratorEn": "Surrounded by flames and thirst, the Crusader cavalry crumbled.",
    "causesAr": "نَقْضُ الصَّلِيبِيِّينَ الْعُهُودَ وَاعْتِدَاءُ أَرْنَاطَ عَلَى الْقَوَافِلِ.",
    "causesEn": "Crusader treaty violations and Reynald of Chatillon's attack on Muslim caravans forced Saladin to respond decisively.",
    "tacticAr": "التَّعْطِيشُ اللُّوجِسْتِيُّ: عَزْلُ الصَّلِيبِيِّينَ عَنِ الْمَاءِ.",
    "tacticEn": "Strategic dehydration: cutting off water supply.",
    "figuresAr": "صَلَاحُ الدِّينِ الْأَيُّوبِيُّ، لُوزِينْيَانُ أُسِرَ، أَرْنَاطُ قُتِلَ",
    "figuresEn": "Saladin al-Ayyubi, King Lusignan who was captured, Reynald of Chatillon who was executed",
    "resultsAr": "أَسْرُ الْمَلِكِ — اسْتِرْدَادُ الْقُدْسِ بَعْدَ ثَمَانِيَةٍ وَثَمَانِينَ عَامًا.",
    "resultsEn": "King captured — Jerusalem liberated after 88 years.",
    "lessonsAr": ["الطَّبِيعَةُ أَسْلِحَةٌ", "حِرْمَانُ الْعَدُوِّ مِنَ الْمَاءِ", "الصَّبْرُ الاِسْتِرَاتِيجِيُّ", "نَقْضُ الْعُهُودِ لَهُ ثَمَنٌ"],
    "lessonsEn": ["Nature and geography are weapons", "Depriving the enemy of water breaks them", "Strategic patience creates the decisive moment", "Breaking treaties has an inevitable price"]
  },
  {
    "id": 14, "yearH": "٦٥٨ هـ", "yearM": "1260 م", "epoch": "658 AH · 1260 CE",
    "nameAr": "مَعْرَكَةُ عَيْنِ جَالُوتَ", "nameEn": "the Battle of Ain Jalut",
    "narratorAr": "صَرَخَ قُطُزُ وَاإِسْلَامَاهْ وَأَلْقَى بِخُوذَتِهِ فَزَلْزَلَتْ أَرْكَانَ الْمَغُولِ.",
    "narratorEn": "Qutuz cast his helmet and cried O Islam and his battle cry infused iron will into his troops, shattered the Mongol forces, and shielded world civilization from total destruction in a single decisive hour.",
    "causesAr": "زَحْفُ الْمَغُولِ الْمُدَمِّرُ بَعْدَ سُقُوطِ بَغْدَادَ.",
    "causesEn": "Mongol devastation following the fall of Baghdad.",
    "tacticAr": "بَيْبَرْسُ يَتَرَاجَعُ وَهْمًا وَقُطُزُ يُطْبِقُ الْكَمَّاشَةَ.",
    "tacticEn": "Baybars feigned retreat, Qutuz closed the iron pincers.",
    "figuresAr": "سَيْفُ الدِّينِ قُطُزَ، رُكْنُ الدِّينِ بَيْبَرْسُ، كَتْبُغَا قُتِلَ",
    "figuresEn": "Sayf al-Din Qutuz, Rukn al-Din Baybars, Kitbuqa the Mongol commander who was killed",
    "resultsAr": "أَوَّلُ هَزِيمَةٍ حَاسِمَةٍ لِلْمَغُولِ.",
    "resultsEn": "First decisive Mongol defeat in recorded history — their westward advance halted permanently, saving Egypt, North Africa and Islamic civilization from total destruction.",
    "lessonsAr": ["كَسْرُ أُسْطُورَةِ الِاتِّقَاءِ", "الصَّرْخَةُ تُضَاعِفُ الطَّاقَةَ", "الِاسْتِدْرَاجُ يَنْقَلِبُ الْمَوْقِفَ", "مَعْرَكَةٌ تُنْقِذُ حَضَارَةً"],
    "lessonsEn": ["Shattering the myth of invincibility", "An inspiring battle cry multiplies energy", "Baiting reverses the battlefield situation", "One battle can save an entire civilization"]
  },
  {
    "id": 15, "yearH": "٨٥٧ هـ", "yearM": "1453 م", "epoch": "857 AH · 1453 CE",
    "nameAr": "فَتْحُ الْقُسْطَنْطِينِيَّةِ", "nameEn": "the Conquest of Constantinople",
    "narratorAr": "عَبَرَتِ السُّفُنُ الصُّخُورَ فِي جَوْفِ اللَّيْلِ لِتَسْتَيْقِظَ الْقُسْطَنْطِينِيَّةُ عَلَى تَكْبِيرَاتِ الْفَاتِحِ.",
    "narratorEn": "Ships traversed rocks at night — Constantinople awoke to the Takbir of Fatih.",
    "causesAr": "تَحْقِيقُ النُّبُوءَةِ النَّبَوِيَّةِ وَإِنْهَاءُ الإِمْبَرَاطُورِيَّةِ الْبِيزَنْطِيَّةِ.",
    "causesEn": "Fulfillment of prophecy and ending the Byzantine Empire.",
    "tacticAr": "مَدَافِعُ ضَخْمَةٌ وَنَقْلُ ٧٠ سَفِينَةً بَرًّا فَوْقَ التِّلَالِ.",
    "tacticEn": "Massive cannons and transporting 70 warships overland.",
    "figuresAr": "مُحَمَّدٌ الْفَاتِحُ ٢١ عَامًا، قُسْطَنْطِينُ الْحَادِي عَشَرَ قُتِلَ، أُرْبَانُ",
    "figuresEn": "Sultan Muhammad al-Fatih at age 21, Emperor Constantine the eleventh who was killed, Urban the Hungarian cannon maker",
    "resultsAr": "نِهَايَةُ الإِمْبَرَاطُورِيَّةِ الْبِيزَنْطِيَّةِ.",
    "resultsEn": "End of the one thousand year Byzantine Roman Empire — Constantinople became the Ottoman capital Istanbul. The Prophetic prophecy fulfilled after 800 years.",
    "lessonsAr": ["الِابْتِكَارُ يَكْسِرُ الْحُصُونَ", "التَّخْطِيطُ الْعَبْقَرِيُّ يَتَجَاوَزُ", "الإِيمَانُ يَزِيدُ الْعَزِيمَةَ", "الشَّبَابُ يُحَقِّقُ الْمُسْتَحِيلَ"],
    "lessonsEn": ["Innovation breaks the strongest fortresses", "Brilliant planning overcomes every obstacle", "Belief in prophecy multiplies resolve", "Youth and confidence achieve the impossible"]
  }
]


def make_text_ar(b):
  txt = f"مَعْرَكَةُ {b['nameAr']}، فِي عَامِ {b['yearH']}، الْمُوَافِقِ {b['yearM']}. "
  txt += f"{b['narratorAr']} "
  txt += "الْأَسْبَابُ: "
  txt += f"{b['causesAr']} "
  txt += "التَّكْتِيكُ الْعَسْكَرِيُّ: "
  txt += f"{b['tacticAr']} "
  txt += "أَبْرَزُ الشَّخْصِيَّاتِ: "
  txt += f"{b['figuresAr']}. "
  txt += "النَّتَائِجُ: "
  txt += f"{b['resultsAr']} "
  txt += "الدُّرُوسُ وَالْعِبَرُ: "
  txt += " ".join([f"{l}." for l in b['lessonsAr']])
  return txt


def make_text_en(b):
  txt = f"The Battle of {b['nameEn']}, in the year {b['epoch']}. "
  txt += f"{b['narratorEn']} "
  txt += "Causes: "
  txt += f"{b['causesEn']} "
  txt += "Military Tactics: "
  txt += f"{b['tacticEn']} "
  txt += "Key Figures: "
  txt += f"{b['figuresEn']} "
  txt += "Outcomes: "
  txt += f"{b['resultsEn']} "
  txt += "Lessons Learned: "
  txt += " ".join([f"{l}." for l in b['lessonsEn']])
  return txt


async def generate(slot, lang, voice, filename, text):
  directory = f"audio/{slot}/{lang}"
  os.makedirs(directory, exist_ok=True)
  filepath = f"{directory}/{filename}"
  communicate = edge_tts.Communicate(text, voice)
  await communicate.save(filepath)
  print(f"  ✓ {filepath}")


async def main():
  print("Generated audio files will be placed in audio/story/...\n")
  for b in BATTLES:
    bid = b["id"]
    print(f"Battle {bid}/{len(BATTLES)}: {b['nameAr']}")

    text_ar = make_text_ar(b)
    text_en = make_text_en(b)

    await generate(SLOT, "ar", VOICES["ar"], f"battle_{bid}.mp3", text_ar)
    await generate(SLOT, "en", VOICES["en"], f"battle_{bid}.mp3", text_en)
    print()

  # Generate intro files
  print("Intro narration...")
  intro_ar = [
    "بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيمِ.",
    "مَرْحَبًا بِكُمْ فِي أَطْلَسِ الْمَعَارِكِ الإِسْلَامِيَّةِ الْكُبْرَى.",
    "إِنَّ دِرَاسَةَ هَذِهِ الْمَعَارِكِ لَيْسَتْ مُجَرَّدَ تَارِيخٍ يُحْفَظُ، بَلْ هِيَ مَدْرَسَةٌ فِي الْقِيَادَةِ وَالْحِكْمَةِ وَالِاسْتِرَاتِيجِيَّةِ.",
    "مِنْ آبَارِ بَدْرٍ إِلَى أَسْوَارِ الْقُسْطَنْطِينِيَّةِ، صَاغَ الْمُسْلِمُونَ مَسَارَ الْحَضَارَةِ الإِنْسَانِيَّةِ عَبْرَ خَمْسَةَ عَشَرَ مَعْرَكَةً فَارِقَةً.",
    "فَلْنَبْدَأْ هَذِهِ الرِّحْلَةَ مَعًا."
  ]
  intro_en = [
    "In the name of God, the Most Gracious, the Most Merciful.",
    "Welcome to the Great Islamic Battles Atlas.",
    "Studying these battles is not mere history — it is a school of leadership, wisdom, and strategy.",
    "From the wells of Badr to the walls of Constantinople, Muslims shaped the course of human civilization through fifteen decisive battles.",
    "Let us begin this journey together."
  ]

  os.makedirs(f"audio/{SLOT}/ar", exist_ok=True)
  os.makedirs(f"audio/{SLOT}/en", exist_ok=True)

  # Combine intro into full text for each language
  full_intro_ar = " ".join(intro_ar)
  full_intro_en = " ".join(intro_en)

  await generate(SLOT, "ar", VOICES["ar"], f"intro_full.mp3", full_intro_ar)
  await generate(SLOT, "en", VOICES["en"], f"intro_full.mp3", full_intro_en)

  for i, (sent_ar, sent_en) in enumerate(zip(intro_ar, intro_en)):
    await generate(SLOT, "ar", VOICES["ar"], f"intro_{i}.mp3", sent_ar)
    await generate(SLOT, "en", VOICES["en"], f"intro_{i}.mp3", sent_en)

  print("\nAll done!")


if __name__ == "__main__":
  asyncio.run(main())
