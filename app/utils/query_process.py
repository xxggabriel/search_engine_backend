import re
import spacy
from spellchecker import SpellChecker
import nltk


nltk.download('punkt')
spacy.cli.download("en_core_web_sm")


class BaseProcessQuery:
    def __init__(self):
        self.spell_checker = SpellChecker()
        self.nlp = spacy.load('en_core_web_sm')


    def normalize(self, query):
        query = query.lower()
        query = re.sub(r'[^\w\s]', '', query)
        return query

    def breakdown_query(self, query):
        terms = nltk.word_tokenize(query)
        return terms

    def identify_entities_and_concepts(self, terms):
        doc = self.nlp(" ".join(terms))
        entities = [ent.text for ent in doc.ents]
        concepts = [token.lemma_ for token in doc if not token.is_stop]
        return entities, concepts

    def disambiguate_and_correct(self, terms):
        corrected_terms = [self.spell_checker.correction(term) for term in terms]
        return corrected_terms

    def query_expansion(self, terms):
        expanded_query = " ".join(terms)
        return expanded_query

    def reconstruct_query(self, terms):
        reconstructed_query = " ".join(terms)
        return reconstructed_query

    def process(self, query):
        normalized_query = self.normalize(query)
        terms = self.breakdown_query(normalized_query)
        entities, concepts = self.identify_entities_and_concepts(terms)
        corrected_terms = self.disambiguate_and_correct(terms)
        expanded_query = self.query_expansion(corrected_terms)
        reconstructed_query = self.reconstruct_query(expanded_query)
        return reconstructed_query, entities, concepts
