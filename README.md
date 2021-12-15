<h1 align="center">
    Fairfield College Preparatory School<br>
    Computer Programming - Mr. Mesquita<br>
    Midterm Part 2
</h1>

<h2 align="center">
    Due before 10:20 AM on 12/14 (50 pts.)<br>
    Be sure to read all of the instructions carefully!
</h2>

__You must answer question 1.__ Then, answer any 2 questions from section 2. You should answer 3 questions in total.

For each of the questions, write a program in Python to solve the problem presented. Make sure each question is answered in its own unique Python file. 

You will not receive any extra credit for any questions answered past the required 3. However, if you do have time to answer more than 3 questions, the 3 best will count towards your grade. Remember to be clear and concise in your code. Include proper units in your output where necessary.

---
### Section 1
<h3 align="center">A long time ago in a galaxy far, far away...</h3>
1. The clone factory on the planet Kamino is responsible for making clone troopers for the Grand Army of the Republic. Though they possess the biomedical expertise to create clone troopers, they do not have a way to automatically assign numbers to each new trooper. Write a program that contains a function that assignes a number to a clone as it is created. The function should first select a random number between `0` and `9999`, and then add leading zeroes to the number as appropriate so the number is 4 digits long. The function should return this number and `CT-` should preceed it to create the clone's name. The program should prompt the user to input `Y` to generate a new name and `N` to stop. When the program stops, it should display a list of all the clone names generated.

   <ins>Sample Run</ins>
   ```
   Name a clone? Y
   New clone trooper name: CT-5555
   Name a clone? Y
   New clone trooper name: CT-0137
   Name a clone? y
   New clone trooper name: CT-0099
   Name a clone? y
   New clone trooper name: CT-0008
   Name a clone? N
   ['CT-5555', 'CT-0137', 'CT-0099', 'CT-0008']
   ```

---
### Section 2
2. Average acceleration is defined as the change in velocity divided by the time. Write a program that prompts the user to input the initial velocity, final velocity, and time. The program should then calculate the average acceleration and print the result. Assume the user enters velocity in meters-per-second and time in seconds.

3. The minimum runway length needed for an starship to take off is the quotient of the square of the take off speed and twice the acceleration of the ship. Write a program that prompts the user to input the ship's acceleration and take-off speed and then calculates the minimum runway length needed for an starship to take off and prints this value. Assume the user enters acceleration in meters-per-second (m/s) and length of the runway in meters (m).

4. Write a program that prompts the user to input the driving distance, landspeeder fuel efficiency, and the price of fuel. Assume distance is in miles (mi.), fuel efficiency is in miles-per-gallon (mpg), and price of fuel is credits-per-gallon. The program should then calculate the cost of the trip and print this value. *HINT: Use dimensional analysis to create your formula.*

<p align="center"><i>Be sure to commit your code before the end of class. Only the latest commit submitted on time will be graded.</i></p>
