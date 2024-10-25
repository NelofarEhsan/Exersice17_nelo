


from db import create_tables, insert_category, insert_movie, get_categories, get_movies_by_category
from objects import Category, Movie

def display_menu():
    print("\nCommand Menu")
    print("1 - View movies by category")
    print("2 - View movies by year")
    print("3 - Add a movie")
    print("4 - Delete a movie")
    print("5 - Exit")

def display_categories():
    print("\nCategories:")
    categories = get_categories()
    for category in categories:
        print(f"{category[0]} - {category[1]}")

def display_movies(category_id):
    print("\nMovies:")
    movies = get_movies_by_category(category_id)
    for movie in movies:
        print(f"{movie[0]:<5} {movie[1]:<30} {movie[2]:<6} {movie[3]:<4} mins")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    create_tables()
    
    while True:
        display_menu()
        choice = get_int_input("Choose a command: ")
        
        if choice == 1:
            display_categories()
            category_id = get_int_input("Choose a category: ")
            display_movies(category_id)
        elif choice == 3:
            name = input("Enter movie name: ")
            year = get_int_input("Enter movie year: ")
            minutes = get_int_input("Enter movie length in minutes: ")
            display_categories()
            category_id = get_int_input("Enter category ID: ")
            insert_movie(name, year, minutes, category_id)
            print("Movie added successfully!")
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

