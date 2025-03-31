import pandas as pd
import numpy as np
import os

# Create directory if it doesn't exist
os.makedirs('oulad_data', exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)

# Sample size
n_students = 1000
n_modules = 5
n_presentations = 2
n_assessments = 4
n_vle_materials = 20
n_days = 240  # Course duration in days

# Generate courses data
modules = [f'AAA', 'BBB', 'CCC', 'DDD', 'EEE']
presentations = ['2013J', '2014B']
course_lengths = [240, 240, 240, 240, 240]

courses_data = []
for module in modules:
    for presentation in presentations:
        courses_data.append({
            'code_module': module,
            'code_presentation': presentation,
            'length': course_lengths[modules.index(module)]
        })

courses_df = pd.DataFrame(courses_data)
courses_df.to_csv('oulad_data/courses.csv', index=False)
print(f"Created courses.csv with {len(courses_df)} rows")

# Generate student info data
genders = ['M', 'F']
regions = ['East Anglian Region', 'Scotland', 'North Western Region', 'South Region', 
           'Wales', 'North Region', 'South West Region', 'West Midlands Region', 
           'East Midlands Region', 'South East Region', 'London Region']
education_levels = ['HE Qualification', 'A Level or Equivalent', 'Lower Than A Level', 
                   'Post Graduate Qualification', 'No Formal quals']
imd_bands = ['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', 
            '70-80%', '80-90%', '90-100%']
age_bands = ['0-35', '35-55', '55<=']
final_results = ['Distinction', 'Pass', 'Fail', 'Withdrawn']

student_info_data = []
for i in range(n_students):
    student_id = i + 1
    for module in np.random.choice(modules, size=np.random.randint(1, 3), replace=False):
        for presentation in np.random.choice(presentations, size=1):
            # Weight final results to make more realistic distribution
            result_weights = [0.15, 0.45, 0.25, 0.15]  # Distinction, Pass, Fail, Withdrawn
            
            student_info_data.append({
                'code_module': module,
                'code_presentation': presentation,
                'id_student': student_id,
                'gender': np.random.choice(genders),
                'region': np.random.choice(regions),
                'highest_education': np.random.choice(education_levels),
                'imd_band': np.random.choice(imd_bands),
                'age_band': np.random.choice(age_bands),
                'num_of_prev_attempts': np.random.randint(0, 3),
                'studied_credits': np.random.choice([30, 60, 90, 120, 150]),
                'disability': np.random.choice(['Y', 'N'], p=[0.1, 0.9]),
                'final_result': np.random.choice(final_results, p=result_weights)
            })

student_info_df = pd.DataFrame(student_info_data)
student_info_df.to_csv('oulad_data/studentInfo.csv', index=False)
print(f"Created studentInfo.csv with {len(student_info_df)} rows")

# Generate assessments data
assessment_types = ['TMA', 'CMA', 'Exam']
assessment_weights = {'TMA': 20, 'CMA': 30, 'Exam': 100}

assessments_data = []
assessment_id = 1

for module in modules:
    for presentation in presentations:
        # Regular assessments
        for i in range(n_assessments - 1):
            assessment_type = np.random.choice(['TMA', 'CMA'])
            assessments_data.append({
                'code_module': module,
                'code_presentation': presentation,
                'id_assessment': assessment_id,
                'assessment_type': assessment_type,
                'date': int(30 + i * 45),  # Spaced throughout the course
                'weight': assessment_weights[assessment_type]
            })
            assessment_id += 1
        
        # Final exam
        assessments_data.append({
            'code_module': module,
            'code_presentation': presentation,
            'id_assessment': assessment_id,
            'assessment_type': 'Exam',
            'date': 230,  # Near the end of the course
            'weight': assessment_weights['Exam']
        })
        assessment_id += 1

assessments_df = pd.DataFrame(assessments_data)
assessments_df.to_csv('oulad_data/assessments.csv', index=False)
print(f"Created assessments.csv with {len(assessments_df)} rows")

# Generate VLE data
activity_types = ['resource', 'url', 'forum', 'quiz', 'oucontent', 'subpage', 'page', 'glossary']

vle_data = []
site_id = 1

for module in modules:
    for presentation in presentations:
        for _ in range(n_vle_materials):
            activity_type = np.random.choice(activity_types)
            week_from = np.random.randint(1, 30)
            week_to = min(week_from + np.random.randint(1, 10), 35)
            
            vle_data.append({
                'id_site': site_id,
                'code_module': module,
                'code_presentation': presentation,
                'activity_type': activity_type,
                'week_from': week_from,
                'week_to': week_to
            })
            site_id += 1

vle_df = pd.DataFrame(vle_data)
vle_df.to_csv('oulad_data/vle.csv', index=False)
print(f"Created vle.csv with {len(vle_df)} rows")

# Generate student registration data
student_registration_data = []

