from re import compile
import regions
import age
import re
import tkinter as tk

def checkValid(fullregnumber):
    # Pattern which must plate match to be correct.
    # It says that your input must consist of
    #    two letters -> [a-zA-Z]{2}
    #    two numbers -> [0-9]{2}
    #    three letters -> [a-zA-Z]{3}
    # Number in {} says exactly how much occurrences of symbols in
    # in [] must be in string to have positive match.
    plate_format = compile('^[a-zA-Z]{2}[0-9]{2}[a-zA-z]{3}$')

    plate = [fullregnumber]

    for theplate in plate:
        if plate_format.match(theplate) is not None:
            print("Correct plate")
            return True
        else:
            print("Incorrect plate")
            return False

def get_item_from_list(l,i):
    return l[i]

# Method for splitting a string into numbers and letters the reg into letters and numbers
def my_split(s):
    return list(filter(None, re.split(r'(\d+)', s)))

def get_reg_number_and_give_region_and_age_1():
    def process_reg_number():
        reg = ent_reg.get()
        if checkValid(reg) == False:
            lbl_result["text"] = "That reg is not the right format, please enter a reg in the correct format"
            ent_reg.delete(0, tk.END)
        # Split the reg into letters and numbers into a list
        #print(reg)
        else:
            regi = my_split(reg)
            # Get the first letters from the reg number from the list
            region_code = get_item_from_list(regi, 0)
            #print(region_code)
            # Find the region from the first letters of the reg
            region = regions.regoins.get(region_code)
            # Get the car age digits from the list
            age_code = get_item_from_list(regi, 1)
            # Find the age code from the numbers in the reg
            car_age = age.age.get(age_code)
            message = ('The car was registered in ' + region + ' and it was registered between the following dates: ' + car_age)
            # Print explained reg number to user
            lbl_result["text"] = message

    # Set-up the window
    window = tk.Tk()
    window.geometry("800x200")
    window.title("UK car registration checker")
    window.resizable(width=True, height=True)
    window.rowconfigure(2, minsize=30)
    window.columnconfigure(0, minsize=30)

    # Create the reg entry frame with an Entry
    # widget and label in it
    frm_entry = tk.Frame(master=window)
    ent_reg = tk.Entry(master=frm_entry, width=10)
    lbl_reg = tk.Label(master=frm_entry, text="Please enter the UK registration number in the box -->")

    # Layout the reg Entry and Label in frm_entry
    # using the .grid() geometry manager
    ent_reg.grid(row=0, column=1, sticky="ew")
    lbl_reg.grid(row=0, column=0, sticky="ew")

    # Create the conversion Button and result display Label
    btn_convert_reg = tk.Button(
        master=window,
        text="Press to check car registration info",
        command=process_reg_number
    )
    lbl_result = tk.Label(master=window, text="Region and date regestered will appear here")

    # Set-up the layout using the .grid() geometry manager
    frm_entry.grid(row=0, column=0, sticky='nsew')
    btn_convert_reg.grid(row=1, column=0, sticky='nsew')
    lbl_result.grid(row=2, column=0, sticky='nsew')

    # Run the application
    window.mainloop()




