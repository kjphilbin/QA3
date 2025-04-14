Quiz Bowl Application:

Description:
The Quiz Bowl Application is a Python-based project that allows administrators to manage quiz questions and users to take quizzes on various topics. The application features a graphical user interface (GUI) built with Tkinter and includes functionality for database management using SQLite. This project was created to showcase capabilities in Python programming, GUI design, and database integration.

Features:
For Administrators:
Login Access: Administrators can securely log in using a password.
Add Questions: Add new multiple-choice questions to specific categories (courses).
View Questions: View the current list of questions stored in the database for each category.
Modify/Delete Questions: Update or remove questions from the database.

For Quiz Takers:
Course Selection: Users can select a course to begin the quiz.
Quiz Interface: Take quizzes with 10 randomly loaded questions from the selected category.
Score Tracking: Users can view their final score upon completing the quiz.

Technologies Used:
Python: The core programming language used for this application.
Tkinter: For building the graphical user interface.
SQLite: For database management and storage of quiz questions.

Each table stores the following fields:
id: Unique identifier for each question
question: The text of the question
option1, option2, option3, option4: Multiple-choice options
correct_option: The correct answer (1-4)

Preloaded Questions
The database includes preloaded questions for testing the application. Additional questions can be added using the "Add Questions" feature in the administrator panel.
