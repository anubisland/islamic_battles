const battles = window.BATTLES || [];

const study = {
  1: {
    theme: "السَّيْطَرَةُ عَلَى الْمَاءِ",
    events: "خَرَجَ الْمُسْلِمُونَ لِاعْتِرَاضِ عِيرِ قُرَيْشٍ، ثُمَّ تَحَوَّلَ الْمَوْقِفُ إِلَى مُوَاجَهَةٍ مَفْصِلِيَّةٍ عِنْدَ آبَارِ بَدْرٍ. تَقَدَّمَتِ الْقُوَّاتُ الْإِسْلَامِيَّةُ إِلَى الْمَاءِ وَأَحْكَمَتِ التَّمَوْضُعَ قَبْلَ وُصُولِ الْخَصْمِ.",
    results: "تَحَقَّقَ نَصْرٌ كَبِيرٌ رَفَعَ مَعْنَوِيَّاتِ الْمَدِينَةِ وَكَسَرَ هَيْبَةَ قُرَيْشٍ. أَثْبَتَتِ الْمَعْرَكَةُ أَنَّ الْمَعْرِفَةَ بِالأَرْضِ وَإِدَارَةَ الْمَوَارِدِ قَدْ تَحْسِمَانِ فَارِقَ الْعَدَدِ.",
  },
  2: {
    theme: "حِمَايَةُ الظَّهْرِ",
    events: "جَاءَتْ قُرَيْشٌ لِلثَّأْرِ بَعْدَ بَدْرٍ، فَاخْتَارَ الْمُسْلِمُونَ مَوْضِعًا يَسْتَنِدُ إِلَى جَبَلِ أُحُدٍ، وَوُضِعَ الرُّمَاةُ عَلَى جَبَلِ عَيْنَيْنِ لِسَدِّ الثُّغْرَةِ الْخَلْفِيَّةِ.",
    results: "تَحَوَّلَ النَّصْرُ الأَوَّلُ إِلَى ابْتِلَاءٍ عَسْكَرِيٍّ بَعْدَ تَرْكِ بَعْضِ الرُّمَاةِ مَوَاقِعَهُمْ. بَقِيَ الدَّرْسُ الأَكْبَرُ أَنَّ الانْضِبَاطَ فِي الْمَوْقِعِ لَيْسَ تَفْصِيلًا، بَلْ هُوَ عُنْصُرُ بَقَاءِ الْخُطَّةِ.",
  },
  3: {
    theme: "الْمَانِعُ الْهَنْدَسِيُّ",
    events: "تَجَمَّعَتِ الأَحْزَابُ لِإِسْقَاطِ الْمَدِينَةِ، فَاسْتُخْدِمَتْ فِكْرَةُ الْخَنْدَقِ لِتَحْوِيلِ الْجِهَةِ الْمَكْشُوفَةِ إِلَى حَاجِزٍ يَشُلُّ الْفُرْسَانَ.",
    results: "فَشِلَ الْحِصَارُ وَتَفَكَّكَ التَّحَالُفُ دُونَ مَعْرَكَةٍ مَفْتُوحَةٍ حَاسِمَةٍ. أَظْهَرَتِ الْغَزْوَةُ أَنَّ الْهَنْدَسَةَ الدِّفَاعِيَّةَ قَادِرَةٌ عَلَى تَغْيِيرِ قَوَاعِدِ الْمِيدَانِ.",
  },
  4: {
    theme: "عَزْلُ الْحُصُونِ",
    events: "اتَّجَهَتِ الْقُوَّاتُ إِلَى خَيْبَرَ لِإِنْهَاءِ مَرْكَزٍ حَصِينٍ يُهَدِّدُ أَمْنَ الْمَدِينَةِ. عُمِلَ عَلَى تَفْكِيكِ الْحُصُونِ وَضَرْبِهَا وَاحِدًا بَعْدَ وَاحِدٍ.",
    results: "سَقَطَتِ الْقِلَاعُ وَانْكَسَرَتْ قُدْرَةُ خَيْبَرَ عَلَى التَّحْرِيكِ السِّيَاسِيِّ وَالْعَسْكَرِيِّ. بَرَزَ دَرْسُ الْعَزْلِ وَمَنْعِ الْخَصْمِ مِنْ تَحْوِيلِ مَوَاقِعِهِ الْمُتَعَدِّدَةِ إِلَى قُوَّةٍ وَاحِدَةٍ.",
  },
  5: {
    theme: "الانْسِحَابُ الْمُنَظَّمُ",
    events: "خَرَجَ الْجَيْشُ بَعْدَ مَقْتَلِ رَسُولِ النَّبِيِّ، وَوَاجَهَ قُوَّةً أَكْبَرَ عَدَدًا. تَعَاقَبَ الْقَادَةُ، ثُمَّ أَعَادَ خَالِدٌ تَرْتِيبَ الصُّفُوفِ لِإِيهَامِ الْعَدُوِّ بِوُصُولِ إِمْدَادٍ.",
    results: "نَجَحَ الْجَيْشُ فِي الْخُرُوجِ مِنْ مَوْقِفٍ غَيْرِ مُتَكَافِئٍ دُونَ تَحَطُّمِ قُوَّتِهِ. يُعَدُّ حِفْظُ الْقُوَّةِ وَالانْسِحَابُ الْمُنَظَّمُ قَرَارًا اسْتِرَاتِيجِيًّا عِنْدَ اخْتِلَالِ الْمِيزَانِ.",
  },
  6: {
    theme: "امْتِصَاصُ الْكَمِينِ",
    events: "بَعْدَ فَتْحِ مَكَّةَ تَجَمَّعَتْ هَوَازِنُ وَثَقِيفٌ فِي مَضَايِقِ حُنَيْنٍ. فَاجَأَ الْكَمِينُ الْجَبَلِيُّ مُقَدِّمَةَ الْجَيْشِ، ثُمَّ أُعِيدَ التَّجَمُّعُ بِثَبَاتِ الْقِيَادَةِ.",
    results: "انْقَلَبَ الاضْطِرَابُ الأَوَّلُ إِلَى نَصْرٍ بَعْدَ اسْتِعَادَةِ السَّيْطَرَةِ. الدَّرْسُ الْمَرْكَزِيُّ أَنَّ الْكَثْرَةَ لا تُغْنِي عَنْ الْجَاهِزِيَّةِ وَالانْضِبَاطِ تَحْتَ الصَّدْمَةِ.",
  },
  7: {
    theme: "الرَّدْعُ طَوِيلُ الْمَدَى",
    events: "بَلَغَتِ الأَنْبَاءُ بِحُشُودِ الرُّومِ فِي الشَّمَالِ، فَخَرَجَ جَيْشُ الْعُسْرَةِ فِي ظَرْفٍ قَاسٍ لِنَقْلِ الْمُبَادَرَةِ إِلَى مَسْرَحِ الْخَصْمِ.",
    results: "تَحَقَّقَ رَدْعٌ سِيَاسِيٌّ وَعَسْكَرِيٌّ دُونَ قِتَالٍ مُبَاشِرٍ كَبِيرٍ. أَثْبَتَتْ تَبُوكُ أَنَّ الْحُضُورَ الْقَوِيَّ فِي الْوَقْتِ الصَّعْبِ قَدْ يَكْفِي لِمَنْعِ الْحَرْبِ.",
  },
  8: {
    theme: "الْكَرَادِيسُ وَالْمُنْحَدَرَاتُ",
    events: "سَعَى الرُّومُ إِلَى إِنْهَاءِ الْوُجُودِ الإِسْلَامِيِّ فِي الشَّامِ، فَتَمَّ تَوْحِيدُ الْقُوَّاتِ وَتَنْظِيمُهَا فِي كَرَادِيسَ مُتَحَرِّكَةٍ عِنْدَ الْيَرْمُوكِ.",
    results: "انْهَارَتِ الْقُوَّةُ الْبِيزَنْطِيَّةُ فِي الشَّامِ، وَفُتِحَ الطَّرِيقُ لِتَثْبِيتِ الْفُتُوحِ. جَمَعَ الدَّرْسُ بَيْنَ الْمُنَاوَرَةِ وَاسْتِغْلَالِ التَّضَارِيسِ وَضَبْطِ الْقِيَادَةِ الْمُوَحَّدَةِ.",
  },
  9: {
    theme: "تَحْيِيدُ الْفِيلَةِ",
    events: "اصْطَدَمَ الْمُسْلِمُونَ بِقُوَّةِ الْفُرْسِ عِنْدَ الْقَادِسِيَّةِ، وَكَانَ لِلْفِيلَةِ أَثَرٌ نَفْسِيٌّ وَمِيدَانِيٌّ عَلَى الْخَيْلِ. تَمَّ تَوْجِيهُ الضَّرْبِ إِلَى مَصَادِرِ الرُّعْبِ وَمَرَاكِزِ السَّيْطَرَةِ.",
    results: "انْكَسَرَتْ قُوَّةُ الْفُرْسِ وَتَقَدَّمَتِ الْفُتُوحُ نَحْوَ الْمَدَائِنِ. أَظْهَرَتِ الْمَعْرَكَةُ أَهَمِّيَّةَ تَحْيِيدِ سِلَاحِ الصَّدْمَةِ قَبْلَ مُوَاجَهَةِ الْجِسْمِ الرَّئِيسِيِّ.",
  },
  10: {
    theme: "الاسْتِدْرَاجُ",
    events: "تَجَمَّعَتْ قُوَّاتُ الْفُرْسِ فِي نَهَاوَنْدَ لِمُحَاوَلَةِ وَقْفِ الْمَدِّ الإِسْلَامِيِّ. اسْتُخْدِمَتْ خُطَّةُ الاسْتِدْرَاجِ لإِخْرَاجِ الْخَصْمِ مِنْ مَوَاضِعِهِ.",
    results: "سُمِّيَتْ فَتْحَ الْفُتُوحِ لِمَا تَرَتَّبَ عَلَيْهَا مِنْ انْهِيَارٍ وَاسِعٍ فِي قُدْرَةِ الدَّوْلَةِ السَّاسَانِيَّةِ. الدَّرْسُ أَنَّ الْخَصْمَ الْمُتَحَصِّنَ يُهْزَمُ أَوَّلًا بِإِخْرَاجِهِ مِنْ مَنْطِقَةِ قُوَّتِهِ.",
  },
  11: {
    theme: "الدِّفَاعُ الْمُرْهَقُ",
    events: "تَقَدَّمَتِ الْقُوَّاتُ الإِسْلَامِيَّةُ فِي جَنُوبِ فَرَنْسَا، فَاصْطَدَمَتْ بِقُوَّةِ الْفِرَنْجِ. طَالَ التَّمَوْضُعُ وَحُرِمَتِ الْقُوَّاتُ مِنْ سُرْعَةِ الْحَرَكَةِ الَّتِي تُمَيِّزُهَا.",
    results: "تَوَقَّفَ التَّمَدُّدُ شَمَالًا، وَبَقِيَتِ الْمَعْرَكَةُ دَرْسًا فِي حُدُودِ الإِمْدَادِ وَبُعْدِ الْمَسَافَةِ عَنْ مَرَاكِزِ الدَّعْمِ. لا تَكْفِي الشَّجَاعَةُ إِنْ ضَعُفَ خَطُّ الْمُؤَنِ وَتَعَذَّرَتِ الْمُنَاوَرَةُ.",
  },
  12: {
    theme: "كَمِينُ الْهِلَالِ",
    events: "تَقَدَّمَتِ الْقُوَّةُ الْبِيزَنْطِيَّةُ لِاسْتِعَادَةِ الْمُبَادَرَةِ فِي الأَنَاضُولِ، فَاسْتَخْدَمَ السَّلَاجِقَةُ حَرَكَةَ تَظَاهُرٍ بِالتَّرَاجُعِ ثُمَّ الْتِفَافًا عَلَى الأَطْرَافِ.",
    results: "أُسِرَ الإِمْبِرَاطُورُ وَتَغَيَّرَ مِيزَانُ الْقُوَّةِ فِي الأَنَاضُولِ. أَكَّدتْ مَلَاذْكِرْدُ أَنَّ السُّرْعَةَ وَالْمَرُونَةَ قَدْ تَغْلِبَانِ الْكَتْلَةَ الثَّقِيلَةَ.",
  },
  13: {
    theme: "التَّعْطِيشُ وَالْحِصَارُ",
    events: "تَحَرَّكََ الصَّلِيبِيُّونَ نَحْوَ طَبَرِيَّةَ فِي قَيْظٍ شَدِيدٍ، فَأَحْكَمَ صَلَاحُ الدِّينِ ضَغْطَهُ عَلَى الْمَاءِ وَالطُّرُقِ حَتَّى وَصَلُوا مُنْهَكِينَ إِلَى حِطِّينَ.",
    results: "انْهَارَ الْجَيْشُ الصَّلِيبِيُّ وَفُتِحَ الطَّرِيقُ إِلَى الْقُدْسِ. جَسَّدَتْ حِطِّينُ قِيمَةَ السَّيْطَرَةِ عَلَى الْمَوَارِدِ وَإِجْبَارِ الْخَصْمِ عَلَى الْقِتَالِ فِي وَقْتٍ وَمَكَانٍ غَيْرِ مُنَاسِبَيْنِ.",
  },
  14: {
    theme: "كَمَّاشَةُ الْكَمِينِ",
    events: "دَخَلَ التَّتَارُ الشَّامَ بَعْدَ انْهِيَارِ مَرَاكِزَ كَبِيرَةٍ، فَاخْتَارَ الْمَمَالِيكُ عَيْنَ جَالُوتَ لِاسْتِدْرَاجِ الطَّلِيعَةِ ثُمَّ إِطْبَاقِ الْكَمِينِ.",
    results: "تَوَقَّفَ الزَّحْفُ الْمَغُولِيُّ وَاسْتَعَادَتِ الْمِنْطَقَةُ تَوَازُنَهَا. الدَّرْسُ أَنَّ الرُّعْبَ الاسْتِرَاتِيجِيَّ يُكْسَرُ بِقَرَارٍ قِيَادِيٍّ وَمَوْضِعٍ مُحْكَمٍ وَتَوْقِيتٍ دَقِيقٍ.",
  },
  15: {
    theme: "الْحِصَارُ وَالنَّارُ وَالْبَحْرُ",
    events: "حُوصِرَتِ الْقُسْطَنْطِينِيَّةُ بِخُطَّةٍ جَمَعَتِ الْمَدَافِعَ الضَّخْمَةَ وَالسَّيْطَرَةَ الْبَحْرِيَّةَ وَنَقْلَ السُّفُنِ إِلَى الْقَرْنِ الذَّهَبِيِّ.",
    results: "فُتِحَتِ الْمَدِينَةُ وَانْتَقَلَ مَرْكَزٌ حَضَارِيٌّ كَبِيرٌ إِلَى عَهْدٍ جَدِيدٍ. الدَّرْسُ أَنَّ الْحِصَارَ النَّاجِحَ يَحْتَاجُ إِلَى ابْتِكَارٍ لُوجِسْتِيٍّ يَكْسِرُ مَا يَعْتَقِدُهُ الْخَصْمُ مُسْتَحِيلًا.",
  },
};

