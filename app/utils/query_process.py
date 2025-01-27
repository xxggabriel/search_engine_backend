import re
import spacy
# import spellchecker
import nltk


# nltk.download('punkt')
# spacy.cli.download("pt_core_news_sm")


class BaseProcessQuery:
    def __init__(self):
        # self.spell_checker = spellchecker.Spellchecker()
        self.nlp = spacy.load('pt_core_news_sm')


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

    # def disambiguate_and_correct(self, terms):
    #     corrected_terms = [self.spell_checker.correction(term) for term in terms]
    #     return corrected_terms

    def query_expansion(self, terms):
        expanded_query = " ".join(terms)
        return expanded_query

    def reconstruct_query(self, terms):
        terms = terms.split()
        doc = self.nlp(" ".join(terms))
        reconstructed_terms = [token.text for token in doc if not token.is_stop]
        return reconstructed_terms

    def process(self, query: str):
        """
        Processa a query realizando as seguintes etapas:
         - normalização
         - tokenização
         - identificação de entidades e conceitos
         - correção ortográfica
         - expansão e reconstrução da query
        Retorna a query reconstruída (lista de termos) juntamente com as entidades e conceitos.
        """
        normalized_query = self.normalize(query)
        terms = self.breakdown_query(normalized_query)
        entities, concepts = self.identify_entities_and_concepts(terms)
        # corrected_terms = self.disambiguate_and_correct(terms)
        corrected_terms = terms
        expanded_query = self.query_expansion(corrected_terms)
        reconstructed_terms = self.reconstruct_query(expanded_query)
        return reconstructed_terms, entities, concepts
