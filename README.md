
# BuddyQuest

BuddyQuest is your ultimate adventure tracker! Whether you're hiking, gaming, or going on a foodie spree, BuddyQuest helps you log your adventures, discover trends, and unlock achievements with your friends. Turn your everyday hangouts into epic quests! 

---

## Features  

- **Log Adventures**: Keep track of your fun activities with friends.  
- **Top Adventure Buddies**: See who your best quest partners are.  
- **Adventure History**: Relive your favorite shared moments.  
- **Trends and Insights**: Visualize your adventures over time.  
- **Achievements**: Unlock badges as you complete more quests.  
- **Activity Recommendations**: Get personalized suggestions based on your history.  

---

## How It Works  

1. **Log Adventures**: Add friends and select an activity category.  
2. **View Trends**: Check your top buddies, activity history, and adventure stats.  
3. **Level Up**: Unlock achievements as you complete more adventures.  
4. **Get Inspired**: Find new adventures based on past activities.  

### Data Flow Diagram  
```plaintext
User Input --> Adventure Logger --> Adventure Database --> Insights and Recommendations  
```

---

## Data Structure  

BuddyQuest uses a dictionary-based data structure to efficiently store and manage adventures.  

### Storage Format  

```python
adventures = {
    "YYYY-MM-DD": {  # Date as the primary key
        "User1-User2-Category": Count  # User pairs, activity category, and count
    }
}
```

### Example Data  

The adventures are stored in a dictionary with dates as keys. Each date contains another dictionary with adventure keys, which are unique strings combining the user pair and the activity category (e.g., `A-B-Hiking`). The count represents how many times that specific activity was logged on that day.

Example data for two days:

```python
{
    "2025-01-24": {
        "A-B-Hiking": 2,
        "A-C-RoadTrip": 1
    },
    "2025-01-25": {
        "A-B-Foodie_Tour": 1,
        "B-C-Gaming_Session": 3
    }
}
```

**Explanation:**

- On **2025-01-24**, the adventure `A-B-Hiking` was logged **2 times**, while `A-C-RoadTrip` was logged **1 time**.
- On **2025-01-25**, the adventure `A-B-Foodie_Tour` was logged **1 time**, and `B-C-Gaming_Session` was logged **3 times**.
 

---

## Computational Complexity  

| **Parameter**          | **Symbol** | **Definition**                                                                                   |
|-------------------------|------------|---------------------------------------------------------------------------------------------------|
| Number of Users         | `U`        | Total number of users in the system.                                                             |
| User Connections (Pairs)| `C`        | Number of unique user pairs, calculated as `C = U * (U - 1) / 2`.                                 |
| Logged Adventures       | `k`        | Total number of logged activities across all users and pairs.                                     |
| Daily Entries           | `D`        | Number of unique adventures logged per day (proportional to active users).                       |
| Space Required          | `S`        | Total storage required for the adventure data.                                                   |

---

### Storage Computation  

For `U` users, the total number of unique connections `C` is calculated as:  

![image](https://github.com/user-attachments/assets/196e18c7-de61-46de-af4a-86816ae05dd5)


If each user logs k adventures daily, the total storage required is proportional to:

![image](https://github.com/user-attachments/assets/b0d3c14e-76c3-4089-9901-3a458b0aa125)


| Users (U) | Connections (C) | Daily Adventures (D) | Estimated Storage |
|-----------|-----------------|-----------------------|-------------------|
| 10        | 45              | 50                    | ~5 KB             |
| 100       | 4,950           | 500                   | ~50 KB            |
| 1,000     | 499,500         | 5,000                 | ~500 KB           |
| 10,000    | 49,995,000      | 50,000                | ~5 MB             |


---

## Visual Representation

### Growth of Connections with Users

```
Connections (C) = U * (U - 1) / 2  

    U -> Users
    C -> Connections
```

Daily Adventures Logged

D = Active Users × k

Example: 1,000 users logging 5 adventures daily each = 5,000 daily entries.

---

## Scalability

### Challenges
- Large User Base: As users grow, the number of connections increases quadratically.
- Frequent Updates: Logging real-time adventures for many users can be intensive.
- Storage Overhead: Adventure data can grow large, especially with high activity levels.

### Optimizations
- Efficient Storage: Group adventures by date to minimize redundancy.
- Archiving: Periodically summarize or archive older data to save space.
- Lookup Efficiency: Use dictionaries for fast O(1) access to user-pair adventures.

---

## Getting Started  

To run BuddyQuest on your machine:  

1. Clone the repository:  

   ```bash
   git clone https://github.com/Kiinitix/BuddyQuest
   ```

2. Navigate into the project directory:  

   ```bash
   cd buddyquest
   ```

3. Install dependencies:  

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:  

   ```bash
   python main.py
   ```

---

## Example Usage
```
Welcome to BuddyQuest!   
-------------------------  
1. Log a new adventure  
2. View top 3 adventure buddies  
3. View adventure history  
4. Visualize adventure trends  
5. Unlock achievements  
6. Recommended activities  
7. Exit  
Choose an option (1-7): 1  
Enter friend names separated by spaces (e.g., A B C): A B  
Available categories: RoadTrip, Movie_Night, Foodie_Tour, Gaming_Session, Concert, Hiking, Beach_Day, Shopping_Spree  
Choose an adventure category: Hiking  
Logging adventure: A-B-Hiking  
Adventure 'Hiking' logged for 2025-01-24!  
```

## Future Enhancements

- Add leaderboard rankings for achievements.
- Integrate social sharing for your quests.
- Introduce advanced trend visualization.

---

## Contributing  

We welcome contributions to BuddyQuest! If you'd like to help, please follow these steps:  

1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/your-feature`).  
3. Make your changes and commit them (`git commit -am 'Add new feature'`).  
4. Push your branch to your forked repository (`git push origin feature/your-feature`).  
5. Open a pull request.  

---