const mapPlans = {
  1: { terrain: "آبَارُ بَدْرٍ", north: "قُرَيْش", south: "الْمُسْلِمُون", feature: "water" },
  2: { terrain: "جَبَلُ أُحُدٍ وَجَبَلُ الرُّمَاة", north: "قُرَيْش", south: "الْمُسْلِمُون", feature: "ridge" },
  3: { terrain: "خَنْدَقُ الْمَدِينَة", north: "الأَحْزَاب", south: "الْمَدِينَة", feature: "trench" },
  4: { terrain: "حُصُونُ خَيْبَر", north: "الْحُصُون", south: "كَتَائِبُ الْفَتْح", feature: "forts" },
  5: { terrain: "مُؤْتَة", north: "الرُّومُ وَالْغَسَاسِنَة", south: "جَيْشُ الْمُسْلِمِينَ", feature: "withdraw" },
  6: { terrain: "وَادِي حُنَيْن", north: "كَمِينُ هَوَازِن", south: "الْمُسْلِمُون", feature: "ambush" },
  7: { terrain: "طَرِيقُ تَبُوك", north: "حُدُودُ الرُّوم", south: "جَيْشُ الْعُسْرَة", feature: "route" },
  8: { terrain: "وَادِي الْيَرْمُوك", north: "الرُّوم", south: "الْكَرَادِيس", feature: "ravine" },
  9: { terrain: "سَهْلُ الْقَادِسِيَّة", north: "الْفُرْسُ وَالْفِيلَة", south: "الْمُسْلِمُون", feature: "elephants" },
  10: { terrain: "نَهَاوَنْد", north: "الْفُرْسُ الْمُتَحَصِّنُون", south: "قُوَّاتُ الاسْتِدْرَاج", feature: "lure" },
  11: { terrain: "بَلَاطُ الشُّهَدَاءِ", north: "الْفِرَنْج", south: "الْقُوَّاتُ الإِسْلَامِيَّة", feature: "squares" },
  12: { terrain: "مَلَاذْكِرْد", north: "الْبِيزَنْطِيُّون", south: "السَّلَاجِقَة", feature: "crescent" },
  13: { terrain: "حِطِّين وَطَبَرِيَّة", north: "الصَّلِيبِيُّون", south: "صَلَاحُ الدِّين", feature: "heat" },
  14: { terrain: "عَيْنُ جَالُوت", north: "الْمَغُول", south: "الْمَمَالِيك", feature: "pincer" },
  15: { terrain: "الْقُسْطَنْطِينِيَّة", north: "الأَسْوَار", south: "الْعُثْمَانِيُّون", feature: "siege" },
};

