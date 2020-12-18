#!/bin/python



import xmltodict
from pathlib import PurePath
import os
from time import sleep



def parse_fdp_xml(filename):

    with open(filename) as f:
        fdp_xml = xmltodict.parse(f.read())

    try:
        path=fdp_xml["AutoProcContainer"]\
                    ["AutoProcProgramContainer"]\
                    ["AutoProcProgramAttachment"][0]\
                    ["filePath"]

        path_parts = PurePath(path).parts
        sample_name_path = '/'.join([path_parts[-4],path_parts[-3]])
        
        #all resolution shells
        overall = fdp_xml["AutoProcContainer"]\
                         ["AutoProcScalingContainer"]\
                         ["AutoProcScalingStatistics"][0]
        #pertinent values for table                 
        res_lim_low_overall = float(overall["resolutionLimitLow"])
        res_lim_high_overall = float(overall["resolutionLimitHigh"])
        r_merge_overall = float(overall["rMerge"])
        cc_half_overall = float(overall["ccHalf"])
        comp_overall = float(overall["completeness"])
        mult_overall = float(overall["multiplicity"])
       
        #outer resolution shell
        outer = fdp_xml["AutoProcContainer"]\
                       ["AutoProcScalingContainer"]\
                       ["AutoProcScalingStatistics"][2]
        #pertinent values for table                 
        res_lim_low_outer = float(outer["resolutionLimitLow"])
        res_lim_high_outer = float(outer["resolutionLimitHigh"])
        r_merge_outer = float(outer["rMerge"])
        cc_half_outer = float(outer["ccHalf"])
        comp_outer = float(outer["completeness"])
        mult_outer = float(outer["multiplicity"])
        
        #symmetry info
        cell = fdp_xml["AutoProcContainer"]["AutoProc"]
        space_group = cell["spaceGroup"]
        a = float(cell["refinedCell_a"])
        b = float(cell["refinedCell_b"])
        c = float(cell["refinedCell_c"])
        alpha = float(cell["refinedCell_alpha"])
        beta = float(cell["refinedCell_beta"])
        gamma = float(cell["refinedCell_gamma"])

        return (sample_name_path,
                res_lim_high_overall,
                res_lim_low_overall,
                r_merge_overall,
                cc_half_overall,
                comp_overall,
                mult_overall,
                res_lim_high_outer,
                res_lim_low_outer,
                r_merge_outer,
                cc_half_outer,
                comp_outer,
                mult_outer,
                space_group,
                a,
                b,
                c,
                alpha,
                beta,
                gamma)

    except KeyError:
        return None

def make_header():
    first_row = ''.join([f"{'':39}",
                         f'{"|---------------Overall------------------|":^14}',
                         f'{"|-------------Outer-Shell----------------|":^14}\n',])
    formatted_string=''.join([f'{"Sample Path":>39}',
                              f'{"Hi":>7}',
                              f'{"Lo":>7}',
                              f'{"R_mrg":>7}',
                              f'{"cc12":>7}',
                              f'{"comp":>7}',
                              f'{"mult":>7}',
                              f'{"Hi":>7}',
                              f'{"Lo":>7}',
                              f'{"R_mrg":>7}',
                              f'{"cc12":>7}',
                              f'{"comp":>7}',
                              f'{"mult":>7}',
                              f'{"symm":>12}',
                              f'{"a":>7}',
                              f'{"b":>7}',
                              f'{"c":>7}',
                              f'{"alpha":>7}',
                              f'{"beta":>7}',
                              f'{"gamma":>7}'])
    return ''.join([first_row,formatted_string])

def format_results_string(*args):
    result_string = args[0]
    try:
        formatted_string=''.join([f'{result_string[0]:>39}',#sample path
                                  f'{result_string[1]:7.2f}',#high res cut overall
                                  f'{result_string[2]:7.2f}',#low res cut overall
                                  f'{result_string[3]:7.3f}',#R_merge overall
                                  f'{result_string[4]:7.2f}',#cc12 overall
                                  f'{result_string[5]:7.2f}',#completeness overall
                                  f'{result_string[6]:7.2f}',#multiplicity overall
                                  f'{result_string[7]:7.2f}',#high res cut outer
                                  f'{result_string[8]:7.2f}',#low res cut outer
                                  f'{result_string[9]:7.3f}',#R_merge outer
                                  f'{result_string[10]:7.2f}',#cc12 outer
                                  f'{result_string[11]:7.2f}',#completeness outer
                                  f'{result_string[12]:7.2f}',#multiplicity outer
                                  f'{result_string[13]:>12}',#space group
                                  f'{result_string[14]:7.1f}',#a
                                  f'{result_string[15]:7.1f}',#b
                                  f'{result_string[16]:7.1f}',#c
                                  f'{result_string[17]:7.1f}',#alpha
                                  f'{result_string[18]:7.1f}',#beta
                                  f'{result_string[19]:7.1f}'])#gamma
        return formatted_string
    except TypeError:
        return result_string

if __name__ == "__main__":
    test_dir = os.getcwd()
    if os.path.basename(test_dir) == "fast_dp_dir":
        mx_directory = PurePath(test_dir).parent
        print(mx_directory)

        with open("fast_dp.summary.txt","w") as f:
            f.write(''.join([make_header(),'\n']))
            print(make_header())

        fast_dp_xml_set = set([])
        while True:
            with open("fast_dp.summary.txt","a") as f:
                for (dpath,dnames,fnames) in os.walk(mx_directory):
                    dnames.sort()
                    for fname in fnames:
                        if fname == "fast_dp.xml" or fname == "autoPROC.xml":
                            fast_dp_xml_path = os.path.join(dpath,fname)
                            if fast_dp_xml_path not in fast_dp_xml_set:
                                results = parse_fdp_xml(fast_dp_xml_path)
                                if results:
                                    f.write(''.join([format_results_string(results),'\n']))
                                    print(format_results_string(results))
                                fast_dp_xml_set.add(fast_dp_xml_path)
            sleep(5)
    else:
        print("summarytable must be launched from fast_dp_dir...")

