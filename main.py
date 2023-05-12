Vote_A = 0
Vote_B = 0

def on_button_pressed_a():
    global Vote_A
    Vote_A += 1
    basic.show_icon(IconNames.YES)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("A")
    basic.show_number(Vote_A)
    basic.show_string("B")
    basic.show_number(Vote_B)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Vote_B
    Vote_B += 1
    basic.show_icon(IconNames.YES)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
