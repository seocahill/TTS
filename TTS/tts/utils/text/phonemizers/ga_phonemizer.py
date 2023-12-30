from TTS.tts.utils.text.phonemizers.base import BasePhonemizer
import sys
sys.path.insert(0, '../g2p')
from g2p import make_g2p

# I can base the mapping on this https://en.wikipedia.org/wiki/Help:IPA/Irish

class GA_Phonemizer(BasePhonemizer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # https://blog.mothertongues.org/g2p-background/
        self._g2p = make_g2p('ga', 'ipa')  # 'ga' is the language code for Irish Gaelic

    @staticmethod
    def name():
        return "ga_phonemizer"

    def phonemize(self, text, language, **kwargs):
        phonemes = self._g2p(text)
        return ' '.join(phonemes)

