import streamlit as st

plant_details = {
    "🌿 🌿 🌿 - A  L  O  E     V  E  R  A - 🌿 🌿 🌿": (
        "https://www.lotusherbals.com/cdn/shop/files/Aloe_Vera_9685987d-616b-471a-b5d6-46695d739ab5_600x.jpg?v=1712989712",
        "Soothes and heals skin conditions and burns with its moisturizing and anti-inflammatory properties. Promotes wound healing and can be used topically for various skin issues."
    ),
    "🌿 🌿 🌿 - B  A  S  I  L - 🌿 🌿 🌿": (
        "https://www.diggers.com.au/cdn/shop/products/basil-thai-s302_6b10e7ed-d626-439b-baba-84b4c3e34a3a_2048x.jpg?v=1637121832",
        "Offers anti-inflammatory and antibacterial benefits. Commonly used to alleviate digestive issues, respiratory ailments, and enhance overall immune health. Adds flavor and medicinal value to a variety of dishes."
    ),
    "🌼 🌼 🌼 - C  H  A  M  O  M  I  L  E - 🌼 🌼 🌼": (
        "https://thegrowers-exchange.com/cdn/shop/products/GermanChamomile_copy_600x.jpg?v=1576945054",
        "Known for its calming effects, chamomile aids in sleep and relaxation. It also supports digestion and relieves stress, making it a popular herbal remedy for calming and soothing the body."
    ),
    "🌸 🌸 🌸 - E  C  H  I  N  A  C  E  A - 🌸 🌸 🌸": (
        "https://www.johnnyseeds.com/dw/image/v2/BJGJ_PRD/on/demandware.static/-/Sites-jss-master/default/dwd03537dc/images/products/vegetables/00842_01_purple_echinacea.jpg?sw=800&cx=302&cy=0&cw=1196&ch=1196",
        "Boosts the immune system and helps prevent or treat colds and infections. Echinacea is widely used to strengthen the body's defense mechanisms and reduce the duration of illnesses."
    ),
    "🌱 🌱 🌱 - G  I  N  G  E  R - 🌱 🌱 🌱": (
        "https://cdn.britannica.com/19/231119-050-35483892/Indian-ginger-Zingiber-officinale.jpg",
        "Provides anti-nausea and anti-inflammatory effects. It supports digestion, alleviates nausea, and helps with inflammation-related conditions. Often used in culinary and medicinal applications for its health benefits."
    ),
    "🌺 🌺 🌺 - L  A  V  E  N  D  E  R - 🌺 🌺 🌺": (
        "https://growhub.ae/cdn/shop/products/english-lavender-lavandula-angustifolia-garden-design_11716_grande.jpg?v=1680718881",
        "Renowned for its calming and relaxing properties. Often used in aromatherapy, lavender helps reduce stress, anxiety, and promotes overall relaxation, making it a popular choice for soothing the mind and body."
    ),
    "🌿 🌿 🌿 - P  E  P  P  E  R  M  I  N  T - 🌿 🌿 🌿": (
        "https://nurserylive.com/cdn/shop/products/nurserylive-seeds-peppermint-herb-seeds-16969106948236.jpg?v=1634204585",
        "Aids in digestion and relieves headaches and muscle pain. Its cooling and soothing properties make it effective for gastrointestinal discomfort and minor pain relief, as well as a refreshing flavoring agent."
    ),
    "🌱 🌱 🌱 - R  O  S  E  M  A  R  Y - 🌱 🌱 🌱": (
        "https://www.swasthyashiksha.com/wp-content/uploads/2024/04/f845d449-122e-4ae5-9f81-af2f215e2e37.png",
        "Contains antioxidants and supports memory and digestion. It is commonly used to enhance cognitive function, improve digestive health, and add flavor to various dishes with its aromatic properties."
    ),
    "🌿 🌿 🌿 - T  U  R  M  E  R  I  C - 🌿 🌿 🌿": (
        "https://myperfectplants.com/cdn/shop/files/YellowTurmeric_2_AS565937632_1080x.jpg?v=1714584689",
        "Rich in curcumin, which has potent anti-inflammatory and antioxidant effects. Turmeric is widely used to combat inflammation, support joint health, and as a beneficial spice in many cuisines."
    ),
    "🌺 🌺 🌺 - V  A  L  E  R  I  A  N - 🌺 🌺 🌺": (
        "https://cdn.shopify.com/s/files/1/0506/7037/0997/articles/HerbalLibrary_Hero_Valerian_1400x1400_d733fff2-bc48-4739-8aa4-c4ccb6434354.jpg?v=1662261053",
        "Provides sedative effects and is commonly used to treat insomnia and anxiety. Valerian helps promote relaxation and improve sleep quality, making it a popular herbal remedy for sleep disorders."
    ),
    "🌱 🌱 🌱 - G  A  R  L  I  C - 🌱 🌱 🌱": (
        "https://plantinfo.co.za/wp-content/uploads/2024/02/fresh-garlic-plant-from-the-garden-plantinfo.co_.za3_.jpg",
        "Has strong antibacterial and antiviral properties. Garlic boosts the immune system, supports cardiovascular health, and has been used for centuries to enhance flavor and provide various health benefits."
    ),
    "🌿 🌿 🌿 - G  I  N  S  E  N  G - 🌿 🌿 🌿": (
        "https://i0.wp.com/breasrl.it/wp-content/uploads/2017/06/panax-ginseng.jpg?resize=1024%2C1024&ssl=1",
        "Boosts energy levels and relieves stress. Known for its adaptogenic properties, ginseng helps improve overall vitality, mental performance, and physical endurance, making it a popular herbal supplement."
    ),
    "🌱 🌱 🌱 - T  H  Y  M  E - 🌱 🌱 🌱": (
        "https://nurserylive.com/cdn/shop/products/nurserylive-seeds-thyme-thymus-vulgaris-herb-seeds-16969124053132.jpg?v=1634205062",
        "Features antiseptic and antibacterial qualities, making it useful for respiratory issues and infections. Thyme also supports digestive health and adds flavor to dishes, enhancing both taste and wellness."
    ),
    "🌿 🌿 🌿 - S  A  G  E - 🌿 🌿 🌿": (
        "https://www.kitchengardenplantcentre.co.uk/storage/img/products/purple-sage.webp",
        "Known for its anti-inflammatory and antioxidant effects. Sage supports digestive health, cognitive function, and overall wellness. Often used in cooking and herbal remedies for its therapeutic properties."
    ),
    "🌼 🌼 🌼 - C  A  L  E  N  D  U  L  A - 🌼 🌼 🌼": (
        "https://www.sementesvivas.bio/pt/1779-large_default/calendula-.jpg",
        "Promotes healing of skin conditions and wounds with its anti-inflammatory properties. Calendula is used topically to soothe and repair damaged skin, and is known for its gentle, healing effects."
    ),
    "🌼 🌼 🌼 - D  A  N  D  E  L  I  O  N - 🌼 🌼 🌼": (
        "https://cdn11.bigcommerce.com/s-a9b4a/images/stencil/1280x1280/products/2907/7918/Dandelion__66808.1677163311.jpg?c=2",
        "Acts as a diuretic and detoxifier, supporting liver and digestive health. Dandelion is used to improve digestion, stimulate appetite, and promote overall detoxification and wellness in the body."
    ),
    "🌿 🌿 🌿 - F  E  N  N  E  L - 🌿 🌿 🌿": (
        "https://cdn.loveandlemons.com/wp-content/uploads/2020/03/fennel.jpg",
        "Supports digestive health and has anti-inflammatory properties. Fennel is used to alleviate bloating, gas, and other digestive discomforts while also providing soothing effects on the gastrointestinal tract."
    ),
    "🌿 🌿 🌿 - L  E  M  O  N     B  A  L  M - 🌿 🌿 🌿": (
        "https://rukminim2.flixcart.com/image/850/1000/xif0q/plant-seed/l/s/7/200-xxl-514-lemon-balm-herb-seed-200-seeds-vibex-original-imagghmm7ehjm52w.jpeg?q=90&crop=false",
        "Provides calming effects and helps reduce anxiety and stress. Lemon balm is used to promote relaxation, improve sleep quality, and support overall emotional well-being through its soothing properties."
    ),
    "🌿 🌿 🌿 - M  I  L  K     T  H  I  S  T  L  E - 🌿 🌿 🌿": (
        "https://www.incredibleseeds.ca/cdn/shop/products/Flower-MilkThistle_460x@2x.jpg?v=1652892424",
        "Known for its liver-protective properties, Milk Thistle helps detoxify and support liver health. Its active ingredient, silymarin, provides antioxidant benefits and promotes overall liver function and well-being."
    ),
    "🌼 🌼 🌼 - S  T  .     J  O  H  N  '  S     W  O  R  T - 🌼 🌼 🌼": (
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT59oKQIqtzHbOdq4CuOTEGeUlC2vVsxt424Q&s",
        "Used to treat mild to moderate depression and anxiety. St. John's Wort helps balance mood and improve emotional well-being with its natural antidepressant effects, often used as a herbal remedy."
    ),
    "🌿 🌿 🌿 - A  S  H  W  A  G  A  N  D  H  A - 🌿 🌿 🌿": (
        "https://static.wixstatic.com/media/20b0a1_a7d4a800950c45ba917bf00fa1df8583~mv2.jpg/v1/fill/w_560,h_560,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/20b0a1_a7d4a800950c45ba917bf00fa1df8583~mv2.jpg",
        "Known for its stress-relieving and energy-boosting properties. Ashwagandha helps improve resilience to stress, enhance vitality, and support overall mental and physical health through its adaptogenic effects."
    ),
    "🌿 🌿 🌿 - C  A  T  N  I  P - 🌿 🌿 🌿": (
        "https://seedsireland.ie/cdn/shop/files/Catnip.webp?v=1707841313",
        "Provides calming effects and helps treat insomnia and anxiety. Catnip is used to promote relaxation, reduce stress, and improve sleep quality, making it a helpful herbal remedy for restful nights."
    ),
    "🌶 🌶 🌶 - C  A  Y  E  N  N  E     P  E  P  P  E  R - 🌶 🌶 🌶": (
        "https://growhoss.com/cdn/shop/files/PepperPhoto.jpg?v=1700226306",
        "Offers pain-relieving properties and boosts metabolism. Cayenne pepper contains capsaicin, which supports pain relief and enhances metabolic function, often used in both culinary and medicinal applications."
    ),
    "🍇 🍇 🍇 - E  L  D  E  R  B  E  R  R  Y - 🍇 🍇 🍇": (
        "https://www.incredibleseeds.ca/cdn/shop/products/BlackElderberry-Sambucuscanadensis.jpg?v=1678470028",
        "Boosts the immune system and helps treat colds and flu. Elderberry is rich in antioxidants and provides support for respiratory health, making it a popular choice for immune-boosting supplements."
    ),
    "🌼 🌼 🌼 - F  E  V  E  R  F  E  W - 🌼 🌼 🌼": (
        "https://files.nccih.nih.gov/feverfew-steven-foster-square.jpg",
        "Helps prevent migraines and reduce fever. Feverfew is used to alleviate headache symptoms and manage fever, providing relief from discomfort and supporting overall health and wellness."
    ),
    "🌿 🌿 🌿 - G  I  N  K  G  O     B  I  L  O  B  A - 🌿 🌿 🌿": (
        "https://jardin-florilege.eu/sites/default/files/images/16%2095%20s%20Ginkgo/Ginkgo%20biloba%20Little%20Joe_002%20(17).jpg",
        "Improves memory and cognitive function. Ginkgo biloba supports brain health and mental clarity, and is often used to enhance cognitive performance and circulation in the brain."
    ),
    "🌿 🌿 🌿 - H  A  W  T  H  O  R  N - 🌿 🌿 🌿": (
        "https://www.snapdragonlife.com/siteimages/blog/hawthorn.jpg",
        "Supports heart health and improves circulation. Hawthorn is used to strengthen cardiovascular function, enhance blood flow, and promote overall heart wellness with its beneficial properties."
    ),
    "🌊 🌊 🌊 - K  E  L  P - 🌊 🌊 🌊": (
        "https://i.natgeofe.com/n/802f1c72-e3b9-489f-b9ca-f930cedaa4ab/KELP-77_square.jpg",
        "Rich in iodine, supports thyroid function and overall health. Kelp provides essential nutrients for thyroid health, metabolism, and maintains overall well-being through its rich mineral content."
    ),
    "🍃 🍃 🍃 - L  E  M  O  N     G  R  A  S  S - 🍃 🍃 🍃": (
        "https://www.greenthumbsgarden.com/cdn/shop/products/LEMONGRASS1_1400x.jpg?v=1653332525",
        "Offers calming effects and supports digestive health. Lemon grass is used to relieve stress, aid digestion, and add flavor to dishes, while also providing a soothing and refreshing experience."
    ),
    "🌶 🌶 🌶 - L  O  N  G     P  E  P  P  E  R - 🌶 🌶 🌶": (
        "https://m.media-amazon.com/images/I/516vwVhtemL.jpg",
        "Provides digestive and respiratory benefits. Long pepper helps improve digestion, alleviate respiratory issues, and is used as a spice and herbal remedy for overall health support."
    ),
    "🌿 🌿 🌿 - L  O  V  A  G  E - 🌿 🌿 🌿": (
        "https://www.myseeds.co/cdn/shop/products/FF_54ed9bd9-447e-43f8-a0d8-221533ef8682_1024x1024.jpg?v=1626113358",
        "Supports digestion and urinary tract health. Lovage is used to enhance digestive function, relieve urinary tract discomfort, and add a distinctive flavor to culinary dishes."
    ),
    "🌺 🌺 🌺 - M  A  C  A     R  O  O  T - 🌺 🌺 🌺": (
        "https://nurserylive.com/cdn/shop/products/nurserylive-plants-lepidium-meyenii-maca-plant.jpg?v=1634223226",
        "Boosts energy and supports hormonal balance. Maca root is used to enhance physical stamina, mental clarity, and hormonal health, making it a popular supplement for overall vitality."
    ),
    "🌺 🌺 🌺 - M  A  R  A  C  U  J  A - 🌺 🌺 🌺": (
        "https://agriconline.com.br/portal/wp-content/uploads/2021/09/muda-de-maracuja-azedo-passiflora-edulis_1_1200.jpg",
        "Supports relaxation and sleep with its calming effects. Maracuja, or passion fruit, is used to promote restful sleep and alleviate stress, offering a natural solution for relaxation."
    ),
    "🌿 🌿 🌿 - M  O  R  I  N  G  A     L  E  A  F - 🌿 🌿 🌿": (
        "https://cdn.shopify.com/s/files/1/0059/8835/2052/products/Moringa_Tree_6.jpg?v=1696348214",
        "Rich in vitamins and minerals, supports overall health and immune function. Moringa provides essential nutrients and antioxidant benefits for enhanced vitality and well-being."
    ),
    "🍇 🍇 🍇 - M  U  L  B  E  R  R  Y     L  E  A  F - 🍇 🍇 🍇": (
        "https://images.squarespace-cdn.com/content/v1/5a87224390bcced019d42596/1707619957476-R9JM49F685639A40VE4F/Trader+Mulberry_Montana+Fruit+Tree+Co.jpg?format=1000w",
        "Offers anti-inflammatory and blood sugar-regulating properties. Mulberry leaf supports healthy blood sugar levels and reduces inflammation, making it a beneficial addition to a balanced diet."
    ),
    "🌿 🌿 🌿 - N  O  N  I - 🌿 🌿 🌿": (
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_IJbUM5E2ZurAAkDSPm8LB1ZYzINXtJQoW5cL8gGXf_so1x1ecFjN6WWGedJpg4WAE9M&usqp=CAU",
        "Supports immune health and has antioxidant properties. Noni is used to strengthen the immune system, improve overall health, and provide antioxidant support for cellular protection."
    ),
    "🌿 🌿 🌿 - O  S  H  A     R  O  O  T - 🌿 🌿 🌿": (
        "https://i0.wp.com/elkmountainherbs.com/wp-content/uploads/2019/12/Osha-800X800.jpg?fit=803%2C800&ssl=1",
        "Used for respiratory health and to alleviate coughs and colds. Osha root helps support respiratory function and relieve symptoms of respiratory discomfort and illness."
    ),
    "🌿 🌿 🌿 - P  A  U     D ' A  R  C  O - 🌿 🌿 🌿": (
        "https://woodlandessence.com/cdn/shop/products/Pau-D-Arco-Website_800x.jpg?v=1672252451",
        "Known for its antifungal and immune-boosting properties. Pau D'Arco supports immune health and combats fungal infections with its natural antifungal compounds."
    ),
    "🌸 🌸 🌸 - P  E  O  N  Y     R  O  O  T - 🌸 🌸 🌸": (
        "https://images-cdn.ubuy.co.in/6451fa242044a3672031e481-peony-roots-candy-stripe-1-root.jpg",
        "Supports hormonal balance and reduces inflammation. Peony root is used to regulate hormonal levels, alleviate inflammation, and promote overall well-being in various health conditions."
    ),
    "🌿 🌿 🌿 - P  E  R  I  W  I  N  K  L  E - 🌿 🌿 🌿": (
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ29Zu2ZoHbrYt79_DC3xhy3PJ4pTqN0fRqdeZ2Imm4qjS2fVgFdhmHvHSOttN3F_BxB48&usqp=CAU",
        "Supports cognitive function and circulation. Periwinkle is used to enhance brain health, improve blood flow, and support cognitive performance and memory."
    ),
    "🌲 🌲 🌲 - P  I  N  E     N  E  E  D  L  E - 🌲 🌲 🌲": (
        "https://pineneedletea.org/cdn/shop/products/ImmuneBoostingWhitePineNeedleTea-Close-upGlassTeaCup_2000x2000.jpg?v=1681435785",
        "Rich in vitamin C, supports immune health and respiratory function. Pine needle provides antioxidant benefits, strengthens the immune system, and aids in respiratory wellness."
    ),
    "🌿 🌿 🌿 - R  E  H  M  A  N  N  I  A - 🌿 🌿 🌿": (
        "https://www.plant-world-seeds.com/images/item_images/000/005/677/large_square/REHMANNIA-ELATA-.JPG?1495393490",
        "Supports adrenal function and helps with hormonal balance. Rehmannia is used to improve adrenal health, manage stress, and promote overall hormonal equilibrium."
    ),
    "🌿 🌿 🌿 - S  A  R  S  A  P  A  R  I  L  L  A - 🌿 🌿 🌿": (
        "https://i.ebayimg.com/images/g/OTIAAOSwRelg3YU1/s-l1200.jpg",
        "Supports hormonal balance and detoxification. Sarsaparilla is used to regulate hormones, promote detoxification, and support overall health and wellness."
    ),
    "🌿 🌿 🌿 - S  C  H  I  S  A  N  D  R  A - 🌿 🌿 🌿": (
        "https://m.media-amazon.com/images/I/71XDrT5slkL._AC_UF894,1000_QL80_.jpg",
        "Adaptogenic herb known for its liver-supporting and stress-relieving properties. Schisandra enhances resilience to stress and supports overall liver function and vitality."
    ),
    "🌿 🌿 🌿 - S  E  R  P  E  N  T  I  N  A - 🌿 🌿 🌿": (
        "https://www.picturethisai.com/wiki-image/1080/218703960964726784.jpeg",
        "Supports digestive health and reduces inflammation. Serpentina helps with gastrointestinal issues, alleviates inflammation, and provides therapeutic benefits."
    ),
    "🌿 🌿 🌿 - S  T  I  N  G  I  N  G     N  E  T  T  L  E - 🌿 🌿 🌿": (
        "https://i0.wp.com/www.hitchcockcenter.org/wp-content/uploads/2015/09/EM_4-14-13.jpg?resize=737%2C600&ssl=1",
        "Offers anti-inflammatory and detoxifying effects. Stinging nettle supports urinary health, reduces inflammation, and aids in detoxification processes."
    ),
    "🌿 🌿 🌿 - S  W  E  E  T     W  O  O  D  R  U  F  F - 🌿 🌿 🌿": (
        "https://chelseagardencenter.com/cdn/shop/products/GalliumSweetWoodruff.webp?v=1718823717",
        "Provides calming effects and supports relaxation and sleep. Sweet woodruff is used to promote restful sleep and reduce stress with its soothing properties."
    ),
    "🌼 🌼 🌼 - T  A  N  S  Y - 🌼 🌼 🌼": (
        "https://thegrowers-exchange.com/cdn/shop/products/Tansy_dc14c7d2-6fcc-41be-b876-6c7120d23797_600x.jpg?v=1668606555",
        "Traditionally used for digestive and menstrual health. Tansy supports digestive function, relieves menstrual discomfort, and provides various herbal benefits."
    ),
    "🌿 🌿 🌿 - T  H  I  S  T  L  E - 🌿 🌿 🌿": (
        "https://files.nccih.nih.gov/milk-thistle-thinkstockphotos-93966680-square-1-.jpg",
        "Supports liver health and detoxification. Thistle aids in liver function, promotes detoxification, and improves overall health with its beneficial properties."
    ),
    "🌿 🌿 🌿 - T  R  I  P  H  A  L  A - 🌿 🌿 🌿": (
        "https://kadiyamnursery.com/cdn/shop/products/TriphalaPlant_1200x1200.jpg?v=1681123958",
        "A blend of three fruits used for digestive health and detoxification. Triphala supports regular bowel movements, detoxifies the body, and improves overall digestive function."
    ),
    "🌿 🌿 🌿 - U  V  A     U  R  S  I - 🌿 🌿 🌿": (
        "https://draxe.com/wp-content/uploads/2021/05/BerryFB-1.jpg",
        "Supports urinary tract health and provides anti-inflammatory effects. Uva Ursi is used to maintain urinary health, alleviate inflammation, and support overall wellness."
    ),
    "🌿 🌿 🌿 - W  O  R  M  W  O  O  D - 🌿 🌿 🌿": (
        "https://images.finegardening.com/app/uploads/2018/01/23143631/artemisiaabsinthium_jwb_2_xlg-main-500x500.jpg",
        "Used to relieve digestive issues and support relaxation. Worm wood helps with gastrointestinal discomfort, reduces stress, and promotes overall well-being."
    ),
    "🌼 🌼 🌼 - Y  A  R  R  O  W - 🌼 🌼 🌼": (
        "https://www.plantex.fr/wp-content/uploads/2024/04/Saule.jpg",
        "Provides pain relief and anti-inflammatory effects. Yarrow is used to alleviate pain, reduce inflammation, and support overall health with its natural analgesic properties."
    )
}

