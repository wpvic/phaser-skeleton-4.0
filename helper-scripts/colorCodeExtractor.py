#0000A0	Earth Blue
#0020C2	Cobalt Blue
#0041C2	Blueberry Blue
#2554C7	Sapphire Blue
#1569C7	Blue Eyes
#2B60DE	Royal Blue
#1F45FC	Blue Orchid
#6960EC	Blue Lotus
#736AFF	Light Slate Blue
#357EC7	Slate Blue
#368BC1	Glacial Blue Ice
#488AC7	Silk Blue
#3090C7	Blue Ivy
#659EC7	Blue Koi
#87AFC7	Columbia Blue
#95B9C7	Baby Blue
#728FCE	Light Steel Blue
#2B65EC	Ocean Blue
#306EFF	Blue Ribbon
#157DEC	Blue Dress
#1589FF	Dodger Blue
#6495ED	Cornflower Blue
#6698FF	Sky Blue
#38ACEC adsadsd

def extractColorCode(colors):
	colors = colors.replace('\t','\n').replace(' ','\n').replace('"','\n').split('\n')
	for i in range(len(colors)-1,0,-1):
		if('#' not in colors[i]):
			colors.remove(colors[i])
	print colors

# extractColorCode('''#000000	Black
#0C090A	Night
#2C3539	Gunmetal
#2B1B17	Midnight
#34282C	Charcoal
#25383C	Dark Slate Grey
#3B3131	Oil
#413839	Black Cat
#3D3C3A	Iridium
#463E3F	Black Eel
#4C4646	Black Cow
#504A4B	Gray Wolf
#565051	Vampire Gray
#5C5858	Gray Dolphin
#625D5D	Carbon Gray
#666362	Ash Gray
#6D6968	Cloudy Gray
#726E6D	Smokey Gray
#736F6E	Gray
#837E7C	Granite
#848482	Battleship Gray
#B6B6B4	Gray Cloud
#D1D0CE	Gray Goose
#E5E4E2	Platinum
#BCC6CC	Metallic Silver
#98AFC7	Blue Gray
#6D7B8D	Light Slate Gray
#657383	Slate Gray
#616D7E	Jet Gray
#646D7E	Mist Blue
#566D7E	Marble Blue
#737CA1	Slate Blue
#4863A0	Steel Blue
#2B547E	Blue Jay
#2B3856	Dark Slate Blue
#151B54	Midnight Blue
#000080	Navy Blue
#342D7E	Blue Whale
#15317E	Lapis Blue
#151B8D	Cornflower Blue
#0000A0	Earth Blue
#0020C2	Cobalt Blue
#0041C2	Blueberry Blue
#2554C7	Sapphire Blue
#1569C7	Blue Eyes
#2B60DE	Royal Blue
#1F45FC	Blue Orchid
#6960EC	Blue Lotus
#736AFF	Light Slate Blue
#357EC7	Slate Blue
#368BC1	Glacial Blue Ice
#488AC7	Silk Blue
#3090C7	Blue Ivy
#659EC7	Blue Koi
#87AFC7	Columbia Blue
#95B9C7	Baby Blue
#728FCE	Light Steel Blue
#2B65EC	Ocean Blue
#306EFF	Blue Ribbon
#157DEC	Blue Dress
#1589FF	Dodger Blue
#6495ED	Cornflower Blue
#6698FF	Sky Blue
#38ACEC	Butterfly Blue
#56A5EC	Iceberg
#5CB3FF	Crystal Blue
#3BB9FF	Deep Sky Blue
#79BAEC	Denim Blue
#82CAFA	Light Sky Blue
#82CAFF	Day Sky Blue
#A0CFEC	Jeans Blue
#B7CEEC	Blue Angel
#B4CFEC	Pastel Blue
#C2DFFF	Sea Blue
#C6DEFF	Powder Blue
#AFDCEC	Coral Blue
#ADDFFF	Light Blue
#BDEDFF	Robin Egg Blue
#CFECEC	Pale Blue Lily
#E0FFFF	Light Cyan
#EBF4FA	Water
#F0F8FF	AliceBlue
#F0FFFF	Azure
#CCFFFF	Light Slate
#93FFE8	Light Aquamarine
#9AFEFF	Electric Blue
#7FFFD4	Aquamarine
#00FFFF	Cyan or Aqua
#7DFDFE	Tron Blue
#57FEFF	Blue Zircon
#8EEBEC	Blue Lagoon
#50EBEC	Celeste
#4EE2EC	Blue Diamond
#81D8D0	Tiffany Blue
#92C7C7	Cyan Opaque
#77BFC7	Blue Hosta
#78C7C7	Northern Lights Blue
#48CCCD	Medium Turquoise
#43C6DB	Turquoise
#46C7C7	Jellyfish
#43BFC7	Macaw Blue Green
#3EA99F	Light Sea Green
#3B9C9C	Dark Turquoise
#438D80	Sea Turtle Green
#348781	Medium Aquamarine
#307D7E	Greenish Blue
#5E7D7E	Grayish Turquoise
#4C787E	Beetle Green
#008080	Teal
#4E8975	Sea Green
#78866B	Camouflage Green
#848b79	Sage Green
#617C58	Hazel Green
#728C00	Venom Green
#667C26	Fern Green
#254117	Dark Forest Green
#306754	Medium Sea Green
#347235	Medium Forest Green
#437C17	Seaweed Green
#387C44	Pine Green
#347C2C	Jungle Green
#347C17	Shamrock Green
#348017	Medium Spring Green
#4E9258	Forest Green
#6AA121	Green Onion
#4AA02C	Spring Green
#41A317	Lime Green
#3EA055	Clover Green
#6CBB3C	Green Snake
#6CC417	Alien Green
#4CC417	Green Apple
#52D017	Yellow Green
#4CC552	Kelly Green
#54C571	Zombie Green
#99C68E	Frog Green
#89C35C	Green Peas
#85BB65	Dollar Bill Green
#8BB381	Dark Sea Green
#9CB071	Iguana Green
#B2C248	Avocado Green
#9DC209	Pistachio Green
#A1C935	Salad Green
#7FE817	Hummingbird Green
#59E817	Nebula Green
#57E964	Stoplight Go Green
#64E986	Algae Green
#5EFB6E	Jade Green
#00FF00	Green
#5FFB17	Emerald Green
#87F717	Lawn Green
#8AFB17	Chartreuse
#6AFB92	Dragon Green
#98FF98	Mint green
#B5EAAA	Green Thumb
#C3FDB8	Light Jade
#CCFB5D	Tea Green
#B1FB17	Green Yellow
#BCE954	Slime Green
#EDDA74	Goldenrod
#EDE275	Harvest Gold
#FFE87C	Sun Yellow
#FFFF00	Yellow
#FFF380	Corn Yellow
#FFFFC2	Parchment
#FFFFCC	Cream
#FFF8C6	Lemon Chiffon
#FFF8DC	Cornsilk
#F5F5DC	Beige
#FBF6D9	Blonde
#FAEBD7	AntiqueWhite
#F7E7CE	Champagne
#FFEBCD	BlanchedAlmond
#F3E5AB	Vanilla
#ECE5B6	Tan Brown
#FFE5B4	Peach
#FFDB58	Mustard
#FFD801	Rubber Ducky Yellow
#FDD017	Bright Gold
#EAC117	Golden brown
#F2BB66	Macaroni and Cheese
#FBB917	Saffron
#FBB117	Beer
#FFA62F	Cantaloupe
#E9AB17	Bee Yellow
#E2A76F	Brown Sugar
#DEB887	BurlyWood
#FFCBA4	Deep Peach
#C9BE62	Ginger Brown
#E8A317	School Bus Yellow
#EE9A4D	Sandy Brown
#C8B560	Fall Leaf Brown
#D4A017	Orange Gold
#C2B280	Sand
#C7A317	Cookie Brown
#C68E17	Caramel
#B5A642	Brass
#ADA96E	Khaki
#C19A6B	Camel brown
#CD7F32	Bronze
#C88141	Tiger Orange
#C58917	Cinnamon
#AF9B60	Bullet Shell
#AF7817	Dark Goldenrod
#B87333	Copper
#966F33	Wood
#806517	Oak Brown
#827839	Moccasin
#827B60	Army Brown
#786D5F	Sandstone
#493D26	Mocha
#483C32	Taupe
#6F4E37	Coffee
#835C3B	Brown Bear
#7F5217	Red Dirt
#7F462C	Sepia
#C47451	Orange Salmon
#C36241	Rust
#C35817	Red Fox
#C85A17	Chocolate
#CC6600	Sedona
#E56717	Papaya Orange
#E66C2C	Halloween Orange
#F87217	Pumpkin Orange
#F87431	Construction Cone Orange
#E67451	Sunrise Orange
#FF8040	Mango Orange
#F88017	Dark Orange
#FF7F50	Coral
#F88158	Basket Ball Orange
#F9966B	Light Salmon
#E78A61	Tangerine
#E18B6B	Dark Salmon
#E77471	Light Coral
#F75D59	Bean Red
#E55451	Valentine Red
#E55B3C	Shocking Orange
#FF0000	Red
#FF2400	Scarlet
#F62217	Ruby Red
#F70D1A	Ferrari Red
#F62817	Fire Engine Red
#E42217	Lava Red
#E41B17	Love Red
#DC381F	Grapefruit
#C34A2C	Chestnut Red
#C24641	Cherry Red
#C04000	Mahogany
#C11B17	Chilli Pepper
#9F000F	Cranberry
#990012	Red Wine
#8C001A	Burgundy
#954535	Chestnut
#7E3517	Blood Red
#8A4117	Sienna
#7E3817	Sangria
#800517	Firebrick
#810541	Maroon
#7D0541	Plum Pie
#7E354D	Velvet Maroon
#7D0552	Plum Velvet
#7F4E52	Rosy Finch
#7F5A58	Puce
#7F525D	Dull Purple
#B38481	Rosy Brown
#C5908E	Khaki Rose
#C48189	Pink Bow
#C48793	Lipstick Pink
#E8ADAA	Rose
#EDC9AF	Desert Sand
#FDD7E4	Pig Pink
#FCDFFF	Cotton Candy
#FFDFDD	Pink Bubblegum
#FBBBB9	Misty Rose
#FAAFBE	Pink
#FAAFBA	Light Pink
#F9A7B0	Flamingo Pink
#E7A1B0	Pink Rose
#E799A3	Pink Daisy
#E38AAE	Cadillac Pink
#F778A1	Carnation Pink
#E56E94	Blush Red
#F660AB	Hot Pink
#FC6C85	Watermelon Pink
#F6358A	Violet Red
#F52887	Deep Pink
#E45E9D	Pink Cupcake
#E4287C	Pink Lemonade
#F535AA	Neon Pink
#FF00FF	Magenta
#E3319D	Dimorphotheca Magenta
#F433FF	Bright Neon Pink
#D16587	Pale Violet Red
#C25A7C	Tulip Pink
#CA226B	Medium Violet Red
#C12869	Rogue Pink
#C12267	Burnt Pink
#C25283	Bashful Pink
#C12283	Carnation Pink
#B93B8F	Plum
#7E587E	Viola Purple
#571B7E	Purple Iris
#583759	Plum Purple
#4B0082	Indigo
#461B7E	Purple Monster
#4E387E	Purple Haze
#614051	Eggplant
#5E5A80	Grape
#6A287E	Purple Jam
#7D1B7E	Dark Orchid
#A74AC7	Purple Flower
#B048B5	Medium Orchid
#6C2DC7	Purple Amethyst
#842DCE	Dark Violet
#8D38C9	Violet
#7A5DC7	Purple Sage Bush
#7F38EC	Lovely Purple
#8E35EF	Purple
#893BFF	Aztech Purple
#8467D7	Medium Purple
#A23BEC	Jasmine Purple
#B041FF	Purple Daffodil
#C45AEC	Tyrian Purple
#9172EC	Crocus Purple
#9E7BFF	Purple Mimosa
#D462FF	Heliotrope Purple
#E238EC	Crimson
#C38EC7	Purple Dragon
#C8A2C8	Lilac
#E6A9EC	Blush Pink
#E0B0FF	Mauve
#C6AEC7	Wisteria Purple
#F9B7FF	Blossom Pink
#D2B9D3	Thistle
#E9CFEC	Periwinkle
#EBDDE2	Lavender Pinocchio
#E3E4FA	Lavender blue
#FDEEF4	Pearl
#FFF5EE	SeaShell
#FEFCFF	Milk White
#FFFFFF	White
# ''')

