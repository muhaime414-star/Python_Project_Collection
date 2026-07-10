import argparse
import os
parser = argparse.ArgumentParser(description="Extreact unique IPs from a log file.")
parser.add_argument('-f', '--file', required=True, help= "The input log file to process")
parser.add_argument('-o', '--output', help="The name of the custom output file (optional)")
args = parser.parse_args()
input_file=args.file 



if args.output:
    output_file=args.output
else:
    base_name=os.path.basename(input_file)
    output_file=f"duplicate_free_{base_name}"

unique_ip=[]

try:
    with open(input_file,'r') as file:
        logs=file.readlines()
    for line in logs:
        clean_ip = line.strip()

        if clean_ip not in unique_ip:
            unique_ip.append(clean_ip)

    with open(output_file,'w')as out_file:
        for ip in unique_ip:
            out_file.write(f"{ip}\n")

    print(f"Success! {len(unique_ip)} unique IPs from {len(logs)} addresses have been saved to '{output_file}'")


except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found. Please check the name and try again.")




