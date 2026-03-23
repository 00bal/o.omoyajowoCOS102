import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

window = tk.Tk()

try:
    employees = pd.read_excel("GIG-logistics.xlsx")

    if employees.iloc[0].astype(str).str.contains('EmployeeID|Name|Department').any():
        employees = employees.iloc[1:].reset_index(drop=True)

    employees['Name'] = employees['Name'].astype(str).str.strip()
    employees['Department'] = employees['Department'].astype(str).str.strip()
    print("Employee data loaded successfully!")
except Exception as e:
    messagebox.showerror("Error", f"Could not load file: {e}")
    employees = pd.DataFrame()

window.title("GIG Logistics - Employee Verification System")
window.geometry("900x600")
window.configure(bg="#f0f2f5")

header = tk.Frame(window, bg="#1e3a8a", height=80)
header.pack(fill=tk.X)
header.pack_propagate(False)

tk.Label(header, text="GIG LOGISTICS", font=("Helvetica", 24, "bold"), bg="#1e3a8a", fg="white").pack(pady=15)
tk.Label(header, text="Employee Verification System", font=("Helvetica", 12), bg="#1e3a8a", fg="#cbd5e1").pack()

main_frame = tk.Frame(window, bg="#f0f2f5", padx=40, pady=30)
main_frame.pack(fill=tk.BOTH, expand=True)

input_box = tk.LabelFrame(main_frame, text="Employee Verification", bg="white", fg="#1e3a8a",
                          font=("Helvetica", 12, "bold"), padx=20, pady=20)
input_box.pack(fill=tk.X, pady=(0, 20))
input_box.columnconfigure(0, weight=1)
input_box.columnconfigure(1, weight=1)

tk.Label(input_box, text="Employee Name:", bg="white", font=("Helvetica", 10, "bold")).grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(input_box, width=40, font=("Helvetica", 11))
name_entry.grid(row=1, column=0, sticky="w", pady=(0, 15))
name_entry.focus()

tk.Label(input_box, text="Department:", bg="white", font=("Helvetica", 10, "bold")).grid(row=0, column=1, sticky="w", padx=(20, 0))

if not employees.empty:
    department_list = sorted(employees['Department'].unique().tolist())
else:
    department_list = []

dept_var = tk.StringVar()
dept_dropdown = ttk.Combobox(input_box, textvariable=dept_var, values=department_list,
                              width=37, font=("Helvetica", 11), state="readonly")
dept_dropdown.grid(row=1, column=1, sticky="w", padx=(20, 0), pady=(0, 15))

results_box = tk.LabelFrame(main_frame, text="Verification Results", bg="white", fg="#1e3a8a",
                             font=("Helvetica", 12, "bold"), padx=20, pady=20)
results_box.pack(fill=tk.BOTH, expand=True)

status_label = tk.Label(results_box, text="Enter employee details and click Verify",
                         bg="white", font=("Helvetica", 11), fg="#64748b")
status_label.pack(pady=(0, 15))

columns = ("EmployeeID", "Name", "Role", "Email", "Phone", "Location")
table = ttk.Treeview(results_box, columns=columns, show="headings", height=10)

for col in columns:
    table.heading(col, text=col, anchor=tk.W)
    table.column(col, width=130, anchor=tk.W)

scrollbar = ttk.Scrollbar(results_box, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scrollbar.set)
table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white")
style.configure("Treeview.Heading", background="#e2e8f0", font=("Helvetica", 10, "bold"))


def verify_employee():
    name = name_entry.get().strip()
    department = dept_var.get().strip()

    if not name or not department:
        messagebox.showwarning("Input Required", "Please enter both Name and Department.")
        return

    found = employees[
        (employees['Name'].str.lower() == name.lower()) &
        (employees['Department'].str.lower() == department.lower())
    ]

    for row in table.get_children():
        table.delete(row)

    if not found.empty:
        emp = found.iloc[0]
        status_label.config(
            text=f"Welcome, {emp['Name']}!\nRole: {emp['Role']} | Location: {emp['Location']}",
            fg="#059669", font=("Helvetica", 12, "bold"), wraplength=700
        )

        dept_members = employees[employees['Department'].str.lower() == department.lower()]
        results_box.config(text=f"Department Members: {department} ({len(dept_members)} total)")

        for _, row in dept_members.iterrows():
            highlight = "highlight" if row['Name'].lower() == name.lower() else ""
            table.insert("", tk.END, values=(
                row['EmployeeID'], row['Name'], row['Role'],
                row['Email'], row['Phone'], row['Location']
            ), tags=(highlight,))

        table.tag_configure("highlight", background="#dbeafe", font=("Helvetica", 9, "bold"))

    else:
        results_box.config(text="Verification Results")
        status_label.config(
            text=f"Employee Not Found\nNo record for '{name}' in {department}. Please check spelling or contact HR.",
            fg="#dc2626", font=("Helvetica", 12), wraplength=700
        )


tk.Button(input_box, text="Verify Employee", command=verify_employee, bg="#2563eb", fg="white",
          font=("Helvetica", 11, "bold"), cursor="hand2", relief=tk.FLAT, padx=20, pady=8).grid(
    row=2, column=0, columnspan=2, pady=(10, 0))

window.mainloop()
