class Person:
    
    def __init__(self, name):
       
        if not isinstance(name, str) or not name:
            raise ValueError("Person must have a non-empty name.")
            
        self.name = name
        self.friends = []
        
    def __repr__(self):
        return f"Person(name='{self.name}', friends={len(self.friends)})"

    def add_friend(self, friend):
        
        if not isinstance(friend, Person):
            raise TypeError("Only Person objects can be added as friends.")
        
        if friend is self:
            raise ValueError("You can't friend yourself. That's what mirrors are for.")
            
        if friend not in self.friends:
            self.friends.append(friend)
            print(f"SUCCESS: {self.name} and {friend.name} are now friends.")
        else:
            print(f"NOTE: {friend.name} is already friends with {self.name}.")
            
# --- Example Usage ---

if __name__ == "__main__":
    
    print("--- Person Class Test ---")
    
   
    alice = Person("Alice")
    bob = Person("Bob")
    charlie = Person("Charlie")
    
    print(alice)
    
   
    alice.add_friend(bob)
    bob.add_friend(alice) 

  
    alice.add_friend(charlie)
    
   
    print(f"\nAlice's friends list length: {len(alice.friends)}")
    print(f"Bob's friends list length: {len(bob.friends)}")
    
    print("\n--- Edge Case Test ---")
    try:
        alice.add_friend(alice)
    except ValueError as e:
        print(f"Caught expected error: {e}")
        
    try:
        alice.add_friend("Dave")
    except TypeError as e:
        print(f"Caught expected error: {e}")


class SocialNetwork:
   
    def __init__(self):
       
        self.people = {}

    def add_person(self, name):
        
        if name in self.people:
            print(f"NOTE: {name} is already in the network.")
            return

        new_person = Person(name)
        self.people[name] = new_person
        print(f"ADDED: {name} has joined the network.")

    def add_friendship(self, person1_name, person2_name):
       
        if person1_name == person2_name:
            print(f"ERROR: Friendship attempt failed. {person1_name} tried to friend themselves.")
            return
            
        person1 = self.people.get(person1_name)
        person2 = self.people.get(person2_name)

        if not person1:
            print(f"ERROR: Could not find user '{person1_name}' in the network.")
            return
        
        if not person2:
            print(f"ERROR: Could not find user '{person2_name}' in the network.")
            return

       
        p1_added = person1.add_friend(person2)
        p2_added = person2.add_friend(person1) 
        
        if p1_added or p2_added:
            print(f"FRIENDSHIP ESTABLISHED: {person1_name} and {person2_name} are now connected.")
        else:
            print(f"NOTE: {person1_name} and {person2_name} were already friends.")


    def print_network(self):
        
        if not self.people:
            print("The social network is currently empty.")
            return

        print("\n--- Social Network Connections ---")
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name:<10}: {friend_names}")
        print("----------------------------------")

# --- Example Usage ---

if __name__ == "__main__":
    
    network = SocialNetwork()
    
    
    network.add_person("Alice")
    network.add_person("Bob")
    network.add_person("Charlie")
    network.add_person("David")
    network.add_person("Eve")
    
    
    print("\n--- Establishing Friendships ---")
    network.add_friendship("Alice", "Bob")
    network.add_friendship("Alice", "Charlie")
    network.add_friendship("Charlie", "David")
    
    
    network.add_friendship("Alice", "Charlie")

    
    network.add_friendship("Frank", "Alice") 
    network.add_friendship("David", "David") 

    
    network.print_network()
    
    # Expected output:
    # Alice     : ['Bob', 'Charlie']
    # Bob       : ['Alice']
    # Charlie   : ['Alice', 'David']
    # David     : ['Charlie']
    # Eve       : []



