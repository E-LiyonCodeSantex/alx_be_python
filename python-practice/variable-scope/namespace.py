# Namespace Exploration

def count_items():
    count = 5  # Local to count_items
    print("Counting items:", count)

def log_events():
    count = "Five events logged"  # Local to log_events
    print("Logging events:", count)

# Call both functions
count_items()
log_events()