const state = {
  activeId: null,
  query: "",
  utterance: null,
};

const homeView = document.querySelector("#homeView");
const detailView = document.querySelector("#detailView");
const cardsGrid = document.querySelector("#cardsGrid");
const detailContent = document.querySelector("#detailContent");
const searchInput = document.querySelector("#searchInput");
const homeButton = document.querySelector("#homeButton");
const backButton = document.querySelector("#backButton");
const speakButton = document.querySelector("#speakButton");
const pauseButton = document.querySelector("#pauseButton");
const stopButton = document.querySelector("#stopButton");
const battleCardTemplate = document.querySelector("#battleCardTemplate");
const introCard = document.querySelector(".intro-card");

function normalize(value) {
  return String(value || "")
    .toLowerCase()
    .replace(/[ًٌٍَُِّْـ]/g, "")
    .trim();
}

function filteredBattles() {
  const query = normalize(state.query);
  if (!query) return battles;
  return battles.filter((battle) => normalize(Object.values(battle).join(" ")).includes(query));
}

function makeEl(tag, className, text) {
  const element = document.createElement(tag);
  if (className) element.className = className;
  if (text !== undefined) element.textContent = text;
  return element;
}

function svgEl(tag, attrs = {}) {
  const element = document.createElementNS("http://www.w3.org/2000/svg", tag);
  Object.entries(attrs).forEach(([key, value]) => element.setAttribute(key, value));
  return element;
}

