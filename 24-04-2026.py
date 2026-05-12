import pandas as pd;
import matplotlib.pyplot as plt;


#pie chart
# subjects = ['Math', 'Science', 'English', 'History']
# marks = [85, 90, 78, 92]
# colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

#plt.pie(marks, labels=subjects, colors=colors, autopct='%1.1f%%', startangle=140)
# plt.title('Marks Distribution')
# plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
# plt.ylabel('Marks')  # Add y-axis label
# plt.xlabel('Subjects')  # Add x-axis label
# explode = (0.1, 0, 0, 0)  # Explode the first slice (Math)
# plt.pie(marks, labels=subjects, colors=colors, autopct='%1.1f%%', startangle=140, explode=explode)
# plt.show()

#histoplot
# data = [85, 90, 78, 92, 88, 95, 80, 82, 91, 89]
# plt.hist(data, bins=5, color='blue', edgecolor='black')
# plt.title('Marks Distribution')
# plt.xlabel('Marks')
# plt.ylabel('Frequency')
# plt.show()

#####histogram
marks = [45,50,55,60,62,65,67,70,72,75,78,80,82,85,88,90,92,95,97,100]
# [100-45]=55
# bins => 55/5=11
# bin1 = 45 to 56 = 3 students 
# bin2 = 56 to 67 = 0 students
# bin3 = 67 to 78 = 5 students
# bin4 = 78 to 89 = 7 students  

# plt.figure(figsize=(10, 6))
# plt.hist(marks, bins=5, color="blue", edgecolor="black")
# plt.title("Marks Distribution")
# plt.xlabel("Marks")     
# plt.ylabel("Frequency")
# plt.xticks(range(40, 101, 10))  # Set x-ticks from 40 to 100 with a step of 10
# plt.show()



#scatter plot   
# hours_studied = [1, 2, 3, 4, 5, 6]
# exam_scores = [35, 45, 50, 60, 70, 85]
# plt.figure(figsize=(10, 6))
# plt.scatter(hours_studied, exam_scores, color='red',s=100,edgecolors='black',alpha=0.9)  # s is the size of the points
# plt.title('Hours Studied vs Exam Scores')
# plt.grid(True)
# plt.xlabel('Hours Studied') 
# plt.ylabel('Exam Scores')
# plt.show()


plt.figure(figsize=(10,8))

plt.subplot(2,2,1) # in 2 x 2 grid, this is the 1st plot
x = [1,2,3,4]
y = [10,20,30,40]
plt.plot(x,y)

plt.subplot(2,2,2) # in 2 x 2 grid, this is the 2nd plot
plt.bar(x,y)

plt.subplot(2,2,3) # in 2 x 2 grid, this is the 3rd plot
marks = [45, 50, 55, 60, 62, 65, 67, 70, 72, 75,
         78, 80, 82, 85, 88, 90, 92, 95, 97, 100]
plt.hist(marks,
         bins=5,
         color='skyblue',
         edgecolor='black')

plt.title("Students Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()

d1 = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],

