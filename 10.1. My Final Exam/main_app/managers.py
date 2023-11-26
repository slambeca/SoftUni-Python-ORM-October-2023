from django.db import models


class AuthorManager(models.Manager):
    def get_authors_by_article_count(self):
        return self.annotate(
            count_articles=models.Count("authors_articles")
        ).order_by(
            "-count_articles", "email"
        )