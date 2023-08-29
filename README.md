# DrugDispenser
We used this project for the 2023 Heal-o-code Hackathon where almost 30 teams, with 150 people participated. We placed second place at the Hackathon and won a prize of ₹10000. The project was made using a Raspberry Pi, a camera module, and two servo motors. The frontend was made using HTML, CSS, and JavaScript. The backend was made using Firebase. The project was made in 24 hours.

Our motto: Dispensing safety somewhere near you.

It is a device made to help people get the right amount of medication, thus preventing any forms of overdose or lack of a certain medicine. This device stores the user’s face and verifies their identity via facial recognition, checks its database to see how many pills are in the person's dosage, then dispenses the appropriate dosage of pills. This eliminates any error in taking medication and makes the process smoother. If this product were utilized by pharmacies, the doctor prescribing would have control of the dosage stored in the system.

This device can be constructed using a Raspberry Pi and two servo motors. We can mount these, as well as multiple medicine tubes, to a wooden board to create the prototype. When a new user uses the device for the first time, their face is scanned and added to the database along with their details and dosage information. Later, when the user needs to take their pills their face is scanned and if it matches with the database, the pills are dispensed into a tray.
      
It dispenses individual pills, using servo motors connected to the Pi, by opening and closing for a calibrated number of times. The device consists of multiple medicine tubes for different types of medicine.


## Running the project
To run the project, run the index.html file in the frontend folder using a live server. Also add your Firebase config details to the user.js file






