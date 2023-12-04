import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from collections import defaultdict

class BMICalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BMI Calculator")

        self.users = defaultdict(list)  # For data storage

        # GUI elements
        self.label_weight = tk.Label(self.root, text="Enter Weight (kg):")
        self.entry_weight = tk.Entry(self.root)

        self.label_height = tk.Label(self.root, text="Enter Height (m):")
        self.entry_height = tk.Entry(self.root)

        self.calculate_button = tk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi)
        self.view_history_button = tk.Button(self.root, text="View History", command=self.view_history)

        # Layout
        self.label_weight.grid(row=0, column=0, padx=10, pady=10)
        self.entry_weight.grid(row=0, column=1, padx=10, pady=10)

        self.label_height.grid(row=1, column=0, padx=10, pady=10)
        self.entry_height.grid(row=1, column=1, padx=10, pady=10)

        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.view_history_button.grid(row=3, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())

            bmi = weight / (height ** 2)
            bmi_category = self.classify_bmi(bmi)

            self.show_bmi_result(bmi, bmi_category)

            # Save data
            self.users["weights"].append(weight)
            self.users["heights"].append(height)
            self.users["bmi_categories"].append(bmi_category)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

    def classify_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def show_bmi_result(self, bmi, bmi_category):
        result_text = f"Your BMI is: {bmi:.2f}\nYou are classified as: {bmi_category}"
        messagebox.showinfo("BMI Result", result_text)

    def view_history(self):
        if not self.users["weights"]:
            messagebox.showinfo("No Data", "No BMI data available.")
            return

        # Data visualization using matplotlib
        plt.scatter(self.users["weights"], self.users["heights"], c='blue', label='Weight vs. Height')
        plt.xlabel('Weight (kg)')
        plt.ylabel('Height (m)')
        plt.title('Weight vs. Height History')
        plt.legend()
        plt.show()

        # Display BMI categories over time
        plt.plot(self.users["bmi_categories"])
        plt.xlabel('Entry')
        plt.ylabel('BMI Category')
        plt.title('BMI Category History')
        plt.show()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    bmi_calculator = BMICalculator()
    bmi_calculator.run()
