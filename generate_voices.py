"""
generate_voices.py
==================
يولّد ملفات MP3 بـ 5 أصوات عربية وإنجليزية مختلفة من Microsoft Edge Neural TTS
لكل نص في أطلس المعارك الإسلامية الكبرى

التشغيل:
    pip install edge-tts
    python generate_voices.py

الوقت المتوقع: 5-10 دقائق
"""

import asyncio, json, os, re
from pathlib import Path

# ── الأصوات المختارة (نفس مشروع السيرة) ─────────────────────
VOICES = {
    "classic": {"ar": "ar-SA-HamedNeural",   "en": "en-US-GuyNeural"},
    "gentle":  {"ar": "ar-SA-ZariyahNeural",  "en": "en-US-AriaNeural"},
    "story":   {"ar": "ar-EG-SalmaNeural",    "en": "en-US-JennyNeural"},
    "warm":    {"ar": "ar-SA-HamedNeural",    "en": "en-US-RyanNeural"},   # reuse + diff rate
    "shakir":  {"ar": "ar-EG-ShakirNeural",   "en": "en-US-BrianNeural"},
}

RATES = {
    "classic": "-8%",
    "gentle":  "-14%",
    "story":   "-4%",
    "warm":    "-10%",
    "shakir":  "+2%",
}

# ── النصوص التى سيتم تحويلها ─────────────────────────────────
# مقدمة الموسوعة
INTRO_AR = [
    "بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيمِ.",
    "مَرْحَبًا بِكُمْ فِي أَطْلَسِ الْمَعَارِكِ الإِسْلَامِيَّةِ الْكُبْرَى.",
    "إِنَّ دِرَاسَةَ هَذِهِ الْمَعَارِكِ لَيْسَتْ مُجَرَّدَ تَارِيخٍ يُحْفَظُ، بَلْ هِيَ مَدْرَسَةٌ فِي الْقِيَادَةِ وَالْحِكْمَةِ وَالِاسْتِرَاتِيجِيَّةِ.",
    "مِنْ آبَارِ بَدْرٍ إِلَى أَسْوَارِ الْقُسْطَنْطِينِيَّةِ، صَاغَ الْمُسْلِمُونَ مَسَارَ الْحَضَارَةِ الإِنْسَانِيَّةِ عَبْرَ خَمْسَةَ عَشَرَ مَعْرَكَةً فَارِقَةً.",
    "فَلْنَبْدَأْ هَذِهِ الرِّحْلَةَ مَعًا.",
]

INTRO_EN = [
    "In the name of God, the Most Gracious, the Most Merciful.",
    "Welcome to the Great Islamic Battles Atlas.",
    "Studying these battles is not mere history — it is a school of leadership, wisdom, and strategy.",
    "From the wells of Badr to the walls of Constantinople, Muslims shaped the course of human civilization through fifteen decisive battles.",
    "Let us begin this journey together.",
]

