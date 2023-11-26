import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout
from django.db.models import Case, When, Value, F


def show_highest_rated_art():
    best_artwork = ArtworkGallery.objects.order_by("-rating", "id").first()

    return f"{best_artwork.art_name} is the highest-rated art with a {best_artwork.rating} rating!"


# artwork1 = ArtworkGallery(artist_name="Vincent van Gogh", art_name="Starry Night", rating=4, price=1200000.0)
# artwork2 = ArtworkGallery(artist_name="Leonardo da Vinci", art_name="Mona Lisa", rating=5, price=1500000.0)


def bulk_create_arts(first_art, second_art):
    ArtworkGallery.objects.bulk_create([
        first_art,
        second_art,
    ])


def delete_negative_rated_arts():
    arts_with_negative_rating = ArtworkGallery.objects.filter(rating__lt=0)

    arts_with_negative_rating.delete()


# delete_negative_rated_arts()


def show_the_most_expensive_laptop():
    best_laptop = Laptop.objects.order_by("-price", "id").first()

    return f"{best_laptop.brand} is the most expensive laptop available for {best_laptop.price}$!"


# laptop1 = Laptop(
#     brand='Asus',
#     processor='Intel Core i5',
#     memory=8,
#     storage=256,
#     operation_system='Windows',
#     price=899.99
# )
#
# laptop2 = Laptop(
#     brand='Apple',
#     processor='Apple M1',
#     memory=16,
#     storage=512,
#     operation_system='MacOS',
#     price=1399.99
#
# )
#
# laptop3 = Laptop(
#     brand='Lenovo',
#     processor='AMD Ryzen 7',
#     memory=12,
#     storage=512,
#     operation_system='Linux',
#     price=999.99,
# )


def bulk_create_laptops(*args):
    Laptop.objects.bulk_create(*args)


# laptops_to_create = [laptop1, laptop2, laptop3]
# bulk_create_laptops(laptops_to_create)

# print(show_the_most_expensive_laptop())


def update_to_512_GB_storage():
    # Laptop.objects.filter(Q(brand="Lenovo") | Q(brand="Asus")).update(storage=512)
    Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)


def update_operation_systems():
    # Laptop.objects.update(
    #     operation_system=Case(
    #         When(brand="Asus", then=Value("Windows")),
    #         When(brand="Apple", then=Value("MacOS")),
    #         When(brand__in=["Dell", "Acer"], then=Value("Linux")),
    #         When(brand="Lenovo", then=Value("Chrome OS")),
    #         default=F("operation_system")
    #     )
    # )

    Laptop.objects.filter(brand__exact="Asus").update(operation_system="Windows")
    Laptop.objects.filter(brand__exact="Apple").update(operation_system="MacOS")
    Laptop.objects.filter(brand__in=["Dell", "Acer"]).update(operation_system="Linux")
    Laptop.objects.filter(brand__exact="Lenovo").update(operation_system="Chrome OS")


def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(*args):
    ChessPlayer.objects.bulk_create(*args)


def delete_chess_players():
    ChessPlayer.objects.filter(title="no title").delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title__exact="GM").update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title__exact="no title").update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")


def grand_chess_title_IM():
    # ChessPlayer.objects.filter(Q(rating__gte=2300) & Q(rating_lt=2400).update(title="IM")
    ChessPlayer.objects.filter(rating__range=[2300, 2399]).update(title="IM")


def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=[2200, 2299]).update(title="FM")


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__range=[0, 2199]).update(title="regular player")


def set_new_chefs():
    Meal.objects.filter(meal_type="Breakfast").update(chef="Gordon Ramsay")
    Meal.objects.filter(meal_type="Lunch").update(chef="Julia Child")
    Meal.objects.filter(meal_type="Dinner").update(chef="Jamie Oliver")
    Meal.objects.filter(meal_type="Snack").update(chef="Thomas Keller")


