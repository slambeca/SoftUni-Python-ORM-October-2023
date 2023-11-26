import os
import django
from django.db.models import Q, Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Author, Article, Review


def get_authors(search_name=None, search_email=None):
    if search_name is not None and search_email is not None:
        searched_authors = Author.objects.filter(
            Q(full_name__icontains=search_name)
            &
            Q(email__icontains=search_email)
        ).order_by("-full_name")
    elif search_name is not None:
        searched_authors = Author.objects.filter(
            Q(full_name__icontains=search_name)
        ).order_by("-full_name")
    elif search_email is not None:
        searched_authors = Author.objects.filter(
            Q(email__icontains=search_email)
        ).order_by("-full_name")
    else:
        return ""

    if not searched_authors.exists():
        return ""

    result = ""
    for author in searched_authors:
        author_status = "Banned" if author.is_banned else "Not Banned"
        result += f"Author: {author.full_name}, email: {author.email}, status: {author_status}\n"

    return result.strip()


# print(get_authors(1))

def get_top_publisher():
    authors = Author.objects.annotate(count_articles=Count("authors_articles")).order_by("-count_articles", "email")

    if not authors or authors.first().count_articles == 0:
        return ""

    author = authors.first()

    return f"Top Author: {author.full_name} with {author.count_articles} published articles."


# print(get_top_publisher())

def get_top_reviewer():
    authors = Author.objects.annotate(count_reviews=Count("author_reviews")).order_by("-count_reviews", "email")

    if not authors or authors.first().count_reviews == 0:
        return ""

    author = authors.first()

    return f"Top Reviewer: {author.full_name} with {author.count_reviews} published reviews."


# print(get_top_reviewer())

def get_latest_article():
    searched_article = Article.objects.order_by("-published_on").first()

    if not searched_article:
        return ""

    authors_of_article = searched_article.authors.all().order_by("full_name")

    author_names = ", ".join([author.full_name for author in authors_of_article])

    count_reviews = Review.objects.filter(article=searched_article).count()
    average_rating = Review.objects.filter(article=searched_article).aggregate(Avg('rating'))['rating__avg']

    if average_rating is None:
        average_rating = 0.0

    return (
        f"The latest article is: {searched_article.title}. "
        f"Authors: {author_names}. "
        f"Reviewed: {count_reviews} times. "
        f"Average Rating: {average_rating:.2f}."
    )


# print(get_latest_article())
def get_top_rated_article():
    articles = Article.objects.filter(article_reviews__isnull=False)

    if not articles:
        return ""

    filtered_articles = articles.annotate(
        average_rating=Avg('article_reviews__rating'),
        num_of_reviews=Count('article_reviews')
    )

    top_rated_articles = filtered_articles.order_by('-average_rating', 'title')

    top_rated_article = top_rated_articles.first()

    if not top_rated_article:
        return ""

    count_reviews = top_rated_article.num_of_reviews

    if top_rated_article.average_rating is None:
        average_rating = 0
    else:
        average_rating = top_rated_article.average_rating

    return (
        f"The top-rated article is: {top_rated_article.title}, "
        f"with an average rating of {average_rating:.2f}, reviewed {count_reviews} times."
    )


# print(get_top_rated_article())


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    searched_author = Author.objects.filter(email=email).first()

    if not searched_author:
        return "No authors banned."

    count_author_reviews = Review.objects.filter(author=searched_author).count()

    Review.objects.filter(author=searched_author).delete()

    searched_author.is_banned = True
    searched_author.save()

    result = f"Author: {searched_author.full_name} is banned! {count_author_reviews} reviews deleted."

    return result


# print(ban_author())