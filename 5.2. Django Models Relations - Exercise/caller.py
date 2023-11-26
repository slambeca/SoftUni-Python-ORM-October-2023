import os
from datetime import date, timedelta

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Artist, Song, Product, Review, DrivingLicense, Driver, Owner, Registration, \
    Car


def show_all_authors_with_their_books() -> str:
    result = ""

    all_authors = Author.objects.order_by("id")    # better way to do it with prefetch

    for author in all_authors:
        books = Book.objects.filter(author=author)
        # books = Author.book_set.all()

        if books:
            book_titles = ", ".join([book.title for book in books])
            result += f"{author.name} has written - {book_titles}!\n"

    return result.rstrip()

# # Create authors
# author1 = Author.objects.create(name="J.K. Rowling")
# author2 = Author.objects.create(name="George Orwell")
# author3 = Author.objects.create(name="Harper Lee")
# author4 = Author.objects.create(name="Mark Twain")
#
# # Create books associated with the authors
# book1 = Book.objects.create(
#     title="Harry Potter and the Philosopher's Stone",
#     price=19.99,
#     author=author1
# )
# book2 = Book.objects.create(
#     title="1984",
#     price=14.99,
#     author=author2
# )
#
# book3 = Book.objects.create(
#     title="To Kill a Mockingbird",
#     price=12.99,
#     author=author3
# )

# authors_with_books = show_all_authors_with_their_books()
# print(authors_with_books)


def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()


# Delete authors without books
# delete_all_authors_without_books()
# print(Author.objects.count())


def add_song_to_artist(artist_name, song_title):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)    # Add the song to the artists collection


def get_songs_by_artist(artist_name):
    artist = Artist.objects.get(name=artist_name)

    return artist.songs.all().order_by("-id")    # return all the songs from a particular artist


def remove_song_from_artist(artist_name, song_title):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)    # We are removing the relation, not the song


def calculate_average_rating_for_product_by_name(product_name):
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()

    total_rating = sum(review.rating for review in reviews)
    average_rating = total_rating / len(reviews)

    return average_rating


# Create some products
# product1 = Product.objects.create(name="Laptop")
# product2 = Product.objects.create(name="Smartphone")
# product3 = Product.objects.create(name="Headphones")
# product4 = Product.objects.create(name="PlayStation 5")
#
# # Create some reviews for products
# review1 = Review.objects.create(description="Great laptop!", rating=5, product=product1)
# review2 = Review.objects.create(description="The laptop is slow!", rating=2, product=product1)
# review3 = Review.objects.create(description="Awesome smartphone!", rating=5, product=product2)


# print(calculate_average_rating_for_product_by_name("Laptop"))

def get_reviews_with_high_ratings(threshold):    # return the reviews with higher or equal rating to
    reviews = Review.objects.filter(rating__gte=threshold)

    return reviews


# print(get_reviews_with_high_ratings(1))


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by("-name")


# products_without_reviews = get_products_with_no_reviews()
# print(f"Products without reviews: {', '.join([p.name for p in products_without_reviews])}")


def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates():
    result = ""
    all_driving_licences = DrivingLicense.objects.order_by("-license_number")

    for driving_license in all_driving_licences:
        result += str(driving_license) + "\n"

    return result.rstrip()


# driver1 = Driver.objects.create(first_name="Tanya", last_name="Petrova")
# driver2 = Driver.objects.create(first_name="Ivan", last_name="Yordanov")
#
# license1 = DrivingLicense.objects.create(license_number="123", issue_date=date(2022, 10, 6), driver=driver1)
# license2 = DrivingLicense.objects.create(license_number="456", issue_date=date(2022, 1, 1), driver=driver2)

# expiration_dates = calculate_licenses_expiration_dates()
# print(expiration_dates)

def get_drivers_with_expired_licenses(due_date):
    expiration_cutoff_date = due_date - timedelta(days=365)

    expired_drivers = Driver.objects.filter(drivinglicense__issue_date__gt=expiration_cutoff_date)

    return expired_drivers


def register_car_by_owner(owner: Owner):
    car = Car.objects.filter(registration__isnull=True).first()
    registration = Registration.objects.filter(car__isnull=True, owner=owner).first()

    car.owner = owner
    car.registration = registration

    car.save()

    registration.registration_date = date.today()    # Judge will test with .today()
    registration.car = car

    registration.save()

    return (f"Successfully registered {car.model} to {owner.name} with registration number "
            f"{registration.registration_number}.")