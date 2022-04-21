# Requirements
* A Calculator's acc is non-existent on construction, so its value should be 0.00
* If one sets the accumulator x then gets it, the value returned is x
* If one adds x to the accumulator then gets the accumulator's value, the value returned is the old accumulator's value + x
* If one subtracts x to the accumulator then gets the accumulator's value, the value returned is the old accumulator's value - x
* If one multiplies x to the accumulator then gets the accumulator's value, the value returned is the old accumulator's value * x
* If one divides x to the accumulator then gets the accumulator's value, the value returned is the old accumulator's value / x
* If one gets the status of the calculator while the accumulator's value is x, the string returned should be "Result: x"
* Dividing by 0 will raise ZeroDivisionError
