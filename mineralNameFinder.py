# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 00:40:08 2021

@author: ankit kumar
"""


import tkinter as tk
from tkinter import messagebox


def extract_mineralDetails():
    val = text.get()
    res = [i for i in spectra_names if val in i]
    if(len(res) > 0):
        dataArray =  res[0].split(' ')
        fileName.set(dataArray.pop(0))
        mineralName.set(' '.join(dataArray))
        
    else:
        fileName.set('')
        mineralName.set('')
        
def copyFileName():
    master.clipboard_clear()
    master.clipboard_append(fileName.get())
    
def copyMineralDetails():
    master.clipboard_clear()
    master.clipboard_append(mineralName.get())
    


spectra_names = ["a-alunit.spc Ammonioalunite NMNH145596", "a-chlori.spc Ammonium_Chloride GDS77", "a-illite.spc Ammonio-Illite/Smec GDS87", "a-jarosi.spc Ammonio-jarosite SCR-NHJ", "a-smecti.spc Ammonio-Smectite GDS86", "acmite.spc Acmite NMNH133746", "actinol1.spc Actinolite HS116.3B", "actinol2.spc Actinolite HS22.3B", "actinol3.spc Actinolite HS315.4B", "actinol4.spc Actinolite NMNH80714", "actinol5.spc Actinolite NMNHR16485", "adularia.spc Adularia GDS57 Orthoclase", "albite1.spc Albite GDS30 74-250um fr", "albite2.spc Albite HS324.3B", "albite3.spc Albite HS66.3B", "allanite.spc Allanite HS293.3B", "almand1.spc Almandine HS114.3B", "almand2.spc Almandine WS475", "almand3.spc Almandine WS476", "almand4.spc Almandine WS477", "almand5.spc Almandine WS478", "almand6.spc Almandine WS479", "alunite1.spc Alunite GDS84 Na03", "alunite2.spc Alunite GDS83 Na63", "alunite3.spc Alunite GDS82 Na82", "alunite4.spc Alunite AL706 Na", "alunite5.spc Alunite HS295.3B", "alunite6.spc Alunite SUSTDA-20", "amphibol.spc Amphibole NMNH78662", "analcime.spc Analcime GDS1", "andalusi.spc Andalusite NMNHR17898", "andesine.spc Andesine HS142.3B", "andradi1.spc Andradite GDS12", "andradi2.spc Andradite HS111.3B", "andradi3.spc Andradite NMNH113829", "andradi4.spc Andradite WS487", "andradi5.spc Andradite WS488", "anhydrit.spc Anhydrite GDS42 <250um", "annite1.spc Annite WS660", "annite2.spc Annite WS661", "anorthi1.spc Anorthite GDS28 Synth.<74", "anorthi2.spc Anorthite HS201.3B", "anorthi3.spc Anorthite HS349.3B", "anthophi.spc Anthophyllite HS286.3B", "antigor1.spc Antigorite NMNH96917 >250", "antigor2.spc Antigorite NMNH96917 165u", "antigor3.spc Antigorite NMNH96917 120u", "antigor4.spc Antigorite NMNH96917 70um", "antigor5.spc Antigorite NMNH96917 32um", "antigor6.spc Antigorite NMNH96917 <30u", "antigor7.spc Antigorite NMNH17958", "arsenopy.spc Arsenopyrite HS262.3B", "augite1.spc Augite NMNH120049", "augite2.spc Augite WS588", "augite3.spc Augite WS592", "axinite.spc Axinite HS34.3B", "azurite.spc Azurite WS316", "barite.spc Barite HS79.3B", "bassanit.spc Bassanite GDS145 (syn)", "beryl1.spc Beryl GDS9 <150um gs", "beryl2.spc Beryl HS180.3B", "biotite.spc Biotite HS28.3B", "bloedite.spc Bloedite GDS147", "bronzite.spc Bronzite HS9.3B", "brookite.spc Brookite HS443.2B", "brucite.spc Brucite HS247.3B", "budding1.spc Buddingtonite GDS85 D-206", "budding2.spc Buddingtonite NHB2301", "butlerit.spc Butlerite GDS25", "bytownit.spc Bytownite HS106.3B", "c-black.spc Carbon_Black GDS68 sm.ap.", "calcite1.spc Calcite WS272", "calcite2.spc Calcite HS48.3B", "calcite3.spc Calcite CO2004", "carnall1.spc Carnallite NMNH98011", "carnall2.spc Carnallite HS430.3B", "cassiter.spc Cassiterite HS279.3B", "cchlore1.spc Clinochlore NMNH83369", "cchlore2.spc Clinochlore_Fe GDS157", "cchlore3.spc Clinochlore GDS158 Flagst", "cchlore4.spc Clinochlore GDS159", "cchlore5.spc Clinochlore_Fe SC-CCa-1.a", "cchlore6.spc Clinochlore_Fe SC-CCa-1.b", "cchlore7.spc Clinochlore_Fe SC-CCa-1.c", "celestit.spc Celestite HS251.3B", "celsian.spc Celsian HS200.3B", "chabazit.spc Chabazite HS193.3B", "chalcedo.spc Chalcedony CU91-6A", "chalpy1.spc Chalcopyrite HS431.3B", "chalpy2.spc Chalcopyrite S26-36", "chert.spc Chert ANP90-6D (White)", "chlorapa.spc Chlorapatite WS423", "chlorit1.spc Chlorite HS179.3B", "chlorit2.spc Chlorite SMR-13.a 104-150", "chlorit3.spc Chlorite SMR-13.b 60-104u", "chlorit4.spc Chlorite SMR-13.c 45-60um", "chlorit5.spc Chlorite SMR-13.d 30-45um", "chlorit6.spc Chlorite SMR-13.e <30um", "chromite.spc Chromite HS281.3B", "chrysoco.spc Chrysocolla HS297.3B", "chrysoti.spc Chrysotile HS323.1B", "cinnabar.spc Cinnabar HS133.3B", "clintoni.spc Clintonite NMNH126553", "cobaltit.spc Cobaltite HS264.3B", "colemani.spc Colemanite GDS143", "cookeit1.spc Cookeite CAr-1.a 104-150u", "cookeit2.spc Cookeite CAr-1.b 60-104um", "cookeit3.spc Cookeite CAr-1.c <30um", "copiapit.spc Copiapite GDS21", "coquimbi.spc Coquimbite GDS22", "cordieri.spc Cordierite HS346.3B", "corrensi.spc Corrensite CorWa-1", "corundum.spc Corundum HS283.3B", "covellit.spc Covellite HS477.2B", "cptilol1.spc Clinoptilolite GDS2", "cptilol2.spc Clinoptilolite GDS152", "cronsted.spc Cronstedtite M3542", "cummingt.spc Cummingtonite HS294.3B", "cuprite.spc Cuprite HS127.3B", "czoisite.spc Clinozoisite HS299.2B", "datolit1.spc Datolite HS442.3B", "datolit2.spc Datolite SU51399", "desertv1.spc Desert_Varnish GDS141", "desertv2.spc Desert_Varnish GDS78A Rhy", "desertv3.spc Desert_Varnish ANP90-14", "diaspore.spc Diaspore HS416.3B", "dickite1.spc Dickite NMNH106242", "dickite2.spc Dickite NMNH46967", "diopsid1.spc Diopside HS317.3B (Cr)", "diopsid2.spc Diopside HS15.3B", "diopsid3.spc Diopside NMNHR18685 ~160", "dipyre.spc Dipyre BM1959-505.HLsp", "dolomit1.spc Dolomite HS102.3B", "dolomit2.spc Dolomite COD2005", "dumortie.spc Dumortierite HS190.3B", "elbaite1.spc Elbaite NMNH94217-1.a 659", "elbaite2.spc Elbaite NMNH94217-1.b 196", "elbaite3.spc Elbaite NMNH94217-1.c <74", "endellit.spc Endellite GDS16", "enstatit.spc Enstatite NMNH128288", "epidote1.spc Epidote GDS26.a 75-200um", "epidote2.spc Epidote GDS26.b <75um", "epidote3.spc Epidote HS328.3B", "epsomite.spc Epsomite GDS149", "erionitm.spc Erionite+Merlinoit GDS144", "erionito.spc Erionite+Offretite GDS72", "eugsteri.spc Eugsterite GDS140 Syn", "europium.spc Europium_Oxide GDS33", "fassaite.spc Fassaite HS118.3B", "ferrihyd.spc Ferrihydrite GDS75 Sy F6", "fluorapa.spc Fluorapatite WS416", "galena1.spc Galena HS37.3", "galena2.spc Galena S102-17", "galena3.spc Galena S102-1B", "galena4.spc Galena S105-2", "galena5.spc Galena S26-39", "galena6.spc Galena S26-40", "gaylussi.spc Gaylussite NMNH102876-2", "gibbsit1.spc Gibbsite HS423.3B", "gibbsit2.spc Gibbsite WS214", "glauconi.spc Glauconite HS313.3B", "glaucoph.spc Glaucophane HS426.3B", "goethit1.spc Goethite WS222", "goethit2.spc Goethite HS36.3", "goethit3.spc Goethite WS219 (limonite)", "goethit4.spc Goethite WS220", "grossul1.spc Grossular HS113.3B-HCL", "grossul2.spc Grossular NMNH155371", "grossul3.spc Grossular WS485", "grossul4.spc Grossular WS483", "grossul5.spc Grossular WS484", "gypsum1.spc Gypsum HS333.3B", "gypsum2.spc Gypsum SU2202", "h2o-ice.spc H2O-Ice GDS136 77K", "halite.spc Halite HS433.3B", "halloys1.spc Halloysite NMNH106236", "halloys2.spc Halloysite NMNH106237", "halloys3.spc Halloysite CM13", "halloys4.spc Halloysite KLH503", "halloys5.spc Halloysite+Kaolinite CM29", "hapatite.spc Hydroxyl-Apatite WS425", "hectori1.spc Hectorite SHCa-1", "hectori2.spc Hectorite SHCa-1.Ac-B", "hedenbe1.spc Hedenbergite NMNH119197", "hedenbe2.spc Hedenbergite HS10.3B", "hematit1.spc Hematite 2%+98%Qtz GDS76", "hematit2.spc Hematite GDS27", "hematit3.spc Hematite GDS69.a 150-250u", "hematit4.spc Hematite GDS69.b 104-150u", "hematit5.spc Hematite GDS69.c 60-104um", "hematit6.spc Hematite GDS69.d 30-45um", "hematit7.spc Hematite GDS69.e 20-30um", "hematit8.spc Hematite GDS69.f 10-20um", "hematit9.spc Hematite GDS69.g <10um", "hematita.spc Hematite HS45.3", "hematitb.spc Hematite WS161", "hematitc.spc Hematite FE2602", "heuland1.spc Heulandite GDS3", "heuland2.spc Heulandite NMNH84534", "hgrossul.spc Hydrogrossular NMNH120555", "holmquis.spc Holmquistite HS291.3B", "hornble1.spc Hornblende_Mg NMNH117329", "hornble2.spc Hornblende_Fe HS115.3B", "hornble3.spc Hornblende HS16.3B", "hornble4.spc Hornblende HS177.3B", "howlite.spc Howlite GDS155", "hyperst1.spc Hypersthene NMNHC2368", "hyperst2.spc Hypersthene PYX02.h >250u", "hyperst3.spc Hypersthene PYX02.c 180um", "hyperst4.spc Hypersthene PYX02.b 120um", "hyperst5.spc Hypersthene PYX02.f 60um", "hyperst6.spc Hypersthene PYX02.e 34um", "hyperst7.spc Hypersthene PYX02.d 23um", "hyperst8.spc Hypersthene PYX02.a 12um", "hyperst9.spc Hypersthene PYX02.g 7um", "illite1.spc Illite GDS4 (Marblehead)", "illite2.spc Illite IMt-1.a", "illite3.spc Illite IMt-1.b <2um", "illite4.spc Illite IL101 (2M2)", "illite5.spc Illite IL105 (1Md)", "ilmenite.spc Ilmenite HS231.3B", "jadeite.spc Jadeite HS343.3B", "jarosit1.spc Jarosite GDS99 K-y 200C", "jarosit2.spc Jarosite GDS98 K-Sy 90C", "jarosit3.spc Jarosite GDS100 Na-Sy 90C", "jarosit4.spc Jarosite GDS101 Na-Sy 200", "jarosit5.spc Jarosite GDS24 Na", "jarosit6.spc Jarosite JR2501 K", "jarosit7.spc Jarosite NMNH95074-1 Na", "jarosit8.spc Jarosite WS368 Pb", "jarosit9.spc Jarosite SJ-1 H3O - 10-20%", "kainite.spc Kainite NMNH83904", "kaolini1.spc Kaolinite CM9", "kaolini2.spc Kaolinite KGa-1 (wxyl)", "kaolini3.spc Kaolinite KGa-2 (pxyl)", "kaolini4.spc Kaolinite KL502 (pxyl)", "kaolini5.spc Kaolinite GDS11 <63um", "kaolini6.spc Kaolinite CM3", "kaolini7.spc Kaolinite CM5", "kaolini8.spc Kaolinite CM7", "kaosmec1.spc Kaolin/Smect KLF506 95%K", "kaosmec2.spc Kaolin/Smect KLF508 85%K", "kaosmec3.spc Kaolin/Smect H89-FR-2 50K", "kaosmec4.spc Kaolin/Smect H89-FR-5 30K", "kaosmec5.spc Kaolin/Smect KLF511 12%K", "kerogenb.spc Kerogen BK-Cornell", "labrado1.spc Labradorite HS105.3B", "labrado2.spc Labradorite HS17.3B", "laumonti.spc Laumontite GDS5", "lazurite.spc Lazurite HS418.3B", "lepidocr.spc Lepidocrosite GDS80 (Sy)", "lepidol1.spc Lepidolite HS167.3B", "lepidol2.spc Lepidolite NMNH105538", "lepidol3.spc Lepidolite NMNH105543", "lepidol4.spc Lepidolite NMNH88526-1", "lepidol5.spc Lepidolite NMNH105541", "limonite.spc Limonite HS41.3", "lizardi1.spc Lizardite NMNHR4687.a 280", "lizardi2.spc Lizardite NMNHR4687.b 165", "lizardi3.spc Lizardite NMNHR4687.c 70", "lizardi4.spc Lizardite NMNHR4687.d <30", "maghemit.spc Maghemite GDS81 Sy (M-3)", "magnesit.spc Magnesite+Hydroma HS47.3B", "magneti1.spc Magnetite HS195.3B", "magneti2.spc Magnetite HS78.3B", "malachit.spc Malachite HS254.3B", "manganit.spc Manganite HS138.3B", "margarit.spc Margarite GDS106", "marialit.spc Marialite NMNH126018-2", "mascagn1.spc Mascagnite GDS65.a (crs)", "mascagn2.spc Mascagnite GDS65.b (fn)", "meionit1.spc Meionite WS700.HLsep", "meionit2.spc Meionite WS701", "mesolite.spc Mesolite+Hydroxyapop GDS6", "microcl1.spc Microcline HS82.3B", "microcl2.spc Microcline HS103.3B", "microcl3.spc Microcline HS107.3B", "microcl4.spc Microcline HS108.3B", "microcl5.spc Microcline HS151.3B", "microcl6.spc Microcline NMNH135231", "mirabili.spc Mirabilite GDS150 Na2SO4", "mizzoni1.spc Mizzonite NMNH113775-1", "mizzoni2.spc Mizzonite BM1931-12", "mizzoni3.spc Mizzonite HS350.3B HLSep", "mizzoni4.spc Mizzonite HS351.3BS", "monazite.spc Monazite HS255.3B", "monticel.spc Monticellite HS339.3B", "montmor1.spc Montmorillonite SWy-1", "montmor2.spc Montmorillonite SAz-1", "montmor3.spc Montmorillonite SCa-2.a", "montmor4.spc Montmorillonite SCa-2.b", "montmor5.spc Montmorillonite CM27", "montmor6.spc Montmorillonite CM20", "montmor7.spc Montmorillonite CM26", "montmor8.spc Montmorillonite STx-1", "montmor9.spc Montmorillonite+Illi CM37", "montmora.spc Montmorillonite+Illi CM42", "mordeni1.spc Mordenite GDS18", "mordeni2.spc Mordenite+Clinopt. GDS151", "muscovi1.spc Muscovite GDS107", "muscovi2.spc Muscovite GDS108", "muscovi3.spc Muscovite GDS111 Guatemal", "muscovi4.spc Muscovite GDS113 Ruby", "muscovi5.spc Muscovite GDS114 Marshall", "muscovi6.spc Muscovite GDS116 Tanzania", "muscovi7.spc Muscovite GDS117 Isinglas", "muscovi8.spc Muscovite GDS118 Capitan", "muscovi9.spc Muscovite GDS119 Mt Alamo", "muscovia.spc Muscovite GDS120 Pegma M.", "muscovib.spc Muscovite HS146.3B", "muscovic.spc Muscovite HS24.3", "muscovid.spc Muscovite IL107", "nacrite.spc Nacrite GDS88", "natroli1.spc Natrolite HS169.3B", "natroli2.spc Natrolite+Zeolit HS168.3B", "natroli3.spc Natrolite NMNH83380", "neodymiu.spc Neodymium_Oxide GDS34", "nephelin.spc Nepheline HS19.3", "nephrite.spc Nephrite HS296.3B", "niter.spc Niter GDS43 (K-Saltpeter)", "nontron1.spc Nontronite GDS41", "nontron2.spc Nontronite NG-1.a", "nontron3.spc Nontronite NG-1.b <2um fr", "nontron4.spc Nontronite SWa-1.a", "nontron5.spc Nontronite SWa-1.b <2um", "oligocl1.spc Oligoclase HS110.3B", "oligocl2.spc Oligoclase HS143.3B", "olivine1.spc Olivine NMNH137044.a 160u", "olivine2.spc Olivine NMNH137044.b <74u", "olivine3.spc Olivine GDS70.a GSB 165um", "olivine4.spc Olivine GDS70.b GSB 115um", "olivine5.spc Olivine GDS70.c GSB 70um", "olivine6.spc Olivine GDS70.d GSB <60um", "olivine7.spc Olivine HS285.4B", "olivine8.spc Olivine HS420.3B", "olivine9.spc Olivine KI3005 <60um", "olivinea.spc Olivine KI3054 <60um", "olivineb.spc Olivine KI3188 <60um", "olivinec.spc Olivine KI3189 <60um", "olivined.spc Olivine KI3291 <60um", "olivinee.spc Olivine KI3377 <60um", "olivinef.spc Olivine KI4143 <60um", "olivineg.spc Olivine GDS71.a TSD 65um", "olivineh.spc Olivine GDS71.b TSD <60um", "opal1.spc Opal WS732", "opal2.spc Opal TM8896 (Hyalite)", "orthocl1.spc Orthoclase NMNH113188", "orthocl2.spc Orthoclase NMNH142137 Fe", "orthocl3.spc Orthoclase HS13.3B", "palygor1.spc Palygorskite CM46", "palygor2.spc Palygorskite PFL-1", "paragoni.spc Paragonite GDS109", "pectoli1.spc Pectolite NMNH94865.a", "pectoli2.spc Pectolite NMNH94865.b", "perthite.spc Perthite HS415.3B", "phalite.spc Polyhalite NMNH92669-4", "phlogop1.spc Phlogopite GDS20 fine fr", "phlogop2.spc Phlogopite HS23.3B", "phlogop3.spc Phlogopite WS496", "phlogop4.spc Phlogopite WS675", "pigeonit.spc Pigeonite HS199.3B", "pinnoite.spc Pinnoite NMNH123943", "plimonit.spc Pitch_Limonite GDS104 Cu", "praseody.spc Praseodymium_Oxide GDS35", "prochlo1.spc Prochlorite SMR-14.a 115u", "prochlo2.spc Prochlorite SMR-14.b 32u", "prochlo3.spc Prochlorite SMR-14.c <30u", "psilomel.spc Psilomelane HS139.3B", "pyrite1.spc Pyrite HS35.3", "pyrite2.spc Pyrite S142-1", "pyrite3.spc Pyrite S26-8", "pyrite4.spc Pyrite S29-4", "pyrite5.spc Pyrite S30", "pyrope.spc Pyrope WS474", "pyrophy1.spc Pyrophyllite PYS1A fine g", "pyrophy2.spc Pyrophyllite PYS1A <850um", "pyrophy3.spc Pyrophyllite SU1421", "pyroxene.spc Pyroxene HS119.3B", "pyrrhoti.spc Pyrrhotite HS269.3B", "quartz1.spc Quartz HS117.3B Aventurin", "quartz2.spc Quartz GDS31 0-74um fr", "quartz3.spc Quartz HS32.4B", "quartz4.spc Quartz GDS74 Sand Ottawa", "rectori1.spc Rectorite ISR202 (RAr-1)", "rectori2.spc Rectorite RAr-1", "rhodoch1.spc Rhodochrosite HS338.3B", "rhodoch2.spc Rhodochrosite HS67 <250um", "rhodoni1.spc Rhodonite NMNHC6148 >250u", "rhodoni2.spc Rhodonite HS325.3B", "richter1.spc Richterite HS336.3B", "richter2.spc Richterite NMNH150800 HCl", "riebeck1.spc Riebeckite NMNH122689", "riebeck2.spc Riebeckite HS326.3B", "rivadavi.spc Rivadavite NMNH170164", "roscoeli.spc Roscoelite EN124", "rutile1.spc Rutile HS126.3B", "rutile2.spc Rutile HS137.3B", "samarium.spc Samarium_Oxide GDS36", "sanidin1.spc Sanidine GDS19", "sanidin2.spc Sanidine NMNH103200", "saponit1.spc Saponite SapCa-1", "saponit2.spc Saponite SapCa-1.AcB", "sauconit.spc Sauconite GDS135", "sbicarbo.spc Sodium_Bicarbonate GDS55", "scolecit.spc Scolecite GDS7 acid trtd", "sepioli1.spc Sepiolite SepNev-1.AcB", "sepioli2.spc Sepiolite SepNev-1", "sepioli3.spc Sepiolite SepSp-1", "sepioli4.spc Sepiolite SepSp-1.AcB", "serpent1.spc Serpentine HS318.4B", "serpent2.spc Serpentine HS8.3B", "siderite.spc Siderite HS271.3B", "sideroph.spc Siderophyllite NMNH104998", "silliman.spc Sillimanite HS186.3B", "smaragdi.spc Smaragdite HS290.3B", "spessar1.spc Spessartine NMNH14143", "spessar2.spc Spessartine HS112.3B", "spessar3.spc Spessartine WS480", "spessar4.spc Spessartine WS481", "sphaler1.spc Sphalerite HS136.3B", "sphaler2.spc Sphalerite S102-7", "sphaler3.spc Sphalerite S102-8", "sphaler4.spc Sphalerite S26-34", "sphaler5.spc Sphalerite S26-35", "sphene.spc Sphene HS189.3B", "spodumen.spc Spodumene HS210.3B", "stauroli.spc Staurolite HS188.3B", "stilbit1.spc Stilbite GDS8", "stilbit2.spc Stilbite HS482.3B", "strontia.spc Strontianite HS272.3B", "sulfur.spc Sulfur GDS94 Reagent", "syngenit.spc Syngenite GDS139", "talc1.spc Talc GDS23 74-250um fr", "talc2.spc Talc HS21.3B", "talc3.spc Talc WS659", "talc4.spc Talc TL2702", "teepleit.spc Teepleite+Tron NMNH102798", "tephroit.spc Tephroite HS419.3B", "thenard1.spc Thenardite GDS146", "thenard2.spc Thenardite HS450.3B", "thuring1.spc Thuringite SMR-15.a 115um", "thuring2.spc Thuringite SMR-15.b 80um", "thuring3.spc Thuringite SMR-15.c 32um", "thuring4.spc Thuringite SMR-15.d <30um", "tincalco.spc Tincalconite GDS142", "topaz1.spc Topaz Wigwam_Area_A_#10", "topaz2.spc Topaz Wigwam_Area_2_#12", "topaz3.spc Topaz Wigwam_Area_3_#13", "topaz4.spc Topaz Wigwam_Area_4_#14", "topaz5.spc Topaz Wigwam_Area_5_#15", "topaz6.spc Topaz Wigwam_Area_6_#16", "topaz7.spc Topaz Harris_Park_#17", "topaz8.spc Topaz Crystal_Park_#2", "topaz9.spc Topaz Jos_#22", "topaza.spc Topaz Harris_Park_#3", "topazb.spc Topaz Tarryalls_#4", "topazc.spc Topaz Little_3_Mine_#41", "topazd.spc Topaz Cameron_Cone_#42", "topaze.spc Topaz Mt._Antero_#5", "topazf.spc Topaz Glen_Cove_#6", "topazg.spc Topaz Glen_Cove_#8", "topazh.spc Topaz Harris_Park_#9", "topazi.spc Topaz HS184.3B", "tourmali.spc Tourmaline HS282.2B", "tremoli1.spc Tremolite HS18.3", "tremoli2.spc Tremolite NMNH117611.HCl", "trona.spc Trona GDS148", "ulexite1.spc Ulexite HS441.3B", "ulexite2.spc Ulexite GDS138 Boron CA", "uralite.spc Uralite HS345.3B", "uvarovit.spc Uvarovite NMNH106661", "vermicu1.spc Vermiculite GDS13 Llano", "vermicu2.spc Vermiculite VTx-1.a <250", "vermicu3.spc Vermiculite VTx-1.fls", "vermicu4.spc Vermiculite WS681", "vesuvian.spc Vesuvianite HS446.3B", "witherit.spc Witherite HS273.3B", "wollasto.spc Wollastonite HS348.3B", "zincite.spc Zincite+Franklin HS147.3B", "zircon.spc Zircon WS522", "zoisite.spc Zoisite HS347.3B"]



master = tk.Tk()

fileName = tk.StringVar()
mineralName = tk.StringVar()

fileName.set('')
mineralName.set('')

master.title('Mineral Type Finder')

tk.Label(master, 
         text="enter text here").grid(row=0)

text = tk.Entry(master)

text.grid(row=0, column=1)

tk.Label(master, 
         text='Mineral: ').grid(row=1, column=0)

tk.Label(master, 
         textvariable=fileName).grid(row=1, column=1)

tk.Label(master, 
         text='Details: ').grid(row=2, column=0)

tk.Label(master, 
         textvariable=mineralName).grid(row=2, column=1)

tk.Button(master, 
          text='Copy', command=copyFileName).grid(row=1, 
                                                       column=2, 
                                                       sticky=tk.W, 
                                                       pady=4)
                                                  
tk.Button(master, 
          text='Copy', command=copyMineralDetails).grid(row=2, 
                                                       column=2, 
                                                       sticky=tk.W, 
                                                       pady=4)


tk.Button(master, 
          text='Mineral Details', command=extract_mineralDetails).grid(row=5, 
                                                       column=0, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.Button(master, 
          text='Quit', command=master.quit).grid(row=5, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

#master.withdraw()
#master.clipboard_clear()
#master.clipboard_append('i has clipboardz?')
#master.update() # now it stays on the clipboard after the window is closed                            
                                                 
tk.mainloop()
#master.destroy()


#pyinstaller --onefile --noconsole encrptionTool.py



