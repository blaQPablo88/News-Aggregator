# News Aggregator

## API: [NewsAPI] https://newsapi.org/

### Description:
The project is a news aggregator app that fetches articles from various sources using NewsAPI. It categorizes news by user interests (e.g., technology, sports) and allows browsing headlines, publication dates, and summaries, with links to full articles. The goal is to simplify staying updated on preferred news topics.

### Key Features:

- Fetch news articles from multiple categories and sources.
- Display headlines, publication dates, and summaries.
- Provide an option to read full articles via external links.

## Iterations:

### Iteration 1: Basic News Fetching
'
- Successfully authenticate and connect to the NewsAPI.
- Fetch news articles from a chosen category (e.g., sports, technology).
- Display the article titles and publication dates in a simple console or basic web interface.(still the first week so showing on the console would be okay)


### Iteration 2: Keyword Filtering

- Implement functionality that allows users to input keywords for filtering articles.
- Display filtered articles that match user search criteria.
- Enhance the user interface to include a search bar for keyword input, making it easy for users to filter articles by topics of interest.

### Iteration 3: User Favorites and Categories

- Allow users to create an account or use a simple system to save favorite articles.(for the specific user, so when I log in, my favourite articles that were saved in the previous session should still be there)
- Implement functionality to categorize saved articles and view them in a dedicated section.
- Provide a more polished user experience and ensure the application is user-friendly and visually appealing.(nothing too hectic though)

### Last Note

To run this project, create a `.env` file in the root directory and add your API key:
NEWS_API_KEY=your_api_key_here