function addSvgText(svg, text, x, y, size = 20, fill = "#23352f", weight = "700") {
  const node = svgEl("text", {
    x,
    y,
    "font-size": size,
    "font-weight": weight,
    fill,
    "text-anchor": "middle",
    "dominant-baseline": "middle",
  });
  node.textContent = text;
  svg.appendChild(node);
}

function addArrow(svg, x1, y1, x2, y2, color, dashed = false) {
  const line = svgEl("line", {
    x1,
    y1,
    x2,
    y2,
    stroke: color,
    "stroke-width": 8,
    "stroke-linecap": "round",
    "marker-end": "url(#arrow)",
  });
  if (dashed) line.setAttribute("stroke-dasharray", "18 12");
  svg.appendChild(line);
}

function addUnit(svg, label, x, y, color, width = 170) {
  const group = svgEl("g");
  group.appendChild(svgEl("rect", {
    x: x - width / 2,
    y: y - 24,
    width,
    height: 48,
    rx: 8,
    fill: color,
    stroke: "#2d2b24",
    "stroke-width": 2,
  }));
  const text = svgEl("text", {
    x,
    y: y + 1,
    "font-size": 18,
    "font-weight": 800,
    fill: "#fffaf0",
    "text-anchor": "middle",
    "dominant-baseline": "middle",
  });
  text.textContent = label;
  group.appendChild(text);
  svg.appendChild(group);
}

