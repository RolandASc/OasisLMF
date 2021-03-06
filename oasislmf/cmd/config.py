from argparse import RawDescriptionHelpFormatter

from .base import OasisBaseCommand


class ConfigCmd(OasisBaseCommand):
    """
    The ``oasislmf`` tool can be configured using using a JSON configuration file. 
    By default this is stored in ``oasislmf.json`` but the path can be overridden using the ``--config`` flag.

    This configuration file should contain any or all of the following properties.
    The path-related keys should be string paths, given relative to the location of JSON file.
    Arguments can be overridden for a specific command using appropriate run time parameter.

    :source_exposures_file_path: File path to source exposure data, in CSV format.
    :source_exposures_validation_file_path: File path to schema for validating source exposure, in XSD format.
    :source_to_canonical_exposures_transformation_file_path: File path to transform to select and store a subset of the source exposure, in XSLT format.
    :canonical_exposures_profile_json_path: File path to profile that describes the structure of the stored data.
    :canonical_exposures_validation_file_path: File path to schema for validating stored exposure, in XSD format.
    :canonical_to_model_exposures_transformation_file_path: File path to transform to select a subset of the stored exposure for invoking the keys lookup logic, in XSD format.
    :lookup_package_path: Path to the Python package that contains the model keys lookup class.
    :keys_data_path: Path to directory containing data files required by the model keys lookup class.
    :model_version_file_path: Path to model version specification file (`ModelVersion.csv`), required to correctly instantiate the model keys lookup class.
    :model_exposures_file_path: File path to the inputs to the model keys lookup class in CSV format.
    :keys_file_path: Path for the file containing keys for locations with successful lookups.
    :keys_error_file_path: Path for the file containing keys for locations with failing or non-matching looups.
    :keys_format: Specifies the format of the keys files generated by the model keys lookup class. The default is `oasis` (Oasis CSV format), with `json` as alternative choice.
    :model_data_path: Path to directory containing the model data.
    :model_run_dir_path: Path to directory in which the canonical files, keys files, Oasis files and output files are generated, including the source files and analysis settings file, which are copied from their original locations.
    :analysis_settings_json_file_path: File path to the settings file that parameterizes the model run.
    :ktools_script_name: Specifies the ktools shell script that performs the model run, which is created and ran from the model_run_dir_path. Default is "run_ktools.sh".
    :ktools_num_processes: Specifies the number of concurrent processes used by the model run. Default is 2. 
    :no_execute: Specifies whether to perform the model run. Default is "False", which means the ktools script is executed.
    :model_package_path: Path to the directory to use as the model specific package (if required)


    As an example, this is the master script configuration file for PiWind

    ::

        {
            "source_exposures_file_path": "tests/data/SourceLocPiWind1K.csv",
            "source_exposures_validation_file_path": "flamingo/PiWind/Files/ValidationFiles/Generic_Windstorm_SourceLoc.xsd",
            "source_to_canonical_exposures_transformation_file_path": "flamingo/PiWind/Files/TransformationFiles/MappingMapToGeneric_Windstorm_CanLoc_A.xslt",
            "canonical_exposures_profile_json_path": "oasislmf-piwind-canonical-loc-profile.json",
            "canonical_exposures_validation_file_path": "flamingo/PiWind/Files/ValidationFiles/Generic_Windstorm_CanLoc_B.xsd",
            "canonical_to_model_exposures_transformation_file_path": "flamingo/PiWind/Files/TransformationFiles/MappingMapTopiwind_modelloc.xslt",
            "lookup_package_path": "src/keys_server",
            "keys_data_path": "keys_data/PiWind",
            "model_version_file_path": "keys_data/PiWind/ModelVersion.csv",
            "model_exposures_file_path": "/tmp/model_exposure_PiWind.csv",
            "keys_file_path": "/tmp/keys_PiWind.csv",
            "keys_error_file_path": "/tmp/keys_erros_PiWind.json",
            "model_data_path": "model_data/PiWind",
            "model_run_dir_path": "/tmp/run_PiWind",
            "analysis_settings_json_file_path": "analysis_settings.json"
        }

    It can also be obtained `here <https://github.com/OasisLMF/OasisPiWind/blob/master/oasislmf.json>`_.

   """
    formatter_class = RawDescriptionHelpFormatter
