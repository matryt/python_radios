import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
from time import sleep

class Radio:
    def __init__(self, nom, url):
        self.nom = nom
        self.url = url

    def play(self, player):
        player.set_media(vlc.media_new(self.url))
        player.play()
        print(f"--- Vous écoutez {self.nom} ---")
        return player

    def get_url(self):
        return self.url

    def __repr__(self):
        return self.nom

def stop(player):
    player.release()

wr = [Radio("Kiss FM", "http://kissfm.ice.infomaniak.ch/kissfm-64.aac"),
       Radio("NRJ", "http://cdn.nrjaudio.fm/audio1/fr/40008/aac_64.mp3"),
       Radio("France Info", "http://direct.franceinfo.fr/live/franceinfo-midfi.mp3"),
       Radio("France Inter","http://direct.franceinter.fr/live/franceinter-midfi.mp3"),
       Radio("Fun Radio", "http://icecast.funradio.fr/fun-1-44-128?listen=webCwsBCggNCQgLDQUGBAcGBg"),
       Radio("Nostalgie", "http://cdn.nrjaudio.fm/audio1/fr/40045/aac_64.mp3"),
       Radio("Radio FG","http://radiofg.impek.com/fg"),
       Radio("RTL", "http://streaming.radio.rtl.fr/rtl-1-44-128"),
       Radio("Skyrock", "http://icecast.skyrock.net/s/natio_mp3_128k"),
       Radio("Radio Vinci Autoroutes 06", "http://str0.creacast.com/radio_vinci_autoroutes_7"),
       Radio("Radio Oxygène","http://str0.creacast.com/oxy-melun"),
       Radio("Radio Alpha","https://ecmanager2.pro-fhi.net/radioalpha?ver=143045"),
       Radio("Chérie FM", "http://cdn.nrjaudio.fm/audio1/fr/40033/aac_64.mp3"),
       Radio("M Radio", "http://mfm.ice.infomaniak.ch/mfm-128.mp3"),
       Radio("Virgin Radio","http://ais-live.cloud-services.paris:8000/virgin.mp3"),
       Radio("Radio Nova", "http://novazz.ice.infomaniak.ch/novazz-128.mp3"),
       Radio("TSF Jazz", "http://tsfjazz.ice.infomaniak.ch/tsfjazz-high.mp3"),
       Radio("Radio Emotion", "http://radioemotion.ice.infomaniak.ch/radioemotion-128.mp3"),
       Radio("Grimaldi", "http://manager2.streaming-ingenierie.fr:8058/stream/1/"),
       Radio("Rire et Chansons", "http://cdn.nrjaudio.fm/audio1/fr/30401/mp3_128.mp3?origine=fluxradios"),
       Radio("Agora Côte d'Azur" ,"http://agoracotedazur.ice.infomaniak.ch/agoracotedazur.mp3"),
       Radio("Radio Monaco", "https://radiomonaco.ice.infomaniak.ch/radiomonaco-128.mp3"),
       Radio("Sud Radio", "http://start-sud.ice.infomaniak.ch/start-sud-high.mp3"),
       Radio("Mouv'", "http://icecast.radiofrance.fr/mouv-midfi.mp3"),
       Radio("Europe 1", "http://ais-live.cloud-services.paris:8000/europe1.mp3"),
       Radio("Nice Radio", "https://niceradio.ice.infomaniak.ch/niceradio.aac"),
       Radio("France Bleu Azur", "http://icecast.radiofrance.fr/fbazur-midfi.mp3"),
       Radio("Durance FM", "http://durance-radio.ice.infomaniak.ch/durance-radio.mp3")]

vlc = vlc.Instance()
radio = vlc.media_player_new()


def numeroRadio():
    print("Quelle radio voulez-vous écouter ?")
    for i in range(len(wr)):
        print(f"    {i} : {str(wr[i])}")
    print("    q : quitter")

numeroRadio()