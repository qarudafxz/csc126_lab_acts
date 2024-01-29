from operator import itemgetter

def user_info():
 details = dict({ 
   "name": "Francis John Saul Tin-ao", 
   "age": 21,
   "gender": "Male", 
   "occupation": "Software Engineer", 
   "primary_school": "Agusan National High School", 
   "college": "Caraga State University", 
   "contact_num": "09949923896",
   "undergrad": "Bachelor of Science in Information Technology",
   "status": "Single",
   "address": "Ampayon",
   "secondary": "Butuan",
   "graduate": "Not yet",
   "color": "Black",
   "hobby": "Coding",
   "height": "5'7",
   "weight": "50kg",
   "bmi": "18.5",
   "blood_type": "A+",
   "religion": "Roman Catholic",
   "fave_subject": "Data Structures and Algorithm"
   })
 
 return details

def main():
 details = user_info()
 
 name, age, gender, occupation, primary_school, college, contact_num, undergrad, status, address, secondary, graduate, color, hobby, height, weight, bmi, blood_type, religion, fave_subject = itemgetter('name', 'age', 'gender', 'occupation', 'primary_school', 'college', 'contact_num', 'undergrad', 'status', 'address','secondary', 'graduate', 'color', 'hobby', 'height', 'weight', 'bmi', 'blood_type', 'religion', 'fave_subject')(details)
 
 print(f"""
                   \t\t\t\tPERSONAL INFORMATION\n
     
  \tName: {name}                           \tAge: {age}
  \tGender: {gender}                        \t\t\t\tOccupation: {occupation}
  \tPrimary School: {primary_school}        \t\tCollege: {college}
  \tContact Number: {contact_num}           \t\t\t\tUndergraduate: {undergrad}
  \tStatus: {status}                        \t\t\t\tAddress: {address}
  \tSecondary: {secondary}                  \t\t\t\tGraduate: {graduate}
  \tFavorite Color: {color}                 \t\t\t\tHobby: {hobby}
  \tHeight: {height}                        \t\t\t\tWeight: {weight}
  \tBMI: {bmi}                              \t\t\t\tBlood Type: {blood_type}
  \tReligion: {religion}                    \t\t\tFavorite Subject: {fave_subject}
       """)
 

if(__name__ == "__main__"):
 main()
