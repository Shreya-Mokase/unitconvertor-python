# importing all widgets and modules from the tkinter library
from tkinter import *

# defining the reset function
def reset():
    # using the delete() method to delete entries in entry field
    input_field.delete(0, END)
    output_field.delete(0, END)
    # setting the value of the option menu to the
    # first index of the list using the set() method
    input_value.set(SELECTIONS[0])
    output_value.set(SELECTIONS[0])

    # setting the focus to input field using the focus_set() method
    input_field.focus_set()


# defining the convert function
def convert():
    # getting the string from entry field and converting it into float
    inputVal = float(input_field.get())
    # getting the values from selection menus
    input_unit = input_value.get()
    output_unit = output_value.get()

    # list of the required combination of the conversion factors
    conversion_factors = [input_unit in length_units and output_unit in length_units,
                          input_unit in weight_units and output_unit in weight_units,
                          input_unit in temperature_units and output_unit in temperature_units,
                          input_unit in area_units and output_unit in area_units,
                          input_unit in volume_units and output_unit in volume_units]

    if any(conversion_factors):  # If both the units are of same type, perform the conversion
        if input_unit == "celsius" and output_unit == "fahrenheit":
            output_field.delete(0, END)
            output_field.insert(0, (inputVal * 1.8) + 32)
        elif input_unit == "fahrenheit" and output_unit == "celsius":
            output_field.delete(0, END)
            output_field.insert(0, (inputVal - 32) * (5 / 9))
        else:
            output_field.delete(0, END)
            output_field.insert(0, round(inputVal * unitDict[input_unit] / unitDict[output_unit], 5))

    else:
        # displaying error if units are of different types
        output_field.delete(0, END)
        output_field.insert(0, "ERROR The input is invalid...!")


if __name__ == "__main__":
    # dictionary of conversion factors
    unitDict = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1.0,
        "kilometer": 1000.0,
        "foot": 0.3048,
        "inch": 0.0254,
        "square meter": 1.0,
        "square kilometer": 1000000.0,
        "square centimeter": 0.0001,
        "square millimeter": 0.000001,
        "hectare": 10000.0,
        "acre": 4046.856,
        "litre": 1.0,
        "millilitre": 0.001,
        "gram": 1.0,
        "kilogram": 1000.0,
        "milligram": 0.001,
        "quintal": 100000.0,
        "ton": 1000000.0,
    }

    # charts for units conversion
    length_units = [
        "millimeter", "centimeter", "meter", "kilometer", "foot","inch"
    ]
    temperature_units = [
        "celsius", "fahrenheit"
    ]
    area_units = [
        "square meter", "square kilometer", "square centimeter", "square millimeter",
        "hectare", "acre"
    ]
    volume_units = [
         "litre", "millilitre"
    ]
    weight_units = [
        "gram", "kilogram", "milligram", "quintal", "ton"
    ]

    # creating the list of options for selection menu
    SELECTIONS = [
        "Select Unit",
        "millimeter",
        "centimeter",
        "meter",
        "kilometer",
        "foot",
        "inch",
        "celsius",
        "fahrenheit",
        "square meter",
        "square kilometer",
        "square centimeter",
        "square millimeter",
        "hectare",
        "acre",
        "litre",
        "millilitre",
        "gram",
        "kilogram",
        "milligram",
        "quintal",
        "ton",
        
    ]




    # creating the main window of the application
    # creating an object of the Tk() class

    guiWindow = Tk()
    
    # setting the title of the main window
    guiWindow.title("Unit Convertor")
    
    # setting the size and position of the main window
    guiWindow.geometry("500x500+500+250")
    
    # disabling the resizing option
    guiWindow.resizable(0, 0)
    
    # setting the background color to #16a085
    guiWindow.configure(bg="#ADFF2F")

    # adding frames to the main window
    header_frame = Frame(guiWindow, bg="#ADFF2F")
    body_frame = Frame(guiWindow, bg="#ADFF2F")

    # setting the positions of the frames
    header_frame.pack(expand=True, fill="both")
    body_frame.pack(expand=True, fill="both")

    # adding the label to the header frame
    header_label = Label(
        header_frame,
        text="STANDARD UNIT CONVERTER",
        font=("Arial Black", 22),
        bg="#FF7256",
        fg="#171717"
    )

    # setting the position of the label
    header_label.pack(expand=True, fill="both")

    # creating the objects of the StringVar() class
    input_value = StringVar()
    output_value = StringVar()
    
    # using the set() method to set the primary
    # value of the objects to index value 0
    # of the SELECTIONS list
    input_value.set(SELECTIONS[0])
    output_value.set(SELECTIONS[0])

    # creating the labels for the body of the main window
    input_label = Label(
        body_frame,
        text="FROM:",
        bg="#16a085",
        fg="#d0ece7"
    )
    output_label = Label(
        body_frame,
        text="TO:",
        bg="#16a085",
        fg="#d0ece7"
    )

    # using the grid() method to set the position of the above labels
    input_label.grid(row=1, column=1, padx=70, pady=30, sticky=W)
    output_label.grid(row=2, column=1, padx=70, pady=30, sticky=W)

    # creating the entry fields for the body of the main window
    # input field to enter data
    input_field = Entry(
        body_frame,
        bg="#e8f8f5"
    )
    # output field to display result
    output_field = Entry(
        body_frame,
        bg="#e8f8f5"
    )

    # using the grid() method to set the position of the above entry fields
    input_field.grid(row=1, column=2)
    output_field.grid(row=2, column=2)

    # adding the option menus to the main window
    input_menu = OptionMenu(
        body_frame,
        input_value,
        *SELECTIONS
    )
    output_menu = OptionMenu(
        body_frame,
        output_value,
        *SELECTIONS
    )

    # using the grid() method to set the position of the above option menus
    input_menu.grid(row=1, column=3, padx=20)
    output_menu.grid(row=2, column=3, padx=20)

    # creating the buttons for the main window
    # CONVERT button
    convert_button = Button(
        body_frame,
        text="CONVERT HERE",
        bg="#0b5345",
        fg="#ffffff",
        command=convert
    )
    # RESET button
    reset_button = Button(
        body_frame,
        text="RESET HERE",
        bg="#f7dc6f",
        fg="#000000",
        command=reset
    )

    # using the grid() method to set the position of the above buttons
    convert_button.grid(row=3, column=2)
    reset_button.grid(row=3, column=3)

    # running the application
    guiWindow.mainloop()
