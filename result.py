from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog


class BehaviorModel1(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu vo vedení,uspokojiť svoju rozhodnosť a individualitu. Pracuje dobre ak sa okolie neustále mení.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Kariéra, výzva, konkurencia, nezávislosť.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Určovať chod udalostí a mať svoj osud vo vlastných rukách.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Hovorí energicky, má jasnú logiku a precízne vyberá slová. Suverénne pracuje s vyhláseniami odborníkov a vie dobre vizualizovať. Vyžaduje rozhodné zapojenie sa účastníkov, dokáže iných veľmi dobre presvedčiť o materiálnych veciach a taktiež dobre o nemateriálnych veciach.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Neohrozený vedúci pracovník, ktorý svojmu tímu dokáže aj v ťažkých situáciách udať správny smer. Odmeňuje verných spolupracovníkov, buduje si rad verných, ktorí ho počúvajú.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Využíva informácie na uplatnenie moci. Robí ťažkosti akonáhle nie je stredobodom pozornosti. Nechce sa začleniť do tímu. Stráca záujem akonáhle nemá novú výzvu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Veci vybaví rýchle, otvorene vyjadruje svoj názor k stanoveným cieľom. Na dosiahnutie cieľov využíva všetky prostriedky. Určí si jedného nepriateľa alebo prekážku, ktorú je nutné zdolať. Dosahuje vrcholné osobné výkony.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Konfrontáciou, reaguje pritom netrpezlivo a nervózne, málo sa zaujíma o to ako ho berú iní a či je obľúbený. Chce dosiahnuť, aby sa iní vzdali svojich cieľov.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Je produktívnejší, nátlak pokladá za nástroj na zavedenie opatrení",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Akceptuje len zmysluplné zmeny, často z vecných dôvodov zastáva názory druhej strany aj keď k nej nepatrí. Očakáva nariadenia, ktoré má plniť. Odmieta ako nadriadeného prijať slabú osobnosť.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-byť vizionárom, priekopníkom a hľadať nové možnosti a cesty\n"
                                                                                "- rozlišovať dôležité od menej dôležitého\n"
                                                                                "- ukázať rozhľad, napr. pri plánovaní alebo v predvídaní následkov konania",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Prejavovať viac pochopenia a porozumenia voči iným, počúvať čo iní hovoria a neprerušovať ich,výhrady iných využívať ako šance dokázať opak; nevytvárať bojové napätie len preto aby ste presvedčili iných, zapojiť iných do práce radšej ako ochotných spolupracovníkov a nie ako podriadených partnerov, viac spolupracovať s ľuďmi, ktorí lepšie dokážu spolupracovať v tíme (Modely 23,32,234)",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel2(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po akceptovaní, spolupatričnosti a spokojnosti. Pracuje dohre keď nie je pod kontrolou a keď sa nemusí zaoberať maličkosťami.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Kontakt so svetom, uznanie, postavenie, prestíž a mnohorakosť.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Zaoberať sa rozličnými aktivitami.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Dokáže druhých zbaviť zaujatosti, prejavuje záujem, vyžaruje šarm a sebave¬domie. Veľa a rád hovorí, vtipkuje, veľa sľubuje. Bagatelizuje ťažkosti. Iných dokáže len ťažko presvedčiť o materiálnych veciach, o nemateriálnych celkom dobre.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Dokáže odstrániť napätie tým. že berie ohľad na to. že jeho tím potrebuje zábavu, akitivity a sociálnu kreativitu. Je pripravený deliť sa o vedenie tímu s inými.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Venuje rutinným úlohám málo pozornosti, zjednodušuje riešenia, nesprávne od¬haduje schopnosti druhých, má často ťažkosti správne odhadnúť potrebný čas na splnenie úloh",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Využíva jestvujúce prostriedky. Myslí si. že nové situácie vyžadujú aj nové me¬tódy. Priťahujú ho také úlohy, ktoré vyžadujú pozitívny prístup a ľudskosť. Chce vždy vytvořit priateľskú, veselú atmosféru a nezaujíma sa o eficieneiu..",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Vyhýba sa im. Myslí si. že konflikty ubližujú ľuďom. Vyžaduje harmóniu, chce aby ho všetci akceptovali a mali radi.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Obnovuje svoje vplyvné kontakty, používa svoj humor a šarm aby sa ubránil kritike.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Stavia mosty tým. že dokáže zabránit napätiu, dokáže sa spoľahnúť na silnú ve¬dúcu osobnosť. Tak zostanú všetci členovia tímu produktívni a disciplinovaní.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-získavať si iných pomocou oduševnených prednášok, iných podporovať a radiť im\n"
                                                                                "-jednať spontánne na základe vnútorného presvedčenia \n"
                                                                                "-dozvedieť sa od iných ich tajné problémy, obavy a pomôcť im.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Koncentrovať sa na úlohu; dodržiavať dohodnuté termíny: hovoriť rozhodne a priamo; byť objektívny pri rozhodovaní: vedieť si poradiť s námietkami; spolupracovať s jednotlivcami, ktorí majú schopnosti v rozvíjaní organizovaného prístupu (Modely 4. 43. 134).",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel3(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Nepokladá osobné schopnosti za dôležité a podceňuje ich. Skrýva svoje osobné nádeje a ambície, čaká čo sa udeje namiesto aby niečo aktívne zmenil.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po spolupráci, spokojnosti a zdržanlivosti. Pracuje dobre, keď má dostatok času na na to. aby postupoval systematicky.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Priateľstvo, istota, plnenie povinností, uznanie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Dosiahnuť úspech pomocou špecializácie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Kľudným a úprimným spôsobom zapája angažovaných a skromných ľudí. prosí iných o pomoc aby bol dosiahnutý úspech pri predstavení výhod produktu alebo nápadu. Dokáže iných relatívne dobre presvedčiť o materiálnych veciach, o ne-materiálnych skôr ťažko.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Je vedúcim, ktorý vychádza iným v ústrety. Umožní tímu vyriešiť ťažkosti keď sa niekoľko kandidátov uchádza o vedúcu pozíciu. Dokáže dobre presmerovať ľudi. ktorí len neochotne spolupracujú.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Má odborné znalosti v jednej oblasti, pri riešení problémov využíva zdravý rozum, krok za krokom sa učí nové metódy. Má ťažkosti odolať nadmernej zod¬povednosti.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Uzatvára kompromisy, aby sa našlo pre obe stránky vyhovujúce riešenie alebo stredná cesta medzi dvoma extrémami.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Ochotne preberá zodpovednosť a hľadá najlepšie trvalé riešenie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Identifikuje sa s tými kolegami, ktorí si želajú prísny štýl vedenia. Pracuje efek¬tívne ako špecialista, dokáže dobre stanovovať priority..",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-je cieľavedomý, napr. v presnom odoslaní termínovaných podkladov \n"
                                                                                "-Prijíma nariadenia a pokyny, bez váhania ich plní a akceptuje\n"
                                                                                "-ovláda obsluhu zariadení a prístrojov",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Aj pod nátlakom nestratiť kontrolu; okamžite pokarhať tých. ktorí sú nezodpovední; stanoviť smernice na dosiahnutie úloh; jednať prezieravo, radšej sa sám chopiť iniciatívy než vyčkávať a reagovať na ľudí alebo udalosti: spolupracovať s jednotlivcami, ktorí majú schopnosti vniesť do práce rôznorodosť (Modely 12.24. 124). ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel4(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po odbornosti, svedomitosti a sebadisciplíne. Pracuje dobre keď môže postupovať podľa jasne stanovených a Strukturovaných línií.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Etický a morálny kódex, vedomosti, precízna práca a uznanie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Vniesť poriadok do chaosu",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Stavia na reťazi argumentov, aby presvedčil iných. Dokáže si získať ich dôveru svojimi uváženými, presnými a zdržanlivými prejavmi. Neprejavuje city. Do¬káže druhých veľmi dobre presvedčiť o materiálnych veciach, o nemateriálnych relatívne dobre. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Je vedúcim technickým pracovníkom, ktorý pomáha tímu pri riešení odborných problémov. Česť a rituály sú preňho dôležité, dbá na dodržiavanie formálnosti v správaní.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Je precitlivelý voči kritike, doslova striehne na dodržiavanie pravidiel a predpisov, je nadmeru starostlivý. Má nedostatok spontánnosti na to, aby dokázal rýchlo zmeniť svoje plány. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Svoje ciele dosahuje vážnym, kľudným a rozhodným spôsobom. Vytvára odbor¬né postupy a vyvíja sa minimálne v jednej časti svojej odbornosti ako odborník. Uprednostňuje úlohy, ktoré si vyžadujú analytické a kritické schopnosti pri riešení problémov",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Vyhýba sa im. Snaží sa nemiešať do problémov, ktoré môžu spôsobiť konflikt. Myslí si. že nemá zmysel pokúšať sa riešiť konflikty.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Stane sa ešte opatrnejším a svedomitejším.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Pred každým rozhodnutím starostlivo zvažuje možné následky. Svojimi kritickými úvahami a zbieraním informácií pomáha všetkým. Dokáže dobre analyzovať. viac sa venuje riešeniu úloh a nezaoberá sa vzťahmi osôb v tíme.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-účtovníctvo, všetko čo súvisí s číslami, napr. pokladňa a štatistiky \n"
                                                                                "-vytváranie plánov a návrhov, napr. plán stavby\n"
                                                                                "-zaraďovanie objektov do kategórií, napr. knihy ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Nadviazať kontakt s novými ľuďmi; vyvinúť schopnosť lepšie znášať konflikty: urýchliť rozhodovanie sa; spoznať, že nie všetky problémy sú komplikované: nacvičovať si rýchlejšie rozhodovanie v menej dôležitých oblastiach: spolupracovať s jednotlivcami, ktorí majú dobré schopnosti nadväzovať kontakty s inými (Modely 2. 24, 123). ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel12(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po rozhodnosti, individualite a plnení úloh. Pracuje dobre keď si môže získať prestíž a autoritu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Výzva, súťaženie, získanie moci a prestíž. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Kreatívne myšlienky zmysluplne zužitkovať na dosiahnutie cieľa.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Vzbudzuje ich zvedavosť, sľubuje im zaujímavé úlohy, zhovára sa s inými aby odhalil ich želania. Dokáže iných dobre presvedčiť o materiálnych ako aj o ne-materiálnych veciach. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Vedie svoj tím ako dirigent a plní tým potrebu tímu po jednote, bez váhania udeľuje úlohy, zaprisaháva členov tímu na jednu spoločnú úlohu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Menej obľúbené úlohy prideľuje iným, nemá trpezlivosť voči pomalejším a dlhšie uvažujúcim kolegom. Často nedokáže delegovať úlohy a vnucuje iným svoje názory.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Sústreďuje sa na to. čo má pre neho a jeho okolie najväčší význam a prináša im najväčšie výhody. Má rád konkurenciu a mimoriadne úlohy. Rád vopred plánuje, zabezpečuje opatrenia. Detaily prenecháva na iných. Pracuje presne, keď má vopred stanovený termín.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Dúfa, že spoluprácou s ostatnými vyrieši konflikty. Pomáha vyriešiť situácie, ktoré vznikli na základe negatívneho a nesprávneho prístupu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Pokým je to možné, dovolí druhým aby mu pomohli. Sám podstupuje riziká a zmätie tým dokonca aj protivníkov.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Vyhľadáva si úlohu zástupcu vedúceho tímu. ktorý vedúceho podporuje. Súčasne ovplyvňuje jeho rozhodnutia, kolíše pri svojich rozhodnutiach medzi náklonnosťou k úlohe a k človeku.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-motivovať druhých aby konali\n"
                                                                                "-byť plný fantázie a pomôcť tak iným vidieť veci z iného hľadiska\n"
                                                                                "-rýchlo sa rozhodovať, napr. ihneď zlepšiť jestvujúci proces",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Dbať viac na dodržiavanie termínov; vyhýbať sa útokom na iných, keď sú títo pod nátlakom; dať za pravdu tým. ktorí majú pravdu po odbornej stránke; nemanipulovat' iných; spolupracovať s jednotlivcami, ktorí majú schopnosti sledovať okolie a vytvoriť predvídateľné prostredie (Modely I4. 34. 134). ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel13(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po nezávislosti, odvahe a praktickosti. Pracuje dobre keď môže sledovať plnenie úlohy po koncepčnej stránke od jej začiatku až po ukončenie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Dobrodružstvo, výhra, vedomosti, psychická vyrovnanosť.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Zvažovať, spoznať rozdiely a stanoviť zmysluplné aktivity.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= " Energicky argumentuje, aby si druhých získal pre svoj postup práce. Rýchlo reaguje na pripomienky, vie bez problémov odpovedať na otázky využívajúc pritom fakty a dokumentáciu. Je vážny a priamy. Dokáže iných relatívne dobre presvedčiť o materiálnych aj nemateriálnych veciach.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Cieľavedomý vedúci tímu. ktorý tímu jasne dáva najavo, že je potrebné tvrdo pracovať. Pri nezhodách okamžite rozhoduje.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Zanedbáva malé rituály, ktoré by druhých ukľudnili. Ak ho naháňajú termíny, je často nemilý a netaktný. Považuje za ťažké delegovať úlohy.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Vyvíja systematické plány vrátane opatrení pre prípad výskytu prekážok. Má úspech svojim rýchlym konaním a to aj bez toho. aby musel prísne kontrolovať. Je rozhodný a agresívny. Pomáha pri zlepšovaní kvality.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Konfrontáciou, provokatérom robí ťažkosti. Odmieta sa vzdať osobných cieľov. Znervózňuje tým druhých a vyvoláva tak nepokoj.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Tvrdohlavosťou, často si volí nesprávny čas na výmenu názorov.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Využíva osobné skúsenosti viac ako svoje vedomosti zo školy, preberá úlohy ktoré sú pre druhých ťažké. Pracuje najlepšie, keď nie je rušený a kontrolovaný prísnym a kritickým vedúcim.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-Usmerňovať druhých a sprevádzať ich pri plnení úloh\n"
                                                                                "-Preverovať a posudzovať, či sú výkony druhých v danej oblasti dostatočné\n"
                                                                                "-Podporovať postup pri práci. napr. povzbudzovaním k rozhodnutiam ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Jasnejšie konať: stanoviť časový limit na rozriešenie konfliktu a dosiahnutie zhody: byť otvorený iným názorom: podporovať nové nápady iných a vyjadriť im aj uznanie; byť ochotný zmeniť tempo alebo vyjsť iným v ústrety: spolupracovať s jednotlivcami, ktorí sú prispôsobivejší a taktnější (Modely 21. 23, 32). ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel14(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po výkone, individualite a ústraní. Pracuje dobre keď má dostatok času na overenie správnosti svojich myšlienok a konania.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Intelektuálna a fyzická výzva, kreativita, uznanie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Vynájsť a implementovat' nové myšlienky.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Využíva moc faktov a je nadšený ak nápad alebo výrobok zodpovedá jeho vysokým nárokom. Uznanie dosahuje svojím dobre organizovaným a priamym postupom. Dokáže druhých nadmieru dobre presvedčiť o materiálnych veciach a taktiež dobre o nemateriálnych veciach. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Je inovatívnym vedúcim pracovníkom, pomáha tímu vyvíjať nové teórie. Je takmer vždy formálny, je vzorom pre iných, preberá priveľa zodpovednosti.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Sústreďuje sa len na jedinú úlohu, čím často trpia ostatné oblasti práce. Často si robí starosti, ktoré sú niekedy neopodstatnené. Je nadmieru opatrný a potrebuje pomoc aby dokázal ukončiť projekt.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Rieši radšej úlohy ako medziľudské problémy. Sústreďuje sa na komplexitu jednej otázky, pracuje dlho a udáva tempo práce, ktoré je pre druhých často veľmi namáhavé.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Spoluprácou, pričom tlačí druhých najprv do defenzívy a skrýva tým svoju vlastnú neistotu. Potom pomenuje všetky starosti a problémy, ktoré vidí.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Je dobre pripravený na všetky eventuality, sám sa zaväzuje ešte viac pracovať.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Uvažuje o jestvujúcich postupoch a metódach, rieši problémy a žiada o povo¬lenie nanovo preveriť a testovať výsledky. Rád preberá úlohy vo výskume a rád hľadá odborné informácie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-byť kreatívnym, napr. vyvinúť nový pracovný postup\n"
                                                                                "-systematizovať a zaviesť poriadok napr. poukladať náradie a nástroje do také¬ho poradia, v ktorom budú použité \n"
                                                                                "-diagnostikovať, napr. nájsť koreň problému",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Dopriať si uvoľnenie od napätia z pracovného úsilia: byť objektívny a starost¬livý: pri vyjadrovaní kritiky voči iným brať do úvahy ich pocity; prejaviť iným uznanie za vynaložené úsilie; spolupracovať s jednotlivcami, ktorí majú lepšie schopnosti v nadväzovaní sociálnych kontaktov a lepšie vedia zvládať napätie (Modely 12. 21.23). ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class BehaviorModel21(Screen):
    m_dialog = None
    oc_dialog = None
    zz_dialog = None
    apd_dialog = None
    avt_dialog = None
    mss_dialog = None
    ru_dialog = None
    ark_dialog = None
    arpn_dialog = None
    act_dialog = None
    nu_dialog = None
    s_dialog = None

    def m_dialog(self):
        self.m_dialog = MDDialog(title="Motivovaný", text= "Príležitosťami uspokojiť vlastnú potrebu po sebarealizácii, spolupatričnosti a mimoriadnych výkonoch. Pracuje dobre keď má možnosť byť v kontakte s rozmanitými ľuďmi.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.m_dialog.open()
    def oc_dialog(self):
        self.oc_dialog = MDDialog(title="Osobné ciele", text= "Výzva, súťaženie, medziľudské kontakty, uznanie.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.oc_dialog.open()
    def zz_dialog(self):
        self.zz_dialog = MDDialog(title="Zameranie", text= "Očakávať úspešné výsledky.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.zz_dialog.open()
    def apd_dialog(self):
        self.apd_dialog = MDDialog(title="Ako presvedčí druhych", text= "Vnáša čerstvý vietor do práce, vyzdvihuje do popredia šance, dokáže sa svojím prejavom prispôsobiť osobnosti poslucháča. Je priateľský a milý. Rád pracuje blízko ostatných a odstraňuje tak bariéry. Dokáže druhých veľmi dobre presvedčiť o materiálnych aj nemateriálnych veciach. ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.apd_dialog.open()
    def avt_dialog(self):
        self.avt_dialog = MDDialog(title="Ako vedúci tímu", text= "Je demokratickou vedúcou osobnosťou, ktorá spľňa predstavy tímu o zaujímavých zážitkoch. Správa sa férovo k druhým, stavia mosty medzi nepriateľmi.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.avt_dialog.open()
    def mss_dialog(self):
        self.mss_dialog = MDDialog(title="Možné slabé stránky", text= "Nemá rád stereotypné činnosti, vyhýba sa jednostrannej práci. Nedokáže ukončiť zle zvolené projekty. Nadmieru sa nadchýna.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.mss_dialog.open()
    def ru_dialog(self):
        self.ru_dialog = MDDialog(title="Riešenie úloh", text= "Teší sa možnostiam prejaviť svoj talent. Dokáže nájsť správne slová na predstavenie svojich plánov, svojím emocionálnym prejavom budí emócie aj u iných. Svoje nadšenie dokáže podmurovať praktickými schopnosťami. Malé práce prenechá na iných, vie dobre povzbudzovať pri dosahovaní cieľov..",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ru_dialog.open()
    def ark_dialog(self):
        self.ark_dialog = MDDialog(title="Ako rieši konflikty", text= "Spoluprácou, na kritiku odpovedá vtipom a humorom. Je pripravený zohľadniť želania druhých.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.ark_dialog.open()
    def arpn_dialog(self):
        self.arpn_dialog = MDDialog(title="Ako reaguje pod nátlakom", text= "Trpezlivosťou, menuje problémy a plánuje to čo je potrebné na ich odstránenie",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.arpn_dialog.open()
    def act_dialog(self):
        self.act_dialog = MDDialog(title="Ako člen tímu", text= "Rád sa venuje ťažkým úlohám. Dáva veci do pohybu, vyjadruje sa k ťažkým otázkam, ktorým sa iní vyhýbajú alebo sa ich obávajú. I lovorím aj v mene slabších členov tímu.",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.act_dialog.open()
    def nu_dialog(self):
        self.nu_dialog = MDDialog(title="Najvhodnejšie úlohy a funkcie", text= "-využívať svoje znalosti, napr. v presvedčovaní druhých \n"
                                                                                "-vytvoriť dobré vzťahy, napr. v komunikácii so zákazníkmi\n"
                                                                                "-viesť druhých, napr. pomôcť tímu odhaliť skryté možnosti ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.nu_dialog.open()
    def s_dialog(self):
        self.s_dialog = MDDialog(title="Stratégie pre vyššiu efektivitu", text= "Spomaliť tempo: vyhýbať sa vyčerpaniu: úprimne pochváliť druhých; dať iným čas vyjadriť ich pochybnosti, obavy a námietky: vyhýbať sa preceňovaniu: vedieť kedy je načase ukončiť presviedčanie iných; spolupracovať s jednotlivcami, ktorí majú schopnosti v organizovaní a systematickom plánovaní (Modely 13. 14. 34). ",
                                      size_hint=[0.8, None], auto_dismiss=True,)

        self.s_dialog.open()



    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"
KV = '''

<BehaviorModel1>:
    name: "1"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 1"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: BOJOVNÍK"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Využíva príležitosti: vychutnáva si zložité situácie, stanoví si priority, dáva nariadenia: robí ľudí zodpovedných za ich konania, meria výsledky,odmeny a tresty: odmieta pomalú a opatrnú cestu spolupráce, uprednostňuje súťaživé úlohy a výzvy,reaguje rýchlo a rozhodne "
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                       
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel2>:
    name: "2"
    
    MDToolbar:
        title: "MODEL SPRÁVANIA 2"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: ZABÁVAČ"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Súperí o pozornosť; chce byť stredobodom pozornosti; delí sa s inými o rady, materiály a úspech; nadväzuje okamžité kontakty s ľuďmi prostredníctvom emocionality a schopnosti presviedčať; povzbudzuje iných, aby vyjadrili svoj názor; nepoučuje iných ; vyhýba sa prístupu ,,oko za oko,,; spolieha sa na podporu iných"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.5
        pos_hint: {"center_x": .5, "center_y": .3}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                    
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()

    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
        
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel3>:
    name: "3"
     
    MDToolbar:
        title: "MODEL SPRÁVANIA 3"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: STABILIZÁTOR"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Určí si stále tempo a drží sa ho; prejavuje trpez¬livosť; dodržiava záväzky; očakáva a prejavuje lojalitu; venuje pozornosť dôležitým detailom; určuje a bráni si vlastné presvedčenia a hodnoty; dokáže sa nadchnúť pre prírodu a krásne okolie "
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.4
        pos_hint: {"center_x": .5, "center_y": .35}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                    
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()
                    
                
    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
                
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel4>:
    name: "4"
    
    MDToolbar:
        title: "MODEL SPRÁVANIA 4"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: PERFEKCIONISTA"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Má sklon súperiť radšej s vecami, než s ľuďmi; snaží sa robiť radosť iným a vychádzať im v ústrety; usiluje sa radšej nadchnúť niekoho pre spoluprácu než ho k tomu nútiť, robí kompromisy keď je to nevyhnutné; dokáže sa podriadiť uznávanej autorite; verí, že tvrdá práca a spravodlivosť sa vyplácajú a vyhľadáva zodpovednosti, ktoré si vyžadujú samostatnú prácu a koncentráciu"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.5
        pos_hint: {"center_x": .5, "center_y": .3}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                    
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()

    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
        
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel12>:
    name: "12"
    
    MDToolbar:
        title: "MODEL SPRÁVANIA 12"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: VÍŤAZNÝ BEŽEC"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Radšej sa oddelí od skupiny, než by bol jed¬ným z mnohých; dosahuje úspech ako pohonný motor so silným vplyvom; nabáda iných k prá¬ci; pracuje voľne a nezávisle; udáva rýchle tem¬po; dokáže pracovať aj bez pokynov"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.5
        pos_hint: {"center_x": .5, "center_y": .3}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                    
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()

    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
        
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel13>:
    name: "13"
    
    MDToolbar:
        title: "MODEL SPRÁVANIA 13"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: PRIEKOPNÍK"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Premieňa frustráciu na prostriedok k vyriešeniu problémov; vyvíja jedinečnú kombináciu rozhodnosti a podrobnej, dôslednej práce; dokáže veľmi presvedčivo prezentovať svoju mienku; dokáže si vynútiť konania; odhodlane sa bráni proti opozícii a rýchlo odhalí slabé argumenty"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.5
        pos_hint: {"center_x": .5, "center_y": .3}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                    
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()

    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
        
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}
            
<BehaviorModel14>:
    name: "14"
    
    MDToolbar:
        title: "MODEL SPRÁVANIA 14"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: VYNÁLEZCA"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Vyberá si praktický prístup; kladie otázky namiesto aby si vynucoval analýzy; nachádza odpovede, ktoré vychádzajú z logického myslenia a skúsenosti; vykonáva rozsiahlu prípravu na úlohy; je iniciátorom a pracuje na vývoji; udržuje si odstup od všetkých okrem najbližších dôverných spolupracovníkov; je spokojný ak môže sám pracovať na projekte; nedovolí iným aby ho obmedzovali"
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.5
        pos_hint: {"center_x": .5, "center_y": .3}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                    
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()

    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
        
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}

<BehaviorModel21>:
    name: "21"
    
    MDToolbar:
        title: "MODEL SPRÁVANIA 21"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": .5, "center_y": .95}   
    
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.3
        pos_hint: {"center_x": .5, "center_y": .73}
        
        MDLabel:
            halign: "left"
            text: "Všeobecný opis správania: PRESVEDČOVATEĽ"
            theme_text_color: "Custom"
            text_color: app.theme_cls.primary_color
            size_hint_y: None
            height: self.texture_size[1]
            
        MDSeparator:
            height: "1dp" 
             
        ScrollView: 
         
            MDLabel:
                text: "Využíva motiváciu iných; upútava pozornosť iných prostredníctvom svojich pozitívnych názorov a vhodne vyberanými slovami; má často podporu iných; snaží sa zopakovať dosiahnuté úspechy; stáva sa podráždeným, keď sa práca stáva rutinou; chce dobre vyzerať a cítiť sa dobre; nemá rád neprehľadné situácie "
                theme_text_color: "Primary"
                size_hint_y: None
                height: self.texture_size[1]
                
    MDCard:
        orientation: "vertical"
        padding: "8dp"
        size_hint: 0.95,0.5
        pos_hint: {"center_x": .5, "center_y": .3}
    
        ScrollView:     
            MDList:
                OneLineAvatarListItem:
                    text: "PRE SEBA" 
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color               
                    IconLeftWidget:
                        icon: "account"
                        
                OneLineListItem:
                    text: "  Možné slabé stránky"
                    theme_text_color: "Custom"
                    on_release: root.mss_dialog()
                     
                OneLineListItem:
                    text: "  Motivovaný"
                    theme_text_color: "Custom"
                    on_release: root.m_dialog()
                    
                OneLineListItem:
                    text: "  Osobné ciele"
                    theme_text_color: "Custom"
                    on_release: root.oc_dialog()
                    
                OneLineListItem:
                    text: "  Základné zameranie"
                    theme_text_color: "Custom"
                    on_release: root.zz_dialog()
                    
                OneLineListItem:
                    text: "  Ako presvedčí druhých"
                    theme_text_color: "Custom"
                    on_release: root.apd_dialog()
                    
                OneLineListItem:
                    text: "  Ako vedúci tímu"
                    theme_text_color: "Custom"
                    on_release: root.avt_dialog()
                    
                OneLineAvatarListItem:
                    text: "PRE TÍM"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    IconLeftWidget:
                        icon: "account-group"
             
                OneLineListItem:
                    text: "  Riešenie úloh"
                    theme_text_color: "Custom"
                    on_release: root.ru_dialog()
                    
                OneLineListItem:
                    text: "  Ako rieši konflikty"
                    theme_text_color: "Custom"
                    on_release: root.ark_dialog()
                    
                OneLineListItem:
                    text: "  Ako reaguje pod nátlakom"
                    theme_text_color: "Custom"
                    on_release: root.arpn_dialog()
                    
                OneLineListItem:
                    text: "  Ako člen tímu"
                    theme_text_color: "Custom"
                    on_release: root.act_dialog()
                    
                OneLineListItem:
                    text: "Najvhodnejšie úlohy/funkcie"
                    theme_text_color: "Custom"
                    on_release: root.nu_dialog()
                    
                OneLineListItem:
                    text: "Stratégie pre vyššiu efektivitu"
                    theme_text_color: "Custom"
                    on_release: root.s_dialog()

    MDRoundFlatButton:
        pos_hint:{ "center_x" :0.1, "center_y": 0.1} 
        size_hint: None, None
        text: "Ok"
        on_press: root.manager.current = "home"
        
    MDFillRoundFlatButton:
        pos_hint:{ "center_x" :0.5, "center_y": 0.1} 
        size_hint: None, None
        text: "Chcem sa zlepšiť"
        on_press: root.manager.current = "goals"
        
    MDFloatingActionButtonSpeedDial:
        callback: root.main_navigate
        data: 
            {'home': 'Domov',
            'lightning-bolt': 'Ciele',
            'notebook': 'Moje testy'}

'''
Builder.load_string(KV)
