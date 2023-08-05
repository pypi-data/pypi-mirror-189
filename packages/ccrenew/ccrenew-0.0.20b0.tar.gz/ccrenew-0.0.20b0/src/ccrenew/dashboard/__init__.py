"""Package for working with Cypress Creek Renewables Dashboard process
"""
print('Starting imports')
import warnings
from pandas.errors import PerformanceWarning
warnings.simplefilter(action='ignore', category=(FutureWarning, PerformanceWarning))
warnings.filterwarnings(action='ignore', message='divide by zero')

from ccrenew.dashboard.data_processing import CCR as ccr

print('Pulling df_keys from Smartsheets...')
all_df_keys = ccr.get_df_keys(retired=True)

from ccrenew.dashboard.utils.dashboard_utils import func_timer

print('Importing DashboardSession')
from ccrenew.dashboard.session import DashboardSession
from ccrenew.dashboard.project import Project
from ccrenew.dashboard.utils.dashboard_utils import run_bluesky
from ccrenew.dashboard.utils.project_neighbors import (
    find_nearby_projects,
    find_nearby_similar_projects,
    find_similar_projects
)
