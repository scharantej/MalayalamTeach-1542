## Flask Application Design for Teaching Malayalam

### HTML Files
- **index.html**: The homepage of the website. It displays general information about the purpose of the site and provides links to the lessons.
- **lessons.html**: Lists all the Malayalam lessons available. Each lesson is linked to its respective lesson page.
- **lessonX.html**: Individual lesson pages. Each lesson page includes the lesson content, such as grammar explanations, vocabulary, and exercises.

### Routes

- **Index Route (/)**: This route handles the homepage. It renders the `index.html` file, displaying information about the website.

- **Lessons Route (/lessons)**: This route displays the list of available lessons. It renders the `lessons.html` file, populating it with a list of lessons and their links.

- **Lesson Route (/lesson/<lesson_number>)**: This route handles individual lesson pages. It takes the lesson number as a parameter and renders the corresponding lesson page (`lessonX.html`), populating it with the lesson content.