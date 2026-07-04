
#student report generator
import csv
#step 1
def process_student_data(input_file, output_file):
  try:
    student_report = []
    with open(input_file,'r') as infile:
      reader=csv.DictReader(infile)
      for row in reader:
        student_name=row['Name']
        math_score=float(row['Math_score'])
        science_score=float(row['Science_score'])
        english_score=float(row['English_score'])
        total_score=math_score+science_score+english_score
        average_score=round(total_score/3,2)
        status='Pass' if average_score>=60 else 'Fail'
        student_report.append({
            'Name':student_name,
            'Math_score':math_score,
            'Science_score':science_score,
            'English_score':english_score,
            'Total_score':total_score,
            'Average_score':average_score,
            'Status':status
        })
    with open(output_file,'w',newline='') as outfile:
      fieldnames=['Name','Math_score','Science_score','English_score','Total_score','Average_score','Status']
      writer=csv.DictWriter(outfile,fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(student_report)
      print(f"Student report generated and saved to {output_file}")
  except FileNotFoundError:
    print("Input file not found")
  except ValueError as e:
    print(f"Error processing data: {e}")
  except Exception as e:
    print(f"An error occurred: {e}")


#main program
input_file='student_data.csv'
output_file='student_report.csv'
process_student_data(input_file,output_file)
