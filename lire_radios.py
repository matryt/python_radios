import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
from time import sleep

wr = [ "http://kissfm.ice.infomaniak.ch/kissfm-64.aac",
       "http://cdn.nrjaudio.fm/audio1/fr/40008/aac_64.mp3",
       "http://direct.franceinfo.fr/live/franceinfo-midfi.mp3",
       "http://direct.franceinter.fr/live/franceinter-midfi.mp3",
       "http://icecast.funradio.fr/fun-1-44-128?listen=webCwsBCggNCQgLDQUGBAcGBg",
       "http://cdn.nrjaudio.fm/audio1/fr/40045/aac_64.mp3",
       "http://radiofg.impek.com/fg",
       "http://streaming.radio.rtl.fr/rtl-1-44-128",
       "http://icecast.skyrock.net/s/natio_mp3_128k",
       "http://str0.creacast.com/radio_vinci_autoroutes_7",
       "http://str0.creacast.com/oxy-melun",
       "https://ecmanager2.pro-fhi.net/radioalpha?ver=143045",
       "http://cdn.nrjaudio.fm/audio1/fr/40033/aac_64.mp3",
       "http://mfm.ice.infomaniak.ch/mfm-128.mp3",
       "http://ais-live.cloud-services.paris:8000/virgin.mp3",
       "http://novazz.ice.infomaniak.ch/novazz-128.mp3",
       "http://tsfjazz.ice.infomaniak.ch/tsfjazz-high.mp3",
       "http://radioemotion.ice.infomaniak.ch/radioemotion-128.mp3",
       "http://manager2.streaming-ingenierie.fr:8058/stream/1/",
       "http://cdn.nrjaudio.fm/audio1/fr/30401/mp3_128.mp3?origine=fluxradios",
       "http://agoracotedazur.ice.infomaniak.ch/agoracotedazur.mp3",
       "https://radiomonaco.ice.infomaniak.ch/radiomonaco-128.mp3",
       "http://start-sud.ice.infomaniak.ch/start-sud-high.mp3",
       "http://icecast.radiofrance.fr/mouv-midfi.mp3",
       "http://ais-live.cloud-services.paris:8000/europe1.mp3",
       "https://niceradio.ice.infomaniak.ch/niceradio.aac",
       "http://icecast.radiofrance.fr/fbazur-midfi.mp3",
       "http://durance-radio.ice.infomaniak.ch/durance-radio.mp3"]

vlc = vlc.Instance()
radio = vlc.media_player_new()


while True:

   clavier = input("quelle radio voulez-vous ? 0-Kiss FM, 1-NRJ, 2-France Info, 3-France Inter, 4-Fun Radio, 5-Nostalgie, 6-Radio FG, 7-RTL, 8-Skyrock, 9-Radio Vinci Autoroutes Côte d\'Azur, 10-Radio Oxygène, 11-Radio Alpha, 12-Chérie FM, 13-M Radio, 14-Virgin Radio, 15-Radio Nova, 16-TSF Jazz, 17-Radio Emotion, 18-Grimaldi, 19-Rire et Chansons, 20-Agora Côte d'Azur, 21-Radio Monaco, 22-Sud Radio, 23-Mouv', 24-Europe 1, 25-Nice Radio, 26-France Bleu Azur, 27-Durance FM, q-arrêter la radio : ")
   print()
   try:
       a = int(clavier)
       url = wr[a]
       w = vlc.media_new(url)
       radio.set_media(w)
       radio.play()

   except:
      if clavier == "q":
         print("Au revoir !")
         radio.release()
      break
