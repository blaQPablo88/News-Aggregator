
import tkinter as tk


# Create the main window
root = tk.Tk()
root.title("News World")
root.geometry("600x500")

# Top Frame (Search Bar)
top_frame = tk.Frame(root, bg="black", padx=10)
top_frame.pack(side=tk.TOP, fill=tk.BOTH)

# search_label = tk.Label(top_frame, text="Search:", bg="orange", font=("Arial", 12))
# search_label.pack(side=tk.LEFT, padx=10)

search_entry = tk.Entry(top_frame, font=("Roboto", 12), width=40)
search_entry.pack(side=tk.LEFT, padx=18)

search_button = tk.Button(top_frame, text="Search", font=("Roboto", 12), bg="skyblue", fg="black")
search_button.pack(side=tk.LEFT, padx=10)

# Middle Frame (Trending News Section)
middle_frame = tk.Frame(root, bg="white", pady=10)
middle_frame.pack(side=tk.LEFT, fill=tk.Y, expand=False)  # expand to accomodate more trending news

news_label = tk.Label(middle_frame, text="Trending:", bg="white", font=("Roboto", 14, "bold"))
news_label.pack(anchor="w", padx=10, pady=10)

top_story_frame = tk.Frame(root, bg="white")
top_story_frame.pack(side=tk.LEFT, padx=5)

# righ side
right_frame = tk.Frame(root, bg="white", width=100)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)

# separate with a vertical line
separator = tk.Frame(root, bg="black", width=2, height=50)
separator.pack(side=tk.RIGHT, fill=tk.Y)

home_button = tk.Button(right_frame, text="Home", font=("Roboto", 12), bg="lightgray")
home_button.pack(pady=10, fill=tk.X)

saved_button = tk.Button(right_frame, text="Saved Articles", font=("Roboto", 12), bg="lightgray")
saved_button.pack(pady=10)

for i in range(10): # for story in news (list of news)
    new_story = tk.Label(middle_frame, text=f"News Article {i + 1}", bg="white", font=("Roboto", 12), anchor="w")
    new_story.pack(fill=tk.X, pady=5, padx=10)

root.mainloop()



	