function renderTacticalMap(battle, compact = false) {
  const plan = mapPlans[battle.id] || mapPlans[1];
  const svg = svgEl("svg", {
    viewBox: "0 0 900 540",
    role: "img",
    "aria-label": `خريطة تكتيكية: ${battle.titleAr}`,
    class: compact ? "tactical-svg compact" : "tactical-svg",
  });

  const defs = svgEl("defs");
  const marker = svgEl("marker", {
    id: "arrow",
    markerWidth: 12,
    markerHeight: 12,
    refX: 10,
    refY: 6,
    orient: "auto",
    markerUnits: "strokeWidth",
  });
  marker.appendChild(svgEl("path", { d: "M2,2 L10,6 L2,10 Z", fill: "#7d2e2a" }));
  defs.appendChild(marker);
  svg.appendChild(defs);

  svg.appendChild(svgEl("rect", { x: 0, y: 0, width: 900, height: 540, fill: "#e9ddb9" }));
  svg.appendChild(svgEl("path", {
    d: "M0 390 C140 340 220 430 360 370 C520 300 650 390 900 315 L900 540 L0 540 Z",
    fill: "#d9c38d",
    opacity: 0.75,
  }));
  svg.appendChild(svgEl("path", {
    d: "M0 88 C160 122 252 78 395 118 C575 168 692 80 900 124",
    fill: "none",
    stroke: "#b7a26e",
    "stroke-width": 26,
    opacity: 0.55,
  }));

  addSvgText(svg, plan.terrain, 450, 42, compact ? 22 : 30, "#5d351e", "900");

  if (["water", "heat"].includes(plan.feature)) {
    [260, 360, 460, 560].forEach((x, index) => {
      svg.appendChild(svgEl("circle", { cx: x, cy: 272 + (index % 2) * 24, r: 22, fill: "#6fb7bd", stroke: "#2e7178", "stroke-width": 4 }));
    });
    addSvgText(svg, plan.feature === "heat" ? "مَوَارِدُ الْمَاءِ" : "آبَارُ الْمَاءِ", 450, 335, 20, "#245a62");
  }

  if (plan.feature === "ridge") {
    svg.appendChild(svgEl("path", { d: "M80 136 C250 75 385 96 530 148 C660 190 760 166 835 126", fill: "none", stroke: "#8f7850", "stroke-width": 54, "stroke-linecap": "round" }));
    addSvgText(svg, "جَبَلُ أُحُد", 440, 130, 24, "#fff8de");
    addUnit(svg, "الرُّمَاة", 210, 312, "#506b3f", 130);
  }

  if (plan.feature === "trench") {
    svg.appendChild(svgEl("path", { d: "M70 235 L830 235", stroke: "#4b3a2c", "stroke-width": 34, "stroke-dasharray": "28 16" }));
    addSvgText(svg, "الْخَنْدَق", 450, 235, 25, "#fff5d4");
  }

  if (plan.feature === "forts") {
    [230, 450, 670].forEach((x) => {
      svg.appendChild(svgEl("rect", { x: x - 58, y: 138, width: 116, height: 86, rx: 4, fill: "#8a6d45", stroke: "#4d3722", "stroke-width": 5 }));
      svg.appendChild(svgEl("rect", { x: x - 36, y: 104, width: 72, height: 42, fill: "#8a6d45", stroke: "#4d3722", "stroke-width": 5 }));
    });
  }

  if (plan.feature === "ravine") {
    svg.appendChild(svgEl("path", { d: "M580 110 C485 225 530 315 430 500", fill: "none", stroke: "#5f4b39", "stroke-width": 60, "stroke-linecap": "round" }));
    addSvgText(svg, "وَادِي الرُّقَاد", 580, 318, 21, "#fff8de");
  }

  if (plan.feature === "elephants") {
    [330, 450, 570].forEach((x) => addUnit(svg, "فِيل", x, 202, "#7c766b", 88));
  }

  if (plan.feature === "crescent" || plan.feature === "pincer") {
    svg.appendChild(svgEl("path", { d: "M180 352 C260 222 645 222 720 352", fill: "none", stroke: "#236d67", "stroke-width": 20, "stroke-linecap": "round" }));
  }

  if (plan.feature === "siege") {
    svg.appendChild(svgEl("rect", { x: 142, y: 116, width: 616, height: 145, rx: 8, fill: "#94724d", stroke: "#49351f", "stroke-width": 8 }));
    addSvgText(svg, "أَسْوَارُ الْمَدِينَة", 450, 190, 28, "#fff8de");
    svg.appendChild(svgEl("path", { d: "M110 360 C280 322 410 388 574 334 C675 302 760 330 830 300", fill: "none", stroke: "#6fb7bd", "stroke-width": 34, opacity: 0.8 }));
  }

  addUnit(svg, plan.north, 450, 132, "#7d2e2a", compact ? 190 : 250);
  addUnit(svg, plan.south, 450, 430, "#236d67", compact ? 190 : 250);

  addArrow(svg, 450, 162, 450, 375, "#7d2e2a", ["withdraw", "lure"].includes(plan.feature));
  if (["pincer", "crescent", "ambush"].includes(plan.feature)) {
    addArrow(svg, 220, 390, 370, 245, "#236d67", false);
    addArrow(svg, 680, 390, 530, 245, "#236d67", false);
  }
  if (plan.feature === "withdraw") addArrow(svg, 450, 410, 450, 500, "#236d67", true);
  if (plan.feature === "route") addArrow(svg, 250, 455, 655, 145, "#236d67", true);

  addSvgText(svg, "خريطة تعليمية مبنية على وصف المصدر", 450, 510, 15, "#65553b", "700");
  return svg;
}

