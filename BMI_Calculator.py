import tkinter as tk
from tkinter import messagebox
class BMI_Calculator:
    def __init__(self):
        
        self.a = tk.Tk()
        self.a.geometry("400x300")
        self.a.title('BMI calculator')
        
        self.label_1 = tk.Label(self.a,text="BMI Calculator", font=("Arial", 20) )
        self.label_1.grid(row=0,column=1, padx=(0,30))
        
        self.entry_1 = tk.Entry(self.a)
        self.entry_1.grid(row=1, column=1,)
        
        self.label_2 = tk.Label(self.a,text="WEIGHT in Kg:", font=("Arial", 15))
        self.label_2.grid(row=1,column=0,padx=(20,0),pady=(20,20))
        
        self.entry_2 = tk.Entry(self.a)
        self.entry_2.grid(row=2, column=1)
        
        label_3 = tk.Label(self.a,text="HEIGHT in meter:", font=("Arial", 15))
        label_3.grid(row=2,column=0,padx=(20,0))
        

        submit_button = tk.Button(self.a, text="submit", command=self.bmi_cal)
        submit_button.grid(row=3, column=0, pady=(30,0))
        
        self.label_4 = tk.Label(self.a, text=" ", font=(12))
        self.label_4.grid(row=4,column=0, padx=(10,0),pady=(20,0))
        
        reset_window = tk.Button(self.a, text="Clear", command=self.reset)
        reset_window.grid(row=3,column=1,pady=(30,0))
        
    
    def bmi_cal(self):
        try:
            weight = float(self.entry_1.get())
            height = float(self.entry_2.get())

            Bmi = weight/(height * height)
            if Bmi<18.5:
                self.label_4.config(text=f"BMI value: {Bmi:.2f}-\n Underweight")
            elif Bmi>=18.5 and Bmi<25:
                self.label_4.config(text=f"BMI value: {Bmi:.2f}-\n Normal")
            elif Bmi>=25 and Bmi<30:
                self.label_4.config(text=f"BMI value: {Bmi:.2f}-\n overweight")
            else:
                self.label_4.config(text=f"BMI value: {Bmi:.2f}-\n obese")
                
        except ValueError:     
            messagebox.showerror('Error','Enter valid weight and height')
    
    def reset(self):
        self.entry_1.delete(0, tk.END)
        self.entry_2.delete(0, tk.END)
        self.label_4.config(text="")
             

if __name__=="__main__":
    window=BMI_Calculator()
    window.a.mainloop()