for _, student_row in student_info_df.iterrows():
    # Registration date (usually before course starts)
    reg_date = -np.random.randint(10, 60)
    
    # If withdrawn, add unregistration date
    unreg_date = None
    if student_row['final_result'] == 'Withdrawn':
        unreg_date = np.random.randint(10, 200)
    
    student_registration_data.append({
        'code_module': student_row['code_module'],
        'code_presentation': student_row['code_presentation'],
        'id_student': student_row['id_student'],
        'date_registration': reg_date,
        'date_unregistration': unreg_date
    })

student_registration_df = pd.DataFrame(student_registration_data)
student_registration_df.to_csv('oulad_data/studentRegistration.csv', index=False)
print(f"Created studentRegistration.csv with {len(student_registration_df)} rows")

# Generate student assessment data
student_assessment_data = []

for _, assessment_row in assessments_df.iterrows():
    # Get students for this module-presentation
    module_students = student_info_df[
        (student_info_df['code_module'] == assessment_row['code_module']) & 
        (student_info_df['code_presentation'] == assessment_row['code_presentation'])
    ]
    
    for _, student_row in module_students.iterrows():
        # Skip if student withdrew before assessment
        if student_row['final_result'] == 'Withdrawn':
            reg_info = student_registration_df[
                (student_registration_df['id_student'] == student_row['id_student']) &
                (student_registration_df['code_module'] == student_row['code_module']) &
                (student_registration_df['code_presentation'] == student_row['code_presentation'])
            ]
            
            if not reg_info.empty and reg_info.iloc[0]['date_unregistration'] is not None:
                if reg_info.iloc[0]['date_unregistration'] < assessment_row['date']:
                    continue
        
        # Determine score based on final result
        if student_row['final_result'] == 'Distinction':
            score = np.random.randint(75, 101)
        elif student_row['final_result'] == 'Pass':
            score = np.random.randint(55, 85)
        elif student_row['final_result'] == 'Fail':
            score = np.random.randint(0, 55)
        else:  # Withdrawn
            # 50% chance they didn't submit
            if np.random.random() < 0.5:
                continue
            score = np.random.randint(0, 70)
        
        # Submission date (usually close to the assessment date)
        submission_date = min(assessment_row['date'] - np.random.randint(0, 7), assessment_row['date'])
        
        student_assessment_data.append({
            'id_assessment': assessment_row['id_assessment'],
            'id_student': student_row['id_student'],
            'date_submitted': submission_date,
            'is_banked': 0,
            'score': score
        })

student_assessment_df = pd.DataFrame(student_assessment_data)
student_assessment_df.to_csv('oulad_data/studentAssessment.csv', index=False)
print(f"Created studentAssessment.csv with {len(student_assessment_df)} rows")

# Generate student VLE data
student_vle_data = []

# For each student
for _, student_row in student_info_df.iterrows():
    # Get VLE materials for this module-presentation
    module_vle = vle_df[
        (vle_df['code_module'] == student_row['code_module']) & 
        (vle_df['code_presentation'] == student_row['code_presentation'])
    ]
    
    # Determine number of interactions based on final result
    if student_row['final_result'] == 'Distinction':
        n_interactions = np.random.randint(50, 200)
    elif student_row['final_result'] == 'Pass':
        n_interactions = np.random.randint(30, 150)
    elif student_row['final_result'] == 'Fail':
        n_interactions = np.random.randint(10, 100)
    else:  # Withdrawn
        n_interactions = np.random.randint(5, 50)
    
    # Generate interactions
    for _ in range(n_interactions):
        # Randomly select a VLE material
        if len(module_vle) > 0:
            vle_material = module_vle.sample(1).iloc[0]
            
            # Determine date of interaction
            if student_row['final_result'] == 'Withdrawn':
                # Find unregistration date
                reg_info = student_registration_df[
                    (student_registration_df['id_student'] == student_row['id_student']) &
                    (student_registration_df['code_module'] == student_row['code_module']) &
                    (student_registration_df['code_presentation'] == student_row['code_presentation'])
                ]
                
                if not reg_info.empty and reg_info.iloc[0]['date_unregistration'] is not None:
                    max_date = reg_info.iloc[0]['date_unregistration']
                else:
                    max_date = 100  # Default if no unregistration date
            else:
                max_date = n_days
            
            date = np.random.randint(1, max_date)
            
            # Number of clicks
            sum_click = np.random.randint(1, 10)
            
            student_vle_data.append({
                'code_module': student_row['code_module'],
                'code_presentation': student_row['code_presentation'],
                'id_student': student_row['id_student'],
                'id_site': vle_material['id_site'],
                'date': date,
                'sum_click': sum_click
            })

student_vle_df = pd.DataFrame(student_vle_data)
student_vle_df.to_csv('oulad_data/studentVle.csv', index=False)
print(f"Created studentVle.csv with {len(student_vle_df)} rows")

print("\nSample data creation complete. You can now run visualize_oulad.py")
