import json
import os
import heapq
import datetime
import plotly.graph_objects as go
from collections import defaultdict
import recommendation_system

DATA_FILE = "adventure_tracker.json"

ADVENTURE_CATEGORIES = [
    "RoadTrip", "Movie_Night", "Foodie_Tour", "Gaming_Session", 
    "Concert", "Hiking", "Beach_Day", "Shopping_Spree"
]

class SocialAdventureTracker:
    def __init__(self):
        self.adventures = defaultdict(lambda: defaultdict(int))
        self.load_data()

    def load_data(self):
        """Load adventure data from the JSON file."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                self.adventures = defaultdict(lambda: defaultdict(int), json.load(f))
        else:
            print("Starting fresh! No previous adventure data found.")

    def save_data(self):
        """Save adventure data to the JSON file."""
        with open(DATA_FILE, 'w') as f:
            json.dump(self.adventures, f)

    def log_adventure(self, friends, category):
        """Records an adventure with friends."""
        if category not in ADVENTURE_CATEGORIES:
            print("Invalid category! Please select a valid adventure type.")
            return
    
        date = datetime.date.today().strftime("%Y-%m-%d")
        
        for i in range(len(friends)):
            for j in range(i + 1, len(friends)):
                user1, user2 = friends[i], friends[j]
                
                self.adventures[date][f"{user1}-{user2}-{category}"] += 1
                self.adventures[date][f"{user2}-{user1}-{category}"] += 1
                
                print(f"Logging adventure: {user1}-{user2}-{category}")

        self.save_data()
        print(f"Adventure '{category}' logged for {date}!")


    def get_top_adventure_buddies(self, user):
        """Get the top 3 friends for adventures."""
        friend_counts = defaultdict(int)
        for date in self.adventures:
            for key, count in self.adventures[date].items():
                friend1, friend2, category = key.split('-')
                if friend1 == user:
                    friend_counts[friend2] += count
                elif friend2 == user:
                    friend_counts[friend1] += count

        if not friend_counts:
            print(f"No adventures found for {user}.")
            return []

        top_3 = heapq.nlargest(3, friend_counts.items(), key=lambda x: x[1])
        return [friend for friend, _ in top_3]

    def show_adventure_history(self, date):
        """Display all adventures on a specific date."""
        if date in self.adventures:
            print(f"Adventures on {date}:")
            for key, count in self.adventures[date].items():
                friend1, friend2, category = key.split('-')
                print(f"{friend1} and {friend2} went for a '{category}' {count} times.")
        else:
            print(f"No adventures found on {date}.")

    def visualize_adventure_trends(self, user):
        """Visualize adventure trends over time."""
        category_counts = defaultdict(int)
    
        for date in sorted(self.adventures):
            for key, count in self.adventures[date].items():
                if user in key:
                    _, _, category = key.split('-')
                    category_counts[category] += count

        if not category_counts:
            print(f"No adventure data available for {user}.")
            return

        categories = list(category_counts.keys())
        counts = list(category_counts.values())

        fig = go.Figure(data=[go.Bar(x=categories, y=counts)])
        fig.update_layout(
            title=f'Adventure Trend for {user}',
            xaxis_title='Adventure Type',
            yaxis_title='Number of Adventures',
            xaxis_tickangle=30,
        )
        fig.show()


    def unlock_badges(self, user):
        """Check and unlock achievements for the user."""
        adventure_count = sum(
            count for date in self.adventures for key, count in self.adventures[date].items() if user in key
        )

        if adventure_count >= 10:
            print(f"🎖️ Congrats {user}, you've earned the 'Adventurer' badge!")
        if adventure_count >= 20:
            print(f"🏆 Wow {user}, you're an 'Explorer' now!")
        if adventure_count >= 50:
            print(f"🌍 Ultimate Traveler Badge Unlocked!")


def main():
    tracker = SocialAdventureTracker()

    while True:
        print("\nSocial Adventure Tracker")
        print("--------------------------")
        print("1. Log a new adventure")
        print("2. View top 3 adventure buddies")
        print("3. View adventure history")
        print("4. Visualize adventure trends")
        print("5. Unlock achievements")
        print("6. Recommended activities")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")

        if choice == '1':
            users = input("Enter friend names separated by spaces (e.g., A B C): ").split()
            print(f"Available categories: {', '.join(ADVENTURE_CATEGORIES)}")
            category = input("Choose an adventure category: ")
            if len(users) < 2:
                print("You need at least two friends to log an adventure.")
            else:
                tracker.log_adventure(users, category)

        elif choice == '2':
            user = input("Enter your name to find your top adventure buddies: ")
            top_buddies = tracker.get_top_adventure_buddies(user)
            if top_buddies:
                print(f"🏅 Top 3 adventure buddies for {user}: {top_buddies}")

        elif choice == '3':
            date = input("Enter the date (YYYY-MM-DD) to view adventure history: ")
            tracker.show_adventure_history(date)

        elif choice == '4':
            user = input("Enter your name to visualize adventure trends: ")
            tracker.visualize_adventure_trends(user)

        elif choice == '5':
            user = input("Enter your name to check achievements: ")
            tracker.unlock_badges(user)

        elif choice == '6':
            recommendation_system.get_adventure_recommendations()

        elif choice == '7':
            print("Goodbye! Keep adventuring!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
