import warnings
VERSION = '0.2.0'
warnings.filterwarnings(
    message='.*Conversion of the second.*',
    action='ignore',
    category=FutureWarning,
    module='h5py'
)
warnings.filterwarnings(
    message='.*(numpy.ufunc|numpy.dtype) size changed.*',
    action='ignore',
    category=RuntimeWarning
)
