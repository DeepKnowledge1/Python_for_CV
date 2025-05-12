import os

# Define the sections and their corresponding shortened titles for folder names
sections = [
    "Sec1_Intro",
    "Sec2_Core_Python_CV",
    "Sec3_OOP_in_CV",
    "Sec4_Working_with_Images",
    "Sec5_File_Folder_Management",
    "Sec6_Image_Manipulation",
    "Sec7_CV_Algorithms",
    "Sec8_Feature_Detection",
    "Sec9_Data_Augmentation",
    "Sec10_Advanced_Segmentation",
    "Sec11_Motion_Analysis",
    "Sec12_Mask_Generation",
    "Sec13_Metadata_Annotation",
    "Sec14_Dataset_Analysis",
    "Sec15_Performance_Optimization",
    "Sec16_CV_and_Deep_Learning",
    "Sec17_Optimizing_PaDiM",
    "Sec18_Model_Validation",
    "Sec19_Final_Project",
    "Sec20_Bonus_Tips"
]

# Create folders and README.md files for each section
base_path = "./"

# Create base directory if it doesn't exist
os.makedirs(base_path, exist_ok=True)

# Loop through each section and create folders and README.md files
for section in sections:
    # Create section folder
    section_folder = os.path.join(base_path, section)
    os.makedirs(section_folder, exist_ok=True)
    
    # Prepare the content for the README.md file
    readme_content = f"# {section.replace('_', ' ').title()}\n\nThis is the README file for the {section.replace('_', ' ').title()}.\n\n### Overview:\nProvide an overview of the section content here.\n"
    
    # Write the README.md file inside the section folder
    readme_path = os.path.join(section_folder, "README.md")
    with open(readme_path, 'w') as readme_file:
        readme_file.write(readme_content)

print("Folders and README.md files created successfully.")
