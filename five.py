import random

def check_triangle_size(size):
 size = int(size)
 if(size < 3):
  size += 2
 
 return size

def get_word_length(params):
 return len(params)

def generate_triangles(size):
 triangles = []
 for _ in range(size):
  triangle = {"side1": random.randint(1, 10), "side2": random.randint(1, 10), "side3": random.randint(1, 10)}
  triangles.append(triangle)
  
 return triangles

def calculate_inner_values_of_triangle(triangles):
  temp = []
  for i in range(len(triangles)):
   side1 = triangles[i]["side1"]
   side2 = triangles[i]["side2"]
   side3 = triangles[i]["side3"]

   temp.append(side1)
   temp.append(side2)
   temp.append(side3)

  print(temp)
  temp = list(set(temp))

  print("INNER VALUES OF A LIST REMOVED DUPLICATE", temp)
  sum_inner_values = sum(temp)

  print("TOTAL INNER VALUES:", sum_inner_values)

def calculate_outer_values_of_triangle(triangles):
 #loop the triangles and sum the sides 
 total_outer_values = []
 for i in range(len(triangles)):
  side1 = triangles[i]["side1"]
  side2 = triangles[i]["side2"]
  side3 = triangles[i]["side3"]
  
  temp = []
  temp.append(side1)
  temp.append(side2)
  temp.append(side3)
  
 #remove duplicates on each row or sides of a triangle
  for j in range(len(temp)):
   for k in range(len(temp)):
    if(j != k):
     if(temp[j] == temp[k]):
      temp.pop(j)
      break
   break
  
  print("OUTER", temp)
  
  #loop each row of temp
  for _ in range(len(temp)):
   sum = 0
   for m in range(len(temp)):
    sum += temp[m]
   total_outer_values.append(sum)
   break
  
 print(total_outer_values)
   
 total = 0
 for i in range(len(total_outer_values)):
  total += total_outer_values[i]
  
 print("TOTAL OUTER SIDES: ", total)

def main():
 last_name = input("Enter your last name: ")
 size = get_word_length(last_name)
 
 size /= 2
 
 final_size = int(check_triangle_size(size))
 triangles = generate_triangles(final_size)
 
 for i in range(len(triangles)):
  print(triangles[i])

 #inner values
 calculate_inner_values_of_triangle(triangles)
 
 #outer values
 calculate_outer_values_of_triangle(triangles)
 
if(__name__ == "__main__"):
 main()