plants=[
    "SEARCH HERE",
    "🌿 🌿 🌿 - A  L  O  E     V  E  R  A - 🌿 🌿 🌿",
    "🌿 🌿 🌿 - B  A  S  I  L - 🌿 🌿 🌿",
    "🌼 🌼 🌼 - C  H  A  M  O  M  I  L  E - 🌼 🌼 🌼",
    "🌸 🌸 🌸 - E  C  H  I  N  A  C  E  A - 🌸 🌸 🌸",
    "🌱 🌱 🌱 - G  I  N  G  E  R - 🌱 🌱 🌱",
    "🌺 🌺 🌺 - L  A  V  E  N  D  E  R - 🌺 🌺 🌺",
    "🌿 🌿 🌿 - P  E  P  P  E  R  M  I  N  T - 🌿 🌿 🌿",
    "🌱 🌱 🌱 - R  O  S  E  M  A  R  Y - 🌱 🌱 🌱",
    "🌿 🌿 🌿 - T  U  R  M  E  R  I  C - 🌿 🌿 🌿",
    "🌺 🌺 🌺 - V  A  L  E  R  I  A  N - 🌺 🌺 🌺",
    "🌱 🌱 🌱 - G  A  R  L  I  C - 🌱 🌱 🌱",
    "🌿 🌿 🌿 - G  I  N  S  E  N  G - 🌿 🌿 🌿",
    "🌱 🌱 🌱 - T  H  Y  M  E - 🌱 🌱 🌱",
    "🌿 🌿 🌿 - S  A  G  E - 🌿 🌿 🌿",
    "🌼 🌼 🌼 - C  A  L  E  N  D  U  L  A - 🌼 🌼 🌼",
    "🌼 🌼 🌼 - D  A  N  D  E  L  I  O  N - 🌼 🌼 🌼",
    "🌿 🌿 🌿 - F  E  N  N  E  L - 🌿 🌿 🌿",
    "🌿 🌿 🌿 - L  E  M  O  N     B  A  L  M - 🌿 🌿 🌿",
    "🌿 🌿 🌿 - M  I  L  K     T  H  I  S  T  L  E - 🌿 🌿 🌿",
    "🌼 🌼 🌼 - S  T  .     J  O  H  N  '  S     W  O  R  T - 🌼 🌼 🌼",
    "🌿 🌿 🌿 - A  S  H  W  A  G  A  N  D  H  A - 🌿 🌿 🌿",
    "🌿 🌿 🌿 - C  A  T  N  I  P - 🌿 🌿 🌿",
    "🌶 🌶 🌶 - C  A  Y  E  N  N  E     P  E  P  P  E  R - 🌶 🌶 🌶",
    "🍇 🍇 🍇 - E  L  D  E  R  B  E  R  R  Y - 🍇 🍇 🍇",
    "🌼 🌼 🌼 - F  E  V  E  R  F  E  W - 🌼 🌼 🌼",
    "🌿 🌿 🌿 - G  I  N  K  G  O     B  I  L  O  B  A - 🌿 🌿 🌿",
    "🌿 🌿 🌿 - H  A  W  T  H  O  R  N - 🌿 🌿 🌿",
    "🌊 🌊 🌊 - K  E  L  P - 🌊 🌊 🌊",
    "🍃 🍃 🍃 - L  E  M  O  N     G  R  A  S  S - 🍃 🍃 🍃",
    "🌶 🌶 🌶 - L  O  N  G     P  E  P  P  E  R - 🌶 🌶 🌶",
    "🌿 🌿 🌿 - L  O  V  A  G  E - 🌿 🌿 🌿",
    "🌺 🌺 🌺 - M  A  C  A     R  O  O  T - 🌺 🌺 🌺",
    "🌺 🌺 🌺 - M  A  R  A  C  U  J  A - 🌺 🌺 🌺",
    "🌿 🌿 🌿 - M  O  R  I  N  G  A     L  E  A  F - 🌿 🌿 🌿",
    "🍇 🍇 🍇 - M  U  L  B  E  R  R  Y     L  E  A  F - 🍇 🍇 🍇",
    "🌿 🌿 🌿 - N  O  N  I - 🌿 🌿 🌿",
    "🌿 🌿 🌿 - O  S  H  A     R  O  O  T - 🌿 🌿 🌿",
    "🌿 🌿 🌿 - P  A  U     D ' A  R  C  O - 🌿 🌿 🌿",
    "🌸 🌸 🌸 - P  E  O  N  Y     R  O  O  T - 🌸 🌸 🌸",
    "🌿 🌿 🌿 - P  E  R  I  W  I  N  K  L  E - 🌿 🌿 🌿",
    "🌲 🌲 🌲 - P  I  N  E     N  E  E  D  L  E - 🌲 🌲 🌲",
    "🌿 🌿 🌿 - R  E  H  M  A  N  N  I  A - 🌿 🌿 🌿",
    "🌿 🌿 🌿 - S  A  R  S  A  P  A  R  I  L  L  A - 🌿 🌿 🌿",
    "🌿 🌿 🌿 - S  C  H  I  S  A  N  D  R  A - 🌿 🌿 🌿",
    "🌿 🌿 🌿 - S  E  R  P  E  N  T  I  N  A - 🌿 🌿 🌿",
    "🌿 🌿 🌿 - S  T  I  N  G  I  N  G     N  E  T  T  L  E - 🌿 🌿 🌿",
    "🌿 🌿 🌿 - S  W  E  E  T     W  O  O  D  R  U  F  F - 🌿 🌿 🌿",
    "🌼 🌼 🌼 - T  A  N  S  Y - 🌼 🌼 🌼",
    "🌿 🌿 🌿 - T  H  I  S  T  L  E - 🌿 🌿 🌿",
    "🌿 🌿 🌿 - T  R  I  P  H  A  L  A - 🌿 🌿 🌿",
    "🌿 🌿 🌿 - U  V  A     U  R  S  I - 🌿 🌿 🌿",
    "🌿 🌿 🌿 - W  O  R  M  W  O  O  D - 🌿 🌿 🌿",
    "🌼 🌼 🌼 - Y  A  R  R  O  W - 🌼 🌼 🌼"
]

def med_page():
    st.title("🎍 MEDICINAL HERBS, PROPERTIES")
    
    # Inject custom CSS for larger text
    st.markdown("""
        <style>
        .description-text {
            font-size: 15 px;
        }
        </style>
        """, unsafe_allow_html=True)
    
    with st.form("med_plant"):
        selected = st.selectbox("MEDICINAL PLANTS", plants)
        search = st.form_submit_button("Search")
        if selected in plant_details and search:
            img_path, description = plant_details[selected]
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(img_path, use_column_width=True)
            with col2:
                st.divider()
                st.markdown(f"<div class='description-text'>{description}</div>", unsafe_allow_html=True)
                st.divider()
    st.divider()
    st.divider()
