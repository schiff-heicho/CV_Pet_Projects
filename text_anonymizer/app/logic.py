import re
from models import model_loader
from langdetect import detect


class TextAnonymizer:
    def __init__(self):
        self.models = model_loader.models
        self.email_pattern = (
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        )
        self.phone_pattern = r'(\+7|7|8)?[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}\b'
        self.date_pattern = r'\b(\d{1,2}[./-]\d{1,2}[./-]\d{2,4}|\d{4}[./-]\d{1,2}[./-]\d{1,2})\b'
        self.credit_card_pattern = (
            r'\b\d{4}[\s\-]?\d{4}[\s\-]?\d{4}[\s\-]?\d{4}\b'
        )
        self.ip_address_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

    def detect_language(self, text: str) -> str:
        try:
            lang = detect(text)
            if lang == 'ru':
                return 'ru'
            else:
                return 'en'
        except (LangDetectException, Exception):
            return 'en'

    def find_sensitive_entities(self, text: str):
        entities = []

        for match in re.finditer(self.email_pattern, text, re.IGNORECASE):
            entities.append((match.start(), match.end(), "EMAIL"))

        for match in re.finditer(self.phone_pattern, text):
            phone_text = match.group()
            digit_count = sum(c.isdigit() for c in phone_text)
            if digit_count >= 10:
                entities.append((match.start(), match.end(), "PHONE"))

        for match in re.finditer(self.date_pattern, text):
            date_text = match.group()
            if any(char.isdigit() for char in date_text):
                entities.append((match.start(), match.end(), "DATE"))

        for match in re.finditer(self.credit_card_pattern, text):
            card_text = match.group().replace(" ", "").replace("-", "")
            if len(card_text) == 16 and self.luhn_check(card_text):
                entities.append((match.start(), match.end(), "CREDIT_CARD"))

        for match in re.finditer(self.ip_address_pattern, text):
            ip_text = match.group()
            if self.is_valid_ip(ip_text):
                entities.append((match.start(), match.end(), "IP_ADDRESS"))

        return entities

    def luhn_check(self, card_number: str) -> bool:
        try:
            digits = list(map(int, card_number))
            odd_digits = digits[-1::-2]
            even_digits = digits[-2::-2]
            total = sum(odd_digits) + sum(
                sum(divmod(d * 2, 10)) for d in even_digits
            )
            return total % 10 == 0
        except:
            return False

    def is_valid_ip(self, ip: str) -> bool:
        try:
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit() or not 0 <= int(part) <= 255:
                    return False
            return True
        except:
            return False

    def anonymize_text(self, text: str, mode: str = "full") -> str:
        if not text.strip():
            return text

        lang = self.detect_language(text)
        if lang not in self.models:
            lang = 'en'

        doc = self.models[lang](text)
        anonymized_tokens = list(text)

        entities_to_redact = []

        for ent in doc.ents:
            if ent.label_ in ["PER", "PERSON", "ORG", "GPE", "LOC", "FAC"]:
                entities_to_redact.append(
                    (ent.start_char, ent.end_char, ent.label_)
                )

        sensitive_entities = self.find_sensitive_entities(text)
        entities_to_redact.extend(sensitive_entities)

        entities_to_redact.sort(key=lambda x: x[0], reverse=True)

        for start, end, entity_type in entities_to_redact:
            if mode == "full":
                replacement = "*******"
            else:
                replacement = f"[{entity_type}]"

            anonymized_tokens[start:end] = [replacement]

        return "".join(anonymized_tokens)
