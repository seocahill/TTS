from TTS.tts.utils.text.phonemizers.base import BasePhonemizer
from g2p import make_g2p

class GA_Phonemizer(BasePhonemizer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._g2p = make_g2p('ga', 'ga-ipa')

    @staticmethod
    def name():
        return "ga_phonemizer"

    def _phonemize(self, text, separator):
        phonemes = self._g2p(text)
        return phonemes.output_string

    @classmethod
    def is_available(cls):
        # return True if the backend is available, False otherwise
        return True

    @classmethod
    def version(cls):
        # return the backend version as a tuple (major, minor, patch)
        return "0.0.1"

    @staticmethod
    def supported_languages():
        # return a dict of language codes -> name supported by the backend
        return {"ga": "Irish"}

        # https://blog.mothertongues.org/g2p-background/
