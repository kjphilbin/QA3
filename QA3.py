import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
def initialize_database():
    conn = sqlite3.connect("quiz_bowl.db")
    cursor = conn.cursor()
    # Create tables for each specified course category
    courses = ["ApplicationsDevelopment", "BusinessLaw", "DataAnalytics", "DatabaseManagement"]
    for course in courses:
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {course} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                option1 TEXT NOT NULL,
                option2 TEXT NOT NULL,
                option3 TEXT NOT NULL,
                option4 TEXT NOT NULL,
                correct_option INTEGER NOT NULL
            )
        """)
    conn.commit()
    conn.close()

    def preload_questions():
        conn = sqlite3.connect("quiz_bowl.db")
        cursor = conn.cursor()

        # Define the questions for each course
        questions = {
            "ApplicationsDevelopment": [
                ("What is the purpose of object-oriented programming?", 
                 "To write reusable code", "To execute faster code", "To store large datasets", 
                 "To design user interfaces", 1),
                ("Which programming language is primarily used for Android app development?", 
                 "Python", "Java", "Swift", "C#", 2),
                ("What is the primary goal of business application development?",
                 "a) Improve employee productivity","b) Automate business processes",
                 "c) Minimize hardware requirements","d) Enhance video editing capabilities",2),
                ("Which methodology is widely used in application development to manage projects?",
                 "a) Agile","b) Waterfall","c) Scrum","d) All of the above",4),
                ("What is the role of a database in business application development?","a) To create user interfaces",
                 "b) To store and manage data","c) To calculate financial projections","d) To visualize data trends",2),
                ("Which tool is commonly used for version control in application development?","a) Git",
                 "b) MySQL","c) Jenkins","d) Figma",1),
                ("What is a key benefit of using cloud platforms for business applications?","a) Reduced development time",
                 "b) High scalability","c) Increased data security","d) All of the above",4),
                ("Which of the following is a front-end framework commonly used in business applications?","a) React",
                 "b) Django","c) Ruby on Rails","d) Spring Boot",1),
                ("What does the term 'API' stand for in application development?","a) Application Programming Interface",
                 "b) Application Protocol Integration","c) Automated Process Implementation","d) Analytics and Performance Insights",1),
                ("What is a common characteristic of microservices architecture?","a) Monolithic codebase",
                 "b) Scalability through independent components","c) Centralized database schema",
                 "d) Lack of API communication",2),
            ],
            
            "BusinessLaw":[
                ("What does 'liability' mean in business law?", 
                 "The ability to manage finances", "Responsibility for damages", 
                 "The right to ownership", "Profit from investments", 2),
                ("What is a contract?", 
                 "An informal agreement", "A legally binding agreement", 
                 "A government rule", "A business operation", 2),
                ("What is the purpose of intellectual property law?","a) To regulate financial transactions",
                 "b) To protect creative works and inventions","c) To govern international trade agreements",
                 "d) To enforce labor contracts",2),
                ("Which of the following is an example of a tort?","a) Breach of contract",
                 "b) Defamation of character","c) Filing for bankruptcy","d) Signing a lease agreement",2),
                ("What is the primary function of employment law?","a) To regulate salary payments",
                 "b) To provide protections for workers and employers","c) To create job opportunities",
                 "d) To issue permits for business startups",2),
                ("What is bankruptcy in business law?","a) A financial penalty for tax fraud","b) A legal process for resolving insolvency",
                 "c) A clause in partnership agreements,","d) A type of corporate investment",2),
                ("Which law governs consumer protection?","a) Contract law","b) Antitrust law","c) Advertising law",
                 "d) Product liability law",4),
                ("What is the role of antitrust law?","a) To regulate intellectual property ownership","b) To prevent unfair competition and monopolies",
                 "c) To protect workers from discrimination","d) To establish taxation rules",2),
                ("Which of the following describes the doctrine of negligence?","a) Failure to exercise reasonable care",
                 "b) Intentionally causing harm","c) Violation of a court order","d) Breach of partnership agreement",1),
                ("Which type of business entity offers limited liability protection?","a) Sole proprietorship","b) General partnership",
                 "c) Limited Liability Company (LLC)","d) Corporation",3)
            ],
       
            "DataAnalytics": [
                ("What is data visualization?", 
                 "Storing data", "Cleaning data", "Graphically representing data", 
                 "Analyzing data statistically", 3),
                ("Which of the following is a common data analytics tool?", 
                 "Excel", "Photoshop", "Final Cut Pro", "AutoCAD", 1),
            ],
       
            "DatabaseManagement": [
                ("What is SQL used for?", 
                "Creating websites", "Managing databases", "Analyzing graphs", 
                "Designing spreadsheets", 2),
                ("Which command is used to retrieve data from a database?", 
                "DELETE", "SELECT", "UPDATE", "INSERT", 2),
            ],
        }
        

        for course, qs in questions.items():
            for q in qs:
                cursor.execute(f"""
                    INSERT INTO {course} (question, option1, option2, option3, option4, correct_option)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, q)

        conn.commit()
        conn.close()

    if __name__ == "__main__":
        preload_questions()

