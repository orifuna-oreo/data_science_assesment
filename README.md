# Data Science Assessment

## Getting Started

1. **Fork this Repository**: Before starting the assessment, please fork this repository to your own GitHub account. This will allow you to submit your work later.

2. **Clone Your Fork**: Clone your forked repository to your local machine to begin working.

3. **Dataset**: This assessment uses the Open University Learning Analytics Dataset (OULAD), which contains student interaction data with a Virtual Learning Environment. Sample data is provided in the `oulad_data` directory, or you can download the full dataset from [the official source](https://analyse.kmi.open.ac.uk/open-dataset/download).

4. **Setup**: Run the following commands to set up your environment if you not sure how to get the training dat:
   ```bash

  #create the data directory
  mkdir oulad_data

   # Install required packages
   pip install pandas numpy matplotlib seaborn scikit-learn
   
   # Generate sample data (if needed)
   python create_sample_data.py
   
   ```

## Assessment Structure

This assessment consists of three main parts, with a total time of approximately 4-5 hours.

### 1. Data Exploration (1 to 1.5 hours)

- **Task**: Perform data analysis (cleaning, visualizations, identifying trends).
- **Goal**: Identify key patterns in student behavior and performance based on content type, topics, and time spent in the Virtual Learning Environment.
- **Deliverables**: 
  - Python notebook or script with your analysis
  - Key visualizations highlighting important patterns
  - Brief summary of your findings

### 2. Model Proposal (1.5 to 2 hours)

- **Task**: Propose a machine learning model to predict student performance or engagement.
- **Goal**: Justify your model choice and provide a basic summary of its performance.
- **Deliverables**:
  - Python notebook or script implementing your model
  - Explanation of why you chose this model (e.g., decision trees, random forest)
  - Performance metrics (accuracy, precision, recall, etc.)
  - Discussion of feature importance

### 3. Presentation Preparation (1.5 to 2 hours)

#### For the Tech Lead:
- Provide a comprehensive README in your repository.
- Include:
  - A technical summary of your model and why it was chosen
  - Key findings from your analysis (trends in content effectiveness, user engagement)
  - Instructions for reproducing your results

#### For the Non-Tech Person:
- Provide 1-2 clear visuals (graphs like bar charts, heatmaps, etc.)
- A basic writeup explaining:
  - Key findings in simple terms (e.g., "Video content helps students perform better in Math")
  - Actionable insights (e.g., "Content personalization can be done based on quiz performance")