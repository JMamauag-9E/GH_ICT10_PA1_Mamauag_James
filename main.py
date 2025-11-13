# Working with Sets
from pyscript import display

Art_Club = {'Abraham', 'Sarah', 'Joseph', 'Esther', 'Daniel'}
Dance_Club = {'Joseph', 'Sarah', 'Kendra', 'Lisa', 'John'}

display(Art_Club ^ Dance_Club, target='output') # All Students involved in at least one club
display(Art_Club & Dance_Club, target='output') # Students who belong to both clubs
display(Art_Club, target='output') # Students only in the first club
display(Dance_Club, target='output') # Students only in the second club
display(Art_Club - Dance_Club, target='output') # students who are exactly in one club