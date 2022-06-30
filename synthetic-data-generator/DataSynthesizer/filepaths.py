import os
import sys
from pathlib import Path

this_filepath = Path(os.path.realpath(__file__))
project_root = str(this_filepath.parents[1])

data_dir = os.path.join(project_root, 'data/')

# add the DataSynthesizer repo to the pythonpath
data_synthesizer_dir = os.path.join(project_root, 'DataSynthesizer/')
sys.path.append(data_synthesizer_dir)

plots_dir = os.path.join(project_root, 'plots/')

hospital_ae_data_deidentify = os.path.join(data_dir, 'datasets_228_482_diabetes.csv')

hospital_ae_data_synthetic_random = os.path.join(
    data_dir, 'datasets_228_482_diabetes.csv')
hospital_ae_data_synthetic_independent = os.path.join(
    data_dir, 'datasets_228_482_diabetes.csv')
hospital_ae_data_synthetic_correlated = os.path.join(
    data_dir, 'datasets_228_482_diabetes.csv')

hospital_ae_description_random = os.path.join(
    data_dir, 'ddatasets_549966_1402864_nation_level_daily_random.json')
hospital_ae_description_independent = os.path.join(
    data_dir, 'datasets_549966_1402864_nation_level_daily_independent.json')
hospital_ae_description_correlated = os.path.join(
    data_dir, 'datasets_549966_1402864_nation_level_daily_correlated.json')

