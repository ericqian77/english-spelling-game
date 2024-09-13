# English Spelling Game

An interactive web-based spelling game for children using Flask and Vanilla JS with a 3x3 word grid and theme-based challenges.

## Features

- Theme-based word challenges
- 3x3 grid of words to guess
- Hint system with points
- Attempt tracking
- Responsive design

## Technologies Used

- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript (Vanilla)
- Database: SQLAlchemy with PostgreSQL

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/english-spelling-game.git
   cd english-spelling-game
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up the database:
   - Ensure you have PostgreSQL installed and running
   - Set the following environment variables:
     - PGHOST
     - PGPASSWORD
     - PGDATABASE
     - PGPORT
     - PGUSER
     - DATABASE_URL

4. Initialize the database:
   ```
   python database.py
   ```

5. Run the application:
   ```
   python main.py
   ```

6. Open a web browser and navigate to `http://localhost:5000` to play the game.

## How to Play

1. When you start the game, you'll see a 3x3 grid of hidden words and a theme.
2. Type a word that you think matches the theme and is in the grid.
3. Submit your guess. If correct, the word will be revealed on the grid.
4. You can use hints by clicking the "Get Hint" button, which costs 3 hint points.
5. Try to guess all 9 words with as few attempts as possible!

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
