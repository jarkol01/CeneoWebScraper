from app.utils import get_item
from app.paremeters import selectors

class Opinion():
    def __init__(self, opinion_id, author, recommendation, stars, content, useful, useless, published, purchased, pros, cons):
        self.opinion_id = opinion_id
        self.author = author
        self.recommendation = recommendation
        self.stars = stars
        self.content = content
        self.useful = useful
        self.useless = useless
        self.published = published
        self.purchased = purchased
        self.pros = pros
        self.cons = cons
    def extract_opinion(self, opinion):
        for key, value in selectors.items():
            setattr(self, key, get_item(opinion, *value))
        self.opinion_id = opinion["data-entry-id"]
        return self
    def __str__(self):
        pass
    def __repr_(self):
        pass
    def to_dict(self):
        pass