function renderCards() {
  cardsGrid.innerHTML = "";
  const items = filteredBattles();

  items.forEach((battle) => {
    const supplement = study[battle.id];
    const card = battleCardTemplate.content.firstElementChild.cloneNode(true);
    card.dataset.id = battle.id;
    card.querySelector(".battle-number").textContent = String(battle.id).padStart(2, "0");
    card.querySelector(".battle-date").textContent = battle.date;
    card.querySelector("h2").textContent = battle.titleAr;
    card.querySelector("p").textContent = supplement?.theme || battle.tacticAr;
    card.querySelector(".mini-map").appendChild(renderTacticalMap(battle, true));
    card.addEventListener("click", () => openBattle(battle.id));
    card.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") openBattle(battle.id);
    });
    cardsGrid.appendChild(card);
  });

  introCard.hidden = Boolean(state.query);
}

function createSection(title, text, className = "") {
  const section = makeEl("section", `study-section ${className}`.trim());
  section.append(makeEl("h3", "", title), makeEl("p", "", text));
  return section;
}

function openIntro() {
  stopNarration();
  state.activeId = null;
  homeView.hidden = true;
  detailView.hidden = false;
  detailContent.innerHTML = "";

  const article = makeEl("div", "intro-detail");
  article.append(
    makeEl("p", "eyebrow", "مقدمة المشروع"),
    makeEl("h2", "", "موسوعة ترى المعركة بوصفها قرارا ومكانا ونتيجة"),
    createSection("أَهَمِّيَّةُ الْمَشْرُوعِ", "يُقَدِّمُ هَذَا الأَطْلَسُ الْمَعَارِكَ الْكُبْرَى فِي صُورَةٍ تَعْلِيمِيَّةٍ حَيَّةٍ؛ فَلا يَقِفُ عِنْدَ ذِكْرِ النَّتِيجَةِ، بَلْ يَرْبِطُهَا بِالأَسْبَابِ وَالأَرْضِ وَالْخُطَّةِ وَالتَّنْفِيذِ."),
    createSection("مَنْهَجُ الْعَرْضِ", "تَبْدَأُ كُلُّ مَعْرَكَةٍ بِسَبَبِهَا وَسِيَاقِهَا، ثُمَّ تُعْرَضُ الْخُطَّةُ الاسْتِرَاتِيجِيَّةُ وَالْخَرِيطَةُ التَّكْتِيكِيَّةُ، ثُمَّ النَّتِيجَةُ وَالدَّرْسُ الْمُسْتَخْلَصُ."),
    createSection("الرَّاوِي وَالتَّشْكِيلُ", "تُقْرَأُ النُّصُوصُ الْعَرَبِيَّةُ الْمُشَكَّلَةُ عَبْرَ الرَّاوِي؛ وَهَذَا يُسَاعِدُ عَلَى سَلَامَةِ النُّطْقِ وَجَعْلِ الْمُشَاهِدِ مُنْدَمِجًا مَعَ تَسَلْسُلِ الْحَدَثِ.")
  );
  detailContent.appendChild(article);
}

