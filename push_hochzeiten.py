#!/usr/bin/env python3
"""Push alle 178 Hochzeiten-Songs aus 9 Playlists nach Firebase."""

import json, urllib.request

FIREBASE_URL = 'https://now-playing-75593-default-rtdb.europe-west1.firebasedatabase.app/hochzeiten.json'

DATA = {
  "playlists": [
    {
      "name": "NightStart — Light Start",
      "tracks": [
        {"title": "Rude Boy - Paul Mond Remix (Clean)", "artist": "Rihanna", "bpm": 97, "key": "2A"},
        {"title": "I Don't Care (Intro)", "artist": "Ed Sheeran & Justin Bieber", "bpm": 102, "key": "B"},
        {"title": "One Dance - King Most Mrs. Officer Remix", "artist": "Drake ft. Wizkid & Kyla", "bpm": 102, "key": "3A"},
        {"title": "Tequila - Stavros Martina & Kevin D Remix", "artist": "The Champs", "bpm": 102, "key": "4A"},
        {"title": "RITMO (Bad Boys For Life)", "artist": "Black Eyed Peas J Balvin", "bpm": 105, "key": "5A"},
        {"title": "Shake It Off - Stavros Martina & Kevin D Remix", "artist": "Taylor Swift", "bpm": 95, "key": "6A"},
        {"title": "Dilemma - Madsko & Dan Bravo Remix (Dirty)", "artist": "Nelly ft. Kelly Rowland", "bpm": 108, "key": "7A"},
        {"title": "Just The Way You Are - Stavros Martina & Kevin D Remix", "artist": "Bruno Mars", "bpm": 109, "key": "7B"},
        {"title": "Can't Feel My Face - Soltice, Naken & Batikboy Remix", "artist": "The Weeknd", "bpm": 113, "key": "8A"},
        {"title": "Hey Mama - Lincoln Baio Lighter Edit", "artist": "David Guetta ft. Nicki Minaj, Bebe Rexha & Afrojack", "bpm": 110, "key": "9A"},
        {"title": "Alejandro - Joan Qveralt Remix", "artist": "Lady Gaga", "bpm": 115, "key": "10A"},
        {"title": "Replay - Merco Remix", "artist": "Iyaz", "bpm": 104, "key": "11B"},
        {"title": "Work It - Tall Boys Lovin On Me Edit (Intro - Clean)", "artist": "Missy Elliot", "bpm": 105, "key": "12A"},
        {"title": "Die With A Smile - Tall Boys Remix", "artist": "Lady Gaga & Bruno Mars", "bpm": 105, "key": "12A"},
        {"title": "Shape Of You - Dan Bravo Remix", "artist": "Ed Sheeran", "bpm": 110, "key": "12A"},
        {"title": "Anti-Hero - Roosevelt Remix", "artist": "Taylor Swift", "bpm": 111, "key": "12A"},
      ]
    },
    {
      "name": "NightStart — Mid",
      "tracks": [
        {"title": "Stupid Love (DJcity Intro)", "artist": "Lady Gaga", "bpm": 118, "key": "5B"},
        {"title": "Ain't Nobody (Loves Me Better)", "artist": "Felix Jaehn & Jasmine Thompson", "bpm": 118, "key": "7A"},
        {"title": "NUEVAYoL - Da Phonk Club Edit (Dirty)", "artist": "Bad Bunny", "bpm": 118, "key": "8A"},
        {"title": "Crazy What Love Can Do - Tommy Glasses Remix", "artist": "David Guetta, Becky Hill & Ella Henderson", "bpm": 120, "key": "9A"},
        {"title": "Ride Wit Me - DJcity vs Richastic 102-118 Throwback Transition (Dirty)", "artist": "Nelly", "bpm": 118, "key": "9A"},
        {"title": "Don't Be Shy", "artist": "Tiësto & KAROL G", "bpm": 120, "key": "10A"},
        {"title": "Love Again (Imanbek Remix)", "artist": "Dua Lipa", "bpm": 120, "key": "11A"},
        {"title": "Talk Dirty - Richastic Remix (Clean)", "artist": "Jason Derulo ft. 2 Chainz", "bpm": 118, "key": "11A"},
        {"title": "Messy - Les Bisous Remix (Intro - Dirty)", "artist": "Lola Young", "bpm": 120, "key": "11A"},
        {"title": "My Humps - Anthem Kingz Bongos Edit (Dirty)", "artist": "Black Eyed Peas ft. Pitbull", "bpm": 122, "key": "12A"},
      ]
    },
    {
      "name": "NightStart — Warm",
      "tracks": [
        {"title": "yes, and? (DJcity Intro - Dirty)", "artist": "Ariana Grande & Mariah Carey", "bpm": 119, "key": "4A"},
        {"title": "Dance Monkey - Groove Safari Remix", "artist": "Tones & I", "bpm": 120, "key": "4A"},
        {"title": "Addicted", "artist": "ZERB & The Chainsmokers ft. Ink", "bpm": 120, "key": "4A"},
        {"title": "Blinding Lights - Chunky Dip & Jesse James More Than You Know Edit", "artist": "The Weeknd", "bpm": 123, "key": "4A"},
        {"title": "Telephone", "artist": "Lady Gaga & Beyoncé", "bpm": 122, "key": "4A"},
        {"title": "Treasure - DJ Beatzilla & Bossa Nova Crazy Edit", "artist": "Bruno Mars", "bpm": 121, "key": "5A"},
        {"title": "Take My Breath - Tommy Glasses Remix", "artist": "The Weeknd", "bpm": 121, "key": "5A"},
        {"title": "Running Up That Hill (A Deal With God) - PATCH SAFARI Remix", "artist": "Kate Bush", "bpm": 121, "key": "5A"},
        {"title": "I Like To Move It (feat. The Mad Stuntman) [Radio Mix]", "artist": "Reel 2 Real & The Mad Stuntman", "bpm": 123, "key": "5A"},
        {"title": "BAILALO - Afro Cumbia DJ Tool", "artist": "Eddie Boy", "bpm": 120, "key": "6A"},
        {"title": "Blurred Lines - Stavros Martina & Kevin D Remix (Dirty)", "artist": "Robin Thicke ft. Pharrell", "bpm": 120, "key": "6A"},
        {"title": "Mwaki", "artist": "Zerb & Sofiya Nzau", "bpm": 120, "key": "6A"},
        {"title": "the boy is mine - DJ Robbie Lewis Remix", "artist": "Ariana Grande", "bpm": 120, "key": "6A"},
        {"title": "Baianá", "artist": "Bakermat", "bpm": 122, "key": "7A"},
        {"title": "Un Gatito Me Llamó (Intro - Dirty)", "artist": "KAROL G", "bpm": 119, "key": "7A"},
      ]
    },
    {
      "name": "NightStart — Hot",
      "tracks": [
        {"title": "Heartbreak Anthem", "artist": "Galantis, David Guetta & Little Mix", "bpm": 124, "key": "3B"},
        {"title": "Sugar - Colin Jay Remix (Intro - Dirty)", "artist": "Maroon 5", "bpm": 124, "key": "3B"},
        {"title": "Rhythm Of The Night - Optical Disco Remix", "artist": "Corona", "bpm": 124, "key": "4A"},
        {"title": "Baby - Robin Roij Remix", "artist": "Justin Bieber", "bpm": 125, "key": "5B"},
        {"title": "Never Going Home", "artist": "Kungs", "bpm": 122, "key": "6A"},
        {"title": "Houdini - Effendi Remix", "artist": "Dua Lipa", "bpm": 123, "key": "7A"},
        {"title": "Like A Prayer - DJ Dark Remix", "artist": "Madonna", "bpm": 125, "key": "7A"},
        {"title": "Move Your Body", "artist": "Öwnboss & SEVEK", "bpm": 125, "key": "7A"},
        {"title": "Danza Kuduro - Tiësto Remix", "artist": "Don Omar & Lucenzo", "bpm": 125, "key": "8A"},
        {"title": "Show Me Love - Marlon Galvao Remix", "artist": "Robin S.", "bpm": 125, "key": "8A"},
        {"title": "Right Round - Anthem Kingz I Wish Edit", "artist": "Flo Rida ft. Ke$ha", "bpm": 124, "key": "8A"},
        {"title": "One Kiss", "artist": "Calvin Harris & Dua Lipa", "bpm": 124, "key": "8A"},
        {"title": "Umbrella - MIRAMAR Remix", "artist": "Rihanna", "bpm": 122, "key": "8A"},
        {"title": "Safe And Sound - De Soffer Remix", "artist": "Capital Cities", "bpm": 122, "key": "8B"},
        {"title": "Mi Gente - ATCG Remix", "artist": "J Balvin & Willy William", "bpm": 122, "key": "9A"},
        {"title": "Animals - Joan Qveralt Remix", "artist": "Maroon 5", "bpm": 120, "key": "9A"},
        {"title": "How Deep Is Your Love", "artist": "Calvin Harris & Disciples", "bpm": 122, "key": "9A"},
        {"title": "Diamonds - DJ GALIN Remix", "artist": "Rihanna", "bpm": 122, "key": "10A"},
        {"title": "One More Time - Capital People Remix", "artist": "Daft Punk", "bpm": 123, "key": "9A"},
        {"title": "Closer - Dazz & Calvo Remix", "artist": "Ne-Yo", "bpm": 123, "key": "9A"},
      ]
    },
    {
      "name": "NightStart — Freak",
      "tracks": [
        {"title": "WHERE IS MY HUSBAND! - Mark Anthony Shivers Edit", "artist": "RAYE", "bpm": 125, "key": "4A"},
        {"title": "Viva La Vida - CHALANT Remix", "artist": "Coldplay", "bpm": 130, "key": "4A"},
        {"title": "Rock This Party (Everybody Dance Now) - MIKIS & ZING Remix", "artist": "Bob Sinclar ft. Big Ali", "bpm": 126, "key": "3A"},
        {"title": "We Found Love", "artist": "Rihanna & Calvin Harris", "bpm": 128, "key": "2B"},
        {"title": "Heads Will Roll - PBH & JACK Remix", "artist": "Yeah Yeah Yeahs", "bpm": 126, "key": "1A"},
        {"title": "Right Round - Gallardo Remix", "artist": "Flo Rida ft. Ke$ha", "bpm": 126, "key": "1A"},
        {"title": "I Love It - Anthem Kingz Heads Will Roll Edit (Dirty)", "artist": "Icona Pop ft. Charli XCX", "bpm": 126, "key": "1A"},
        {"title": "I Love It - Mark Anthony Phatt Bass Edit (Dirty)", "artist": "Icona Pop", "bpm": 128, "key": "1A"},
        {"title": "I Love It - MARROW LET'S GO Slam Intro Edit (Dirty)", "artist": "Icona Pop ft. Charli XCX", "bpm": 129, "key": "1A"},
        {"title": "I Love It (feat. Charli XCX)", "artist": "Icona Pop & Charli XCX", "bpm": 126, "key": "2B"},
        {"title": "Y.M.C.A. - DJ Getdown Remix", "artist": "Village People", "bpm": 126, "key": "2A"},
        {"title": "We Found Love - Colin Jay Remix (Clean)", "artist": "Rihanna ft. Calvin Harris", "bpm": 128, "key": "2B"},
        {"title": "Poker Face - CHALANT Remix", "artist": "Lady Gaga", "bpm": 130, "key": "2A"},
        {"title": "Just Dance - Freejak Remix", "artist": "Lady Gaga ft. Colby O'Donis", "bpm": 128, "key": "1A"},
        {"title": "Bulletproof", "artist": "La Roux, Gamper & Dadoni", "bpm": 126, "key": "2A"},
        {"title": "Bulletproof - FÄT TONY & Medun Remix", "artist": "La Roux", "bpm": 128, "key": "2A"},
        {"title": "Hit The Road Jack - Pizzata & Klein Remix", "artist": "Ray Charles", "bpm": 126, "key": "1A"},
        {"title": "Low - SANDERSVILLE Remix", "artist": "Flo Rida ft. T-Pain", "bpm": 128, "key": "2A"},
        {"title": "Play Hard - Gallardo Remix", "artist": "David Guetta ft. Ne-Yo & Akon", "bpm": 126, "key": "1A"},
        {"title": "Let Me Blow Ya Mind - Lincoln Baio Beggin' Edit (Dirty)", "artist": "Eve ft. Gwen Stefani", "bpm": 126, "key": "1A"},
        {"title": "Barbie Girl - Anthem Kingz Party Starter", "artist": "Aqua", "bpm": 126, "key": "12A"},
        {"title": "Levels - RICHIE ROZEX Remix", "artist": "Avicii", "bpm": 128, "key": "12A"},
        {"title": "Don't Stop The Music - Spryte Remix", "artist": "Rihanna", "bpm": 125, "key": "11A"},
        {"title": "Pompeii - J Bruus Remix", "artist": "Bastille", "bpm": 130, "key": "11B"},
        {"title": "Fresh - Kide & Giorgio Dala Remix", "artist": "Kool & The Gang", "bpm": 130, "key": "10A"},
        {"title": "Who's That Chick? - Joan Qveralt Remix", "artist": "David Guetta ft. Rihanna", "bpm": 128, "key": "10B"},
        {"title": "LoveGame - Pegassi Remix", "artist": "Lady Gaga", "bpm": 125, "key": "10A"},
        {"title": "Hot In Herre - Andrew Lux Remix", "artist": "Nelly", "bpm": 125, "key": "9A"},
        {"title": "Jump Around - MOONLGHT Remix (Intro - Clean)", "artist": "House Of Pain", "bpm": 128, "key": "9A"},
        {"title": "Where You Are", "artist": "John Summit & HAYLA", "bpm": 125, "key": "8A"},
        {"title": "Señorita - CAVALLI Afro House Remix", "artist": "Shawn Mendes ft. Camila Cabello", "bpm": 128, "key": "8A"},
        {"title": "Gimme! Gimme! Gimme! (A Man After Midnight) - HAWK Remix", "artist": "ABBA", "bpm": 126, "key": "7A"},
        {"title": "Freed From Desire - 5HOURS & Martina Minelli Remix", "artist": "Gala", "bpm": 126, "key": "7A"},
        {"title": "I Got You (I Feel Good) - Marijn Jansen Remix", "artist": "James Brown & The Famous Flames", "bpm": 128, "key": "7A"},
        {"title": "High Hopes (Don Diablo Remix)", "artist": "Panic! At The Disco", "bpm": 125, "key": "7A"},
        {"title": "Sexy And I Know It", "artist": "LMFAO", "bpm": 130, "key": "6A"},
        {"title": "Rainfall (Praise You)", "artist": "Tom Santa", "bpm": 128, "key": "6A"},
        {"title": "Break Free - Gael Borrego Remix", "artist": "Ariana Grande", "bpm": 130, "key": "6A"},
        {"title": "Paparazzi - Waltry Remix", "artist": "Lady Gaga", "bpm": 128, "key": "5A"},
        {"title": "Treasure - Mr. Sherman Remix (Clean)", "artist": "Bruno Mars", "bpm": 126, "key": "5A"},
        {"title": "Hit 'Em Up Style (Oops!)", "artist": "Essel & James Hurr", "bpm": 125, "key": "4A"},
        {"title": "Titanium - DJ Smerk Don't Wake Me Up Edit", "artist": "David Guetta ft. Sia", "bpm": 130, "key": "5A"},
        {"title": "When I Grow Up - Deux Twins Remix", "artist": "The Pussycat Dolls", "bpm": 129, "key": "4A"},
        {"title": "Watch Out For This (Bumaye) - Alex Guesta Mas Gasolina Edit", "artist": "Major Lazer ft. Busy Signal, The Flexican & FS Green", "bpm": 126, "key": "4A"},
        {"title": "Memories - Freejak Remix (Intro - Dirty)", "artist": "David Guetta ft. Kid Cudi", "bpm": 130, "key": "3A"},
      ]
    },
    {
      "name": "NightStart — NightyJam",
      "tracks": [
        {"title": "No Broke Boys (Intro - Dirty)", "artist": "Disco Lines & Tinashe", "bpm": 131, "key": "1A"},
        {"title": "I Knew You Were Trouble - Pascal West Remix", "artist": "Taylor Swift", "bpm": 132, "key": "2A"},
        {"title": "Dark Horse", "artist": "Katy Perry & Juicy J", "bpm": 132, "key": "3A"},
        {"title": "Maneater - Nala Remix", "artist": "Nelly Furtado", "bpm": 133, "key": "3A"},
        {"title": "Break It Off (feat. Rihanna)", "artist": "Sean Paul & Rihanna", "bpm": 134, "key": "3A"},
        {"title": "Don't Phunk With My Heart - WOODERSON Remix", "artist": "Black Eyed Peas", "bpm": 132, "key": "4A"},
        {"title": "Party Rock Anthem - YuB Remix", "artist": "LMFAO", "bpm": 130, "key": "4A"},
        {"title": "Hollaback Girl - JUDO Remix (Dirty)", "artist": "Gwen Stefani", "bpm": 130, "key": "4A"},
        {"title": "Crank That (Soulja Boy) - EVERLAKE & Ruse Remix", "artist": "Soulja Boy Tell 'Em", "bpm": 130, "key": "5A"},
        {"title": "Das geht ab (wir feiern die ganze Nacht)", "artist": "Die Atzen", "bpm": 131, "key": "5A"},
        {"title": "Alles neu", "artist": "Peter Fox", "bpm": 134, "key": "5B"},
        {"title": "What Is Love - BVRNOUT Remix", "artist": "Haddaway", "bpm": 132, "key": "6A"},
        {"title": "bad guy", "artist": "Billie Eilish", "bpm": 135, "key": "6A"},
        {"title": "Hotline Bling - Tall Boys Remix (Intro)", "artist": "Drake", "bpm": 135, "key": "7A"},
        {"title": "Gimme! Gimme! Gimme! (A Man After Midnight) - Spryte Give It To Me Good Edit", "artist": "ABBA", "bpm": 132, "key": "7A"},
        {"title": "Anxiety - Sir Marcus & MarkCutz Remix (Dirty)", "artist": "Doechii", "bpm": 130, "key": "7A"},
        {"title": "Beauty And A Beat - Martial Simon & Zillionaire Remix", "artist": "Justin Bieber ft. Nicki Minaj", "bpm": 132, "key": "8B"},
        {"title": "Don't You Worry Child - Destivine & TEAM PEACH Remix", "artist": "Swedish House Mafia ft. John Martin", "bpm": 134, "key": "10A"},
        {"title": "If I Lose Myself - Daevo & Jost Remix", "artist": "OneRepublic", "bpm": 132, "key": "10B"},
        {"title": "Immer Sommer", "artist": "Tropikel Ltd & futurebae", "bpm": 135, "key": "11A"},
        {"title": "Disco Pogo", "artist": "Die Atzen", "bpm": 132, "key": "12A"},
        {"title": "Breakin' Dishes - Kelland Remix", "artist": "Rihanna", "bpm": 134, "key": "3A"},
      ]
    },
    {
      "name": "Peak — Banger b. 125 BPM",
      "tracks": [
        {"title": "EoO - MarkCutz Hype Intro (Dirty)", "artist": "Bad Bunny", "bpm": 102, "key": "1A"},
        {"title": "In Da Club - NAO Remix (Dirty)", "artist": "50 Cent", "bpm": 125, "key": "1A"},
        {"title": "Thrift Shop - Spracto Remix (Dirty)", "artist": "Macklemore & Ryan Lewis ft. Wanz", "bpm": 124, "key": "1A"},
        {"title": "We Dem Boyz - Jablonski Calabria Edit (Clean)", "artist": "Wiz Khalifa", "bpm": 125, "key": "2A"},
        {"title": "Who's That Girl? - Richastic Remix (Intro)", "artist": "Eve", "bpm": 125, "key": "3A"},
        {"title": "We No Speak Americano - 10th Anniversary Edit", "artist": "Yolanda Be Cool & DCUP", "bpm": 125, "key": "3A"},
        {"title": "Titanium - Jablonski Tantalizing Edit", "artist": "David Guetta ft. Sia", "bpm": 123, "key": "5A"},
        {"title": "Without Me - Rogerson Remix (Clean)", "artist": "Eminem", "bpm": 125, "key": "6A"},
        {"title": "The Rhythm", "artist": "Don Diablo", "bpm": 124, "key": "9A"},
        {"title": "Sweet Memories", "artist": "Cid & Kaskade", "bpm": 125, "key": "9A"},
      ]
    },
    {
      "name": "Peak — Banger b. 150 BPM",
      "tracks": [
        {"title": "I Like It - Dillon Francis Remix (Intro - Dirty)", "artist": "Cardi B ft. Bad Bunny & J Balvin", "bpm": 150, "key": "4A"},
        {"title": "Losing It - Henry Himself Remix (Clean)", "artist": "FISHER", "bpm": 132, "key": "6A"},
        {"title": "Losing It - CHALANT & DEDRO Remix", "artist": "FISHER", "bpm": 128, "key": "6A"},
        {"title": "What Is Love - MNYKR Remix", "artist": "Haddaway", "bpm": 130, "key": "6A"},
        {"title": "Where Is The Love? - DJ Sanders Remix", "artist": "Black Eyed Peas", "bpm": 130, "key": "7A"},
        {"title": "Jamaican (Bam Bam) - DJ Mag Guaracha Remix", "artist": "HUGEL & SOLTO (FR)", "bpm": 128, "key": "9A"},
        {"title": "Freaks - Joan Qveralt Remix", "artist": "Timmy Trumpet & Savage", "bpm": 126, "key": "10A"},
        {"title": "LET'S GO - Rob DVS Classic House Intro (Dirty)", "artist": "Jaden Bojsen & Sami Brielle", "bpm": 130, "key": "1A"},
        {"title": "LET'S GO - MFresh Hype Intro (Dirty)", "artist": "Jaden Bojsen & Sami Brielle", "bpm": 129, "key": "1A"},
        {"title": "LET'S GO - VINCCI Remix (Dirty)", "artist": "Jaden Bojsen & Sami Brielle", "bpm": 128, "key": "1A"},
        {"title": "LET'S GO (Dirty)", "artist": "Jaden Bojsen & Sami Brielle", "bpm": 128, "key": "1A"},
        {"title": "LET'S GO - MarkCutz Hype Edit (Clean)", "artist": "Jaden Bojsen & Sami Brielle", "bpm": 130, "key": "1A"},
        {"title": "It's That Time - FISHER Remix", "artist": "Marlon Hoffstadt & FISHER", "bpm": 130, "key": "4A"},
        {"title": "leavemealone - SUBSHIFT Remix", "artist": "Fred again.. & Baby Keem", "bpm": 128, "key": "8A"},
        {"title": "leavemealone (DJcity Intro - Dirty)", "artist": "Fred again.. & Baby Keem", "bpm": 174, "key": "7A"},
      ]
    },
    {
      "name": "NightStart — HighFly",
      "tracks": [
        {"title": "Sarà Perché Ti Amo (Stereoact Remix)", "artist": "DJ Redblack & Stereoact", "bpm": 138, "key": "12B"},
        {"title": "Wildberry Lillet (Rave Remix by twocolors)", "artist": "Nina Chuba", "bpm": 135, "key": "11A"},
        {"title": "Take On Me - FÄT TONY Remix", "artist": "a-ha", "bpm": 135, "key": "11B"},
        {"title": "Meet Her At The Love Parade - Polar Youth Remix", "artist": "Da Hool", "bpm": 137, "key": "10B"},
        {"title": "Friesenjung - PRIDE & PARKER Remix", "artist": "Ski Aggu, Joost & Otto Waalkes", "bpm": 140, "key": "10A"},
        {"title": "Changed the Way You Kissed Me", "artist": "player1", "bpm": 140, "key": "9A"},
        {"title": "Ein Affe und ein Pferd", "artist": "K.I.Z", "bpm": 138, "key": "8A"},
        {"title": "Shiver - 21SWINGS & GABEREAL Remix", "artist": "John Summit & Hayla", "bpm": 140, "key": "9A"},
        {"title": "The Power of Love II [edit]", "artist": "Love Regenerator & Calvin Harris", "bpm": 136, "key": "8A"},
        {"title": "Axel F - Dibs & MGM Nite Mode Edit (Dirty)", "artist": "Crazy Frog", "bpm": 140, "key": "7A"},
        {"title": "Vois sur ton chemin (Techno Mix)", "artist": "Bennett", "bpm": 138, "key": "7A"},
        {"title": "How Much Is The Fish?", "artist": "Scooter", "bpm": 140, "key": "7A"},
        {"title": "BIER", "artist": "Drunken Masters, Maxim K.I.Z", "bpm": 140, "key": "7A"},
        {"title": "When We Were Young (The Logical Song)", "artist": "David Guetta & Kim Petras", "bpm": 140, "key": "5B"},
        {"title": "APT. - Da Phonk & Funky J Shatta Remix (Intro)", "artist": "Rosé & Bruno Mars", "bpm": 180, "key": "6A"},
        {"title": "APT. (DJcity Intro)", "artist": "Rosé & Bruno Mars", "bpm": 149, "key": "5B"},
        {"title": "Dernière danse (Techno Mix)", "artist": "Indila & Bennett", "bpm": 140, "key": "5A"},
        {"title": "Baller (Intro)", "artist": "Abor & Tynna", "bpm": 138, "key": "5A"},
        {"title": "Sie Liebt Techno (Intro)", "artist": "Romero", "bpm": 140, "key": "4A"},
        {"title": "Hey DJ - Joel Corry VIP Mix", "artist": "Joel Corry", "bpm": 140, "key": "4A"},
        {"title": "Temperature - Denero Remix", "artist": "Sean Paul", "bpm": 136, "key": "3A"},
        {"title": "Harlem Shake", "artist": "Baauer", "bpm": 140, "key": "3A"},
        {"title": "Believe - Deux Twins Remix", "artist": "Cher", "bpm": 137, "key": "2A"},
        {"title": "Right Now (Na Na Na) - Sandersville Remix", "artist": "Akon", "bpm": 138, "key": "1A"},
        {"title": "Dorfkinder", "artist": "Finnel", "bpm": 140, "key": "1A"},
      ]
    },
  ]
}

# Sortiere Tracks jeder Playlist nach BPM
for p in DATA["playlists"]:
    p["tracks"].sort(key=lambda t: t["bpm"])

# Zähle Songs zur Verifikation
total = sum(len(p["tracks"]) for p in DATA["playlists"])
print(f"Songs gesamt: {total} (erwartet: 178)")
for p in DATA["playlists"]:
    print(f"  {p['name']}: {len(p['tracks'])} Songs")

print("\nPushe nach Firebase...")
req = urllib.request.Request(
    FIREBASE_URL,
    data=json.dumps(DATA, ensure_ascii=False).encode(),
    method='PUT',
    headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'},
)
urllib.request.urlopen(req, timeout=15)
print("Firebase: OK ✓")
print(f"Pfad: hochzeiten/playlists/")
