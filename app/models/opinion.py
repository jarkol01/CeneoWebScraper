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
        return f"{self.opinion_id}, {self.author}, {self.recommendation}, {self.stars}, {self.content}, {self.useful}, {self.useless}, {self.published}, {self.purchased}, {self.pros}, {self.cons}"
    def __repr_(self):
        return f'Opinion("{self.opinion_id}","{self.author}","{self.recommendation}","{self.stars}","{self.content}","{self.useful}","{self.useless}","{self.published}","{self.purchased}",,"{self.pros}","{self.cons}")'
    def to_dict(self) -> dict:
        return {
            "opinion_id": self.opinion_id,
            "author": self.author,
            "recommendation": self.recommendation,
            "stars": self.stars,
            "content": self.content,
            "useful": self.useful,
            "useless": self.useless,
            "published": self.published,
            "purchased": self.purchased,
            "pros": self.pros,
            "cons": self.cons
        }