function openBattle(id) {
  stopNarration();
  state.activeId = id;
  const battle = battles.find((item) => item.id === id);
  const supplement = study[id];
  if (!battle || !supplement) return;

  homeView.hidden = true;
  detailView.hidden = false;
  detailContent.innerHTML = "";

  const hero = makeEl("header", "battle-hero");
  const heroCopy = makeEl("div", "battle-hero-copy");
  heroCopy.append(
    makeEl("p", "eyebrow", `المعركة ${String(battle.id).padStart(2, "0")} | ${battle.date}`),
    makeEl("h2", "", battle.titleAr),
    makeEl("p", "", supplement.theme)
  );
  const heroMap = makeEl("div", "hero-map");
  heroMap.appendChild(renderTacticalMap(battle));
  hero.append(heroCopy, heroMap);

  const grid = makeEl("div", "study-grid");
  grid.append(
    createSection("الأَسْبَابُ وَالأَحْدَاثُ الَّتِي أَدَّتْ إِلَيْهَا", `${battle.causesLocationAr} ${supplement.events}`),
    createSection("الْخُطَّةُ الاسْتِرَاتِيجِيَّةُ وَالتَّكْتِيكُ", battle.tacticAr),
    createSection("أَهَمُّ الشَّخْصِيَّاتِ", battle.figuresAr),
    createSection("النَّتَائِجُ", supplement.results),
    createSection("الدُّرُوسُ وَالْعِبَرُ", battle.lessonsAr),
    createSection("صَوْتُ الرَّاوِي", battle.narratorAr, "narrator-section")
  );

  const sourceMap = makeEl("section", "source-map");
  sourceMap.append(makeEl("h3", "", "الخريطة النصية الأصلية من المصدر"), makeEl("pre", "", battle.mapAscii));

  const english = createSection("Strategic English Summary", battle.strategicEn, "english-section");
  detailContent.append(hero, grid, sourceMap, english);
}

