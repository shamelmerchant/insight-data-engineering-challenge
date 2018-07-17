#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 20:26:21 2018

@author: shamel
"""

import os
import sys
import csv
from collections import defaultdict
from collections import OrderedDict

def read_data(input_file):
    '''
    Read csv data and store number of unique prescribers and total cost for each drug
    
    @param input_file: Path to input file
    @return output: Dictionary containing no of 'uniqe_prescribers' and 'total_cost' for each drug
    
    '''
    # TODO: Check what is the right unique ID (last,first) ot (id)  
    
    output = {}
    prescriber_id = defaultdict(set)
    
    with open(input_file,'r') as file:
        reader = csv.DictReader(file)
        
        try:
            for row in reader:
                drug = row['drug_name']
                # Define uid as last name, first name
                uid =  row['prescriber_last_name'],row['prescriber_first_name'] #int(row['id'])
                cost = float(row['drug_cost'])
                
                # Check if drug is present in the output
                if drug in output.keys():
                    # Check if prescriber is already add to the output
                    if uid in prescriber_id[drug]:
                        # Prescriber is already present, just update the cost
                        output[drug]['total_cost'] += cost
                    else:
                        # New prescriber found, append the id
                        prescriber_id[drug].add(uid)
                        # Update the uniqe prescribers and the cost
                        output[drug]['num_unique_prescriber'] += 1
                        output[drug]['total_cost'] += cost
                    
                else:
                    # Add the drug name to output, and set prescribers to 1 and total cost of drug to cost  
                    output[drug] = {'num_unique_prescriber':1,
                                    'total_cost':cost}
                    
                    # Initialize the prescriber id
                    prescriber_id[drug].add(uid)
        
        except csv.Error as e:
            sys.exit('File {}, failed at line {}: {}'.format(input_file, reader.line_num, e))
            
    return output


def write_output(output, output_file):
    '''
    Write output to csv file
    
    @param output: Output dictionary containing drug, number of prescribers and total cost
    @param output_file: Path to output file
    
    '''
    # Sort the output on basis of total_cost then drug name
    output = OrderedDict(sorted(output.items(), key=lambda x:(-x[1]['total_cost'],x[0])))
    
    # Write the csv output
    with open(output_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['drug_name','num_prescriber','total_cost'])
        for drug, drug_data in output.items():
            writer.writerow([drug,drug_data['num_unique_prescriber'],round(drug_data['total_cost'])])


def main():
    
    # Read in the sys argument
    args = sys.argv
    
    # TODO: change to argparse
    # Check if the two arguments are given, 
    if len(sys.argv) > 3:
        print('Please provide path to input_file and output_file')
        sys.exit(1)
    
    
    input_file = args[1]  #  path to input file
    output_file = args[2] #  path to output file
    
    output = read_data(input_file)
    write_output(output, output_file)

if __name__ == '__main__':
    main()

