let Vote_A = 0
let Vote_B = 0
input.onButtonPressed(Button.A, function () {
    Vote_A += 1
    basic.showIcon(IconNames.Yes)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("A")
    basic.showNumber(Vote_A)
    basic.showString("B")
    basic.showNumber(Vote_B)
})
input.onButtonPressed(Button.B, function () {
    Vote_B += 1
    basic.showIcon(IconNames.Yes)
    basic.clearScreen()
})
