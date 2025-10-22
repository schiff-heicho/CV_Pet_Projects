import spacy


class ModelLoader:
    def __init__(self):
        self.models = {}

    def load_models(self):
        try:
            self.models['en'] = spacy.load("en_core_web_md")
            self.models['ru'] = spacy.load("ru_core_news_md")
            print("Модели spaCy успешно загружены.")
        except OSError:
            raise Exception("Модели не найдены!\n")


model_loader = ModelLoader()