extractColorCode(''' #FF4848	#FF68DD	#FF62B0	#FE67EB	#E469FE	
#D568FD
#9669FE
#FF7575	#FF79E1	#FF73B9	#FE67EB	#E77AFE	
#D97BFD
#A27AFE
#FF8A8A	#FF86E3	#FF86C2	#FE8BF0	#EA8DFE	#DD88FD	#AD8BFE
#FF9797	#FF97E8	#FF97CB	#FE98F1	#ED9EFE	#E29BFD	#B89AFE
#FFA8A8	#FFACEC	#FFA8D3	#FEA9F3	#EFA9FE	#E7A9FE	#C4ABFE
#FFBBBB	#FFACEC	#FFBBDD	#FFBBF7	#F2BCFE	#EDBEFE	#D0BCFE
#FFCECE	#FFC8F2	#FFC8E3	#FFCAF9	#F5CAFF	#F0CBFE	#DDCEFF
#FFDFDF	#FFDFF8	#FFDFEF	#FFDBFB	#F9D9FF	#F4DCFE	#E6DBFF
#FFECEC	#FFEEFB	#FFECF5	#FFEEFD	#FDF2FF	#FAECFF	#F1ECFF
#FFF2F2	#FFFEFB	#FFF9FC	#FFF9FE	#FFFDFF	#FDF9FF	#FBF9FF

 
Table 2: Purple Toward Blue & Beyond (Some Tones)
"#800080"
"#872187"
"#9A03FE"
"#892EE4"
"#3923D6"
"#2966B8"
"#23819C"
"#BF00BF"
"#BC2EBC"
"#A827FE"
"#9B4EE9"
"#6755E3"
"#2F74D0"
"#2897B7"
"#DB00DB"
"#D54FD5"
"#B445FE"
"#A55FEB"
"#8678E9"
"#4985D6"
"#2FAACE"
"#F900F9"
"#DD75DD"
"#BD5CFE"
"#AE70ED"
"#9588EC"
"#6094DB"
"#44B4D5"
"#FF4AFF"	"#DD75DD"	"#C269FE"	
"#AE70ED"
"#A095EE"	"#7BA7E1"	"#57BCD9"
"#FF86FF"	"#E697E6"	"#CD85FE"	"#C79BF2"	"#B0A7F1"	"#8EB4E6"	"#7BCAE1"
"#FFA4FF"	"#EAA6EA"	"#D698FE"	"#CEA8F4"	"#BCB4F3"	"#A9C5EB"	"#8CD1E6"
"#FFBBFF"	"#EEBBEE"	"#DFB0FF"	"#DBBFF7"	"#CBC5F5"	"#BAD0EF"	"#A5DBEB"
"#FFCEFF"	"#F0C4F0"	"#E8C6FF"	"#E1CAF9"	"#D7D1F8"	"#CEDEF4"	"#B8E2EF"
"#FFDFFF"	"#F4D2F4"	"#EFD7FF"	"#EDDFFB"	"#E3E0FA"	"#E0EAF8"	"#C9EAF3"
"#FFECFF"	"#F4D2F4"	"#F9EEFF"	"#F5EEFD"	"#EFEDFC"	"#EAF1FB"	"#DBF0F7"
"#FFF9FF"	"#FDF9FD"	"#FEFDFF"	"#FEFDFF"	"#F7F5FE"	"#F8FBFE"	"#EAF7FB"

 
Table 3: Blue Tints Toward Greenish Tints
"#5757FF"
"#62A9FF"
"#62D0FF"	"#06DCFB"	"#01FCEF"	"#03EBA6"	"#01F33E"
"#6A6AFF"
"#75B4FF"
"#75D6FF"	"#24E0FB"	"#1FFEF3"	"#03F3AB"	"#0AFE47"
"#7979FF"
"#86BCFF"	"#8ADCFF"	"#3DE4FC"	"#5FFEF7"	"#33FDC0"	"#4BFE78"
"#8C8CFF"	"#99C7FF"	"#99E0FF"	"#63E9FC"	"#74FEF8"	"#62FDCE"	"#72FE95"
"#9999FF"	"#99C7FF"	"#A8E4FF"	"#75ECFD"	"#92FEF9"	"#7DFDD7"	"#8BFEA8"
"#AAAAFF"	"#A8CFFF"	"#BBEBFF"	"#8CEFFD"	"#A5FEFA"	"#8FFEDD"	"#A3FEBA"
"#BBBBFF"	"#BBDAFF"	"#CEF0FF"	"#ACF3FD"	"#B5FFFC"	"#A5FEE3"	"#B5FFC8"
"#CACAFF"	"#D0E6FF"	"#D9F3FF"	"#C0F7FE"	"#CEFFFD"	"#BEFEEB"	"#CAFFD8"
"#E1E1FF"	"#DBEBFF"	"#ECFAFF"	"#C0F7FE"	"#E1FFFE"	"#BDFFEA"	"#EAFFEF"
"#EEEEFF"	"#ECF4FF"	"#F9FDFF"	"#E6FCFF"	"#F2FFFE"	"#CFFEF0"	"#EAFFEF"
"#F9F9FF"	"#F9FCFF"	"#FDFEFF"	"#F9FEFF"	"#FDFFFF"	"#F7FFFD"	"#F9FFFB"

 
Table 4:
"#1FCB4A"	"#59955C"	"#48FB0D"	"#2DC800"	"#59DF00"	"#9D9D00"	"#B6BA18"
"#27DE55"	"#6CA870"	"#79FC4E"	"#32DF00"	"#61F200"	"#C8C800"	"#CDD11B"
"#4AE371"	"#80B584"	"#89FC63"	"#36F200"	"#66FF00"	"#DFDF00"	"#DFE32D"
"#7CEB98"	"#93BF96"	"#99FD77"	"#52FF20"	"#95FF4F"	"#FFFFAA"	"#EDEF85"
"#93EEAA"	"#A6CAA9"	"#AAFD8E"	"#6FFF44"	"#ABFF73"	"#FFFF84"	"#EEF093"
"#A4F0B7"	"#B4D1B6"	"#BAFEA3"	"#8FFF6F"	"#C0FF97"	"#FFFF99"	"#F2F4B3"
"#BDF4CB"	"#C9DECB"	"#CAFEB8"	"#A5FF8A"	"#D1FFB3"	"#FFFFB5"	"#F5F7C4"
"#D6F8DE"	"#DBEADC"	"#DDFED1"	"#B3FF99"	"#DFFFCA"	"#FFFFC8"	"#F7F9D0"
"#E3FBE9"	"#E9F1EA"	"#EAFEE2"	"#D2FFC4"	"#E8FFD9"	"#FFFFD7"	"#FAFBDF"
"#E3FBE9"	"#F3F8F4"	"#F1FEED"	"#E7FFDF"	"#F2FFEA"	"#FFFFE3"	"#FCFCE9"
"#FAFEFB"	"#FBFDFB"	"#FDFFFD"	"#F5FFF2"	"#FAFFF7"	"#FFFFFD"	"#FDFDF0"
Table 5:
"#BABA21"	"#C8B400"	"#DFA800"	"#DB9900"	"#FFB428"	"#FF9331"	"#FF800D"
"#E0E04E"	"#D9C400"	"#F9BB00"	"#EAA400"	"#FFBF48"	"#FFA04A"	"#FF9C42"
"#E6E671"	"#E6CE00"	"#FFCB2F"	"#FFB60B"	"#FFC65B"	"#FFAB60"	"#FFAC62"
"#EAEA8A"	"#F7DE00"	"#FFD34F"	"#FFBE28"	"#FFCE73"	"#FFBB7D"	"#FFBD82"
"#EEEEA2"	"#FFE920"	"#FFDD75"	"#FFC848"	"#FFD586"	"#FFC48E"	"#FFC895"
"#F1F1B1"	"#FFF06A"	"#FFE699"	"#FFD062"	"#FFDEA2"	"#FFCFA4"	"#FFCEA2"
"#F4F4BF"	"#FFF284"	"#FFECB0"	"#FFE099"	"#FFE6B5"	"#FFD9B7"	"#FFD7B3"
"#F7F7CE"	"#FFF7B7"	"#FFF1C6"	"#FFEAB7"	"#FFEAC4"	"#FFE1C6"	"#FFE2C8"
"#F9F9DD"	"#FFF9CE"	"#FFF5D7"	"#FFF2D2"	"#FFF2D9"	"#FFEBD9"	"#FFE6D0"
"#FBFBE8"	"#FFFBDF"	"#FFFAEA"	"#FFF9EA"	"#FFF7E6"	"#FFF4EA"	"#FFF1E6"
"#FEFEFA"	"#FFFEF7"	"#FFFDF7"	"#FFFDF9"	"#FFFDF9"	"#FFFEFD"	"#FFF9F4"

 
Table 6:
"#D1D17A"	"#C0A545"	
"#C27E3A"
"#C47557"
"#B05F3C"
"#C17753"
"#B96F6F"
"#D7D78A"	"#CEB86C"	"#C98A4B"	
"#CB876D"
"#C06A45"
"#C98767"
"#C48484"
"#DBDB97"	"#D6C485"	"#D19C67"	"#D29680"	
"#C87C5B"
"#D0977B"
"#C88E8E"
"#E1E1A8"	"#DECF9C"	"#DAAF85"	"#DAA794"	"#CF8D72"	"#DAAC96"	"#D1A0A0"
"#E9E9BE"	"#E3D6AA"	"#DDB791"	"#DFB4A4"	"#D69E87"	"#E0BBA9"	"#D7ACAC"
"#EEEECE"	"#EADFBF"	"#E4C6A7"	"#E6C5B9"	"#DEB19E"	"#E8CCBF"	"#DDB9B9"
"#E9E9C0"	"#EDE4C9"	"#E9D0B6"	"#EBD0C7"	"#E4C0B1"	"#ECD5CA"	"#E6CCCC"
"#EEEECE"	"#EFE7CF"	"#EEDCC8"	"#F0DCD5"	"#EACDC1"	"#F0DDD5"	"#ECD9D9"
"#F1F1D6"	"#F5EFE0"	"#F2E4D5"	"#F5E7E2"	"#F0DDD5"	"#F5E8E2"	"#F3E7E7"
"#F5F5E2"	"#F9F5EC"	"#F9F3EC"	"#F9EFEC"	"#F5E8E2"	"#FAF2EF"	"#F8F1F1"
"#FDFDF9"	"#FDFCF9"	"#FCF9F5"	"#FDFAF9"	"#FDFAF9"	"#FCF7F5"	"#FDFBFB"

 
Table 7:
"#F70000"
"#B9264F"
"#990099"
"#74138C"
"#0000CE"
"#1F88A7"
"#4A9586"
"#FF2626"	
"#D73E68"
"#B300B3"
"#8D18AB"
"#5B5BFF"
"#25A0C5"
"#5EAE9E"
"#FF5353"	"#DD597D"	"#CA00CA"	
"#A41CC6"
"#7373FF"
"#29AFD6"	"#74BAAC"
"#FF7373"	"#E37795"	"#D900D9"	"#BA21E0"	"#8282FF"	"#4FBDDD"	"#8DC7BB"
"#FF8E8E"	"#E994AB"	"#FF2DFF"	"#CB59E8"	"#9191FF"	"#67C7E2"	"#A5D3CA"
"#FFA4A4"	"#EDA9BC"	"#F206FF"	"#CB59E8"	"#A8A8FF"	"#8ED6EA"	"#C0E0DA"
"#FFB5B5"	"#F0B9C8"	"#FF7DFF"	"#D881ED"	"#B7B7FF"	"#A6DEEE"	"#CFE7E2"
"#FFC8C8"	"#F4CAD6"	"#FFA8FF"	"#EFCDF8"	"#C6C6FF"	"#C0E7F3"	"#DCEDEA"
"#FFEAEA"	"#F8DAE2"	"#FFC4FF"	"#EFCDF8"	"#DBDBFF"	"#D8F0F8"	"#E7F3F1"
"#FFEAEA"	"#FAE7EC"	"#FFE3FF"	"#F8E9FC"	"#EEEEFF"	"#EFF9FC"	"#F2F9F8"
"#FFFDFD"	"#FEFAFB"	"#FFFDFF"	"#FFFFFF"	"#FDFDFF"	"#FAFDFE"	"#F7FBFA"
''')