# بيانات المعارك (مستخرجة من atlas_v5.html)
BATTLES = [
    {"id": 1, "nameAr": "غَزْوَةُ بَدْرٍ الْكُبْرَى", "yearH": "٢ هجرية", "yearM": "624 ميلادية",
     "narratorAr": "وَقَفَ الْمُسْلِمُونَ صَفًّا وَاحِدًا كَالْبُنْيَانِ الْمَرْصُوصِ أَمَامَ جَيْشٍ يَفُوقُهُمْ ثَلَاثَةَ أَضْعَافٍ، لَكِنَّ التَّخْطِيطَ الْجُغْرَافِيَّ الْمُحْكَمَ وَالسَّيْطَرَةَ عَلَى الْمَاءِ صَنَعَا النَّصْرَ الْأَوَّلَ لِلإِسْلَامِ.",
     "narratorEn": "Muslims stood unified against a force three times their size. Masterful geographic planning and water control secured Islam's first great victory at the wells of Badr."},
    {"id": 2, "nameAr": "غَزْوَةُ أُحُدٍ", "yearH": "٣ هجرية", "yearM": "625 ميلادية",
     "narratorAr": "صَعِدَ الرُّمَاةُ جَبَلَ عَيْنَيْنِ بِأَمْرٍ نَبَوِيٍّ صَارِمٍ أَلَّا يَبْرَحُوا مَكَانَهُمْ، لَكِنَّ اسْتِعْجَالَ الْغَنِيمَةِ فَتَحَ ثُغْرَةً اسْتِرَاتِيجِيَّةً قَلَبَتْ مَوَازِينَ الْمَعْرَكَةِ فِي لَحَظَاتٍ.",
     "narratorEn": "Archers held position by Prophetic order — until the lure of spoils opened a fatal flank Khalid exploited with devastating precision."},
    {"id": 3, "nameAr": "غَزْوَةُ الْخَنْدَقِ", "yearH": "٥ هجرية", "yearM": "627 ميلادية",
     "narratorAr": "عَشَرَةُ آلَافِ مُقَاتِلٍ جَاءُوا لِاسْتِئْصَالِ الْمُسْلِمِينَ فَوَقَفُوا مَذْهُولِينَ أَمَامَ أُخْدُودٍ عَمِيقٍ لَمْ تَعْرِفْهُ الْعَرَبُ قَطُّ.",
     "narratorEn": "Ten thousand warriors stood frozen before a trench completely alien to Arabian warfare."},
    {"id": 4, "nameAr": "غَزْوَةُ خَيْبَرَ", "yearH": "٧ هجرية", "yearM": "628 ميلادية",
     "narratorAr": "حُمِلَتِ الرَّايَةُ بِأَمْرٍ نَبَوِيٍّ لِرَجُلٍ يُحِبُّ اللهَ وَرَسُولَهُ فَتَهَاوَتْ قِلَاعُ خَيْبَرَ الْمَنِيعَةُ.",
     "narratorEn": "The banner was entrusted to the true lover of Allah — and Khaybar's mighty fortresses fell one by one."},
    {"id": 5, "nameAr": "مَعْرَكَةُ مُؤْتَةَ", "yearH": "٨ هجرية", "yearM": "629 ميلادية",
     "narratorAr": "أَعَادَ خَالِدٌ تَرْتِيبَ الْمَجْنَحَتَيْنِ فِي جَوْفِ اللَّيْلِ فَظَنَّ الرُّومُ أَنَّ مَدَدًا هَائِلًا وَصَلَ فَتَنَحَّوْا خَوْفًا.",
     "narratorEn": "Khalid reshuffled flanks at night — Byzantines believed reinforcements arrived and pulled back."},
    {"id": 6, "nameAr": "غَزْوَةُ حُنَيْنٍ", "yearH": "٨ هجرية", "yearM": "630 ميلادية",
     "narratorAr": "أَنَا النَّبِيُّ لَا كَذِبْ أَنَا ابْنُ عَبْدِ الْمُطَّلِبْ! صَرْخَةٌ نَبَوِيَّةٌ زَلْزَلَتِ الْوَادِيَ فَأَعَادَتْ صُفُوفًا تَمَزَّقَتْ.",
     "narratorEn": "I am the Prophet — no lie — son of Abd al-Muttalib! A Prophetic war cry rallied shattered lines to decisive victory."},
    {"id": 7, "nameAr": "غَزْوَةُ تَبُوكَ", "yearH": "٩ هجرية", "yearM": "630 ميلادية",
     "narratorAr": "سَارَ جَيْشُ الْعُسْرَةِ فِي هَجِيرِ الصَّيْفِ فَنَصَرَ اللهُ نَبِيَّهُ بِالرُّعْبِ فِي قُلُوبِ الرُّومِ.",
     "narratorEn": "The Army of Hardship marched through punishing deserts — Allah cast terror into Byzantine hearts."},
    {"id": 8, "nameAr": "مَعْرَكَةُ الْيَرْمُوكِ", "yearH": "١٣ هجرية", "yearM": "634 ميلادية",
     "narratorAr": "أَعَادَ خَالِدٌ صِيَاغَةَ الْعُلُومِ الْعَسْكَرِيَّةِ بِتَكْتِيكِ الْكَرَادِيسِ لِيَهْزِمَ إِمْبَرَاطُورِيَّةً لَا تُقْهَرُ.",
     "narratorEn": "Khalid rewrote the science of war with his Karadis system, shattering an empire deemed unconquerable."},
    {"id": 9, "nameAr": "مَعْرَكَةُ الْقَادِسِيَّةِ", "yearH": "١٥ هجرية", "yearM": "636 ميلادية",
     "narratorAr": "أَرْبَعَةُ أَيَّامٍ غَيَّرَتْ التَّارِيخَ حَيْثُ تَحَوَّلَتْ فِيلَةُ الْفُرْسِ إِلَى نَقْمَةٍ عَلَيْهِمْ.",
     "narratorEn": "Four days of combat — Sasanian elephants were blinded and turned against their own legions."},
    {"id": 10, "nameAr": "مَعْرَكَةُ نَهَاوَنْدَ", "yearH": "٢١ هجرية", "yearM": "642 ميلادية",
     "narratorAr": "أُخْرِجَ الْفُرْسُ مِنْ قِلَاعِهِمْ بِخُدْعَةِ الاِنْسِحَابِ فَكَانَتْ نَهَاوَنْدُ فَتْحَ الْفُتُوحِ.",
     "narratorEn": "Persian forces lured from fortresses — Nahavand became the Conquest of Conquests."},
    {"id": 11, "nameAr": "مَعْرَكَةُ بَلَاطِ الشُّهَدَاءِ", "yearH": "١١٤ هجرية", "yearM": "732 ميلادية",
     "narratorAr": "عَلَى أَرْضِ فِرَنْسَا اسْتُشْهِدَ الْغَافِقِيُّ لِتَقِفَ حُدُودُ التَّمَدُّدِ الْأُمَوِيِّ.",
     "narratorEn": "On French soil, Al-Ghafiqi was martyred — Umayyad expansion into Europe came to a permanent halt."},
    {"id": 12, "nameAr": "مَعْرَكَةُ مَلَاذْكِرْدَ", "yearH": "٤٦٣ هجرية", "yearM": "1071 ميلادية",
     "narratorAr": "بِثِيَابِ كَفَنِهِ قَادَ أَلْبُ أَرْسَلَانُ كَمِينَ الاِنْسِحَابِ لِيَفْتَحَ أَبْوَابَ الْأَنَاضُولِ.",
     "narratorEn": "In his burial shroud, Alp Arslan led the ambush — opening Anatolia's gates to Muslims forever."},
    {"id": 13, "nameAr": "مَعْرَكَةُ حِطِّينَ", "yearH": "٥٨٣ هجرية", "yearM": "1187 ميلادية",
     "narratorAr": "أَحَاطَتِ النِّيرَانُ بِفُرْسَانِ الصَّلِيبِ الْمُنْهَكِينَ مِنَ الْعَطَشِ فَفُتِحَ الطَّرِيقُ لِلْقُدْسِ.",
     "narratorEn": "Surrounded by flames and thirst, the Crusader cavalry crumbled — opening the path to liberate Jerusalem."},
    {"id": 14, "nameAr": "مَعْرَكَةُ عَيْنِ جَالُوتَ", "yearH": "٦٥٨ هجرية", "yearM": "1260 ميلادية",
     "narratorAr": "صَرَخَ قُطُزُ وَاإِسْلَامَاهْ وَأَلْقَى بِخُوذَتِهِ فَزَلْزَلَتْ أَرْكَانَ الْمَغُولِ.",
     "narratorEn": "Qutuz cried 'O Islam!' — shattering the Mongol army and shielding world civilization."},
    {"id": 15, "nameAr": "فَتْحُ الْقُسْطَنْطِينِيَّةِ", "yearH": "٨٥٧ هجرية", "yearM": "1453 ميلادية",
     "narratorAr": "عَبَرَتِ السُّفُنُ الصُّخُورَ فِي جَوْفِ اللَّيْلِ لِتَسْتَيْقِظَ الْقُسْطَنْطِينِيَّةُ عَلَى تَكْبِيرَاتِ الْفَاتِحِ.",
     "narratorEn": "Ships traversed rocks at night — Constantinople awoke to the Takbir of Fatih, prophecy fulfilled."},
]