# Main application class
class QuizBowlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl Application")
        self.current_frame = None
        self.show_login_screen()

    def show_quiz_taker_workflow(self):
        """Show the quiz taker workflow."""
        self.clear_frame()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        tk.Label(self.current_frame, text="Select a course to begin the quiz:").pack(pady=10)
        self.quiz_course_var = tk.StringVar()
        course_dropdown = tk.OptionMenu(self.current_frame, self.quiz_course_var,
                                        "ApplicationsDevelopment", "BusinessLaw", 
                                        "DataAnalytics", "DatabaseManagement")
        course_dropdown.pack()

        tk.Button(self.current_frame, text="Start Quiz", 
                  command=lambda: self.launch_quiz(self.quiz_course_var.get())).pack(pady=10)
        tk.Button(self.current_frame, text="Back", command=self.show_login_screen).pack(pady=10)

    def launch_quiz(self, course):
        """Launch the quiz interface for the selected course."""
        if not course:
            messagebox.showerror("Error", "Please select a course!")
            return
        self.clear_frame()
        start_quiz(self.root, course)

    def clear_frame(self):
        """Destroy the current frame to transition to a new one."""
        if self.current_frame:
            self.current_frame.destroy()

    def show_login_screen(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        tk.Label(self.current_frame, text="Welcome to Quiz Bowl! Please log in.").pack(pady=10)

        # Administrator login
        tk.Label(self.current_frame, text="Administrator Login").pack(pady=5)
        self.password_entry = tk.Entry(self.current_frame, show="*")
        self.password_entry.pack()
        tk.Button(self.current_frame, text="Login as Administrator", command=self.admin_login).pack(pady=10)

        # Quiz taker access
        tk.Label(self.current_frame, text="Quiz Taker Access").pack(pady=5)
        tk.Button(self.current_frame, text="Continue as Quiz Taker", command=self.show_quiz_taker_workflow).pack(pady=10)

    def admin_login(self):
        """Handle administrator login."""
        if self.password_entry.get() == "admin123":  # Example password
            messagebox.showinfo("Success", "Welcome, Administrator!")
            self.show_admin_workflow()
        else:
            messagebox.showerror("Error", "Incorrect Password!")

    def show_admin_workflow(self):
        """Show the administrator panel."""
        self.clear_frame()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        tk.Label(self.current_frame, text="Administrator Panel").pack(pady=10)
        tk.Button(self.current_frame, text="Add Questions", command=self.show_add_question_screen).pack(pady=5)
        tk.Button(self.current_frame, text="View Questions", command=self.show_view_questions_screen).pack(pady=5)
        tk.Button(self.current_frame, text="Modify/Delete Questions", command=self.show_modify_delete_screen).pack(pady=5)
        tk.Button(self.current_frame, text="Logout", command=self.show_login_screen).pack(pady=10)

    def show_add_question_screen(self):
        """Show the form for adding questions."""
        self.clear_frame()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        tk.Label(self.current_frame, text="Add Question").pack(pady=10)

        tk.Label(self.current_frame, text="Course:").pack(pady=5)
        self.course_var = tk.StringVar()
        course_dropdown = tk.OptionMenu(self.current_frame, self.course_var, 
                                        "ApplicationsDevelopment", "BusinessLaw", 
                                        "DataAnalytics", "DatabaseManagement")
        course_dropdown.pack()

        tk.Label(self.current_frame, text="Question Text:").pack(pady=5)
        self.question_entry = tk.Entry(self.current_frame, width=50)
        self.question_entry.pack()

        tk.Label(self.current_frame, text="Option 1:").pack(pady=5)
        self.option1_entry = tk.Entry(self.current_frame, width=50)
        self.option1_entry.pack()

        tk.Label(self.current_frame, text="Option 2:").pack(pady=5)
        self.option2_entry = tk.Entry(self.current_frame, width=50)
        self.option2_entry.pack()

        tk.Label(self.current_frame, text="Option 3:").pack(pady=5)
        self.option3_entry = tk.Entry(self.current_frame, width=50)
        self.option3_entry.pack()

        tk.Label(self.current_frame, text="Option 4:").pack(pady=5)
        self.option4_entry = tk.Entry(self.current_frame, width=50)
        self.option4_entry.pack()

        tk.Label(self.current_frame, text="Correct Option (1-4):").pack(pady=5)
        self.correct_option_entry = tk.Entry(self.current_frame, width=10)
        self.correct_option_entry.pack()

        tk.Button(self.current_frame, text="Submit Question", command=self.submit_question).pack(pady=10)
        tk.Button(self.current_frame, text="Back", command=self.show_admin_workflow).pack(pady=5)

    def submit_question(self):
        """Submit a new question to the database."""
        course = self.course_var.get()
        question_text = self.question_entry.get()
        option1 = self.option1_entry.get()
        option2 = self.option2_entry.get()
        option3 = self.option3_entry.get()
        option4 = self.option4_entry.get()
        correct_option = self.correct_option_entry.get()

        if not course or not question_text or not option1 or not option2 or not option3 or not option4 or not correct_option:
            messagebox.showerror("Error", "Please fill in all fields!")
            return

        try:
            correct_option = int(correct_option)
            if correct_option < 1 or correct_option > 4:
                raise ValueError("Correct option must be between 1 and 4.")
        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid correct option: {ve}")
            return

        try:
            conn = sqlite3.connect("quiz_bowl.db")
            cursor = conn.cursor()
            cursor.execute(f"""
                INSERT INTO {course} (question, option1, option2, option3, option4, correct_option)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (question_text, option1, option2, option3, option4, correct_option))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Question added successfully to {course}!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add question: {e}")
            return
        
    def show_view_questions_screen(self):
        """Show all questions from the database for a selected course."""
        self.clear_frame()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        tk.Label(self.current_frame, text="View Questions").pack(pady=10)

        tk.Label(self.current_frame, text="Select Course:").pack(pady=5)
        self.view_course_var = tk.StringVar()
        course_dropdown = tk.OptionMenu(self.current_frame, self.view_course_var,
                                        "ApplicationsDevelopment", "BusinessLaw", 
                                        "DataAnalytics", "DatabaseManagement")
        course_dropdown.pack()

        def load_questions():
            course = self.view_course_var.get()
            if not course:
                messagebox.showerror("Error", "Please select a course!")
                return

            try:
                conn = sqlite3.connect("quiz_bowl.db")
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {course}")
                questions = cursor.fetchall()
                conn.close()

                # Display questions in a new frame
                self.clear_frame()
                self.current_frame = tk.Frame(self.root)
                self.current_frame.pack()

                tk.Label(self.current_frame, text=f"Questions for {course}").pack(pady=10)
                for question in questions:
                    question_text = question[1]  # Question text is in the second column
                    tk.Label(self.current_frame, text=f"Q: {question_text}").pack(pady=5)

                tk.Button(self.current_frame, text="Back", command=self.show_admin_workflow).pack(pady=10)

            except Exception as e:
                messagebox.showerror("Error", f"Failed to load questions: {e}")

        tk.Button(self.current_frame, text="Load Questions", command=load_questions).pack(pady=10)
        tk.Button(self.current_frame, text="Back", command=self.show_admin_workflow).pack(pady=5)

    def show_modify_delete_screen(self):
        """Show the modify/delete questions screen."""
        self.clear_frame()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        tk.Label(self.current_frame, text="Modify or Delete Questions").pack(pady=10)

        tk.Label(self.current_frame, text="Select Course:").pack(pady=5)
        self.modify_course_var = tk.StringVar()
        course_dropdown = tk.OptionMenu(self.current_frame, self.modify_course_var,
                                        "ApplicationsDevelopment", "BusinessLaw", 
                                        "DataAnalytics", "DatabaseManagement")
        course_dropdown.pack()

        def load_questions_for_modification():
            course = self.modify_course_var.get()
            if not course:
                messagebox.showerror("Error", "Please select a course!")
                return

            try:
                conn = sqlite3.connect("quiz_bowl.db")
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM {course}")
                questions = cursor.fetchall()
                conn.close()

                # Display questions for modification/deletion
                self.clear_frame()
                self.current_frame = tk.Frame(self.root)
                self.current_frame.pack()

                tk.Label(self.current_frame, text=f"Questions for {course}").pack(pady=10)
                for question in questions:
                    question_id = question[0]
                    question_text = question[1]
                    tk.Label(self.current_frame, text=f"ID: {question_id} | Q: {question_text}").pack(pady=5)

                    tk.Button(self.current_frame, text="Modify", 
                              command=lambda q_id=question_id, c=course: self.show_modify_question_form(q_id, c)).pack(pady=2)
                    tk.Button(self.current_frame, text="Delete", 
                              command=lambda q_id=question_id, c=course: self.delete_question(q_id, c)).pack(pady=2)

                tk.Button(self.current_frame, text="Back", command=self.show_admin_workflow).pack(pady=10)

            except Exception as e:
                messagebox.showerror("Error", f"Failed to load questions: {e}")

        tk.Button(self.current_frame, text="Load Questions", command=load_questions_for_modification).pack(pady=10)
        tk.Button(self.current_frame, text="Back", command=self.show_admin_workflow).pack(pady=5)

    def delete_question(self, question_id, course):
        """Delete a question from the database."""
        try:
            conn = sqlite3.connect("quiz_bowl.db")
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {course} WHERE id = ?", (question_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Question ID {question_id} deleted successfully!")
            self.show_modify_delete_screen()  # Refresh the screen
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete question: {e}")

    def show_modify_question_form(self, question_id, course):
        """Show a form to modify a question."""
        self.clear_frame()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        tk.Label(self.current_frame, text="Modify Question").pack(pady=10)

        tk.Label(self.current_frame, text="New Question Text:").pack(pady=5)
        self.new_question_entry = tk.Entry(self.current_frame, width=50)
        self.new_question_entry.pack()

        tk.Label(self.current_frame, text="New Option 1:").pack(pady=5)
        self.new_option1_entry = tk.Entry(self.current_frame, width=50)
        self.new_option1_entry.pack()

        tk.Label(self.current_frame, text="New Option 2:").pack(pady=5)
        self.new_option2_entry = tk.Entry(self.current_frame, width=50)
        self.new_option2_entry.pack()

        tk.Label(self.current_frame, text="New Option 3:").pack(pady=5)
        self.new_option3_entry = tk.Entry(self.current_frame, width=50)
        self.new_option3_entry.pack()

        tk.Label(self.current_frame, text="New Option 4:").pack(pady=5)
        self.new_option4_entry = tk.Entry(self.current_frame, width=50)
        self.new_option4_entry.pack()

        tk.Label(self.current_frame, text="New Correct Option (1-4):").pack(pady=5)
        self.new_correct_option_entry = tk.Entry(self.current_frame, width=10)
        self.new_correct_option_entry.pack()

        tk.Button(self.current_frame, text="Submit Changes", 
                  command=lambda: self.modify_question(question_id, course)).pack(pady=10)
        tk.Button(self.current_frame, text="Back", command=self.show_modify_delete_screen).pack(pady=5)

    def modify_question(self, question_id, course):
        """Modify a question in the database."""
        new_question = self.new_question_entry.get()
        new_option1 = self.new_option1_entry.get()
        new_option2 = self.new_option2_entry.get()
        new_option3 = self.new_option3_entry.get()
        new_option4 = self.new_option4_entry.get()
        new_correct_option = self.new_correct_option_entry.get()

        if not new_question or not new_option1 or not new_option2 or not new_option3 or not new_option4 or not new_correct_option:
            messagebox.showerror("Error", "Please fill in all fields!")
            return

        try:
            new_correct_option = int(new_correct_option)
            if new_correct_option < 1 or new_correct_option > 4:
                raise ValueError("Correct option must be between 1 and 4.")
        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid correct option: {ve}")
            return

        try:
            conn = sqlite3.connect("quiz_bowl.db")
            cursor = conn.cursor()
            cursor.execute(f"""
                UPDATE {course}
                SET question = ?, option1 = ?, option2 = ?, option3 = ?, option4 = ?, correct_option = ?
                WHERE id = ?
            """, (new_question, new_option1, new_option2, new_option3, new_option4, new_correct_option, question_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Question ID {question_id} modified successfully!")
            self.show_modify_delete_screen()  # Refresh the screen
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load questions: {e}")

import tkinter as tk
from tkinter import messagebox
import sqlite3

class QuizTaker:
    def __init__(self, root, course):
        self.root = root
        self.course = course
        self.max_questions = 10  # Initialize max_questions here
        self.questions = self.load_questions()
        self.current_question_index = 0
        self.score = 0
        self.quiz_frame = tk.Frame(self.root)
        self.quiz_frame.pack()
        self.show_question()

    def load_questions(self):
        """Load questions from the database for the selected course."""
        try:
            conn = sqlite3.connect("quiz_bowl.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self.course}")
            questions = cursor.fetchall()
            conn.close()
            return questions[:self.max_questions]  # Limit to 10 questions
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load questions: {e}")
            return []

    def show_question(self):
        """Display the current question."""
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            question_text = question[1]
            options = question[2:6]

            for widget in self.quiz_frame.winfo_children():
                widget.destroy()

            tk.Label(self.quiz_frame, text=f"Question {self.current_question_index + 1}: {question_text}").pack(pady=10)

            self.selected_option = tk.IntVar()
            for i, option in enumerate(options, start=1):
                tk.Radiobutton(self.quiz_frame, text=option, variable=self.selected_option, value=i).pack(pady=5)

            tk.Button(self.quiz_frame, text="Submit", command=lambda: self.submit_answer(question)).pack(pady=10)
        else:
            self.show_final_score()

    def submit_answer(self, question):
        """Check the selected answer and move to the next question."""
        if self.selected_option.get() == 0:
            messagebox.showerror("Error", "Please select an answer!")
            return

        correct_option = question[6]
        if self.selected_option.get() == correct_option:
            self.score += 1

        self.current_question_index += 1
        self.show_question()

    def show_final_score(self):
        """Display the final score."""
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()

        tk.Label(self.quiz_frame, text=f"Quiz Completed! Your score: {self.score}/{self.max_questions}").pack(pady=10)
        tk.Button(self.quiz_frame, text="Back to Main Menu", command=self.quiz_frame.destroy).pack(pady=10)

        tk.Label(self.quiz_frame, text=f"Quiz Completed! Your score: {self.score}/{self.max_questions}").pack(pady=10)
        tk.Button(self.quiz_frame, text="Back to Main Menu", command=self.quiz_frame.destroy).pack(pady=10)

# Function to launch the quiz interface
def start_quiz(root, course):
    QuizTaker(root, course)

# Main application
import tkinter as tk
from tkinter import messagebox
import sqlite3

class QuizTaker:
    def __init__(self, root, course):
        self.root = root
        self.course = course
        self.questions = self.load_questions()
        self.current_question_index = 0
        self.score = 0
        self.quiz_frame = tk.Frame(self.root)
        self.quiz_frame.pack()
        self.show_question()

    def load_questions(self):
        """Load questions from the database for the selected course."""
        try:
            conn = sqlite3.connect("quiz_bowl.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self.course}")
            questions = cursor.fetchall()
            conn.close()
            return questions
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load questions: {e}")
            return []

    def show_question(self):
        """Display the current question."""
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            question_text = question[1]
            options = question[2:6]

            for widget in self.quiz_frame.winfo_children():
                widget.destroy()

            tk.Label(self.quiz_frame, text=f"Question {self.current_question_index + 1}: {question_text}").pack(pady=10)

            self.selected_option = tk.IntVar()
            for i, option in enumerate(options, start=1):
                tk.Radiobutton(self.quiz_frame, text=option, variable=self.selected_option, value=i).pack(pady=5)

            tk.Button(self.quiz_frame, text="Submit", command=lambda: self.submit_answer(question)).pack(pady=10)
        else:
            self.show_final_score()

    def submit_answer(self, question):
        """Check the selected answer and move to the next question."""
        if self.selected_option.get() == 0:
            messagebox.showerror("Error", "Please select an answer!")
            return

        correct_option = question[6]
        if self.selected_option.get() == correct_option:
            self.score += 1

        self.current_question_index += 1
        self.show_question()

    def show_final_score(self):
        """Display the final score."""
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()

        tk.Label(self.quiz_frame, text=f"Quiz Completed! Your score: {self.score}/{len(self.questions)}").pack(pady=10)
        tk.Button(self.quiz_frame, text="Back to Main Menu", command=self.quiz_frame.destroy).pack(pady=10)

# Function to launch the quiz interface
def start_quiz(root, course):
    QuizTaker(root, course)

if __name__ == "__main__":
    initialize_database()
    root = tk.Tk()
    app = QuizBowlApp(root)
    root.mainloop()
