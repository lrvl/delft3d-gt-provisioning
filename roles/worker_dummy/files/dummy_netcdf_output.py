import logging
import numpy as np
import os
import time

import configparser
import netCDF4

# Python script generated by netCDF kickstarter
# at 2016-04-12T07:31Z
# http://publicwiki.deltares.nl/display/OET/netCDF%20kickstarter

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# CREATE A NEW FILE
with netCDF4.Dataset(os.path.join('input', 'trim-a.nc'), mode='w') as nc:

    logger.info('Write netcdf')

    # ADD DIMENSIONS
    nc.createDimension('x', 10)
    nc.createDimension('y', 10)
    nc.createDimension('time', 0)

    # ADD VARIABLES
    nc.createVariable('x', 'float32', (u'x',))
    nc.variables['x'].long_name = 'x-coordinate'
    nc.variables['x'].standard_name = 'projection_x_coordinate'
    nc.variables['x'].units = 'm'
    nc.variables['x'].axis = 'X'
    nc.variables['x'].valid_min = 0
    nc.variables['x'].valid_max = 0
    nc.variables['x'].bounds = 'x_bounds'
    nc.variables['x'].grid_mapping = 'crs'
    nc.variables['x'].comment = ''

    nc.createVariable('y', 'float32', (u'y',))
    nc.variables['y'].long_name = 'y-coordinate'
    nc.variables['y'].standard_name = 'projection_y_coordinate'
    nc.variables['y'].units = 'm'
    nc.variables['y'].axis = 'Y'
    nc.variables['y'].valid_min = 0
    nc.variables['y'].valid_max = 0
    nc.variables['y'].bounds = 'y_bounds'
    nc.variables['y'].grid_mapping = 'crs'
    nc.variables['y'].comment = ''

    nc.createVariable('time', 'float64', (u'time',))
    nc.variables['time'].long_name = 'time'
    nc.variables['time'].standard_name = 'time'
    nc.variables['time'].units = 'seconds since 1970-01-01 00:00:00 0:00'
    nc.variables['time'].calendar = 'julian'
    nc.variables['time'].axis = 'T'
    nc.variables['time'].bounds = 'time_bounds'
    nc.variables['time'].ancillary_variables = ''
    nc.variables['time'].comment = ''

    nc.createVariable('random', 'float32', (u'time', u'y', u'x'))
    nc.variables['random'].long_name = 'random'
    nc.variables['random'].standard_name = 'random'
    nc.variables['random'].units = 'm'
    nc.variables['random'].scale_factor = 1.0
    nc.variables['random'].add_offset = 0.0
    nc.variables['random'].valid_min = 0
    nc.variables['random'].valid_max = 0
    nc.variables['random'].coordinates = 'time y x'
    nc.variables['random'].grid_mapping = 'crs'
    nc.variables['random'].source = ''
    nc.variables['random'].references = ''
    nc.variables['random'].cell_methods = ''
    nc.variables['random'].ancillary_variables = ''
    nc.variables['random'].comment = ''

    nc.createVariable('crs', 'int32', ())
    nc.variables['crs'].grid_mapping_name = 'oblique_stereographic'
    nc.variables['crs'].epsg_code = 'EPSG:28992'
    nc.variables['crs'].semi_major_axis = 6377397.155
    nc.variables['crs'].semi_minor_axis = 6356078.96282
    nc.variables['crs'].inverse_flattening = 299.1528128
    nc.variables['crs'].latitude_of_projection_origin = 52.0922178
    nc.variables['crs'].longitude_of_projection_origin = 5.23155
    nc.variables['crs'].scale_factor_at_projection_origin = 0.9999079
    nc.variables['crs'].false_easting = 155000.0
    nc.variables['crs'].false_northing = 463000.0
    nc.variables['crs'].proj4_params = '+proj=sterea +lat_0=52.15616055555555 +lon_0=5.38763888888889 +k=0.999908 +x_0=155000 +y_0=463000 +ellps=bessel +units=m +towgs84=565.4174,50.3319,465.5542,-0.398957388243134,0.343987817378283,-1.87740163998045,4.0725 +no_defs'

    # ADD GLOBAL ATTRIBUTES
    # see http://www.unidata.ucar.edu/software/thredds/current/netcdf-java/formats/DataDiscoveryAttConvention.html
    nc.Conventions = 'CF-1.6'
    nc.Metadata_Conventions = 'Unidata Dataset Discovery v1.0'
    nc.featureType = 'grid'
    nc.cdm_data_type = 'grid'
    nc.standard_name_vocabulary = 'CF-1.6'
    nc.title = 'Dummy delft3d data'
    nc.summary = 'dummy delft3d data for delft3dgt project'
    nc.geospatial_lat_min = 0
    nc.geospatial_lat_max = 0
    nc.geospatial_lat_units = 'degrees_north'
    nc.geospatial_lat_resolution = ''
    nc.geospatial_lon_min = 0
    nc.geospatial_lon_max = 0
    nc.geospatial_lon_units = 'degrees_east'
    nc.geospatial_lon_resolution = ''
    nc.geospatial_vertical_min = 0
    nc.geospatial_vertical_max = 0
    nc.geospatial_vertical_units = ''
    nc.geospatial_vertical_resolution = ''
    nc.geospatial_vertical_positive = ''
    nc.date_created = '2016-04-12T07:31Z'
    nc.date_modified = '2016-04-12T07:31Z'
    nc.date_issued = '2016-04-12T07:31Z'
    nc.metadata_link = '0'

    nc.sync()

    config = configparser.ConfigParser()
    config.read(os.path.join('input', 'input.ini'))
    n_steps = int(config.get('steps', 'values'))

    nc.variables['x'][:] = np.linspace(0, 9, 10)
    nc.variables['y'][:] = np.linspace(0, 9, 10)
    timeseries = np.linspace(0, n_steps-1, 10)

    for i in timeseries:
        nc.variables['random'][i, :, :] = np.random.random((10, 10))
        nc.variables['time'][i] = i
        nc.sync()
        time_left = timeseries[-1]*n_steps-i*n_steps
        percentage_done = (i*n_steps)/(timeseries[-1]*n_steps)*100
        steps_left = timeseries[-1]-i
        logger.info('Time to finish {0}, {1}% completed, time steps  left {2}'.format(time_left, percentage_done, steps_left))
        time.sleep(n_steps)
    logger.info('Finished')
