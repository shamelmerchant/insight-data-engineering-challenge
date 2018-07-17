# Table of Contents
1. [Problem](README.md#problem)
2. [Input Dataset](README.md#input-dataset)
3. [Approach](README.md#approach)
4. [How to Run](README.md#run)
5. [Dependencies](README.md#dependencies)

# Problem

We are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name. 

# Input Dataset

The original dataset was obtained from the Centers for Medicare & Medicaid Services but has been cleaned and simplified to match the scope of the coding challenge. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name.  It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication. 

# Approach
The number of unique prescribers and the total cost for each drug is extracted as the data file is read. The unique id (UID) used here is the last name, first name of the prescriber instead of the provided ID.

The extracted data is stored in a dictionary which is sorted and written to output file

To speed up the code we use a defaultdict to store the UID instead of dict 

# Run
The pharmacy_counting script is launched by running _run.sh_ Bash script:

	./run.sh

The results will be available in the files _output/top_cost_drug.txt_.

# Dependencies
- Python3