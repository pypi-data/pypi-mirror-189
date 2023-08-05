import calendar
from collections import namedtuple
from datetime import (
    datetime,
    timedelta
)
from dateutil import parser
from dateutil.parser import ParserError
import logging
from numbers import Number
import numpy as np
from matplotlib import pyplot as plt, rcParams
from matplotlib.figure import Figure
import os
from pandas import Timedelta
from PyQt5.QtGui import QGuiApplication
import sys
import warnings


plt.ion()  # turn on interactive plots
plt.style.use('ggplot')

# Create logger
logger = logging.getLogger(__name__)

# Create namedtuple for storing plots
_Plot = namedtuple('_Plot', 'fig ax')

# Python 2 compatibility
if sys.version_info.major == 3:
    unicode = str
    long = float


class Plotter(object):
    """Object to coordinate drawing of plots for a project.

    Args:
        project (Project): A CCR Dashboard `Project` object
    """
    
    def __init__(self, project, *args, **kwargs):
        self.project = project
        self.persist = kwargs.get('persist', False)
        self.plot_list = {}
        """ A list of plots that have been generated by the `Plotter` object."""


    def __repr__(self):
        return 'Plotter object for {}'.format(self.project.project_name)
    

    def __str__(self):
        return 'Plotter object for {}'.format(self.project.project_name)


    def draw_dashboard_plots(self, plot_order=None, **kwargs):
        """Draws plots for Dashboard

        Args:
            plot_order (list or str, optional): A list of plots to draw. This can be
                any number of plots from one to all plots. Defaults to all plots in the below order.
            <h2>Acceptable Options & Default Order:</h2>
            * `xplot_pwr_poa`: Crossplot of meter & POA data.
            * `xplot_temp`: Crossplot of meter & POA, colored by Tamb.
            * `temps`: Tcell temperature comparison.
            * `inv`: Inverters.
            * `pr`: Hourly PR plot.
            * `8760`: Measured vs 8760 comparison.
            * `weather`: Weather sensors.
            * `mtr_corrected`: Meter corrections.
            * `mtr_dif`: Meter correction dif.
            * `poas`: POA sensors.
            * `pwr_poa`: Meter & POA avg.
            * `ghi`: GHI sensors.
            * `irrad`: POA & GHI sensors.
            * `tz`: Timezone check.
            * `losses`: Losses by type.
            * `poa_corr`: POA correlation check.
            * `battery`: Battery plot - will only show for battery sites.
            * `tracker`: Tracker angle plot - will only show for tracker sites.

        """
        mth = kwargs.get('mth', None)
        close_plots = kwargs.get('close_plots', True)
        min_date = kwargs.get('min_date', None)
        max_date = kwargs.get('max_date', None)
        poa_onboarding = kwargs.get('poa_onboarding', False)
        open_folder = kwargs.get('open_folder', False)
        fullscreen = kwargs.get('fullscreen', True)
            
        # Close all existing plots if requested
        if close_plots:
            if isinstance(close_plots, bool):
                self.close_plots()
            else:
                self.close_plots(close_plots)

        # Default month to a month previous to today
        if not mth:
            mth = datetime.now().month - 1
            
        def parse_date(dt, direction, days=None):
            if isinstance(dt, (int, float, long)):
                if direction == 'backward':
                    dt = datetime.today() - timedelta(days=abs(dt))
                else:
                    dt = datetime.today() + timedelta(days=abs(dt))
            else:
                try:
                    dt = parser.parse(dt)
                except (ValueError, ParserError):
                    if direction == 'backward':
                        days = 45 if not days else days
                        dt = datetime.today() - timedelta(days)
                    else:
                        days = 4 if not days else days
                        dt = datetime.today() + timedelta(days)
                except TypeError:
                    pass

            return dt

        # Set min & max dates for plots
        # If no min_date supplied we'll just leave it as None to show the whole plot
        if min_date:
            min_date = parse_date(min_date, 'backward')

        # Default max_date to 4 days from today to give some padding to the right side of the plot
        if max_date:
            max_date = parse_date(max_date, 'forward', 0)
        else:
            max_date = parse_date(datetime.today(), 'forward')

        # Set default date format parameters
        rcParams["date.autoformatter.day"] = "%#m/%#d/%Y"
        rcParams["date.autoformatter.hour"] = "%#m/%#d %H:%M"
        rcParams['figure.titlesize'] = 'xx-large'
        rcParams['figure.titleweight'] = 'bold'

        plot_params = {'mth': mth,
                       'min_date': min_date,
                       'max_date': max_date,
                       'poa_onboarding': poa_onboarding,
                       'fullscreen': fullscreen}

        # Display plots
        if not plot_order:
            self.plot_order = [
                'xplot_pwr_poa',
                'xplot_temp',
                'temps',
                'inv',
                'pr',
                '8760',
                'weather',
                'mtr_corrected',
                'mtr_dif',
                'poas',
                'pwr_poa',
                'ghi',
                'irrad',
                'tz',
                'losses',
                'poa_corr',
            ]
        
            if self.project.Battery_AC_site:
                self.plot_order.append('battery')
            if self.project.Tracker_site:
                self.plot_order.append('tracker')
        else:
            self.plot_order = plot_order

        if isinstance(plot_order, (str, unicode)):
            self.plot_order = [plot_order]

        for plot_name in self.plot_order:
            self.plot_list[plot_name] = _Plot(*self.__plot(plot_name, plot_params, **kwargs))

        if self.persist:
            plt.show(block=True)
        else:
            plt.show()

        if open_folder:
            os.startfile(os.path.join(self.project.dashboard_dir,
                                      self.project.project_directory,
                                      self.project.project_name))
            

    def __plot(self, plot_name, plot_params, **kwargs):
        # Assign parameters
        mth = plot_params['mth']
        min_date = plot_params['min_date']
        max_date = plot_params['max_date']
        poa_onboarding = plot_params['poa_onboarding']
        fullscreen = plot_params['fullscreen']

        default_tool = kwargs.get('default_tool', 'zoom')
        screen = kwargs.get('screen', None)
        tight_layout = kwargs.get('tight_layout', True)

        # Initialize fig & ax variables
        fig, ax, fig_list = None, None, None

        # Closure for drawing multiple axes on a single figure
        def draw_multiple_axes(dfs, axs, min_date, max_date):
            for df, ax in zip(dfs, axs):
                try:
                    df.plot(ax=ax)
                    ax.set_xlim(left=min_date, right=max_date)
                except TypeError:
                    continue


        if plot_name.replace(' ', '_').lower() == 'xplot_pwr_poa':
            # Power vs POA Crossplot
            # We'll start by preparing the data into numpy arrays
            y = self.project.df_Pvsyst.loc[(self.project.df_Pvsyst.index.month == mth), ['Year 0 Actual Production (kWh)']].values
            x = self.project.df_Pvsyst.loc[(self.project.df_Pvsyst.index.month == mth), ['POA (W/m2)']].values
            y1 = self.project.df.loc[(self.project.df.index.month == mth), ['Meter_Corrected_2']].values
            x1 = self.project.df.loc[(self.project.df.index.month == mth), ['POA_avg']].values

            # Then create our figure & axes objects
            fig, ax = plt.subplots(num='Power vs POA - {}'.format(self.project.project_name))    
            fig.suptitle('{}\nMonth: '.format(self.project.project_name) + calendar.month_name[mth],fontsize=14, fontweight='bold')

            # Finally, we'll plot the data
            if self.project.Battery_DC_site:
                title = ('{} Power vs POA\nBattery DC Site'.format(self.project.project_name))
            elif self.project.Battery_AC_site:
                title = ('{} Power vs POA\nBattery AC Site'.format(self.project.project_name))
            else:
                title = ('{} Power vs POA'.format(self.project.project_name))
            ax.set_title(title)
            ax.scatter(x, y, c='b', label='Pvsyst [kWh/POA]')
            ax.scatter(x1, y1, c= 'r', label='Meter [kWh/POA]')
            ax.set_xlabel('POA W/m2')
            ax.set_ylabel('Power Generation kW')
            ax.legend()


        elif plot_name.replace(' ', '_').lower() == 'pwr_poa':
            # Power & POA Timeseries Plot
            # The following plots we'll use a slightly different convention
            # Instead of `ax.plot()` we'll use the pandas pyplot wrapper `df.plot()`
            # In our data preparation stage, if we create a pandas Series object, we'll set the name, which will pass through to the label & legend in pyplot
            # QUESTION: looks like we have two separate y-axis limits, which one do we want?
            y_orig_meter = self.project.df_Meter_ORIGINAL.loc[:,self.project.pos_Meter_ORIGINAL].sum(axis=1)
            y_orig_meter.name = 'Original'
            y_meter_corrected = self.project.df.loc[:, 'Meter_Corrected_2']
            y_meter_corrected.name = 'Meter Corrected'
            y_inv_sum = self.project.ava.loc[:, 'Inv_sum']
            y_inv_sum.name = 'Inv Sum'
            y_poa = self.project.df.loc[:, 'POA_avg']
            y_poa.name = 'POA Avg'
            mc_max = y_meter_corrected.max()
            meter_corrected_ylim = [-0.05*mc_max, mc_max/0.9]
            poa_max = y_poa.max()
            poa_ylim = [-0.05*poa_max, poa_max/0.9]

            fig, ax = plt.subplots(num='Power & POA - {}'.format(self.project.project_name))
            fig.suptitle(self.project.project_name)
            ax_power = ax
            ax_poa = ax_power.twinx()

            if self.project.Battery_DC_site:
                title = 'Power & POA\nBattery DC Site'.format(self.project.project_name)
            elif self.project.Battery_AC_site:
                title = 'Power & POA\nBattery AC Site'.format(self.project.project_name)
            elif self.project.df_proj_keys['Fund'] == 'USB 1':
                title = 'Power & POA\n***NOTE: USB site - will need a utility invoice for meter data***'.format(self.project.project_name)
            else:
                title = 'Power & POA'.format(self.project.project_name)
            ax.set_title(title)
            y_orig_meter.plot(ax=ax_power)
            y_meter_corrected.plot(ax=ax_power, linestyle=':', linewidth=5)
            y_inv_sum.plot(ax=ax_power, linestyle='-.')
            ax.axhline(y = self.project.MWAC * 1000, color = 'r', linestyle = '--', label='Clipping Limit')
            y_poa.plot(ax=ax_poa, color='grey')
            ax_power.set_xlim(left=min_date, right=max_date)
            ax_power.set_ylim(meter_corrected_ylim)
            ax_poa.set_ylim(poa_ylim)
            fig.legend()


        elif plot_name.replace(' ', '_').lower() == 'mtr_corrected':
            # Meter Corrections
            y_orig_meter = self.project.df_Meter_ORIGINAL.loc[:,self.project.pos_Meter_ORIGINAL].sum(axis=1)
            y_orig_meter.name = 'Original'
            y_meter_corrected = self.project.df.loc[:, 'Meter_Corrected_2']
            y_meter_corrected.name = 'Meter Corrected'
            y_inv_sum = self.project.ava.loc[:, 'Inv_sum']
            y_inv_sum.name = 'Inv Sum'
            y_cum_orig = self.project.df_Meter_ORIGINAL.loc[:,self.project.pos_Meter_Cum_ORIGINAL].sum(axis=1)
            y_cum_orig.name = 'Original'
            y_cum_corrected = self.project.df.loc[:, 'Meter_cum_corrected_2']
            y_cum_corrected.name = 'Meter Corrected'
            inv_offset = self.project.df[self.project.pos_Inv_cum].sum(axis=1).subtract(self.project.df_Meter_ORIGINAL.loc[:,self.project.pos_Meter_Cum_ORIGINAL].sum(axis=1)).median()
            y_cum_inv = self.project.df[self.project.pos_Inv_cum].sum(axis=1).subtract(inv_offset)
            y_cum_inv.name = 'Inv Sum'   

            fig, axs = plt.subplots(2, num='Meter Corrections - {}'.format(self.project.project_name), sharex=True)
            fig.suptitle(self.project.project_name)
            ax_power = axs[0]
            ax_cum = axs[1]
            
            if self.project.Battery_DC_site:
                title = 'Power Meter Correction\nBattery DC Site'
            elif self.project.Battery_AC_site:
                title = 'Power Meter Correction\nBattery AC Site'
            elif self.project.df_proj_keys['Fund'] == 'USB 1':
                title = 'Power Meter Correction\n***NOTE: USB site - will need a utility invoice for meter data***'
            else:
                title = ' Power Meter Correction'
            ax_power.set_title(title)
            y_orig_meter.plot(ax=ax_power)
            y_meter_corrected.plot(ax=ax_power, linestyle=':',linewidth=5)
            y_inv_sum.plot(ax=ax_power, linestyle='-.')
            ax_power.axhline(y = self.project.MWAC * 1000, color = 'r', linestyle = '--', label='Clipping Limit')
            ax_power.set_xlim(left=min_date, right=max_date)
            ax_power.set_ylim([-100, self.project.MWAC * 1.3 * 1000])
            ax_power.legend()

            ax_cum.set_title('Cumulative Energy Meter Correction')
            y_cum_orig.plot(ax=ax_cum)
            y_cum_corrected.plot(ax=ax_cum)
            y_cum_inv.plot(ax=ax_cum, linestyle='-.')
            ax_cum.set_xlim(left=min_date, right=max_date)
            ax_cum.legend()

            # We'll turn the x-axis labels back on for the top plot because pyplot disables those by default when you share an axis
            ax_power.xaxis.set_tick_params(labelbottom=True, which='both')


        elif plot_name.replace(' ', '_').lower() == 'poas':
            # POA sensors
            y_poa = self.project.df.loc[:, self.project.pos_POA]
            y_poa_avg = self.project.df.loc[:, 'POA_avg']
            y_poa_avg.name = 'POA Avg'
            racking = self.project.df_proj_keys.get('Racking')
            
            fig, ax = plt.subplots(num='POAs - {}'.format(self.project.project_name))
            fig.suptitle(self.project.project_name)

            title = 'Irradiance - Racking: {}'.format(racking)
            if self.project.df_proj_keys['Fund'] == 'Soltage Landfill':
                title = 'Irradiance - Racking: {}\n***NOTE: POAs might be off tilt from each other due to site geography. The average may still be acceptable.***'.format(racking)
            ax.set_title(title)
            y_poa.plot(ax=ax)
            y_poa_avg.plot(ax=ax, marker='o', linestyle='None')
            ax.set_xlim(left=min_date, right=max_date)
            ax.legend()
            

        elif plot_name.replace(' ', '_').lower() == 'poa_corr':
            # POA Correlations
            if len(self.project.pos_POA) > 1:
                if poa_onboarding:
                    # Plot all months
                    y = self.project.df.loc[:,self.project.pos_POA]
                else:
                    # Plot only selected month
                    y = self.project.df.loc[self.project.df.index.month == mth, self.project.pos_POA]
                
                y.set_index(y.columns[0], drop=False, inplace=True)

                fig, ax = plt.subplots(num='POA Correlations - {}'.format(self.project.project_name))
                fig.suptitle(self.project.project_name)

                title='POA Correlation Check'
                if self.project.df_proj_keys['Fund'] == 'Soltage Landfill':
                    title='POA Correlation Check\n***NOTE: POA correlation may show hysteresis due to site geography***'
                ax.set_title(title)
                y.plot(ax=ax, marker='o', linestyle='None')
                ax.set_xlim(-10,1300)
                ax.set_ylim(-10,1300)
                ax.legend()  
            else:
                print('Only one POA! No plot for correlation')
                    
        
        elif plot_name.replace(' ', '_').lower() == 'inv':
            # Inverters
            y = self.project.df.loc[:, self.project.pos_Inv]

            fig, ax = plt.subplots(num='Inverters - {}'.format(self.project.project_name))
            fig.suptitle(self.project.project_name)

            ax.set_title('Inverter KW')
            y.plot(ax=ax)
            ax.set_xlim(left=min_date, right=max_date)
            ax.legend()
            
            # TODO: is this for determining inverter outages?
            def list_pairs(lis):
                #find pairs that are at least 2 hours in duration
                beg = []
                end = []
                            
                start_time = 0
                
                while start_time < len(lis):
                    end_time = start_time+1
                    while end_time < len(lis) and lis[end_time] - lis[end_time-1] == Timedelta('1h'):
                        end_time = end_time+1
                    # end_time overshoots by one hour, so adjust to make sure it's longer than 1 hr
                    if (end_time-1) - start_time >= 1:
                        beg.append(lis[start_time])
                        end.append(lis[end_time-1])
                    start_time = end_time
                return beg, end
                
            beg, end = list_pairs(list(self.project.df.loc[self.project.df['Meter_&_ava'] > self.project.df['Meter_Corrected_2'], :].index) )

            for beg,end in zip(beg,end):
                ax.axvspan(beg, end, facecolor='#2ca02c', alpha=0.5)


        elif plot_name.replace(' ', '_').lower() == 'pr':
            # Hourly PR
            freq = 'h'
            top = self.project.df.loc[:, 'Gen_NO_Clipping'].resample(freq).sum()
            bottom = self.project.df.loc[:, 'DC_corrected_PR'].resample(freq).sum()
            y = top.div(bottom)
            y_avg = y.dropna().rolling(48).mean()

            fig, ax = plt.subplots(num='PR - {}'.format(self.project.project_name))
            fig.suptitle(self.project.project_name)

            ax.set_title('Hourly PR')
            y.plot(ax=ax, marker='o', linestyle='None', label='Hourly PR')
            try:
                y_avg.plot(ax=ax, label='48 Hour Rolling Avg')
            except Exception as e:
                print('Skipped adding PR line for {}'.format(self.project.project_name))
                logger.warn('{} error plotting PR rolling avg for {}'.format(e, self.project.project_name))
            ax.set_xlim(left=min_date, right=max_date)
            ax.legend()


        elif plot_name.replace(' ', '_').lower() == 'losses':
            # Losses
            y_losses = self.project.losses

            # If single inverter site, remove losses where meter_corrected_2 > 0
            if len(self.project.pos_Inv) == 1:
                y_losses.loc[(y_losses['Meter_Corrected_2'] > 0), 'Inv_losses'] = 0
            
            # Set negative losses to zero
            y_losses.clip(lower=0, inplace=True)

            fig, ax = plt.subplots(num = 'Losses - {}'.format(self.project.project_name))
            fig.suptitle(self.project.project_name)

            ax.set_title('Losses by Type')
            y_losses.plot.area(ax=ax, linewidth=0)
            ax.set_xlim(left=min_date, right=max_date)

            # Assign column labels to lines because Pandas `plot.area()` doesn't do that for you automagically like `plot()` does
            for (ln, col) in zip(ax.lines, y_losses.columns):
                ln.set_label(col)


        elif plot_name.replace(' ', '_').lower() == 'temps':
            # Temperatures
            y_tcell = self.project.df['Tcell']
            y = self.project.df[['Tamb_avg', 'Tcell_AMB', 'Tcell_MOD']]
            
            # Add Fahrenheit conversion
            y_tcell_fahr = y_tcell*1.8+32
            y_fahr = y*1.8+32

            fig, ax = plt.subplots(num='Temperatures - {}'.format(self.project.project_name))
            ax_cels = ax
            ax_fahr = ax_cels.twinx()
            fig.suptitle(self.project.project_name)

            project_state = self.project.df_proj_keys['State']
            ax_cels.set_title(f'Temperatures - {project_state}')
            y_tcell.plot(ax=ax_cels, marker='o', color='r')
            y.plot(ax=ax_cels)
            y_tcell_fahr.plot(ax=ax_fahr, style='None', grid=False)
            y_fahr.plot(ax=ax_fahr, style='None', grid=False)
            ax_cels.set_ylabel('Temperature (C)')
            ax_fahr.set_ylabel('Temperature (F)')
            ax_cels.set_xlim(left=min_date, right=max_date)

            ax_cels.legend()
            ax_fahr.legend().set_visible(False)


        elif plot_name.replace(' ', '_').lower() == 'weather':
            # Weather Sensors
            y_poa = self.project.df['POA_avg']
            y_temp = self.project.df['Tamb_avg']
            y_wind = self.project.df['Wind_speed']

            fig, axs = plt.subplots(3, num='Weather Sensors - {}'.format(self.project.project_name), sharex=True)
            fig.suptitle(self.project.project_name)
            ax_poa = axs[0]
            ax_temp = axs[1]
            ax_wind = axs[2]

            ax_poa.set_title('Irradiance')
            y_poa.plot(ax=ax_poa, label='POA Avg')
            ax_temp.set_title('Ambient Temperature')
            y_temp.plot(ax=ax_temp, label='Tamb Avg')
            ax_wind.set_title('Wind Speed')
            y_wind.plot(ax=ax_wind, label='Wind Speed')
            for ax in axs:
                ax.set_xlim(left=min_date, right=max_date)
                ax.legend()


        elif plot_name.replace(' ', '_').lower() == 'ghi':
            #GHI plot
            if len(self.project.pos_GHI) > 0:
                y_ghi = self.project.df.loc[:, self.project.pos_GHI]
                y_ghi_avg = self.project.df.loc[:, 'GHI_avg']
                y_poa = self.project.df.loc[:, self.project.pos_POA]
                y_poa_avg = self.project.df.loc[:, 'POA_avg']
                
                try:
                    fig, ax = plt.subplots(num = 'GHI - {}'.format(self.project.project_name))
                    fig.suptitle(self.project.project_name)
                
                    ax.set_title('GHI Sensors')
                    y_ghi.plot(ax=ax)
                    y_ghi_avg.plot(ax=ax, style='o', label='GHI Avg')
                    ax.set_xlim(left=min_date, right=max_date)
                    ax.legend()

                except:
                    print("Couldn't make GHI_avg plot")
                    fig, ax = 'GHI plot error', 'GHI plot error'
            else:
                print("No GHI sensors to build the GHI plots")
                fig, ax = 'No GHI to plot', 'No GHI to plot'
                

        elif plot_name.replace(' ', '_').lower() == 'irrad':
            #POA & GHI Plot
            # Get GHI sensors if present
            if len(self.project.pos_GHI) > 0:
                y_ghi = self.project.df.loc[:, self.project.pos_GHI]
                y_ghi_avg = self.project.df.loc[:, 'GHI_avg']

            # Get POAs
            y_poa = self.project.df.loc[:, self.project.pos_POA]
            y_poa_avg = self.project.df.loc[:, 'POA_avg']

            try:
                fig, ax = plt.subplots(num = 'POA & GHI - {}'.format(self.project.project_name))
                fig.suptitle(self.project.project_name)
                
                ax.set_title('Irradiance Sensors')
                y_ghi.plot(ax=ax)
                y_ghi_avg.plot(ax=ax, label='GHI Avg', style='-.')
                y_poa.plot(ax=ax)
                y_poa_avg.plot(ax=ax, label='POA Avg', style=':')                               
                ax.set_xlim(left=min_date, right=max_date)
                ax.legend()
                
            except Exception as e:
                print("Couldn't make POA vs GHI plot. Exception: {}".format(e))
                fig, ax = 'POA vs GHI plot error', 'POA vs GHI plot error'
            

        elif plot_name.replace(' ', '_').lower() == 'tz':
            #Timezone plot and night check
            x = self.project.df_filt.index.hour
            y_meter = self.project.df_filt['Meter_Corrected_2']
            y_poa = self.project.df_filt['POA_avg']*4
            scale = self.project.df_filt.index.month
            interp_hours_list = list(set(self.project.df_filt.loc[self.project.df_filt['interp_check'] == 1, 'Hour Index Copy'].tolist()))

            fig, ax = plt.subplots(num='Timezone Check - {}'.format(self.project.project_name))
            fig.suptitle(self.project.project_name)

            ax.set_title('Timezone Check')
            # We'll store the scatter plot in a variable so we can reference it with the colorbar
            sp = ax.scatter(x, y_meter, c=scale, cmap ='jet')
            sp = ax.scatter(x, y_poa, c=scale, cmap ='jet')
            cb = plt.colorbar(sp)
            cb.set_label('Month')
            ax.set_xlim(0,24)

            for interp_hour in interp_hours_list:
                ax.axvspan(interp_hour - 0.25, interp_hour + 0.25, facecolor='#2ca02c', alpha=0.5)
            

        elif plot_name.replace(' ', '_').lower() == 'mtr_dif':
            # Meter Corrected Dif
            try:
                original_meter_cum = self.project.df_Meter_ORIGINAL.drop(self.project.pos_Meter_ORIGINAL,1).sum(axis=1)
                corrected_meter_cum = self.project.df['Meter_cum_corrected_2']
                y = original_meter_cum.subtract(corrected_meter_cum)
                min_y = y[(self.project.df_Meter_ORIGINAL.drop(self.project.pos_Meter_ORIGINAL,1) != 0).all(axis=1)].min()
                max_y = y[(self.project.df_Meter_ORIGINAL.drop(self.project.pos_Meter_ORIGINAL,1) != 0).all(axis=1)].max()
                
                fig, ax = plt.subplots(num='Meter Correction Dif - {}'.format(self.project.project_name))
                fig.suptitle(self.project.project_name)
                
                ax.set_title('Meter Correction Dif')
                y.plot(ax=ax)
                ax.set_xlim(left=min_date, right=max_date)
                ax.set_ylim(min_y, max_y)
            except:
                print("Couldn't build the meter corrected difference plot")
                fig, ax = 'Meter corrected dif error', 'Meter corrected dif error'
                    
            
        elif plot_name.replace(' ', '_').lower() == '8760':
            # 8760 vs Measured Power
            y_8760 = self.project.df_Pvsyst['Year 0 Actual Production (kWh)']
            y_meter_corrected = self.project.df['Meter_Corrected_2']


            fig, ax = plt.subplots(num='Measured/8760 Generation Comparison - {}'.format(self.project.project_name))
            fig.suptitle(self.project.project_name)

            ax.set_title('Measured/8760 Generation Comparison')
            y_8760.plot(ax=ax, label='8760', c='blue')
            y_meter_corrected.plot(ax=ax, label='Meter Corrected', c='red')
            ax.legend()
            

        elif plot_name.replace(' ', '_').lower() == 'xplot_temp':
            # Power vs POA by Temperature
            x = self.project.df.loc[:, 'POA_avg']
            y = self.project.df.loc[:, 'Meter_Corrected_2']
            x_max = 1300
            y_max = self.project.df['Meter_Corrected_2'].max()*1.05
            scale = self.project.df.loc[:, 'Tamb_avg']

            fig, ax = plt.subplots(num='YTD Power vs POA, colored by ambient temp - {}'.format(self.project.project_name))
            fig.suptitle(self.project.project_name)

            ax.set_title('YTD Power vs POA, colored by ambient temp')
            # We'll store the scatter plot in a variable so we can reference it with the colorbar
            sp = ax.scatter(x, y, c=scale, cmap='jet')    
            cb = plt.colorbar(sp)
            cb.set_label('Tamb Avg')
            ax.set_xlim(0, x_max)
            ax.set_ylim(0, y_max)
            ax.set_ylabel('Production [KWh]')
            ax.set_xlabel('Irradiance [W/m2]')
        

        elif plot_name.replace(' ', '_').lower() == 'native':
            poa_cols = [col for col in self.project.pos_POA if any([col in nat for nat in self.project.pos_Native])]
            ghi_cols = [col for col in self.project.pos_GHI if any([col in nat for nat in self.project.pos_Native])]
            tamb_cols = [col for col in self.project.pos_Tamb if any([col in nat for nat in self.project.pos_Native])]
            tmod_cols = [col for col in self.project.pos_Tmod if any([col in nat for nat in self.project.pos_Native])]
            wind_cols = [col for col in self.project.pos_Wind if any([col in nat for nat in self.project.pos_Native])]
            poa = self.project.df[poa_cols]
            ghi = self.project.df[ghi_cols]
            tamb = self.project.df[tamb_cols]
            tmod = self.project.df[tmod_cols]
            wind = self.project.df[wind_cols]

            fig, axs = plt.subplots(5, sharex=True, num='Native Weather - {}'.format(self.project.project_name))
            fig.suptitle(self.project.project_name)

            draw_multiple_axes([poa, ghi, tamb, tmod, wind], axs, min_date, max_date)


        elif plot_name.replace(' ', '_').lower() == 'meters':
            fig_list = []
            for i in range(len(self.project.pos_Meter)):
                y_meter_orig = self.project.df_Meter_ORIGINAL.iloc[:,i]
                y_meter_corr = self.project.df[self.project.pos_Meter[i]]
                y_cum_orig = self.project.df_Meter_ORIGINAL.iloc[:,[i+len(self.project.pos_Meter)]]
                y_cum_corr = self.project.df[[self.project.pos_Meter[i]]].cumsum()
                
                # Add in a vertical offset if the original & corrected cum meters don't match up
                condition = y_cum_orig.loc[(y_cum_orig[y_cum_orig.columns[0]] > 0), :].index
                offset = np.mean(y_cum_orig.loc[condition, :].values - y_cum_corr.loc[condition, :].values)
                y_cum_corr = y_cum_corr.add(offset)

                fig, axs = plt.subplots(2, num='Meter {} - {}'.format(i+1, self.project.project_name), sharex=True)
                fig.suptitle('{}'.format(self.project.project_name))
                ax_meter = axs[0]
                ax_cum = axs[1]

                ax_meter.set_title('Meter {}'.format(i+1))
                y_meter_orig.plot(ax=ax_meter)
                y_meter_corr.plot(ax=ax_meter)
                ax_meter.set_xlim(left=min_date, right=max_date)
                ax_meter.legend(['Original', 'Corrected'])

                y_cum_orig.plot(ax=ax_cum)
                y_cum_corr.plot(ax=ax_cum)
                ax_cum.set_xlim(left=min_date, right=max_date)
                ax_cum.legend(['Original', 'Corrected'])

                fig_list.append(fig)


        elif plot_name.replace(' ', '_').lower() == 'snow':
            # Snow Plots
            y_snow_data = self.project.snow_data['snow']
            y_snow_coverage = self.project.snow_coverage

            fig, ax = plt.subplots(num='Snow Data - {}'.format(self.project.project_name))
            fig.suptitle(self.project.project_name)

            ax.set_title('Snow Data')
            y_snow_data.plot(ax=ax, label='Snowfall', c='blue')
            y_snow_coverage.plot(ax=ax, label='Coverage', c='red')
            ax.legend()


        elif plot_name.replace(' ', '_').lower() == 'battery':
            if self.project.Battery_AC_site:
                # Battery Discharge
                poi_cols = [s for s in self.project.df_POI_ORIGINAL.columns if 'POI_kw_' in s]
                y_poi_measured = self.project.df_POI_ORIGINAL.loc[:, poi_cols].sum(axis=1)
                y_poi_modeled = self.project.df.loc[:, 'POI_modeled']
                y_discharge = self.project.df.loc[self.project.df.Rates == self.project.df.Rates.max(), poi_cols].sum(axis=1)
                y_comparison = self.project.df.loc[:, 'POI_modeled'] - self.project.df['POI_Corrected_2']
                y_comparison.loc[self.project.df.Rates == self.project.df.Rates.min()] = 0

                fig, axs = plt.subplots(2, num='Battery Discharge - {}'.format(self.project.project_name), sharex=True)
                fig.suptitle(self.project.project_name)
                ax_discharge = axs[0]
                ax_comparison = axs[1]

                ax_discharge.set_title('Measured/Expected Battery Discharge Comparison')
                ax_discharge.plot(y_poi_measured, label='POI Measured')
                ax_discharge.plot(y_poi_modeled, label='POI Modeled')
                ax_discharge.plot(y_discharge, label='Discharge', c = 'k', ls='', marker = 'x', ms = 8)
                ax.set_xlim(left=min_date, right=max_date)
                ax_discharge.legend()

                ax_comparison.set_title('Expected/Measured Difference')
                ax_comparison.plot(y_comparison)
                            
                # POI Energy Correction
                poi_cols = [s for s in self.project.df_POI_ORIGINAL.columns if 'POI_kw_' in s]
                poi_cum_cols = [s for s in self.project.df_POI_ORIGINAL.columns if 'POI_kwhnet_' in s]
                y_poi_original = self.project.df_POI_ORIGINAL[poi_cols].sum(axis=1)
                y_poi_corrected = self.project.df.loc[:, 'POI_Corrected_2']
                y_poi_cum_original = self.project.df_POI_ORIGINAL[poi_cum_cols].sum(axis=1)
                # These next three lines adjust the corrected cum meter to match the y-intercept of the original cum meter
                poi_cum_corrected = self.project.df.loc[:, 'POI_Corrected_2'].cumsum()
                poi_cum_meter_offset = self.project.df_POI_ORIGINAL[poi_cum_cols].sum(axis=1).subtract(poi_cum_corrected).median()
                y_poi_cum_corrected = self.project.df.loc[:, 'POI_cum_corrected_2'].add(poi_cum_meter_offset)

                fig, axs = plt.subplots(2, num='POI Energy Correction - {}'.format(self.project.project_name), sharex=True)
                fig.suptitle(self.project.project_name)
                ax_correction = axs[0]
                ax_cum_correction = axs[1]

                ax_correction.set_title('POI Energy Correction')
                ax_correction.plot(y_poi_original, label='Original')  
                ax_correction.plot(y_poi_corrected, label='Corrected')
                ax_correction.axhline(y = self.project.MWAC * 1000, color = 'r', linestyle = '--', label='MWAC')
                ax_correction.set_xlim(left=min_date, right=max_date)
                ax_correction.set_ylim = [-100, self.project.MWAC*1.3*1000]
                ax_correction.legend()

                ax_cum_correction.set_title('POI Energy Correction')
                ax_cum_correction.plot(y_poi_cum_original, label='Original')
                ax_cum_correction.plot(y_poi_cum_corrected, label='Corrected')
                ax_cum_correction.legend()
            

        elif plot_name.replace(' ', '_').lower() == 'tracker':
            if self.project.Tracker_site:
                y = self.project.df[self.project.pos_Tracker]

                fig, ax = plt.subplots(num='Tracker Angles - {}'.format(self.project.project_name))
                fig.suptitle(self.project.project_name)

                ax.set_title('Tracker Angles')
                y.plot(ax=ax)
                ax.set_xlim(left=min_date, right=max_date)
                ax.set_ylim(-60,60)
        
        else:
            print('`{}` is not a valid plot name. See documentation for valid names & try again'.format(plot_name))
            fig, ax = 'Invalid plot_name', 'Invalid plot_name'


        # If we have multiple subplots we'll overwrite `ax` with the list of subplots stored in `axs`
        if not ax:
            try:
                ax = axs
            except:
                print('Error creating {} plot.'.format(plot_name))
                fig, ax = 'Error creating {} plot'.format(plot_name), 'Error creating {} plot'.format(plot_name)
        

        format_kwargs = {'screen': screen,
                         'fullscreen': fullscreen,
                         'tight_layout': tight_layout,
                         'default_tool': default_tool}

        if fig_list:
            for fig in fig_list:
                self.format_fig(fig, **format_kwargs)
        else:
            self.format_fig(fig, **format_kwargs)

        return fig, ax


    def format_fig(self, fig, **kwargs):
        screen = kwargs.get('screen', None)
        fullscreen = kwargs.get('fullscreen', None)
        tight_layout = kwargs.get('tight_layout', None)
        default_tool = kwargs.get('default_tool', None)

        if isinstance(fig, Figure):
            try:
                # Move plots to the selected screen
                if screen:
                    if isinstance(screen, Number):
                        try:
                            screen = screen-1
                            screens = QGuiApplication.screens()
                            top_left = screens[screen].availableGeometry().topLeft()
                            fig.canvas.manager.window.move(top_left)
                        except IndexError:
                            warnings.warn('`screen` index out of range. Please supply a number less than or equal to the number of screens you have.')
                    else:
                        warnings.warn('TypeError - please supply a number for `screen` to select your desired plot screen')

                # Set plots to fullscreen if desired
                if fullscreen:
                    fig.canvas.manager.window.showMaximized()
                
                # Remove unnecessary whitespace around plots
                if tight_layout:
                    fig.set_tight_layout(True)

                # Set the default tool for zooming/panning
                if default_tool == 'zoom':
                    fig.canvas.manager.toolbar.zoom()
                elif default_tool == 'pan':
                    fig.canvas.manager.toolbar.pan()
            except Exception as e:
                print(e)

        
    def close_plots(self, plots=None):
        """Method to close plots"""
        if not plots:
            plt.close('all')
        else:
            if isinstance(plots, str):
                plots = [plots]
            for plot_name in plots:
                self.close_plot(plot_name)

    
    def close_plot(self, plot_name):
        plot = self.plot_list[plot_name].fig
        plt.close(plot)
