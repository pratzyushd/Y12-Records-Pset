# Y12-Records-Pset
Y12 Records Problem Set

- Create a data structure called Record
- It should have the following private attributes (consider appropriate data types):
  - forename -> str mandatory
  - surname -> str mandatory
  - age -> int mandatory
  - gender -> "F","M","O"
  - CS_student -> "True", "False"

- The data structure should have the following methods:
  - Getters and Setters for each atrribute (validation required)


 - Extension:
 - Add a new method:
   - created
    - Outputs the date and time that the Record was created
      - NOTE: You will need a new attribute to store this
   - day_born
    - Add a DOB attribute
    - instead of requesting age from the user, calculate the age from the DOB
    - the day_born method when invoked should return the DAY the person was born