def set_new_preparation_times():
    Meal.objects.filter(meal_type="Breakfast").update(preparation_time="10 minutes")
    Meal.objects.filter(meal_type="Lunch").update(preparation_time="12 minutes")
    Meal.objects.filter(meal_type="Dinner").update(preparation_time="15 minutes")
    Meal.objects.filter(meal_type="Snack").update(preparation_time="5 minutes")


def update_low_calorie_meals():
    Meal.objects.filter(meal_type__in=["Breakfast", "Dinner"]).update(calories=400)


def update_high_calorie_meals():
    Meal.objects.filter(meal_type__in=["Lunch", "Snack"]).update(calories=700)


def delete_lunch_and_snack_meals():
    Meal.objects.filter(meal_type__in=["Lunch", "Snack"]).delete()


def show_hard_dungeons():
    result = ""

    hard_dungeons = Dungeon.objects.filter(difficulty="Hard").order_by("-location")

    for dungeon in hard_dungeons:
        result += f"{dungeon.name} is guarded by {dungeon.boss_name} who has {dungeon.boss_health} health points!\n"

    return result.rstrip()


def bulk_create_dungeons(*args):
    Dungeon.objects.bulk_create(*args)


def update_dungeon_names():
    Dungeon.objects.filter(difficulty="Easy").update(name="The Erased Thombs")
    Dungeon.objects.filter(difficulty="Medium").update(name="The Coral Labyrinth")
    Dungeon.objects.filter(difficulty="Hard").update(name="The Lost Haunt")


def update_dungeon_bosses_health():
    Dungeon.objects.exclude(difficulty="Easy").update(boss_health=500)


def update_dungeon_recommended_levels():
    Dungeon.objects.filter(difficulty="Easy").update(recommended_level=25)
    Dungeon.objects.filter(difficulty="Medium").update(recommended_level=50)
    Dungeon.objects.filter(difficulty="Hard").update(recommended_level=75)


def update_dungeon_rewards():
    Dungeon.objects.filter(boss_health=500).update(reward="1000 Gold")
    Dungeon.objects.filter(location__startswith="E").update(reward="New dungeon unlocked")
    Dungeon.objects.filter(location__endswith="s").update(reward="Dragonheart Amulet")


def set_new_locations():
    Dungeon.objects.filter(recommended_level=25).update(location="Enchanted Maze")
    Dungeon.objects.filter(recommended_level=50).update(location="Grimstone Mines")
    Dungeon.objects.filter(recommended_level=75).update(location="Shadowed Abyss")


def show_workouts():
    result = ""

    workouts = Workout.objects.filter(workout_type__in=["Calisthenics", "CrossFit"])

    for workout in workouts:
        result += f"{workout.name} from {workout.workout_type} type has {workout.difficulty} difficulty!\n"

    return result.rstrip()


def get_high_difficulty_cardio_workouts():
    return Workout.objects.filter(workout_type__exact="Cardio", difficulty="High").order_by("instructor")


def set_new_instructors():
    Workout.objects.filter(workout_type__exact="Cardio").update(instructor="John Smith")
    Workout.objects.filter(workout_type__exact="Strength").update(instructor="Michael Williams")
    Workout.objects.filter(workout_type__exact="Yoga").update(instructor="Emily Johnson")
    Workout.objects.filter(workout_type__exact="CrossFit").update(instructor="Sarah Davis")
    Workout.objects.filter(workout_type__exact="Calisthenics").update(instructor="Chris Heria")


def set_new_duration_times():
    Workout.objects.filter(instructor__exact="John Smith").update(duration="15 minutes")
    Workout.objects.filter(instructor__exact="Sarah Davis").update(duration="30 minutes")
    Workout.objects.filter(instructor__exact="Chris Heria").update(duration="45 minutes")
    Workout.objects.filter(instructor__exact="Michael Williams").update(duration="1 hour")
    Workout.objects.filter(instructor__exact="Emily Johnson").update(duration="1 hour and 30 minutes")


def delete_workouts():
    Workout.objects.exclude(workout_type__in=["Strength", "Calisthenics"]).delete()