function showHome() {
  stopNarration();
  detailView.hidden = true;
  homeView.hidden = false;
  state.activeId = null;
}

function narrationText() {
  if (state.activeId === null) {
    return Array.from(detailContent.querySelectorAll("h2, h3, p"))
      .map((node) => node.textContent)
      .join(". ");
  }
  const battle = battles.find((item) => item.id === state.activeId);
  const supplement = study[state.activeId];
  if (!battle || !supplement) return "";
  return [
    battle.titleAr,
    "الأسباب والأحداث التي أدت إليها.",
    battle.causesLocationAr,
    supplement.events,
    "الخطة الاستراتيجية والتكتيك.",
    battle.tacticAr,
    "النتائج.",
    supplement.results,
    "الدروس والعبر.",
    battle.lessonsAr,
    "صوت الراوي.",
    battle.narratorAr,
  ].join(". ");
}

function speakNarration() {
  if (!("speechSynthesis" in window)) {
    alert("المتصفح الحالي لا يدعم الراوي الصوتي.");
    return;
  }
  if (speechSynthesis.paused) {
    speechSynthesis.resume();
    return;
  }
  stopNarration();
  const utterance = new SpeechSynthesisUtterance(narrationText());
  utterance.lang = "ar-SA";
  utterance.rate = 0.88;
  utterance.pitch = 1;
  state.utterance = utterance;
  speechSynthesis.speak(utterance);
}

function pauseNarration() {
  if ("speechSynthesis" in window && speechSynthesis.speaking) speechSynthesis.pause();
}

function stopNarration() {
  if ("speechSynthesis" in window) speechSynthesis.cancel();
  state.utterance = null;
}

searchInput.addEventListener("input", (event) => {
  state.query = event.target.value;
  renderCards();
});
homeButton.addEventListener("click", showHome);
backButton.addEventListener("click", showHome);
introCard.addEventListener("click", openIntro);
introCard.addEventListener("keydown", (event) => {
  if (event.key === "Enter" || event.key === " ") openIntro();
});
speakButton.addEventListener("click", speakNarration);
pauseButton.addEventListener("click", pauseNarration);
stopButton.addEventListener("click", stopNarration);
window.addEventListener("beforeunload", stopNarration);

renderCards();

const requestedBattle = Number(new URLSearchParams(window.location.search).get("battle"));
if (requestedBattle && battles.some((battle) => battle.id === requestedBattle)) {
  openBattle(requestedBattle);
}