OUTPUT_DIR = Path("audio")
OUTPUT_DIR.mkdir(exist_ok=True)

async def gen(text, voice, rate, outpath):
    """Generate one MP3 file using edge-tts"""
    try:
        import edge_tts
        communicate = edge_tts.Communicate(text, voice, rate=rate)
        await communicate.save(str(outpath))
        size = outpath.stat().st_size if outpath.exists() else 0
        print(f"  ✅ {outpath.name} ({size//1024}KB)")
    except Exception as e:
        print(f"  ❌ {outpath.name}: {e}")

async def main():
    import edge_tts
    print("=== Islamic Battles Atlas — TTS Generator ===")
    print(f"Output: {OUTPUT_DIR.absolute()}")
    print()

    tasks = []

    for slot_id, voices in VOICES.items():
        slot_dir_ar = OUTPUT_DIR / slot_id / "ar"
        slot_dir_en = OUTPUT_DIR / slot_id / "en"
        slot_dir_ar.mkdir(parents=True, exist_ok=True)
        slot_dir_en.mkdir(parents=True, exist_ok=True)
        rate = RATES[slot_id]

        print(f"[{slot_id}] AR: {voices['ar']} | EN: {voices['en']} | rate: {rate}")

        # Intro
        for i, (text_ar, text_en) in enumerate(zip(INTRO_AR, INTRO_EN)):
            tasks.append(gen(text_ar, voices["ar"], rate, slot_dir_ar / f"intro_{i}.mp3"))
            tasks.append(gen(text_en, voices["en"], rate, slot_dir_en / f"intro_{i}.mp3"))

        # Battle narrators
        for b in BATTLES:
            bid = b["id"]
            ar_text = f"مَعْرَكَةُ {b['nameAr']}، فِي عَامِ {b['yearH']}، الْمُوَافِقِ {b['yearM']}. {b['narratorAr']}"
            en_text = f"The Battle of {b['nameAr']}, in the year {b['yearH']}, {b['yearM']}. {b['narratorEn']}"
            tasks.append(gen(ar_text, voices["ar"], rate, slot_dir_ar / f"battle_{bid}.mp3"))
            tasks.append(gen(en_text, voices["en"], rate, slot_dir_en / f"battle_{bid}.mp3"))

    print(f"\nGenerating {len(tasks)} audio files...\n")
    # Run in batches of 5 to avoid rate limiting
    for i in range(0, len(tasks), 5):
        batch = tasks[i:i+5]
        await asyncio.gather(*batch)
        await asyncio.sleep(0.5)

    print("\n=== DONE ===")
    total = sum(1 for f in OUTPUT_DIR.rglob("*.mp3") if f.exists())
    print(f"Generated: {total} files in {OUTPUT_DIR}/")
    print("\nNext step: commit and push the 'audio/' folder to GitHub")
    print("  git add audio/")
    print('  git commit -m "feat: add neural TTS audio files"')
    print("  git push origin main")

if __name__ == "__main__":
    try:
        import edge_tts
    except ImportError:
        print("Installing edge-tts...")
        os.system("pip install edge-tts")
        import edge_tts
    asyncio.run(main())
