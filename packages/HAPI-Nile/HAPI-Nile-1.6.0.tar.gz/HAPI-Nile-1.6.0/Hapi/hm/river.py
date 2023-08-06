"""River Module.

river module to read the river data and do hydraulic analysisf or each
segment
"""
import datetime as dt
import os
import zipfile
from bisect import bisect
from pathlib import Path
from typing import Any, Optional, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml
from loguru import logger
from matplotlib.figure import Figure
from pandas.core.frame import DataFrame
from pyramids.raster import Raster as raster
from scipy.stats import genextreme, gumbel_r
from serapeum_utils.utils import class_attr_initialize, class_method_parse
from statista import metrics as Pf
from statista.distributions import GEV, Gumbel  # , PlottingPosition

from Hapi.hapi_warnings import SilencePandasWarning
from Hapi.hm.saintvenant import SaintVenant
from Hapi.plot.visualizer import Visualize as V

SilencePandasWarning()

hours = list(range(1, 25))


class River:
    """River.

    River class reads all the data of the river, (cross sections,
    simulation results) and analyse the results and do visualisation
    """

    initial_args = dict(
        name={"type": str},
        version={"default": 3, "type": int},
        dto={"default": 60, "type": int},
        dx={"default": 500, "type": int},
        start={"default": "1950-1-1", "type": str},
        days={"default": 36890, "type": int},  # 100 years
        rrm_start={"default": None, "type": str},
        rrm_days={"default": 36890, "type": int},  # 100 years
        left_overtopping_suffix={"default": "_left.txt", "type": str},
        right_overtopping_suffix={"default": "_right.txt", "type": str},
        depth_prefix={"default": "DepthMax", "type": str},
        duration_prefix={"default": "Duration", "type": str},
        return_period_prefix={"default": "ReturnPeriod", "type": str},
        compressed={"default": True, "type": bool},
        fmt={"default": "%Y-%m-%d", "type": str},
        one_d_result_path={"default": "/results/1d", "type": str},
        two_d_result_path={"default": "/results/2d", "type": str},
    )

    river_attributes = dict(
        one_min_result_path=None,
        us_bc_path=None,
        first_day=None,
        referenceindex_results=None,
        wd=None,
        XSF=None,
        laterals_file=None,
        BCF=None,
        river_network_file=None,
        slope_file=None,
        NoSeg=None,
        CalibrationF=None,
        Coupling1D2DF=None,
        RunMode=None,
        Subid=None,
        Customized_BC_F=None,
        ResultsDetails=None,
        RRMTemporalResolution=None,
        HMTemporalResolution=None,
        HMStoreTimeStep=None,
        TS=None,
        SimStartIndex=None,
        SimEndIndex=None,
        SimStart=None,
        SimEnd=None,
        OneDTempR=None,
        D1=None,
        D2=None,
        cross_sections=None,
        xsno=None,
        xs_names=None,
        q_bc_1min=None,
        h_bc_1min=None,
        h=None,
        q=None,
        from_beginning=None,
        first_day_results=None,
        last_day=None,
        days_list=None,
        id=None,
        QBC=None,
        HBC=None,
        usbc=None,
        dsbc=None,
        results_1d=None,
        Q=None,
        H=None,
        slope=None,
        event_index=None,
        rivernetwork=None,
        SP=None,
        customized_runs_path=None,
        Segments=None,
        RP=None,
        rrm_path=None,
        reach_ids=None,
        customized_runs_config=None,
        parameters=None,
        results_config=None,
        rrm_paths=None,
        rrm_config=None,
        river_1d_paths=None,
        river_1d_config=None,
        config=None,
        results_paths=None,
        one_min_results_config=None,
        hourlt_results_config=None,
    )

    @class_method_parse(initial_args)
    @class_attr_initialize(river_attributes)
    def __init__(
        self,
        name: str,
        version: int = 3,
        start: str = "1950-1-1",
        end: Union[int, str] = None,
        *args,
        **kwargs,
    ):
        """River.

        to instantiate the river class you need to provide the following
        parameters

        Parameters
        ----------
        name : [str]
            name of the river.
        version : [integer], optional
            version of the model hydraulic model. The default is 3.
        start : [str], optional
            start date. The default is "1950-1-1".
        days : [integer], optional
            length of the simulation in days. The default is 36890.
        rrm_start : [str], optional
            the start date of the rainfall-runoff data. The default is
            "1950-1-1".
        rrm_days : [integer], optional
            the length of the data of the rainfall-runoff data in days.
            The default is 36890.
        dto : [integer]
            time step (sec) of the 1d routing model. default is 60 second.
        left_overtopping_suffix : [str], optional
            the prefix you used to name the overtopping form the left bank
            files.
            The default is "_left.txt".
        righ_tovertopping_suffix : TYPE, optional
            the prefix you used to name the overtopping form the right bank
            files. The default is "_right.txt".
        depth_prefix : [str], optional
            the prefix you used to name the Max depth raster result maps.
            The default is "DepthMax".
        duration_prefix : [str], optional
            the prefix you used to name the inundation duration raster result
            maps. The default is "Duration".
        return_period_prefix : [str], optional
            the prefix you used to name the Return Period raster result maps.
            The default is "ReturnPeriod".
        compressed : [bool], optional
            True if the result raster/ascii files are compressed. The default
            is True.
        one_d_result_path : [str], optional
            path to the folder where the 1D river routing results exist.
            The default is ''.
        two_d_result_path : [str], optional
            path to the folder where the 1D river routing results exist.
            The default is ''.
        fmt: [string]
            format of the date. fmt="%Y-%m-%d %H:%M:%S"

        Returns
        -------
        None.
        """
        # positional arguments
        assert isinstance(start, str), "start argument has to be string"
        assert isinstance(version, int), "version argument has to be integer number"

        self.name = name
        self.version = version
        self.start = dt.datetime.strptime(start, self.fmt)

        if end is None:
            self.end = self.start + dt.timedelta(days=self.days)
        else:
            self.end = dt.datetime.strptime(end, self.fmt)
            self.days = (self.end - self.start).days

        self.dt = self.dto
        if self.dt < 60:
            self.freq = str(self.dt) + "S"
        else:
            self.freq = str(int(self.dt / 60)) + "Min"
        # ----------------------------------------------------
        ref_ind = pd.date_range(self.start, self.end, freq="D")
        # the last day is not in the results day Ref_ind[-1]
        # write the number of days + 1 as python does not include the last
        # number in the range
        # 19723 days so write 19724
        if self.days == 1:
            self.days = 2
            self.reference_index = pd.DataFrame(index=list(range(1, self.days + 1)))
            self.reference_index["date"] = ref_ind
        else:
            self.reference_index = pd.DataFrame(index=list(range(1, self.days + 1)))
            self.reference_index["date"] = ref_ind[:-1]

        if self.rrm_start is None:
            self.rrm_start = self.start
        else:
            self.rrm_start = dt.datetime.strptime(self.rrm_start, self.fmt)

        self.rrm_end = self.rrm_start + dt.timedelta(days=self.rrm_days)
        ref_ind = pd.date_range(self.rrm_start, self.rrm_end, freq="D")
        self.rrm_reference_index = pd.DataFrame(index=list(range(1, self.rrm_days + 1)))
        self.rrm_reference_index["date"] = ref_ind[:-1]
        self.no_time_steps = len(self.rrm_reference_index)

        self.indsub = pd.date_range(self.start, self.end, freq=self.freq)

    def indexToDate(self, index: int):
        """IndexToDate.

        IndexToDate takes an integer number and returns the date coresponding
        to this date based on a time series starting from the "start" attribute
        of  River object and for a length of the value of the "days" attribute

        Parameters
        ----------
        index : [Integer]
            Integer number ranges from 1 and max value of the value of the
            attribute "days" of the River object.

        Returns
        -------
        [Date time ]
            date object.
        """
        # convert the index into date
        return self.reference_index.loc[index, "date"]

    def dateToIndex(self, date: Union[dt.datetime, str], fmt: str = "%Y-%m-%d"):
        """DateToIndex.

        DateToIndex takes a date and returns a the order of the days in the
        time series. The time series starts from the value of the "start" for
        a length of "days" value

        Parameters
        ----------
        date : [string/date time object]
            string in the format of "%Y-%m-%d" or a date time object.
        fmt: [string]
            format of the date. fmt="%Y-%m-%d %H:%M:%S"
        Returns
        -------
        [Integer]
            the order oif the date in the time series.
        """
        if isinstance(date, str):
            date = dt.datetime.strptime(date, fmt)
        try:
            return np.where(self.reference_index["date"] == date)[0][0] + 1
        except:
            raise ValueError(
                f"The input date {date} is out of the range"
                f"Simulation is between {self.reference_index.loc[1, 'date']} and "
                f"{self.reference_index.loc[len(self.reference_index), 'date']}"
            )

    def indexToDateRRM(self, index: int):
        """IndexToDateRRM.

        IndexToDate takes an integer number and returns the date coresponding
        to this date based on a time series starting from the "start" attribute
        of  River object and for a length of the value of the "days" attribute

        Parameters
        ----------
        index : [Integer]
            Integer number ranges from 1 and max value of the value of the attribute
            "days" of the River object.

        Returns
        -------
        [Date time ]
            date object.
        """
        # convert the index into date
        return self.reference_index.loc[index, "date"]

    def dateToIndexRRM(self, date: Union[str, dt.datetime], fmt: str = "%Y-%m-%d"):
        """DateToIndexRRM.

        DateToIndex takes a date and returns a the order of the days in the
        time series. The time series starts from the value of the "start" for
        a length of "days" value

        Parameters
        ----------
        date : [string/date time object]
            string in the format of "%Y-%m-%d" or a date time object.
        fmt: [string]
            format of the date. fmt="%Y-%m-%d %H:%M:%S"
        Returns
        -------
        [Integer]
            the order oif the date in the time series.
        """
        if isinstance(date, str):
            date = dt.datetime.strptime(date, fmt)
        return np.where(self.reference_index["date"] == date)[0][0] + 1

    @staticmethod
    def round(number, roundto):
        """Round fload number."""
        return round(number / roundto) * roundto

    def readConfig(self, path):
        """Read the hydraulic model configuration file.

        Parameters
        ----------
        path: [str]
            path to the configuration file (yaml files)
        """
        if not os.path.exists(path):
            raise FileNotFoundError(
                f"The Configuration file You have entered: {path} does not exist"
            )
        with open(path, "r") as stream:
            config = yaml.safe_load(stream)
        # project directory
        self.wd = config.get("project directory")
        self.config = config
        # river
        river_files = config.get("river description")
        self.river_1d_config = river_files
        river_rdir = Path(river_files.get("root directory"))
        self.river_1d_paths = dict(
            river_rdir=river_rdir,
            xs_file=river_rdir.joinpath(river_files.get("cross sections")),
            river_network=river_rdir.joinpath(river_files.get("river network")),
            river_slope=river_rdir.joinpath(river_files.get("slope")),
            coupling_2d=river_rdir.joinpath(river_files.get("1D-2D coupling")),
            calibration_table=river_rdir.joinpath(river_files.get("results locations")),
        )
        # rainfall runoff model
        rrm_files = config.get("rainfall-runoff files")
        self.rrm_config = rrm_files
        rrm_rdir = Path(rrm_files.get("root directory"))
        rrm_results = rrm_files.get("river routing blocked results")
        self.rrm_paths = dict(
            rrm_rdir=rrm_rdir,
            laterals_table_path=rrm_rdir.joinpath(rrm_files.get("laterals")),
            boundary_condition_table=rrm_rdir.joinpath(
                rrm_files.get("boundary condition")
            ),
            laterals_dir=rrm_rdir,
            boundary_condition_path=rrm_rdir,
            rrm_location_1=Path(rrm_results.get("location-1")),  # rrm_path
            rrm_location_2=Path(rrm_results.get("location-2")),
        )
        # result files
        results_files = config.get("Results 1D")
        self.results_config = results_files
        results_rdir = Path(results_files.get("root directory"))
        hourlt_results = results_files.get("hourly")
        self.hourlt_results_config = hourlt_results
        one_min_results = results_files.get("one min")
        self.one_min_results_config = one_min_results
        # 2D
        results_files = config.get("Results 2D")
        self.results_paths = dict(
            results_rdir=results_rdir,
            one_d_result_path=results_rdir.joinpath(hourlt_results.get("folder")),
            one_min_result_path=results_rdir,
            us_bc_path=results_rdir.joinpath(one_min_results.get("usbc").get("folder")),
            two_d_result_path=Path(results_files.get("root directory")),
        )
        # parameters
        parameters = config.get("simulation parameters")
        self.parameters = parameters
        customized_runs = parameters.get("customized simulation")
        self.customized_runs_config = customized_runs
        customized_runs_path = Path(customized_runs.get("previous run results"))
        self.customized_runs_path = customized_runs_path

    def read1DConfigFile(self, path: str):
        """Read1DConfigFile.

        Read the configuration file

        Parameters
        ----------
        path : TYPE
            DESCRIPTION.

        Returns
        -------
        None.
        """
        file = open(path)
        wholefile = file.readlines()
        file.close()
        # project path
        self.wd = wholefile[1][:-1]
        # cross sections file
        self.XSF = wholefile[4][:-1]
        self.readXS(self.wd + "/inputs/1d/topo/" + self.XSF)
        # Laterals file, BC file
        self.laterals_file, self.BCF = wholefile[6][:-1].split(" ")
        # RiverNetwork file
        self.river_network_file = wholefile[8][:-1]
        self.readRiverNetwork(self.wd + "/inputs/1d/topo/" + self.river_network_file)
        # Slope File
        self.slope_file = wholefile[10][:-1]
        self.readSlope(self.wd + "/inputs/1d/topo/" + self.slope_file)
        self.NoSeg = len(self.slope)
        # Calibration file
        self.calibration_file = wholefile[12][:-1]
        # 1D-2D Coupling file
        self.Coupling1D2DF = wholefile[14][:-1]
        # Run mode
        RunMode, Subid = wholefile[16][:-1].split("#")[0].strip().split(" ")
        self.RunMode = int(RunMode)
        # Segment id
        self.Subid = int(Subid)
        # Customized Run file
        self.Customized_BC_F = wholefile[18][:-1]
        self.customized_runs_path = wholefile[19][:-1]

        # Results
        DeleteOld = wholefile[22][:-1]
        DeleteOld = int(DeleteOld)
        SaveHourly, SaveOverToppingTot, SaveOverToppingDetailed = wholefile[24][
            :-1
        ].split(" ")
        SaveHourly = int(SaveHourly)
        SaveOverToppingTot = int(SaveOverToppingTot)
        SaveOverToppingDetailed = int(SaveOverToppingDetailed)
        SaveQ, SaveWL, SaveUSBC = wholefile[26].split("#")[0][:-1].split(" ")
        SaveQ = int(SaveQ)
        SaveWL = int(SaveWL)
        SaveUSBC = int(SaveUSBC)

        self.ResultsDetails = dict(
            DeleteOld=DeleteOld,
            SaveHourly=SaveHourly,
            SaveOverToppingTot=SaveOverToppingTot,
            SaveOverToppingDetailed=SaveOverToppingDetailed,
            SaveQ=SaveQ,
            SaveWL=SaveWL,
            SaveUSBC=SaveUSBC,
        )

        # Temporal Resolution
        self.RRMTemporalResolution = wholefile[31].split("#")[0][:-1]
        self.HMTemporalResolution = int(wholefile[32].split("#")[0][:-1])
        self.HMStoreTimeStep = int(wholefile[33].split("#")[0][:-1])

        if self.RRMTemporalResolution == "Daily":
            # number of time steps for the 1D model
            self.TS = 24 * self.HMTemporalResolution

        Start, End = wholefile[35][:-1].split(" ")
        self.SimStartIndex = int(Start)
        self.SimEndIndex = int(End)
        self.SimStart = self.indexToDate(self.SimStartIndex)
        self.SimEnd = self.indexToDate(self.SimEndIndex)
        self.OneDTempR = 60  # in seconds

        # 1D thresholds
        MinQ, MinDepth = wholefile[37][:-1].split(" ")
        MinQ = float(MinQ)
        MinDepth = float(MinDepth)

        # 1D or 2D
        ModelMode, OvertoppingOnly = wholefile[39][:-1].split(" ")
        ModelMode = int(ModelMode)
        OvertoppingOnly = int(OvertoppingOnly)

        self.D1 = dict(
            MinQ=MinQ,
            MinDepth=MinDepth,
            ModelMode=ModelMode,
            OvertoppingOnly=OvertoppingOnly,
        )

        DischargeThreshold = int(wholefile[41][:-1])

        SimulationMode = int(wholefile[43][:-1])
        ResultsFormat = int(wholefile[45][:-1])
        CalcInundationDuration = int(wholefile[47][:-1])
        CalcReturnPerion = int(wholefile[49][:-1])
        self.D2 = dict(
            DischargeThreshold=DischargeThreshold,
            SimulationMode=SimulationMode,
            ResultsFormat=ResultsFormat,
            CalcInundationDuration=CalcInundationDuration,
            CalcReturnPerion=CalcReturnPerion,
        )

    def readXS(self, path: str):
        """readXS.

            Read crossSections file

        readXS method reads the cross section data of the river and assign it
        to an attribute "Crosssections" of type dataframe

        Parameters
        ----------
        path: [str]
            path to the cross-section file

        Returns
        -------
        cross_sections : [dataframe]
            a dataframe attribute will be created
        """
        if self.version == 3:
            self.cross_sections = pd.read_csv(path, delimiter=",")
            self.xsno = len(self.cross_sections)
            self.reach_ids = list(set(self.cross_sections["id"].tolist()))
        else:
            self.cross_sections = pd.read_csv(path, delimiter=",")
            self.xsno = len(self.cross_sections)
            # TODO to be checked later now for testing of version 4
            self.xs_names = self.cross_sections["xsid"].tolist()
            self.reach_ids = list(set(self.cross_sections["id"].tolist()))

    def readBoundaryConditions(
        self,
        start: str = "",
        end: str = "",
        path: str = "",
        fmt: str = "%Y-%m-%d",
        ds: bool = False,
        dsbcpath: str = "",
    ):
        """ReadBoundaryConditions.

        Read Boundary Conditions

        ReadBoundaryConditions method reads the BC files and since these files
        are separated each day is written in a file so the code is reading a
        lot of files, therefor you can specify a specific day to start read
        the BC H & Q from that day till the end of the simulated period

        for version 4
        - boundary condition for all points is stored in one file with the date
            stored in the first column.
        - the method will also resample the boundary condition time series to
            whatever temporal resolution you will define when instantiating the
            River object.
        - now the boundary condition is Q for the kinematic wave Approx later
            this method will be adjusted to read any boundaryu condition

        Parameters
        ----------
        start: [int/str], optional
                the day you want to read the result from, the first day is 1
                not zero, you can also enter the date of the day.
                The default is ''.
        end: [int], optional
                the day you want to read the result to.
        path: [String], optional
            path to read the results from. The default is ''.
        fmt: [string]
            format of the date. fmt="%Y-%m-%d %H:%M:%S"
        ds: [bool]

        dsbcpath: [str]


        Returns
        -------
        QBC: [dataframe attribute]
            dataframe contains the Discharge boundary conditions for each
            day as a row and for each column are the hours
        HBC: [dataframe attribute]
            dataframe contains the water depth boundary conditions for each
            day as a row and for each column are the hours
        """
        if path != "":
            self.us_bc_path = path

        if self.version < 4:
            if start == "":
                start = 1
            if end == "":
                end = len(self.reference_index_results) - 1

            if isinstance(start, str):
                start = dt.datetime.strptime(start, fmt)
                start = np.where(self.reference_index_results == start)[0][0] + 1

            if isinstance(end, str):
                end = dt.datetime.strptime(end, fmt)
                end = np.where(self.reference_index_results == end)[0][0] + 1

            QBC = pd.DataFrame(
                index=self.reference_index_results[start - 1 : end], columns=hours
            )
            HBC = pd.DataFrame(
                index=self.reference_index_results[start - 1 : end], columns=hours
            )

            for i in self.days_list[start - 1 : end]:
                bc_q = np.loadtxt(
                    self.us_bc_path + str(self.id) + "-" + str(i) + ".txt",
                    dtype=np.float16,
                )
                QBC.loc[self.reference_index.loc[i, "date"], :] = bc_q[:, 0].tolist()[
                    0 : bc_q.shape[0] : 60
                ]
                HBC.loc[self.reference_index.loc[i, "date"], :] = bc_q[:, 1].tolist()[
                    0 : bc_q.shape[0] : 60
                ]

            self.QBC = QBC
            self.HBC = HBC

        else:

            def convertdate(date):
                return dt.datetime.strptime(date, fmt)

            BC = pd.read_csv(self.us_bc_path)
            BC.index = BC[BC.columns[0]].apply(convertdate)
            BC = BC.drop(BC.columns[0], axis=1)

            ind = pd.date_range(BC.index[0], BC.index[-1], freq=self.freq)
            self.usbc = pd.DataFrame(index=ind, columns=BC.columns)

            self.usbc.loc[:, :] = (
                BC.loc[:, :].resample(self.freq).mean().interpolate("linear")
            )

            if ds:
                BC = pd.read_csv(dsbcpath)
                BC.index = BC[BC.columns[0]].apply(convertdate)
                BC = BC.drop(BC.columns[0], axis=1)

                ind = pd.date_range(BC.index[0], BC.index[-1], freq=self.freq)
                self.dsbc = pd.DataFrame(index=ind, columns=BC.columns)

                self.dsbc.loc[:, :] = (
                    BC.loc[:, :].resample(self.freq).mean().interpolate("linear")
                )

    def readSubDailyResults(
        self,
        start: str,
        end: str,
        fmt: str = "%Y-%m-%d",
        last_river_reach: bool = False,
    ):
        """ReadSubDailyResults.

        Read Reach-Daily Results

        Read1DResults1Min method is used by the sub sub-class, so most of the
        parameters (xs_names,...) are assigned to values after reading results
        with other methods in the sub class

        version 4
        -

        Parameters
        ----------
        start : [string]
            DESCRIPTION.
        end : [string]
            DESCRIPTION.
        fmt: [string]
            format of the date. fmt="%Y-%m-%d %H:%M:%S"
        last_river_reach : [bool]

        Returns
        -------
        h : [dataframe]
        dataframe containsthe water level time series, index is the date, and
        columns are the cross-section ids.
        """
        if self.version == 4:
            assert self.cross_sections, "please read the cross sections first"

        assert isinstance(self.us_bc_path, str), (
            "please input the 'us_bc_path' attribute in "
            "the River or the Reach instance"
        )

        if isinstance(start, str):
            start = dt.datetime.strptime(start, fmt)

        if isinstance(end, str):
            end = dt.datetime.strptime(end, fmt)

        indmin = pd.date_range(start, end + dt.timedelta(days=1), freq=self.freq)[:-1]

        # how many time steps per day
        nstep = (
            len(pd.date_range(start, start + dt.timedelta(days=1), freq=self.freq)) - 1
        )

        # US boundary condition (for each day in a separate row)
        index_daily = pd.date_range(start, end + dt.timedelta(days=1), freq="D")[:-1]
        bc_q = pd.DataFrame(index=index_daily, columns=list(range(1, nstep + 1)))
        bc_h = pd.DataFrame(index=index_daily, columns=list(range(1, nstep + 1)))

        xsname = [int(i) for i in self.xs_names]
        h = pd.DataFrame(index=indmin, columns=xsname)
        q = pd.DataFrame(index=indmin, columns=xsname)

        ii = self.dateToIndex(start)
        ii2 = self.dateToIndex(end) + 1
        list2 = list(range(ii, ii2))

        if self.version < 4:
            # read results for each day
            for i in list2:
                path = (
                    self.one_min_result_path
                    + "{0}/"
                    + str(self.id)
                    + "-{0}-"
                    + str(i)
                    + ".txt"
                )
                hh = np.transpose(np.loadtxt(path.format("h"), dtype=np.float16))
                logger.debug(path.format("h") + "- file is read")
                qq = np.transpose(np.loadtxt(path.format("q"), dtype=np.float16))
                logger.debug(path.format("q") + " file is read")
                if not last_river_reach:
                    hh = hh[:, :-1]
                    qq = qq[:, :-1]
                # add the bed level to the water depth
                hh = hh + self.cross_sections["gl"].values
                # assign the sub-daily results in the big dataframe
                ind1 = h.index[(i - list2[0]) * nstep]
                ind2 = h.index[(i - list2[0]) * nstep + nstep - 1]
                h.loc[ind1:ind2, :] = hh
                q.loc[ind1:ind2, :] = qq

                # BC
                bc = np.loadtxt(
                    self.us_bc_path + str(self.id) + "-" + str(i) + ".txt",
                    dtype=np.float16,
                )
                bc_q.loc[bc_q.index[i - list2[0]], :] = bc[:, 0]
                bc_h.loc[bc_h.index[i - list2[0]]] = bc[:, 1]

            self.h = h[:]
            self.q = q[:]
            self.q_bc_1min = bc_q[:]
            self.h_bc_1min = bc_h[:]
        else:
            for i in list2:
                path = (
                    f"{self.one_min_result_path}H-{str(self.indexToDate(i))[:10]}.csv"
                )
                hh = np.transpose(np.loadtxt(path, delimiter=",", dtype=np.float16))
                path = (
                    f"{self.one_min_result_path}Q-{str(self.indexToDate(i))[:10]}.csv"
                )
                qq = np.transpose(np.loadtxt(path, delimiter=",", dtype=np.float16))

                h = h + self.cross_sections["bed level"].values
                ind1 = h.index[(i - list2[0]) * len(indmin)]
                ind2 = h.index[(i - list2[0]) * len(indmin) + len(indmin) - 1]
                h.loc[ind1:ind2] = hh
                q.loc[ind1:ind2] = qq

            self.h = h
            self.q = q

            # check the first day in the results and get the date of the first day and last day
            # create time series
            # TODO to be checked later now for testing
            self.from_beginning = 1  # self.results_1d['day'][0]

            self.first_day = self.indexToDate(self.from_beginning)
            # if there are empty days at the beginning the filling missing days is not going to detect it
            # so ignore it here by starting from the first day in the data (data['day'][0]) dataframe
            # empty days at the beginning
            self.first_day_results = self.indexToDate(self.from_beginning)
            self.last_day = self.indexToDate(len(self.reference_index))

            # last days+1 as range does not include the last element
            self.days_list = list(range(self.from_beginning, len(self.reference_index)))
            self.reference_index_results = pd.date_range(
                self.first_day_results, self.last_day, freq="D"
            )

    @staticmethod
    def _read_chuncks(path, chunksize=10e5):
        """Read csv file in chuncks.

        Parameters
        ----------
        path: [str]
            file path
        chunksize: [int]
            chunck size to particion reading the file

        Returns
        -------
        DataFrame
        """
        iterator = pd.read_csv(
            path,
            header=None,
            delimiter=r"\s+",
            chunksize=chunksize,
            iterator=True,
            compression="infer",
        )

        data = pd.DataFrame()
        cond = True

        while cond:
            try:
                chunk = iterator.get_chunk(chunksize)
                data = pd.concat([data, chunk], ignore_index=True, sort=False)
            except StopIteration:
                cond = False

        return data

    def read1DResult(
        self,
        Subid: int,
        from_day: Optional[int] = None,
        to_day: Optional[int] = None,
        path: str = None,
        fill_missing: bool = False,
        chunk_size: int = None,
        extension: str = ".txt",
    ):
        """Read1DResult.

        Read-1D Result

        Read1DResult method reads the 1D results and fill the missing days in the middle

        Parameters
        ----------
        Subid : [integer]
            id of the sub-basin you want to read its data.
        from_day : [integer], optional
            the index of the day you want the data to start from. The default is empty.
            means read everything
        to_day : [integer], optional
            the index of the day you want the data to end to. The default is empty.
            means read everything
        path : [String], optional
            path to read the results from. The default is ''.
        fill_missing : [Bool], optional
            Fill the missing days. The default is False.
        chunk_size: [int]
            size of the chunk if you want to read the file in chunks Default is = None
        extension: [str]
            the extension of the file. Default is ".txt"

        Returns
        -------
        results_1d : [attribute]
            the results read will be stored (as it is without any filter)
            in the attribute "results_1d"
        """
        # if the path is not given try to read from the object predefined one_d_result_path
        t1 = dt.datetime.now()
        if path is None:
            path = self.one_d_result_path

        path = os.path.join(path, f"{Subid}{extension}")

        if chunk_size is None:
            data = pd.read_csv(
                path,
                header=None,
                delimiter=r"\s+",
                index_col=False,
                compression="infer",
                # engine="pyarrow"
            )
        else:
            # read the file in chunks
            data = self._read_chuncks(path, chunksize=chunk_size)

        data.columns = ["day", "hour", "xs", "q", "h", "wl"]
        days = list(set(data["day"]))
        days.sort()

        if from_day:
            if from_day not in days:
                raise ValueError(
                    f"Please use the GetDays method to select from_day:{from_day} that exist in the data"
                )
        if to_day:
            if to_day not in days:
                raise ValueError(
                    f"please use the GetDays method to select to_day: {to_day} that exist in the data"
                )

        if from_day:
            data = data.loc[data["day"] >= from_day, :]

        if to_day:
            data = data.loc[data["day"] <= to_day]

        #  data.index = list(range(0, len(data)))

        # Cross section data add one more xs at the end
        xsname = self.xs_names + [self.xs_names[-1] + 1]
        # data["xs"][data["day"] == data["day"][1]][data["hour"] == 1].tolist()

        if fill_missing:
            # check if there is missing days (Q was < threshold so the model didn't run)
            # fill these values with 0
            # days = list(set(data["day"]))
            # days.sort()
            missing_days = list(set(range(days[0], days[-1])) - set(days))
            if len(missing_days) > 0:
                if len(missing_days) > 10000:
                    missing_days_list = list()
                    missing_hours = list()
                    missing_xs = list()
                    for day_i in missing_days:
                        for hour_i in hours:
                            for xs_i in xsname:
                                missing_days_list.append(day_i)
                                missing_hours.append(hour_i)
                                missing_xs.append(xs_i)
                else:
                    missing = [
                        (i, j, h) for i in missing_days for j in hours for h in xsname
                    ]
                    missing_days_list = [i[0] for i in missing]
                    missing_hours = [i[1] for i in missing]
                    missing_xs = [i[2] for i in missing]

                missing = pd.DataFrame(
                    index=range(len(missing_days_list)), dtype=np.float64
                )
                missing["day"] = missing_days_list
                missing["hour"] = missing_hours
                missing["xs"] = missing_xs

                missing["q"] = 0
                missing["h"] = 0
                missing["wl"] = 0
                data = data.append(missing)
                # delete for the memory problem
                del missing, missing_days_list, missing_hours, missing_xs, missing_days
                data = data.sort_values(by=["day", "hour", "xs"], ascending=True)
                data.reset_index(inplace=True)

        # calculate time and print it
        t2 = dt.datetime.now()
        time_min = (t2 - t1).seconds / 60
        print(f"Time taken to read the file: {time_min:0.3f} min")
        self.results_1d = data

    @staticmethod
    def collect1DResults(
        path,
        FolderNames,
        Left,
        Right,
        Savepath,
        OneD,
        fromf="",
        tof="",
        FilterbyName=False,
    ):
        """Collect1DResults.

        Collect1DResults method reads the 1D separated result files and filter
        then between two number to remove any warmup period if exist then stack
        the result in one table then write it.

        Parameters
        ----------
        path : [String]
            path to the folder containing the separated folder.
        FolderNames : [List]
            list containing folder names.
        Left : [Bool]
            True if you want to combine left overtopping files.
        Right : [Bool]
            True if you want to combine right overtopping files.
        Savepath : [String]
            path to the folder where data will be saved.
        OneD : [Bool]
            True if you want to combine 1D result files.
        fromf : [Integer], optional
            if the files are very big and the cache memory has a problem
            reading all the files you can specify here the order of the file
            the code will start from to combine. The default is ''.
        tof : [Integer], optional
            if the files are very big and the cache memory has a problem
            reading all the files you can specify here the order of the file
            the code will end to combine. The default is ''.
        FilterbyName : [Bool], optional
            if the results include a wanm up period at the beginning
            or has results for some days at the end you want to filter out
            you want to include the period you want to be combined only
            in the name of the folder between () and separated with -
            ex 1d(5000-80000). The default is False.

        Returns
        -------
            combined files will be written to the Savepath .
        """
        second = "=pd.DataFrame()"
        if fromf == "":
            fromf = 0

        for i in range(len(FolderNames)):
            logger.debug(f"{i} - {FolderNames[i]}")

            if tof == "":
                tof = len(os.listdir(path + "/" + FolderNames[i]))

            FileList = os.listdir(path + "/" + FolderNames[i])[fromf:tof]
            # tof is only renewed if it is equal to ''
            tof = ""
            if FilterbyName:
                filter1 = int(FolderNames[i].split("(")[1].split("-")[0])
                filter2 = int(FolderNames[i].split("(")[1].split("-")[1].split(")")[0])

            for j in range(len(FileList)):

                go = False

                if Left and FileList[j].split(".")[0].endswith("_left"):
                    logger.debug(f"{i} - {j} -  {FileList[j]}")
                    # create data frame for the sub-basin
                    first = "L" + FileList[j].split(".")[0]
                    go = True

                elif Right and FileList[j].split(".")[0].endswith("_right"):
                    logger.debug(str(i) + "-" + str(j) + "-" + FileList[j])
                    first = "R" + FileList[j].split(".")[0]
                    go = True

                ## try to get the integer of the file name to make sure that it is
                ## one of the 1D results file
                elif (
                    OneD
                    and not FileList[j].split(".")[0].endswith("_right")
                    and not FileList[j].split(".")[0].endswith("_left")
                ):
                    logger.debug(str(i) + "-" + str(j) + "-" + FileList[j])
                    # create data frame for the sub-basin
                    first = "one" + FileList[j].split(".")[0]
                    go = True

                if go:
                    # get the updated list of variable names
                    variables = locals()

                    # read the file
                    try:
                        temp_df = pd.read_csv(
                            f"{path}/{FolderNames[i]}/{FileList[j]}",
                            header=None,
                            delimiter=r"\s+",
                        )

                        if FilterbyName:
                            temp_df = temp_df[temp_df[0] >= filter1]
                            temp_df = temp_df[temp_df[0] <= filter2]
                        # check whether the variable exist or not
                        # if this is the first time this file exist
                        if first not in variables.keys():
                            # create a datafame with the name of the sub-basin
                            total = first + second
                            exec(total)

                        # concatenate the
                        exec(first + "= pd.concat([" + first + ", temp_df])")
                    except:
                        continue

        # Save files
        variables = list(locals().keys())
        # get sub-basins variables (starts with "One")
        for i in range(len(variables)):
            var = variables[i]
            if var.endswith("_left"):
                # put the dataframe in order first
                exec(var + ".sort_values(by=[0,1,2],ascending = True, inplace = True)")
                path = f"{Savepath}/{var[1:]}.txt"
                exec(var + ".to_csv(path ,index= None, sep = ' ', header = None)")
            elif var.endswith("_right"):
                # put the dataframe in order first
                exec(var + ".sort_values(by=[0,1,2],ascending = True, inplace = True)")
                path = f"{Savepath}/{var[1:]}.txt"
                exec(var + ".to_csv(path ,index= None, sep = ' ', header = None)")
            elif var.startswith("one"):
                # put the dataframe in order first
                exec(var + ".sort_values(by=[0,1,2],ascending = True, inplace = True)")
                logger.debug(f"Saving {var[3:]}.txt")
                path = f"{Savepath}/{var[3:]}.txt"
                exec(var + ".to_csv(path ,index= None, sep = ' ', header = None)")

    @staticmethod
    def _readRRMResults(
        version: int,
        rrm_reference_index,
        path: str,
        node_id: Union[int, str],
        from_day: int,
        to_day: int,
        date_format: str = "%d_%m_%Y",
    ) -> DataFrame:
        """ReadRRMResults.

        ReadRRMResults is a static method to read the results of the rainfall-runoff
        model

        Parameters
        ----------
        version: []

        rrm_reference_index: []

        path : [String]
            path to the result files.
        node_id : [Integer]
            the id given the the sub-basin .
        from_day : [integer], optional
                the day you want to read the result from, the first day is 1 not zero.The default is ''.
        to_day : [integer], optional
                the day you want to read the result to.
        date_format: [str]
            format of the date string
        Returns
        -------
        Q : [Dataframe]
            time series of the runoff .
        """
        rpath = os.path.join(path, f"{node_id}.txt")
        if version < 3:
            Q = pd.read_csv(rpath, header=None)
            Q = Q.rename(columns={0: node_id})
            Q.index = list(range(1, len(Q) + 1))

            if not from_day:
                from_day = 1
            if not to_day:
                to_day = len(Q)

            Q = Q.loc[Q.index >= from_day, :]
            Q = Q.loc[Q.index <= to_day]
        else:
            Q = pd.read_csv(rpath, header=None, skiprows=1)

            Q.index = [dt.datetime.strptime(date, date_format) for date in Q[0]]
            del Q[0]

            # convert the date into integer index
            s = np.where(rrm_reference_index["date"] == Q.index[0])[0][0] + 1
            e = np.where(rrm_reference_index["date"] == Q.index[-1])[0][0] + 1
            Q.index = list(range(s, e + 1))

            if not from_day:
                from_day = s
            if not to_day:
                to_day = e

            Q = Q.loc[Q.index >= from_day, :]
            Q = Q.loc[Q.index <= to_day, :]

            Q = Q[1].to_frame()
            Q = Q.rename(columns={1: node_id})

        return Q

    def kinematicwave(self, start: str = "", end: str = "", fmt: str = "%Y-%m-%d"):
        """kinematicwave.

        kinematicwave apply the kinematic wave approximation of the shallow
        water equation to the 1d river reach

        fmt: [string]
            format of the date. fmt="%Y-%m-%d %H:%M:%S"

        Returns
        -------
        1- Q : [array]
            discharge time series with the rows as time and columns as space
        2- H: [array]
            water depth time series with the rows as time and columns as space
        """
        if start == "":
            start = self.start
        else:
            start = dt.datetime.strptime(start, fmt)

        if end == "":
            end = self.end
        else:
            end = dt.datetime.strptime(end, fmt)

        # ind = pd.date_range(start, end, freq=self.freq)

        # TODO to be checked later now for testing
        # self.from_beginning = self.indsub[np.where(self.indsub == start)[0][0]]

        self.first_day = self.indsub[np.where(self.indsub == start)[0][0]]
        # if there are empty days at the beginning the filling missing days is not going to detect it
        # so ignore it here by starting from the first day in the data (data['day'][0]) dataframe
        # empty days at the beginning
        # self.first_day_results = self.indsub[np.where(self.indsub == start)[0][0]]
        self.last_day = self.indsub[np.where(self.indsub == end)[0][0]]

        # last days+1 as range does not include the last element
        # self.days_list = list(range(self.from_beginning, len(self.reference_index)))
        self.reference_index_results = pd.date_range(
            self.first_day, self.last_day, freq=self.freq
        )

        usbc = self.usbc.loc[self.reference_index_results, :]
        SaintVenant.kinematic1d(self, usbc)

    def preissmann(
        self,
        start: str = "",
        end: str = "",
        fmt: str = "%Y-%m-%d",
        maxiteration: int = 10,
        beta: int = 1,
        epsi: float = 0.5,
        theta: float = 0.5,
    ):
        """preissmann.

        preissmann scheme solving the whole shallow water equation.

        Parameters
        ----------
        start : TYPE, optional
            DESCRIPTION. The default is ''.
        end : TYPE, optional
            DESCRIPTION. The default is ''.
        fmt: [string]
            format of the date. fmt="%Y-%m-%d %H:%M:%S"
        maxiteration : TYPE, optional
            DESCRIPTION. The default is 10.
        beta : TYPE, optional
            DESCRIPTION. The default is 1.
        epsi : TYPE, optional
            DESCRIPTION. The default is 0.5.
        theta : TYPE, optional
            DESCRIPTION. The default is 0.5.

        Returns
        -------
        None.
        """

        if start == "":
            start = self.start
        else:
            start = dt.datetime.strptime(start, fmt)

        if end == "":
            end = self.end
        else:
            end = dt.datetime.strptime(end, fmt)

        # ind = pd.date_range(start, end, freq=self.freq)

        # TODO to be checked later now for testing
        # self.from_beginning = self.indsub[np.where(self.indsub == start)[0][0]]

        self.first_day = self.indsub[np.where(self.indsub == start)[0][0]]
        # if there are empty days at the beginning the filling missing days is not going to detect it
        # so ignore it here by starting from the first day in the data (data['day'][0]) dataframe
        # empty days at the beginning
        # self.first_day_results = self.indsub[np.where(self.indsub == start)[0][0]]
        self.last_day = self.indsub[np.where(self.indsub == end)[0][0]]

        # last days+1 as range does not include the last element
        # self.days_list = list(range(self.from_beginning, len(self.reference_index)))
        self.reference_index_results = pd.date_range(
            self.first_day, self.last_day, freq=self.freq
        )

        # usbc = self.qusbc.loc[self.reference_index_results,:]
        # dsbc = self.qusbc.loc[self.reference_index_results, :]
        saintpreis = SaintVenant(
            maxiteration=maxiteration, beta=beta, epsi=epsi, theta=theta
        )
        saintpreis.preissmann(self)

    def storagecell(self, start: str = "", end: str = "", fmt: str = "%Y-%m-%d"):
        """storagecell.

        kinematicwave apply the kinematic wave approximation of the shallow
        water equation to the 1d river reach

        fmt: [string]
            format of the date. fmt="%Y-%m-%d %H:%M:%S"

        Returns
        -------
        1- Q : [array]
            discharge time series with the rows as time and columns as space
        2- H: [array]
            water depth time series with the rows as time and columns as space
        """
        if start == "":
            start = self.start
        else:
            start = dt.datetime.strptime(start, fmt)

        if end == "":
            end = self.end
        else:
            end = dt.datetime.strptime(end, fmt)
        # ind = pd.date_range(start, end, freq=self.freq)

        # TODO to be checked later now for testing
        # self.from_beginning = self.indsub[np.where(self.indsub == start)[0][0]]

        self.first_day = self.indsub[np.where(self.indsub == start)[0][0]]
        # if there are empty days at the beginning the filling missing days is not going to detect it
        # so ignore it here by starting from the first day in the data (data['day'][0]) dataframe
        # empty days at the beginning
        # self.first_day_results = self.indsub[np.where(self.indsub == start)[0][0]]
        self.last_day = self.indsub[np.where(self.indsub == end)[0][0]]

        # last days+1 as range does not include the last element
        # self.days_list = list(range(self.from_beginning, len(self.reference_index)))
        self.reference_index_results = pd.date_range(
            self.first_day, self.last_day, freq=self.freq
        )

        usbc = self.usbc.loc[self.reference_index_results, :]
        SaintVenant.storagecell(self, usbc)

    def animatefloodwave(
        self,
        start,
        end,
        interval: float = 0.00002,
        xs: int = 0,
        xsbefore: int = 10,
        xsafter: int = 10,
        fmt: str = "%Y-%m-%d %H:%M:%S",
        textlocation: float = 2,
        xaxislabelsize: float = 15,
        yaxislabelsize: float = 15,
        nxlabels: float = 50,
        # plot_bankfull_depth=False,
    ):
        """animatefloodwave.

        animatefloodwave method animate 1d the flood wave

        Parameters
        ----------
        start : [string]
            DESCRIPTION.
        end : [string]
            DESCRIPTION.
        fmt: [string]
            format of the date. fmt="%Y-%m-%d %H:%M:%S"

        interval: []

        xs: []

        xsbefore: []

        xsafter: []

        textlocation: []

        xaxislabelsize: []

        yaxislabelsize: []

        nxlabels: []

        Returns
        -------
        None.
        """
        anim = V.river1d(
            self,
            start,
            end,
            interval=interval,
            xs=xs,
            xs_before=xsbefore,
            xs_after=xsafter,
            fmt=fmt,
            text_location=textlocation,
            x_axis_label_size=xaxislabelsize,
            y_axis_label_size=yaxislabelsize,
            xlabels_number=nxlabels,
        )
        return anim

    def saveResult(self, path: str):  # , fmt="%.3f"):
        """SaveResult.

        Save Result

        Parameters
        ----------
        path : TYPE
            DESCRIPTION.

        Returns
        -------
        None.
        """
        for i in range(len(self.reference_index)):
            name = str(self.reference_index.loc[self.reference_index.index[i], "date"])[
                :10
            ]
            # space is rows , time is columns
            # save results of each day separately
            np.savetxt(
                path + "Q-" + name + ".csv",
                self.Q.transpose(),
                fmt="%.3f",
                delimiter=",",
            )
            np.savetxt(
                path + "H-" + name + ".csv",
                self.H.transpose(),
                fmt="%.3f",
                delimiter=",",
            )

    def readSlope(self, path: str):
        """readSlope.

            readSlope

        Parameters
        ----------
        path : [String]
            path to the Guide.csv file including the file name and extention
            "RIM1Files + "/Guide.csv".

        Returns
        -------
        slope: [DataFrame]
            dataframe of the boundary condition reaches that has slope
        """
        self.slope = pd.read_csv(path, delimiter=",", header=None, skiprows=1)
        self.slope.columns = ["id", "slope"]

    def returnPeriod(self, path):
        """ReturnPeriod.

        ReturnPeriod method reads the HQ file which contains all the computational nodes
        with HQ2, HQ10, HQ100
        Parameters
        ----------
            1-path : [String]
                path to the HQ.csv file including the file name and extention
                "RIM1Files + "/HQRhine.csv".

        Returns
        -------
            1-RP:[data frame attribute]
                containing the river computational node and calculated return period
                for with columns ['node','HQ2','HQ10','HQ100']
        """
        self.RP = pd.read_csv(path, delimiter=",", header=None)
        self.RP.columns = ["node", "HQ2", "HQ10", "HQ100"]

    def readRiverNetwork(self, path):
        """RiverNetwork.

        RiverNetwork method rad the table of each computational node followed by
        upstream and then downstream node

        Parameters
        ----------
        path : [String]
            path to the Trace.txt file including the file name and extention
                            "path/Trace.txt".

        Returns
        -------
        rivernetwork:[data frame attribute]
            containing the river network with columns ['Subid','US','DS']
        """
        File = open(path)
        wholefile = File.readlines()
        File.close()
        rivernetwork = pd.DataFrame(columns=wholefile[0][:-1].split(","))
        # all lines excpt the last line
        for i in range(1, len(wholefile)):
            rivernetwork.loc[i - 1, rivernetwork.columns[0:2].tolist()] = [
                int(j) for j in wholefile[i][:-1].split(",")[0:2]
            ]
            rivernetwork.loc[i - 1, rivernetwork.columns[2]] = [
                int(j) for j in wholefile[i][:-1].split(",")[2:]
            ]
        # last line does not have the \n at the end
        i = len(wholefile) - 1
        rivernetwork.loc[i - 1, rivernetwork.columns[0:2].tolist()] = [
            int(j) for j in wholefile[i][:-1].split(",")[0:2]
        ]
        rivernetwork.loc[i - 1, rivernetwork.columns[2]] = [
            int(j) for j in wholefile[i].split(",")[2:]
        ]
        rivernetwork.columns = ["No", "id", "us"]
        self.rivernetwork = rivernetwork[:]
        self.Segments = self.rivernetwork["id"].tolist()

    def traceSegment(self, sub_id):
        """TraceSegment.

        Trace method takes sub basin id and trace it to get the upstream and
        down stream computational nodes


        Parameters
        ----------
        sub_id : TYPE
            DESCRIPTION.

        Returns
        -------
        USnode : [Integer]
            the Upstream computational node from Configuration file.
        DSnode : [Integer]
            the Downstream computational node from Configuration file.

        Examples
        --------
        >>> Subid = 42
        >>> River.traceSegment(Subid)
        """
        US = self.rivernetwork["us"][np.where(self.rivernetwork["id"] == sub_id)[0][0]]
        for i in range(len(self.rivernetwork)):
            if id in self.rivernetwork.loc[i, "us"]:
                DS = self.rivernetwork.loc[i, "id"]
                break
            else:
                DS = []

        return US, DS

    def trace2(self, sub_id, US):
        """Trace2.

        trace the river network

        Parameters
        ----------
        sub_id : TYPE
            DESCRIPTION.
        US : TYPE
            DESCRIPTION.

        Returns
        -------
        None.
        """
        # trace the given segment
        US1, _ = self.traceSegment(sub_id)
        if len(US1) > 0:
            for i in range(len(US1)):
                US.append(US1[i])
                self.trace2(US1[i], US)

    def trace(self, sub_id):
        """Trace.

        Trace method takes the id of the segment and trace it upstream

        Parameters
        ----------
        sub_id : TYPE
            DESCRIPTION.

        Returns
        -------
        US : [list attribute], optional
            the id of all the upstream reaches are going to be stored in a list
            attribute.
        """
        self.US = []
        self.trace2(sub_id, self.US)

    def statisticalProperties(self, path: str, Distibution: str = "GEV"):
        """StatisticalProperties.

            StatisticalProperties method reads the parameters of the distribution and
            calculates the the 2, 5, 10, 15, 20, 50, 100, 200, 500, 1000 return
            period discharge for each sub-basin to create the parameters file use
            the code StatisticalProperties in the 07ReturnPeriod folder

        Parameters
        ----------
        path : [String]
            path to the "Statistical Properties.txt" file including the
            file name and extention "path/Statistical Properties.txt".
            >>> "Statistical Properties.txt"
            id,c,loc,scale,D-static,P-Value
            23800100,-0.0511,115.9465,42.7040,0.1311,0.6748
            23800500,0.0217,304.8785,120.0510,0.0820,0.9878
            23800690,0.0215,455.4108,193.4242,0.0656,0.9996

        Distibution: [str]
            The distribution used to fit the data. Default is "GEV".

        Returns
        -------
        SP: [data frame attribute]
            containing the river computational nodes US of the sub basins
            and estimated gumbel distribution parameters that fit the time
            series ['node','HQ2','HQ10','HQ100']

        Examples
        --------
        >>> import Hapi.hm.river as R
        >>> HM = R.River('Hydraulic model')
        >>> stat_properties_path = "path/to/results/statistical analysis/DistributionProperties.csv"
        >>> HM.statisticalProperties(stat_properties_path)
        >>> HM.SP
                       id       c        loc      scale  D-static  P-Value
        0        23800100 -0.0511   115.9465    42.7040    0.1311   0.6748
        1        23800500  0.0217   304.8785   120.0510    0.0820   0.9878
        2        23800690  0.0215   455.4108   193.4242    0.0656   0.9996
        3        23700200  0.1695  2886.8037   900.1678    0.0820   0.9878
        """
        self.SP = pd.read_csv(path, delimiter=",")
        # calculate the 2, 5, 10, 15, 20 return period doscharge
        T = np.array([2, 5, 10, 15, 20, 50, 100, 200, 500, 1000, 5000])
        self.SP = self.SP.assign(
            RP2=0,
            RP5=0,
            RP10=0,
            RP15=0,
            RP20=0,
            RP50=0,
            RP100=0,
            RP200=0,
            RP500=0,
            RP1000=0,
            RP5000=0,
        )
        F = 1 - (1 / T)
        for i in range(len(self.SP)):
            if self.SP.loc[i, "loc"] != -1:
                col1 = self.SP.columns.to_list().index("RP2")
                if Distibution == "GEV":
                    dist = GEV()
                    self.SP.loc[
                        i, self.SP.keys()[col1:].tolist()
                    ] = dist.theporeticalEstimate(
                        self.SP.loc[i, "c"],
                        self.SP.loc[i, "loc"],
                        self.SP.loc[i, "scale"],
                        F,
                    )
                else:
                    dist = Gumbel()
                    self.SP.loc[
                        i, self.SP.keys()[col1:].tolist()
                    ] = dist.theporeticalEstimate(
                        self.SP.loc[i, "loc"], self.SP.loc[i, "scale"], F
                    )

    def getReturnPeriod(
        self,
        Subid: int,
        Q: Union[float, int, np.ndarray, list],
        distribution: str = "GEV",
    ):
        """GetReturnPeriod.

            GetReturnPeriod method takes given discharge and using the distribution
            properties of a particular sub basin it calculates the return period

        Parameters
        ----------
        Subid : [Integer]
            sub-basin id.
        Q : [Float]
            Discharge value.
        distribution: [str]
            the distribution used to fit the discharge data. Default is "GEV".

        Returns
        -------
        return Period :[Float]
            return periodcal culated for the given discharge using the
            parameters of the distribution for the catchment.
        """
        if not isinstance(self.SP, DataFrame):
            raise ValueError(
                "Please read the statistical properties file for the catchment first"
            )
        try:
            loc = np.where(self.SP["id"] == Subid)[0][0]
            if distribution == "GEV":
                # dist = GEV()
                # rp = dist.getRP(
                #     self.SP.loc[loc, "c"],
                #     self.SP.loc[loc, "loc"],
                #     self.SP.loc[loc, "scale"],
                #     Q
                # )

                F = genextreme.cdf(
                    Q,
                    c=self.SP.loc[loc, "c"],
                    loc=self.SP.loc[loc, "loc"],
                    scale=self.SP.loc[loc, "scale"],
                )
            else:
                # dist = Gumbel()
                # rp = dist.getRP(self.SP.loc[loc, "loc"], self.SP.loc[loc, "scale"], Q)
                F = gumbel_r.cdf(
                    Q, loc=self.SP.loc[loc, "loc"], scale=self.SP.loc[loc, "scale"]
                )

            return 1 / (1 - F)
        except IndexError:
            return -1

    def getQForReturnPeriod(self, Subid, T, distribution: str = "GEV"):
        """GetQForReturnPeriod.

            get the corespondiong discharge to a specific return period

        Parameters
        ----------
        Subid : [int]
            DESCRIPTION.
        T : TYPE
            DESCRIPTION.
        distribution: [str]
            statistical distribution. Default is "GEV"

        Returns
        -------
        TYPE
            DESCRIPTION.
        """
        if not isinstance(self.SP, DataFrame):
            raise ValueError(
                "Please read the statistical properties file for the catchment first"
            )

        if "id" not in self.SP.columns:
            raise ValueError(
                "the SP dataframe should have a column 'id' containing the id of the gauges"
            )

        F = 1 - (1 / T)
        try:
            loc = np.where(self.SP["id"] == Subid)[0][0]
            if distribution == "GEV":
                Q = genextreme.ppf(
                    F,
                    c=self.SP.loc[loc, "c"],
                    loc=self.SP.loc[loc, "loc"],
                    scale=self.SP.loc[loc, "scale"],
                )
            else:
                Q = gumbel_r.ppf(
                    F, loc=self.SP.loc[loc, "loc"], scale=self.SP.loc[loc, "scale"]
                )
            return Q
        except:
            return -1

    def getBankfullDepth(self, function, ColumnName):
        """GetBankfullDepth.

        GetBankfullDepth method takes a function that calculates the bankful
        depth as a function of bankful width and calculate the depth

        Parameters
        ----------
            1-function : [function]
                function that takes one input and calculates the depth.
            2-ColumnName : [String]
                A name for the column to store the calculated depth at the
                cross section dataframe.

        Returns
        -------
            dataframe column in the cross section attribute with the calculated
            depth.
        """
        self.cross_sections[ColumnName] = (
            self.cross_sections["b"].to_frame().applymap(function)
        )

    def getCapacity(self, ColumnName: str, Option: int = 1, distribution: str = "GEV"):
        """GetCapacity.

            GetCapacity method calculates the discharge that is enough to fill the
            cross section using kinematic wave approximation (using bed slope with manning)

            In order to calculate the return period coresponding to each cross-section discharge
            each cross section needs to be assigned the id of a specific gauge, as the statistical
            analysis  is being done for the gauges only, so the distribution parameters are estimated
            only for the gauges.

        Parameters
        ----------
        ColumnName : [String]
            A name for the column to store the calculated depth at the
            cross section dataframe.
        Option : [Integer]
            1 if you want to calculate the capacity of the bankfull area,
            2 if you want to calculate the capacity of the whole cross section
            to the lelvel of the lowest dike
        distribution: [str]
            The distribution you used to fit the discharge data. Default is GEV

        Returns
        -------
        the cross_sections dataframe will be updated with the following columns.

        Discharge: [dataframe column]
            the calculated discharge will be stored in the cross_sections
            attribute in the River object in a columns with the given ColumnName
        ColumnName+"RP":[dataframe column]
            if you already rad the statistical properties another column containing
            the coresponding return period to the discharge,
            the calculated return period will be stored in a column with a name
            the given ColumnName+"RP", if the ColumnName was QC then the discharge
            will be in a Qc columns and the return period will be in QcRP column
        """
        for i in range(len(self.cross_sections) - 1):
            # get the slope
            if self.cross_sections.loc[i, "id"] == self.cross_sections.loc[i + 1, "id"]:
                slope = (
                    self.cross_sections.loc[i, "gl"]
                    - self.cross_sections.loc[i + 1, "gl"]
                ) / self.dx
            else:
                slope = (
                    abs(
                        self.cross_sections.loc[i, "gl"]
                        - self.cross_sections.loc[i - 1, "gl"]
                    )
                    / self.dx
                )
            self.cross_sections.loc[i, "Slope"] = slope

            if Option == 1:
                # bankfull area
                self.cross_sections.loc[i, ColumnName] = (
                    (1 / self.cross_sections.loc[i, "m"])
                    * self.cross_sections.loc[i, "b"]
                    * (self.cross_sections.loc[i, "dbf"]) ** (5 / 3)
                )
                self.cross_sections.loc[i, ColumnName] = self.cross_sections.loc[
                    i, ColumnName
                ] * slope ** (1 / 2)

            else:
                # lowest dike
                # get the vortices of the cross sections
                H = self.cross_sections.loc[i, ["zl", "zr"]].min()
                Hl, Hr, Bl, Br, B, dbf = self.cross_sections.loc[
                    i, ["hl", "hr", "bl", "br", "b", "dbf"]
                ].tolist()
                BedLevel = self.cross_sections.loc[i, "gl"]
                Coords = self.getVortices(H - BedLevel, Hl, Hr, Bl, Br, B, dbf)
                # get the area and perimeters
                Area, Perimeter = self.polygonGeometry(Coords)
                # self.cross_sections.loc[i,'Area'] = Area
                # self.cross_sections.loc[i,'Perimeter'] = Perimeter
                self.cross_sections.loc[i, ColumnName] = (
                    (1 / self.cross_sections.loc[i, "m"])
                    * Area
                    * ((Area / Perimeter) ** (2 / 3))
                )
                self.cross_sections.loc[i, ColumnName] = self.cross_sections.loc[
                    i, ColumnName
                ] * slope ** (1 / 2)

            if isinstance(self.SP, DataFrame):
                if "gauge" not in self.cross_sections.columns.tolist():
                    raise ValueError(
                        "To calculate the return period for each cross-section a column with "
                        "the coresponding gauge id should be in the cross-section file"
                    )
                RP = self.getReturnPeriod(
                    self.cross_sections.loc[i, "gauge"],
                    self.cross_sections.loc[i, ColumnName],
                    distribution=distribution,
                )
                if np.isnan(RP):
                    RP = -1
                self.cross_sections.loc[i, ColumnName + "RP"] = round(RP, 2)

    def calibrateDike(self, ObjectiveRP: Union[str, int], CurrentRP: Union[str, int]):
        """CalibrateDike.

            CalibrateDike method takes cross section and based on a given return period

        Parameters
        ----------
        ObjectiveRP : [string]
            Column name in the cross section dataframe you have to enter it.
        CurrentRP : [string]
            Column name in the cross section dataframe created by the GetCapacity
            method.

        Returns
        -------
        New RP: [data frame column]
            column in the cross section dataframe containing the new return period.
        New Capacity: [data frame column]
            column in the cross section dataframe containing the the discharge enough
            to fill the cross section after raising the dikes to the objective
            return period.
        """
        if not isinstance(self.SP, DataFrame):
            raise TypeError(
                "Please read the statistical properties file first using StatisticalProperties method"
            )

        if not isinstance(self.cross_sections, DataFrame):
            raise TypeError(
                "please read the cross section data first with the method CrossSections"
            )

        if CurrentRP not in self.cross_sections.columns:
            raise ValueError(
                f"{CurrentRP} in not in the cross section data please use GetCapacity method to "
                f"calculate the current return perion"
            )

        if ObjectiveRP not in self.cross_sections.columns:
            raise ValueError(
                f"{ObjectiveRP} in not in the cross section data please create a column in the cross "
                "section data containing the objective return period"
            )

        self.cross_sections.loc[:, "zlnew"] = self.cross_sections.loc[:, "zl"]
        self.cross_sections.loc[:, "zrnew"] = self.cross_sections.loc[:, "zr"]

        for i in range(len(self.cross_sections) - 2):

            if self.cross_sections.loc[i, "id"] == self.cross_sections.loc[i + 1, "id"]:
                slope = (
                    self.cross_sections.loc[i, "gl"]
                    - self.cross_sections.loc[i + 1, "gl"]
                ) / self.dx
            else:
                slope = (
                    abs(
                        self.cross_sections.loc[i, "gl"]
                        - self.cross_sections.loc[i - 1, "gl"]
                    )
                    / self.dx
                )
            # self.cross_sections.loc[i,'Slope'] = slope
            Hl, Hr, Bl, Br, B, dbf = self.cross_sections.loc[
                i, ["hl", "hr", "bl", "br", "b", "dbf"]
            ].tolist()
            BedLevel = self.cross_sections.loc[i, "gl"]

            # compare the current return period with the desired return period.
            if (
                self.cross_sections.loc[i, CurrentRP]
                < self.cross_sections.loc[i, ObjectiveRP]
                and self.cross_sections.loc[i, CurrentRP] != -1
            ):
                logger.debug("XS-" + str(self.cross_sections.loc[i, "xsid"]))
                logger.debug("Old RP = " + str(self.cross_sections.loc[i, CurrentRP]))
                logger.debug(
                    "Old H = " + str(self.cross_sections.loc[i, ["zl", "zr"]].min())
                )

                self.cross_sections.loc[i, "New RP"] = self.cross_sections.loc[
                    i, CurrentRP
                ]

                while (
                    self.cross_sections.loc[i, "New RP"]
                    < self.cross_sections.loc[i, ObjectiveRP]
                ):
                    # get the vortices of the cross sections
                    if (
                        self.cross_sections.loc[i, "zlnew"]
                        < self.cross_sections.loc[i, "zrnew"]
                    ):
                        self.cross_sections.loc[i, "zlnew"] = (
                            self.cross_sections.loc[i, "zlnew"] + 0.1
                        )
                    else:
                        self.cross_sections.loc[i, "zrnew"] = (
                            self.cross_sections.loc[i, "zrnew"] + 0.1
                        )

                    H = self.cross_sections.loc[i, ["zlnew", "zrnew"]].min()
                    Coords = self.getVortices(H - BedLevel, Hl, Hr, Bl, Br, B, dbf)
                    # get the area and perimeters
                    Area, Perimeter = self.polygonGeometry(Coords)
                    self.cross_sections.loc[i, "New Capacity"] = (
                        (1 / self.cross_sections.loc[i, "m"])
                        * Area
                        * ((Area / Perimeter) ** (2 / 3))
                    )
                    self.cross_sections.loc[
                        i, "New Capacity"
                    ] = self.cross_sections.loc[i, "New Capacity"] * slope ** (1 / 2)

                    RP = self.getReturnPeriod(
                        self.cross_sections.loc[i, "gauge"],
                        self.cross_sections.loc[i, "New Capacity"],
                    )

                    self.cross_sections.loc[i, "New RP"] = round(RP, 2)

                logger.info(f"New RP = {round(RP, 2)}")
                logger.info(f"New H = {round(H, 2)}")
                logger.info("---------------------------")

    def overtopping(self, overtopping_result_path: str = None):
        """Overtopping.

        Overtopping method reads the overtopping files and for each cross section
        in each sub-basin it will strore the days where overtopping happens
        in this cross section.

        you do not need to delete empty files or anything just give the code
        the sufix you used for the left overtopping file and the sufix you used
        for the right overtopping file

        Inputs:
        -------
        overtopping_result_path: [str]
            a path to the folder includng 2D results.

        Returns
        -------
        OverToppingSubsLeft : [dictionary attribute]
            dictionary having sub-basin ids as a key and for each sub-basins
            it contains dictionary for each cross section having the days of
            overtopping.
        OverToppingSubsRight : [dictionary attribute]
            dictionary having sub-basin ids as a key and for each sub-basins
            it contains dictionary for each cross section having the days of
            overtopping.
        """
        # sort files
        leftOverTop = list()
        RightOverTop = list()
        # get names of files that has _left or _right at its end
        if overtopping_result_path is None:
            overtopping_result_path = self.onedresultpath

        All1DFiles = os.listdir(overtopping_result_path)
        for i in range(len(All1DFiles)):
            if All1DFiles[i].endswith(self.leftovertopping_suffix):
                leftOverTop.append(All1DFiles[i])
            if All1DFiles[i].endswith(self.rightovertopping_suffix):
                RightOverTop.append(All1DFiles[i])

        # two dictionaries for overtopping left and right
        OverToppingSubsLeft = dict()
        OverToppingSubsRight = dict()
        # the _left and _right files has all the overtopping discharge
        # but sometimes the sum of all the overtopping is less than a threshold specified
        # and then the 2D  algorithm does not run so these cross sections you will not find
        # any inundation beside it in the maps but you will find it in the _left or _right maps

        # for each sub-basin that has overtopping from the left dike
        for i in range(len(leftOverTop)):

            try:
                # open the file (if there is no column sthe file is empty)
                data = pd.read_csv(
                    rf"{overtopping_result_path}\{leftOverTop[i]}",
                    header=None,
                    delimiter=r"\s+",
                )
                # add the sub basin to the overtopping dictionary of sub-basins
                OverToppingSubsLeft[
                    leftOverTop[i][: -len(self.leftovertopping_suffix)]
                ] = dict()
            except:
                continue
            # get the XS that overtopping happened from
            XSs = list(set(data.loc[:, 2]))
            # for each XS get the days
            for j in range(len(XSs)):
                OverToppingSubsLeft[
                    leftOverTop[i][: -len(self.leftovertopping_suffix)]
                ][XSs[j]] = list(set(data[0][data[2] == XSs[j]].tolist()))

        for i in range(len(RightOverTop)):

            try:
                # open the file
                data = pd.read_csv(
                    rf"{overtopping_result_path}\{RightOverTop[i]}",
                    header=None,
                    delimiter=r"\s+",
                )
                # add the sub basin to the overtopping dictionary of sub-basins
                OverToppingSubsRight[
                    RightOverTop[i][: -len(self.rightovertopping_suffix)]
                ] = dict()
            except:
                continue
            # get the XS that overtopping happened from
            XSs = list(set(data.loc[:, 2]))
            # for each XS get the days
            for j in range(len(XSs)):
                OverToppingSubsRight[
                    RightOverTop[i][: -len(self.rightovertopping_suffix)]
                ][XSs[j]] = list(set(data[0][data[2] == XSs[j]].tolist()))

        self.OverToppingSubsLeft = OverToppingSubsLeft
        self.OverToppingSubsRight = OverToppingSubsRight

    def getOvertoppedXS(self, day, allEventdays=True):
        """GetOvertoppedXS.

        GetOvertoppedXS method get the cross sections that was overtopped in
        a given date(you have to read the overtopping data first with the method
        Overtopping), since inudation maps gets the max depth for the whole event
        the method can also trace the event back to the beginning and get all
        the overtopped XS from the beginning of the Event till the given day
        (you have to give the River object the event_index attribute from the
        Event Object)

        Parameters
        ----------
            1-day : [Integer]
                the day you want to get the overtopped cross section for.
            2-allEventdays : [Bool], optional
                if you want to get the overtopped cross section for this day only
                or for the whole event. The default is True.

        Returns
        -------
            1-XSLeft : [list]
                list of cross section ids that has overtopping from the left bank.
            2-XSRight : [list]
                list of cross section ids that has overtopping from the right bank.
        Example:
            1- for a given day
                RIM2River = RV.River('RIM2.0')
                RIM2River.Overtopping(wpath2 + "/results/1d/")
                day = 1122
                XSleft, XSright = RIM2River.GetOvertoppedXS(day,False)

            2- from the beginning of the event till the given day
                RIM2River = RV.River('RIM2.0')
                RIM2River.Overtopping(wpath2 + "/results/1d/")
                # read precreated event_index table
                RIM2Event.ReadEventIndex(wpath2 + "/" + "event_index.txt")
                # give the event_index table to the River Object
                RIM2River.event_index = RIM1.event_index
                day = 1122
                XSleft, XSright = RIM2River.GetOvertoppedXS(day,False)
        """
        if allEventdays:
            loc = np.where(self.EventIndex["id"] == day)[0][0]
            # get all the days in the same event before that day as the inundation in the maps may
            # happen due to any of the days before not in this day
            Eventdays = self.EventIndex.loc[
                loc - self.EventIndex.loc[loc, "IndDiff"] : loc, "id"
            ].tolist()
        else:
            Eventdays = [day]

        XSLeft = list()
        XSRight = list()

        for k in range(len(Eventdays)):
            dayi = Eventdays[k]
            # for each sub-basin in the overtopping left dict
            for i in range(len(self.OverToppingSubsLeft.keys())):
                Subid = list(self.OverToppingSubsLeft.keys())[i]
                # get all cross section that overtopped before
                XSs = list(self.OverToppingSubsLeft[Subid].keys())
                # for each xross section check if the day is sored inside
                for j in range(len(XSs)):
                    if dayi in self.OverToppingSubsLeft[Subid][XSs[j]]:
                        XSLeft.append(XSs[j])

            for i in range(len(self.OverToppingSubsRight.keys())):
                Subid = list(self.OverToppingSubsRight.keys())[i]
                XSs = list(self.OverToppingSubsRight[Subid].keys())
                for j in range(len(XSs)):
                    if dayi in self.OverToppingSubsRight[Subid][XSs[j]]:
                        XSRight.append(XSs[j])

        XSLeft = list(set(XSLeft))
        XSRight = list(set(XSRight))

        return XSLeft, XSRight

    def getSubBasin(self, xsid):
        """GetSubBasin.

        GetSubBasin method returned the sub-basin that the Cross section belong
        Parameters
        ----------
            1-xsid : [Integer]
                cross section id.

        Returns
        -------
            [Integer]
                sub-basin id.
        """
        loc = np.where(self.cross_sections["xsid"] == xsid)[0][0]
        return self.cross_sections.loc[loc, "id"]

    def getFloodedSubs(self, OvertoppedXS=[], day=[1], allEventdays=True):
        """GetFloodedSubs.

            GetFloodedSubs gets the inundeated sub-basins

        Parameters
        ----------
        OvertoppedXS : [list], optional
            list of cross sections overtopped (if you already used the GetOvertoppedXS
            method to get the overtopped XSs for a specific day).The default is [].
            If entered the algorithm is not going to look at the over arguments
            of the method.
        day : [list], optional
            if you want to get the flooded subs for a specific list of days. The default is 1.
        allEventdays : [Bool], optional in case user entered OvertoppedXS
            if the user entered day the allEventdays is a must. The default is True.

        Returns
        -------
        Subs : TYPE
            DESCRIPTION.

        Examples
        --------
        - get the flooded subs for a specific days
            >>> floodedSubs = River.GetFloodedSubs(day = [1122,1123], allEventdays=False)

        - get the flooded subs from already obtained overtopped XSs
            >>> day = 1122
            >>> XSleft, XSright = River.GetOvertoppedXS(day,False)
            >>> floodedSubs = River.GetFloodedSubs(OvertoppedXS = XSleft + XSright, allEventdays=False)
        """
        Subs = list()
        # if you already used the GetOvertoppedXS and have a list of xs overtopped
        # at specific day
        if len(OvertoppedXS) > 0:
            OvertoppedXS = list(set(OvertoppedXS))
            for i in range(len(OvertoppedXS)):
                Subs.append(self.getSubBasin(OvertoppedXS[i]))
        else:
            for j in range(len(day)):
                XSLeft, XSRight = self.getOvertoppedXS(day[j], allEventdays)
                OvertoppedXS = XSLeft + XSRight
                OvertoppedXS = list(set(OvertoppedXS))

                for i in range(len(OvertoppedXS)):
                    Subs.append(self.getSubBasin(OvertoppedXS[i]))

        # to remove duplicate subs
        Subs = list(set(Subs))
        return Subs

    def detailedOvertopping(self, floodedSubs, eventdays):
        """DetailedOvertopping.

        DetailedOvertopping method takes list of days and the flooded subs-basins
        in those days and get the left and right overtopping for each sub-basin for
        each day

        Parameters
        ----------
            1-floodedSubs : [list]
                list of sub-basins that are flooded during the given days.
            2-eventdays : [list]
                list od daysof an event.

        Returns
        -------
            1-detailed_overtopping_left : [dataframe attribute]
                dataframe having for each day of the event the left overtopping
                to each sub-basin.

            2-detailed_overtopping_right : [dataframe attribute]
                dataframe having for each day of the event the right overtopping
                to each sub-basin.
        """
        columns = floodedSubs + ["sum"]
        self.detailed_overtopping_left = pd.DataFrame(
            index=eventdays + ["sum"], columns=columns
        )
        self.detailed_overtopping_right = pd.DataFrame(
            index=eventdays + ["sum"], columns=columns
        )

        # Left Bank
        for i in range(len(floodedSubs)):
            try:
                # try to open and read the overtopping file
                data = pd.read_csv(
                    rf"{self.onedresultpath}\{floodedSubs[i]}{self.leftovertopping_suffix}",
                    header=None,
                    delimiter=r"\s+",
                )
                # get the days in the sub
                days = list(set(data.loc[:, 0]))

                for j in range(len(eventdays)):
                    # check whether this sub basin has flooded in this particular day
                    if eventdays[j] in days:
                        # filter the dataframe to the discharge column (3) and the days
                        self.detailed_overtopping_left.loc[
                            eventdays[j], floodedSubs[i]
                        ] = data.loc[data[0] == eventdays[j], 3].sum()
                    else:
                        self.detailed_overtopping_left.loc[
                            eventdays[j], floodedSubs[i]
                        ] = 0
            except:
                self.detailed_overtopping_left.loc[:, floodedSubs[i]] = 0
                continue

        # right Bank
        for i in range(len(floodedSubs)):
            try:
                # try to open and read the overtopping file
                data = pd.read_csv(
                    rf"{self.onedresultpath}\{floodedSubs[i]}{self.rightovertopping_suffix}",
                    header=None,
                    delimiter=r"\s+",
                )
                # get the days in the sub
                days = list(set(data.loc[:, 0]))

                for j in range(len(eventdays)):
                    # check whether this sub basin has flooded in this particular day
                    if eventdays[j] in days:
                        # filter the dataframe to the discharge column (3) and the days
                        self.detailed_overtopping_right.loc[
                            eventdays[j], floodedSubs[i]
                        ] = data.loc[data[0] == eventdays[j], 3].sum()
                    else:
                        self.detailed_overtopping_right.loc[
                            eventdays[j], floodedSubs[i]
                        ] = 0
            except:
                self.detailed_overtopping_right.loc[eventdays[j], floodedSubs[i]] = 0
                continue

        # sum overtopping for each day
        for j in range(len(eventdays)):
            self.detailed_overtopping_left.loc[
                eventdays[j], "sum"
            ] = self.detailed_overtopping_left.loc[eventdays[j], :].sum()
            self.detailed_overtopping_right.loc[
                eventdays[j], "sum"
            ] = self.detailed_overtopping_right.loc[eventdays[j], :].sum()
        # sum overtopping for each sub basin
        for j in range(len(floodedSubs)):
            self.detailed_overtopping_left.loc[
                "sum", floodedSubs[j]
            ] = self.detailed_overtopping_left.loc[:, floodedSubs[j]].sum()
            self.detailed_overtopping_right.loc[
                "sum", floodedSubs[j]
            ] = self.detailed_overtopping_right.loc[:, floodedSubs[j]].sum()

        # self.detailed_overtopping_left.loc['sum','sum'] = self.detailed_overtopping_left.loc[:,'sum'].sum()
        # self.detailed_overtopping_right.loc['sum','sum'] = self.detailed_overtopping_right.loc[:,'sum'].sum()

    def coordinates(self, Bankful=False):
        """Coordinates.

        Coordinates method calculate the real coordinates for all the vortixes
        of the cross section

        Parameters
        ----------
            Bankful : [Bool], optional
                if the cross section data has a bankful depth or not. The default is False.

        Returns
        -------
            1-coordenates will be added to the "crosssection" attribute.
        """
        if Bankful:
            self.cross_sections = self.cross_sections.assign(
                x1=0,
                y1=0,
                z1=0,
                x2=0,
                y2=0,
                z2=0,
                x3=0,
                y3=0,
                z3=0,
                x4=0,
                y4=0,
                z4=0,
                x5=0,
                y5=0,
                z5=0,
                x6=0,
                y6=0,
                z6=0,
                x7=0,
                y7=0,
                z7=0,
                x8=0,
                y8=0,
                z8=0,
            )

            for i in range(len(self.cross_sections)):
                inputs = self.cross_sections.loc[
                    i, list(self.cross_sections.columns)[3:15]
                ].tolist()
                dbf = self.cross_sections.loc[i, list(self.cross_sections.columns)[16]]

                outputs = self.getCoordinates(inputs, dbf)

                self.cross_sections.loc[
                    i, ["x1", "x2", "x3", "x4", "x5", "x6", "x7", "x8"]
                ] = outputs[0]

                self.cross_sections.loc[
                    i, ["y1", "y2", "y3", "y4", "y5", "y6", "y7", "y8"]
                ] = outputs[1]

                self.cross_sections.loc[
                    i, ["z1", "z2", "z3", "z4", "z5", "z6", "z7", "z8"]
                ] = outputs[2]
        else:
            self.cross_sections = self.cross_sections.assign(
                x1=0,
                y1=0,
                z1=0,
                x2=0,
                y2=0,
                z2=0,
                x3=0,
                y3=0,
                z3=0,
                x4=0,
                y4=0,
                z4=0,
                x5=0,
                y5=0,
                z5=0,
                x6=0,
                y6=0,
                z6=0,
            )
            dbf = False
            for i in range(len(self.cross_sections)):
                inputs = self.cross_sections.loc[
                    i, list(self.cross_sections.columns)[3:15]
                ].tolist()

                outputs = self.getCoordinates(inputs, dbf)

                self.cross_sections.loc[
                    i, ["x1", "x2", "x3", "x4", "x5", "x6"]
                ] = outputs[0]

                self.cross_sections.loc[
                    i, ["y1", "y2", "y3", "y4", "y5", "y6"]
                ] = outputs[1]

                self.cross_sections.loc[
                    i, ["z1", "z2", "z3", "z4", "z5", "z6"]
                ] = outputs[2]

        # TODO create a method to take the created coordinates and convert each cross section
        # into  a polygon
        # TODO another method to take the cross section coordinates of a whole sub basins
        # and convert them into one polygon

    # def CreatePolygons(self):

    @staticmethod
    def polygonGeometry(Coords):
        """PolygonGeometry.

        PolygonGeometry method calculates the area and perimeter of some coordinates

        Parameters
        ----------
            1-Coords : [array]
                numpy array in the shape of (n*2) where n is the number of points

        Returns
        -------
            1-area : [float]
                area between the coordinates.
            2-peri : [float]
                perimeter between the coordinates.

        Example
        -------
            coords = np.array([[0,1],[0,0],[5,0],[5,1]])
            RV.River.PolygonGeometry(coords)
        """
        area = 0.0
        peri = 0.0
        for i in range(np.shape(Coords)[0] - 1):
            area = (
                area + Coords[i, 0] * Coords[i + 1, 1] - Coords[i + 1, 0] * Coords[i, 1]
            )
            peri = (
                peri
                + (
                    (Coords[i + 1, 0] - Coords[i, 0]) ** 2
                    + (Coords[i + 1, 1] - Coords[i, 1]) ** 2
                )
                ** 0.5
            )
        area = (
            area
            + Coords[np.shape(Coords)[0] - 1, 0] * Coords[0, 1]
            - Coords[0, 0] * Coords[np.shape(Coords)[0] - 1, 1]
        )
        area = area * 0.5

        return area, peri

    @staticmethod
    def polyArea(Coords):
        """PolyArea.

        PolyArea method calculates the the area between given coordinates

        Parameters
        ----------
            1-Coords : [array]
                numpy array in the shape of (n*2) where n is the number of points

        Returns
        -------
            1-area : [float]
                area between the coordinates.

        Example:
        -------
            coords = np.array([[0,1],[0,0],[5,0],[5,1]])
            River.PolyArea(coords)
        """
        Coords = np.array(Coords)
        area = 0.0
        for i in range(np.shape(Coords)[0] - 1):
            # cros multiplication
            area = (
                area + Coords[i, 0] * Coords[i + 1, 1] - Coords[i + 1, 0] * Coords[i, 1]
            )
        area = (
            area
            + Coords[np.shape(Coords)[0] - 1, 0] * Coords[0, 1]
            - Coords[0, 0] * Coords[np.shape(Coords)[0] - 1, 1]
        )
        area = area * 0.5

        return area

    @staticmethod
    def polyPerimeter(Coords):
        """PolyPerimeter.

        PolyPerimeter method calculates the the perimeter between given coordinates

        Parameters
        ----------
            1-Coords : [array]
                numpy array in the shape of (n*2) where n is the number of points

        Returns
        -------
            2-peri : [float]
                perimeter between the coordinates.

        Example
        -------
            coords = np.array([[0,1],[0,0],[5,0],[5,1]])
            RV.River.PolyPerimeter(coords)
        """
        peri = 0.0
        for i in range(np.shape(Coords)[0] - 1):
            # next point coord - current point coord
            peri = (
                peri
                + (
                    (Coords[i + 1, 0] - Coords[i, 0]) ** 2
                    + (Coords[i + 1, 1] - Coords[i, 1]) ** 2
                )
                ** 0.5
            )

        return peri

    @staticmethod
    def getCoordinates(XSGeometry, dbf):
        """GetCoordinates.

        GetCoordinates calculates the coordinates of all the points (vortices)
        of the cross section

        Parameters
        ----------
            1- BedLevel : [Float]
                DESCRIPTION.
            2- BankLeftLevel : [Float]
                DESCRIPTION.
            3- BankRightLevel : [Float]
                DESCRIPTION.
            4- InterPLHeight : [Float]
                Intermediate point left.
            5- InterPRHeight : [Float]
                Intermediate point right.
            6- Bl : [Float]
                DESCRIPTION.
            7- Br : [Float]
                DESCRIPTION.
            8- xl : [Float]
                DESCRIPTION.
            9- yl : [Float]
                DESCRIPTION.
            10- xr : [Float]
                DESCRIPTION.
            11- yr : [Float]
                DESCRIPTION.
            12- B : [Float]
                DESCRIPTION.
            13- dbf : [Float/Bool]
                DESCRIPTION.

        Returns
        -------
        Xcoords : [List]
            DESCRIPTION.
        Xcoords : [List]
            DESCRIPTION.
        Zcoords : [List]
            DESCRIPTION.
        """
        BedLevel = XSGeometry[0]
        BankLeftLevel = XSGeometry[1]
        BankRightLevel = XSGeometry[2]
        InterPLHeight = XSGeometry[3]
        InterPRHeight = XSGeometry[4]
        Bl = XSGeometry[5]
        Br = XSGeometry[6]
        xl = XSGeometry[7]
        yl = XSGeometry[8]
        xr = XSGeometry[9]
        yr = XSGeometry[10]
        B = XSGeometry[11]

        Xcoords = list()
        Ycoords = list()
        Zcoords = list()
        # point 1
        Xcoords.append(xl)
        Ycoords.append(yl)
        Zcoords.append(BankLeftLevel)
        # 8 points cross sections
        if dbf:
            # point 2
            Xcoords.append(xl)
            Ycoords.append(yl)
            Zcoords.append(BedLevel + dbf + InterPLHeight)
            # point 3
            Xcoords.append(xl + (Bl / (Bl + Br + B)) * (xr - xl))
            Ycoords.append(yl + (Bl / (Bl + Br + B)) * (yr - yl))
            Zcoords.append(BedLevel + dbf)
            # point 4
            Xcoords.append(xl + (Bl / (Bl + Br + B)) * (xr - xl))
            Ycoords.append(yl + (Bl / (Bl + Br + B)) * (yr - yl))
            Zcoords.append(BedLevel)
            # point 5
            Xcoords.append(xl + ((Bl + B) / (Bl + Br + B)) * (xr - xl))
            Ycoords.append(yl + ((Bl + B) / (Bl + Br + B)) * (yr - yl))
            Zcoords.append(BedLevel)
            # point 6
            Xcoords.append(xl + ((Bl + B) / (Bl + Br + B)) * (xr - xl))
            Ycoords.append(yl + ((Bl + B) / (Bl + Br + B)) * (yr - yl))
            Zcoords.append(BedLevel + dbf)
            # point 7
            Xcoords.append(xr)
            Ycoords.append(yr)
            Zcoords.append(BedLevel + dbf + InterPRHeight)
        else:
            # point 2
            Xcoords.append(xl)
            Ycoords.append(yl)
            Zcoords.append(BedLevel + InterPLHeight)
            # point 3
            Xcoords.append(xl + (Bl / (Bl + Br + B)) * (xr - xl))
            Ycoords.append(yl + (Bl / (Bl + Br + B)) * (yr - yl))
            Zcoords.append(BedLevel)
            # point 4
            Xcoords.append(xl + ((Bl + B) / (Bl + Br + B)) * (xr - xl))
            Ycoords.append(yl + ((Bl + B) / (Bl + Br + B)) * (yr - yl))
            Zcoords.append(BedLevel)
            # point 5
            Xcoords.append(xr)
            Ycoords.append(yr)
            Zcoords.append(BedLevel + InterPRHeight)

        # point 8
        Xcoords.append(xr)
        Ycoords.append(yr)
        Zcoords.append(BankRightLevel)

        return Xcoords, Ycoords, Zcoords

    @staticmethod
    def getVortices(H, Hl, Hr, Bl, Br, B, dbf):
        """GetVortices.

        GetCoordinates calculates the coordinates of all the points (vortices)
        of the cross section

        Parameters
        ----------
            1- H:[Float]
                water depth
            4- InterPLHeight : [Float]
                Intermediate point right height above the bankfull level.
            5- InterPRHeight : [Float]
                Intermediate point right height above the bankfull level.
            6- Bl : [Float]
                DESCRIPTION.
            7- Br : [Float]
                DESCRIPTION.
            12- B : [Float]
                DESCRIPTION.
            13- dbf : [Float/Bool]
                DESCRIPTION.

        Returns
        -------
        Xcoords : [List]
            DESCRIPTION.
        Xcoords : [List]
            DESCRIPTION.
        Zcoords : [List]
            DESCRIPTION.
        """
        # left side slope  Horizontal: Vertical = 1:sl
        Sl = Hl / Bl
        # right side slope Horizontal: Vertical = 1:sr
        Sr = Hr / Br
        # put vertexes to the local coordination system
        Xcoords = list()
        Ycoords = list()

        if H <= dbf:
            # Point 1
            Xcoords.append(0)
            Ycoords.append(H)
            # Point 2
            Xcoords.append(0)
            Ycoords.append(0)
            # Point 3
            Xcoords.append(B)
            Ycoords.append(0)
            # Point 4
            Xcoords.append(B)
            Ycoords.append(H)
            # PropXS8P = PolygonGeometry(mp)
        elif H - dbf < min(Hl, Hr):
            Hnew = H - dbf
            # Trapizoidal cross section with 4 points
            # case 1
            # Point 1
            Xcoords.append(0)
            Ycoords.append(H)
            # Point 2
            Xcoords.append(Hnew / Sl)
            Ycoords.append(dbf)
            # Point 3
            Xcoords.append(Hnew / Sl)
            Ycoords.append(0)
            # Point 4
            Xcoords.append((Hnew / Sl) + B)
            Ycoords.append(0)
            # Point 5
            Xcoords.append((Hnew / Sl) + B)
            Ycoords.append(dbf)
            # Point 6
            Xcoords.append(Hnew / Sl + B + Hnew / Sr)
            Ycoords.append(H)
        elif H - dbf < max(Hl, Hr) and Hl < Hr:
            Hnew = H - dbf
            # the height of one of the slopes is higher than the water depth.
            # so the shape of the cross section is 5 points
            # case 2
            # Point 1
            Xcoords.append(0)
            Ycoords.append(H)
            # Point 2
            Xcoords.append(0)
            Ycoords.append(Hl + dbf)
            # Point 3
            Xcoords.append(Bl)
            Ycoords.append(dbf)
            # Point 4
            Xcoords.append(Bl)
            Ycoords.append(0)
            # Point 5
            Xcoords.append(Bl + B)
            Ycoords.append(0)
            # Point 6
            Xcoords.append(Bl + B)
            Ycoords.append(dbf)
            # Point 7
            Xcoords.append(Bl + B + Hnew / Sr)
            Ycoords.append(H)
        elif H - dbf < max(Hl, Hr) and Hl > Hr:
            Hnew = H - dbf
            # case 3
            # Point 1
            Xcoords.append(0)
            Ycoords.append(H)
            # Point 2
            Xcoords.append(Hnew / Sl)
            Ycoords.append(dbf)
            # Point 3
            Xcoords.append(Hnew / Sl)
            Ycoords.append(0)
            # Point 4
            Xcoords.append(Hnew / Sl + B)
            Ycoords.append(0)
            # Point 5
            Xcoords.append(Hnew / Sl + B)
            Ycoords.append(dbf)
            # Point 6
            Xcoords.append(Hnew / Sl + B + Br)
            Ycoords.append(Hr + dbf)
            # Point 7
            Xcoords.append(Hnew / Sl + B + Br)
            Ycoords.append(H)
        else:
            #       elif H - dbf  > max(Hl,Hr):
            # Hnew = H - dbf
            # the whole 6 points cross section
            # case 4
            # Point 1
            Xcoords.append(0)
            Ycoords.append(H)
            # Point 2
            Xcoords.append(0)
            Ycoords.append(Hl + dbf)
            # Point 3
            Xcoords.append(Bl)
            Ycoords.append(dbf)
            # Point 4
            Xcoords.append(Bl)
            Ycoords.append(0)
            # Point 5
            Xcoords.append(Bl + B)
            Ycoords.append(0)
            # Point 6
            Xcoords.append(Bl + B)
            Ycoords.append(dbf)
            # Point 7
            Xcoords.append(Bl + B + Br)
            Ycoords.append(Hr + dbf)
            # Point 8
            Xcoords.append(Bl + B + Br)
            Ycoords.append(H)
            # calculate the area & perimeter of the bankful area
            # area
            # PropXS8P(1) = PropXS8P(1) + (dbf * mw)
            # perimeter
            # PropXS8P(2) = PropXS8P(2) + (2*dbf)
        Coords = np.array([Xcoords, Ycoords]).transpose()

        return Coords

    def getRatingCurve(self, MaxH=20, interval=0.02, dx=500):
        """GetRatingCurve.

        calculate the depth coresponding to each discharge value for a given
        cross section using manning equation.

        Parameters
        ----------
        MaxH : TYPE, optional
            DESCRIPTION. The default is 20.
        interval : TYPE, optional
            DESCRIPTION. The default is 0.02.
        dx : TYPE, optional
            DESCRIPTION. The default is 500.

        Returns
        -------
        None.
        """
        So = self.slope / dx
        # Rating Curve
        geom = self.cross_sections.loc[self.cross_sections.index[0], :]
        # 0  1   2   3  4 5  6  7  8  9  10 11 12 13 14 15
        "id,xsid,gl,zl,zr,hl,hr,bl,br,xl,yl,xr,yr,b,m,dbf"

        Nint = int(
            (max(geom["zl"] - geom["gl"], geom["zr"] - geom["gl"]) + MaxH) / interval
        )

        Table = np.zeros(shape=(Nint, 10))
        HQ = np.zeros(shape=(Nint, 2))

        for i in range(Nint):
            Table[i, 0] = interval * (i + 1)
            # calculate area & perimeter
            Coords = self.getVortices(
                Table[i, 0],
                geom["hl"],
                geom["hr"],
                geom["bl"],
                geom["br"],
                geom["b"],
                geom["dbf"],
            )
            Table[i, 1:3] = self.polygonGeometry(Coords)

            # area & perimeter of the Upper part only
            if Table[i, 0] <= geom["dbf"]:
                Table[i, 3] = 0
                Table[i, 4] = 0
            else:
                # area of upper part only
                Table[i, 3] = Table[i, 1] - geom["dbf"] * geom["b"]
                # perimeter of upper part
                Table[i, 4] = Table[i, 2] - 2 * geom["dbf"] - geom["b"]

            # area & perimeter of the lower part only
            Table[i, 5] = Table[i, 1] - Table[i, 3]
            Table[i, 6] = Table[i, 2] - Table[i, 4]

            # Discharge of Upper & lower
            if Table[i, 0] <= geom["dbf"]:
                Table[i, 7] = 0
            else:
                Table[i, 7] = Table[i, 3] * ((Table[i, 3] / Table[i, 4]) ** (2.0 / 3.0))

            Table[i, 8] = Table[i, 5] * ((Table[i, 5] / Table[i, 6]) ** (2.0 / 3.0))

            Table[i, 7] = (1.0 / geom["m"]) * Table[i, 7] * (abs(So) ** 0.5)
            Table[i, 8] = (1.0 / geom["m"]) * Table[i, 8] * (abs(So) ** 0.5)

            # total discharge
            Table[i, 9] = Table[i, 7] + Table[i, 8]

        HQ[:, 0] = Table[:, 0]
        HQ[:, 1] = Table[:, 9]

        self.HQ = HQ[:, :]

    def getDays(self, from_day: int, to_day: int):
        """getDays.

        GetDays method check if input days exist in the 1D result data
        or not since RIM1.0 simulate only days where discharge is above
        a certain value (2 years return period), you have to enter the
        one_d_result_path attribute of the instance first to read the results of
        the given sub-basin

        Parameters
        ----------
            1-from_day : [integer]
                the day you want to read the result from.
            2-to_day : [integer]
                the day you want to read the result to.

        Returns
        -------
            1-Message stating whether the given days exist or not, and if not two
            alternatives are given instead (the earliest day before the given day
                                            and the earliest day after the given
                                            day).
        """
        data = pd.read_csv(
            rf"{self.one_d_result_path}\{self.id}.txt", header=None, delimiter=r"\s+"
        )
        data.columns = ["day", "hour", "xs", "q", "h", "wl"]
        days = list(set(data["day"]))
        days.sort()

        if from_day not in days:
            Alt1 = from_day

            stop = 0
            # search for the from_day in the days column
            while stop == 0:
                try:
                    np.where(data["day"] == Alt1)[0][0]  # loc =
                    stop = 1
                except:
                    Alt1 = Alt1 - 1
                    # logger.debug(Alt1)
                    if Alt1 <= 0:
                        stop = 1
                    continue

            Alt2 = from_day
            # from_day =
            # search for closest later days
            stop = 0
            while stop == 0:
                # for i in range(0,10):
                try:
                    np.where(data["day"] == Alt2)[0][0]  # loc =
                    stop = 1
                except:
                    Alt2 = Alt2 + 1
                    # logger.debug(Alt2)
                    if Alt2 >= data.loc[len(data) - 1, "day"]:
                        stop = 1
                    continue

            text = (
                """"
            the from_day you entered does not exist in the data, and the closest day earlier than your input day is
            """
                + str(Alt1)
                + """  and the closest later day is """
                + str(Alt2)
            )
            logger.debug(text)

            if abs(Alt1 - from_day) > abs(Alt2 - from_day):
                Alt1 = Alt2
        else:
            logger.debug("from_day you entered does exist in the data ")
            # Alt1 = False
            Alt1 = from_day

        # if to_day does not exist in the results
        if to_day not in days:
            Alt3 = to_day

            stop = 0
            # search for the to_day in the days column
            while stop == 0:
                # for i in range(0,10):
                try:
                    np.where(data["day"] == Alt3)[0][0]  # loc =
                    stop = 1
                except:
                    Alt3 = Alt3 - 1
                    # logger.debug(Alt1)
                    if Alt3 <= 0:
                        stop = 1
                    continue

            Alt4 = to_day
            # from_day =
            # search for closest later days
            stop = 0
            while stop == 0:
                # for i in range(0,10):
                try:
                    np.where(data["day"] == Alt4)[0][0]  # loc =
                    stop = 1
                except:
                    Alt4 = Alt4 + 1
                    # logger.debug(Alt2)
                    if Alt4 >= data.loc[len(data) - 1, "day"]:
                        Alt4 = data.loc[len(data) - 1, "day"]
                        stop = 1
                    continue
            # Alt3 = [Alt3, Alt4]
            text = (
                """"
            the to_day you entered does not exist in the data, and the closest day earlier than your input day is
            """
                + str(Alt3)
                + """  and the closest later day is """
                + str(Alt4)
            )
            logger.debug(text)

            if abs(Alt3 - to_day) > abs(Alt4 - to_day):
                Alt3 = Alt4

        else:
            logger.debug("to_day you entered does exist in the data ")
            # Alt3 = False
            Alt3 = to_day

        return Alt1, Alt3

    @staticmethod
    def correctMaps(DEMpath, Filelist, Resultpath, MapsPrefix, FilterValue, Saveto):
        """CorrectMaps.

        CorrectMaps method check every 2D result that starts with the given Mapsprefix
        and replace the Nan value with zeros and the values higher than 99 with zeros

        Parameters
        ----------
        DEMpath : [String]
            path to the DEM ascii file including the name and extension
            (i.e., c/files/RhineDEM.asc) .
        Filelist : [String]
            - if you have a list of files to correct enter the Filelist as the path to the file
            containing the names
            ex,
                Filelist = "F:/RFM/RIM_all/RIM1.0/M35(done)/errorlist.txt"

            - if you want to check all the files in the resultpath enter the
            Filelist as '0'
            ex,
                Filelist = '0'
        Resultpath : [String]
            path where the Maps exist.
        MapsPrefix : [String]
            the name prefix that distinguish the maps you want to correct from
            other maps in the same folder, like the first part of the name you
            use to name all files.
        FilterValue: []

        Saveto : [String]
            path to where you will save the corrected files.

        Returns
        -------
        Errors : [list]
            list of the files' names that has errors and are already corrected.
        """
        DEM, SpatialRef = raster.readASCII(DEMpath)
        NoDataValue = SpatialRef[-1]

        # filter and get the required maps
        if Filelist == "0":
            # read list of file names
            AllResults = os.listdir(Resultpath)

            MapsNameList = list()
            for i in range(len(AllResults)):
                if AllResults[i].startswith(MapsPrefix):
                    MapsNameList.append(AllResults[i])
        elif type(Filelist) == str:
            MapsNameList = pd.read_csv(Filelist, header=None)[0].tolist()

        Errors = list()

        for k in range(len(MapsNameList)):
            try:
                # open the zip file
                compressedfile = zipfile.ZipFile(Resultpath + "/" + MapsNameList[k])
            except:
                logger.debug("Error Opening the compressed file")
                Errors.append(MapsNameList[k][len(MapsPrefix) : -4])
                continue

            # get the file name
            fname = compressedfile.infolist()[0]
            # get the time step from the file name
            timestep = int(fname.filename[len(MapsPrefix) : -4])
            logger.debug("File No = " + str(k))

            ASCIIF = compressedfile.open(fname)
            SpatialRef = ASCIIF.readlines()[:6]
            ASCIIF = compressedfile.open(fname)
            ASCIIRaw = ASCIIF.readlines()[6:]
            rows = len(ASCIIRaw)
            cols = len(ASCIIRaw[0].split())
            MapArray = np.ones((rows, cols), dtype=np.float32) * 0
            # read the ascii file
            for i in range(rows):
                x = ASCIIRaw[i].split()
                MapArray[i, :] = list(map(float, x))

            Save = 0
            # Clip all maps
            if MapArray[DEM == NoDataValue].max() > 0:
                MapArray[DEM == NoDataValue] = 0
                Save = 1
            # replace nan values with zero
            if len(MapArray[np.isnan(MapArray)]) > 0:
                MapArray[np.isnan(MapArray)] = 0
                Save = 1
            # replace FilterValue in the result raster with 0
            if len(MapArray[MapArray >= FilterValue]) > 0:
                MapArray[MapArray >= FilterValue] = 0
                Save = 1

            if Save == 1:
                logger.debug("File= " + str(timestep))
                # write the new file
                fname = MapsPrefix + str(timestep) + ".asc"
                newfile = Saveto + "/" + fname

                with open(newfile, "w") as File:
                    # write the first lines
                    for i in range(len(SpatialRef)):
                        File.write(str(SpatialRef[i].decode()[:-2]) + "\n")

                    for i in range(rows):
                        File.writelines(list(map(raster.stringSpace, MapArray[i, :])))
                        File.write("\n")

                # zip the file
                with zipfile.ZipFile(
                    Saveto + "/" + fname[:-4] + ".zip", "w", zipfile.ZIP_DEFLATED
                ) as newzip:
                    newzip.write(Saveto + "/" + fname, arcname=fname)
                # delete the file
                os.remove(Saveto + "/" + fname)

        return Errors

    def listAttributes(self):
        """ListAttributes.

        Print Attributes List
        """
        logger.debug("\n")
        logger.debug(
            f"Attributes List of: {repr(self.__dict__['name'])} - {self.__class__.__name__} Instance\n"
        )
        self_keys = list(self.__dict__.keys())
        self_keys.sort()
        for key in self_keys:
            if key != "name":
                logger.debug(str(key) + " : " + repr(self.__dict__[key]))

        logger.debug("\n")


class Reach(River):
    """Reach segment object.

    represent a segment of the river to create the Reach instance the
    river object has to have the cross-sections read using the
    'ReadCrossSections' method
    """

    reach_attr = dict(
        extracted_values=dict(),
        xs_hydrograph=None,
        neg_qmin=None,
        Negative=None,
        xs_water_level=None,
        xs_water_depth=None,
        RRM=None,
        RRM2=None,
        resampled_q=None,
        resampled_wl=None,
        resampled_h=None,
        Qrp=None,
        detailed_overtopping_left=None,
        detailed_overtopping_right=None,
        all_overtopping_vs_xs=None,
        all_overtopping_vs_time=None,
        BC=None,
        area_per_high=None,
        area_per_Low=None,
        total_flow=None,
        rrm_progression=None,
        laterals_table=None,
        Laterals=None,
        results_1d=None,
        us_hydrographs=None,
    )

    @class_attr_initialize(reach_attr)
    def __init__(self, sub_id: int, River, run_model: bool = False, *args, **kwargs):
        # initializa the attributes with the river attributes
        for key, val in River.__dict__.items():
            setattr(self, key, val)

        self.id = sub_id

        if not isinstance(River.cross_sections, DataFrame):
            raise ValueError(
                "please Read the cross section for the whole river with 'ReadCrossSections' "
                "method before creating the sub-segment instance"
            )
        # filter the whole cross section file and get the cross section of the segment
        self.cross_sections = River.cross_sections[River.cross_sections["id"] == sub_id]
        self._getXS(run_model=run_model)

        if isinstance(River.slope, DataFrame) and self.id in River.slope["id"].tolist():
            self.slope = River.slope[River.slope["id"] == sub_id]["slope"].tolist()[0]

        if isinstance(River.rivernetwork, DataFrame):
            self.usnode, self.dsnode = River.traceSegment(sub_id)
        else:
            self.usnode, self.dsnode = [], []

        if isinstance(River.RP, DataFrame):
            self.RP = River.RP.loc[
                River.RP["node"] == self.usnode, ["HQ2", "HQ10", "HQ100"]
            ]

        if isinstance(River.SP, DataFrame):
            self.SP = River.SP.loc[River.SP["id"] == self.id, :]
            self.SP.index = list(range(len(self.SP)))

    def _getXS(self, run_model: bool):
        """Get the cross sections of the current river reach.

        Parameters
        ----------
        run_model: [bool]
            If True the values (as array) for each attribute of the cross section will be stored in the reach object

        Returns
        -------
        cross_sections: [DataFrame]
            Replaces the cross_sections attributes in the reach object from the whole river cross sections
            to the cross section of the current reach only
        last_xs: [int]
            the id of the last cross section
        first_xs: [int]
            the id of the last cross section
        xs_names: [List]
            list of current reach cross sections id
        xsno: [int]
            number of cross sections in the current river reach
        """
        if run_model:
            self.xsid = self.cross_sections.loc[:, "xsid"].values
            self.dbf = self.cross_sections.loc[:, "dbf"].values
            self.bedlevel = self.cross_sections.loc[:, "gl"].values
            self.hl = self.cross_sections.loc[:, "hl"].values
            self.cl = self.cross_sections.loc[:, "bl"].values
            self.zl = self.cross_sections.loc[:, "zl"].values
            self.hr = self.cross_sections.loc[:, "hr"].values
            self.cr = self.cross_sections.loc[:, "br"].values
            self.zr = self.cross_sections.loc[:, "zr"].values
            self.mw = self.cross_sections.loc[:, "b"].values
            self.mn = self.cross_sections.loc[:, "m"].values

        self.cross_sections.index = list(range(len(self.cross_sections)))
        self.last_xs = self.cross_sections.loc[len(self.cross_sections) - 1, "xsid"]
        self.first_xs = self.cross_sections.loc[0, "xsid"]
        self.xs_names = self.cross_sections["xsid"].tolist()
        self.xsno = len(self.xs_names)

    def read1DResult(
        self,
        from_day: Union[int, str] = None,
        to_day: Union[int, str] = None,
        fill_missing: bool = True,
        addHQ2: bool = False,
        path: str = None,
        xsid: int = None,
        chunk_size: int = None,
        extension: str = ".txt",
    ):
        """read1DResult.

        - Read1DResult method reads the 1D result of the river reach the method is returns the hydrograph of the first
        and last cross section.
        - the method will not read the 1D result file again if you tried to read results of the same sub-basin again,
        so you have to re-instantiate the object.

        Parameters
        ----------
        from_day : [integer], optional
            the order of the day you want the data to start from.
            The default is None. it means read everything
        to_day : [integer], optional
            the order of the day you want the data to end to. The default
            is empty. means read everything
        fill_missing : [Bool], optional
            Fill the missing days with zeroes. The default is True.
        addHQ2 : [Bool], optional
            to add the value of HQ2. The default is False.
        path : [String], optional
            path to read the results from. The default is None.
        xsid : [Integer], optional
            id of a specific cross section you want to extract the results for
            it. The default is None.
        chunk_size: [int]
            size of the chunk if you want to read the file in chunks Default is = None.
        extension: [str]
            The extension of the file. Default is ".txt"

        Returns
        -------
        results_1d : [attribute]
            The results read from the file as is, will be stored in the attribute "results_1d"
        xs_hydrograph : [dataframe attribute]
            dataframe containing hydrographs at the position of the first
            and last cross section
        xs_water_level : [dataframe attribute]
            dataframe containing waterlevels at the position of the first
            and last cross section
        first_day_results:[attribute]
            the first day in the 1D result
        last_day:[attribute]
            the last day in the 1D result
        """
        if path is None and self.one_d_result_path == "":
            raise ValueError(
                "User have to either enter the value of the 'path' parameter or"
                " define the 'one_d_result_path' parameter for the River object"
            )
        # if the results are not read yet read it
        if not isinstance(self.results_1d, DataFrame):
            River.read1DResult(
                self,
                self.id,
                from_day,
                to_day,
                path=path,
                fill_missing=fill_missing,
                chunk_size=chunk_size,
                extension=extension,
            )
        # get the index of the days and convert them into  dates
        if not from_day:
            from_day = self.results_1d.loc[0, "day"]
        if not to_day:
            to_day = self.results_1d.loc[len(self.results_1d) - 1, "day"]

        start = self.indexToDate(from_day)
        end = self.indexToDate(to_day + 1)

        if not isinstance(self.xs_hydrograph, DataFrame):
            self.xs_hydrograph = pd.DataFrame(
                index=pd.date_range(start, end, freq="H")[:-1]
            )
            self.xs_water_level = pd.DataFrame(
                index=pd.date_range(start, end, freq="H")[:-1]
            )
            self.xs_water_depth = pd.DataFrame(
                index=pd.date_range(start, end, freq="H")[:-1]
            )

        # check if the xsid is in the sub-basin
        if xsid:
            if xsid not in self.xs_names:
                raise ValueError(
                    f"The given cross-section {xsid} does not exist inside the "
                    f"current Segment of the river, first XS is {self.first_xs}, and last "
                    f"XS is {self.last_xs}"
                )

        # get the simulated hydrograph and add the cutted HQ2
        if addHQ2:
            self.xs_hydrograph[self.last_xs] = (
                self.results_1d.loc[self.results_1d["xs"] == self.last_xs, "q"].values
                + self.RP["HQ2"].tolist()[0]
            )
            self.xs_hydrograph[self.first_xs] = (
                self.results_1d.loc[self.results_1d["xs"] == self.first_xs, "q"].values
                + self.RP["HQ2"].tolist()[0]
            )

            if xsid:
                self.xs_hydrograph[xsid] = (
                    self.results_1d.loc[self.results_1d["xs"] == xsid, "q"].values
                    + self.RP["HQ2"].tolist()[0]
                )
        else:
            self.xs_hydrograph[self.last_xs] = self.results_1d.loc[
                self.results_1d["xs"] == self.last_xs, "q"
            ].values
            self.xs_hydrograph[self.first_xs] = self.results_1d.loc[
                self.results_1d["xs"] == self.first_xs, "q"
            ].values
            if xsid:
                self.xs_hydrograph[xsid] = self.results_1d.loc[
                    self.results_1d["xs"] == xsid, "q"
                ].values

        self.xs_water_level[self.last_xs] = self.results_1d.loc[
            self.results_1d["xs"] == self.last_xs, "wl"
        ].values
        self.xs_water_level[self.first_xs] = self.results_1d.loc[
            self.results_1d["xs"] == self.first_xs, "wl"
        ].values

        self.xs_water_depth[self.last_xs] = self.results_1d.loc[
            self.results_1d["xs"] == self.last_xs, "h"
        ].values
        self.xs_water_depth[self.first_xs] = self.results_1d.loc[
            self.results_1d["xs"] == self.first_xs, "h"
        ].values

        if xsid:
            self.xs_water_level[xsid] = self.results_1d.loc[
                self.results_1d["xs"] == xsid, "wl"
            ].values
            self.xs_water_depth[xsid] = self.results_1d.loc[
                self.results_1d["xs"] == xsid, "h"
            ].values

        # check the first day in the results and get the date of the first day and last day
        ## create time series
        self.from_beginning = self.results_1d["day"][0]
        self.first_day = self.indexToDate(self.from_beginning)
        # if there are empty days at the beginning the filling missing days is
        # not going to detect it so ignore it here by starting from the first
        # day in the data (data['day'][0]) dataframe empty days at the
        # beginning
        # TODO
        # the from_beginning and first_day_results are exactly the same
        # delete one of them
        self.first_day_results = self.indexToDate(self.results_1d.loc[0, "day"])
        last_day = self.results_1d.loc[self.results_1d.index[-1], "day"]
        self.last_day = self.indexToDate(last_day)

        # last days+1 as range does not include the last element
        self.days_list = list(
            range(
                self.results_1d.loc[0, "day"],
                self.results_1d.loc[self.results_1d.index[-1], "day"] + 1,
            )
        )
        self.reference_index_results = pd.date_range(
            self.first_day_results, self.last_day, freq="D"
        )

    def extractXS(self, xsid: int, addHQ2: bool = False, WaterLevel: bool = True):
        """ExtractXS.

        ExtractXS method extracts the hydrodraph and water levels of a specific
        xsid from the already been read 1D results

        Parameters
        ----------
            1-xsid : [Integer], optional
                id of a specific cross section you want to get the results on it.
            2-addHQ2 : [Bool], optional
                to add the value of HQ2. The default is False.

        Returns
        -------
        None.
        """
        assert isinstance(
            self.results_1d, DataFrame
        ), "please use the Read1DResult method to read the results first"
        # assert hasattr(self,"RP"), "please use the Read1DResult method to read the results first"
        if addHQ2:
            self.xs_hydrograph[xsid] = (
                self.results_1d["q"][self.results_1d["xs"] == xsid].values
                + self.RP["HQ2"].tolist()[0]
            )
        else:
            self.xs_hydrograph[xsid] = self.results_1d["q"][
                self.results_1d["xs"] == xsid
            ].values

        if WaterLevel:
            self.xs_water_level[xsid] = self.results_1d["wl"][
                self.results_1d["xs"] == xsid
            ].values

    def CheckNegativeQ(self, plot: bool = False, TS: str = "hourly"):
        """CheckNegativeQ. CheckNegativeQ check whether there are any negative discharge values in the 'q' column in the 1D results or not, you need to read the result first.

        Returns
        -------
            1-Negative.[attribute]
                dictionary with ['NegQ', 'NegXS', 'NegQind'] as keys
        """
        if TS == "hourly":
            assert isinstance(self.results_1d, DataFrame), (
                "please use the results_1d method to read the "
                "result of this sub-basin first"
            )

            if self.results_1d["q"].min() < 0:
                logger.debug("NegativeDischarge")
                # extract -ve discharge data if exist
                self.Negative = dict()
                self.Negative["NegQ"] = self.results_1d[self.results_1d["q"] < 0]
                self.Negative["NegXS"] = list(set(self.Negative["NegQ"]["xs"]))
                self.Negative["NegQind"] = self.Negative["NegQ"].index.tolist()

                self.Negative["QN"] = pd.DataFrame()
                for i in range(len(self.Negative["NegXS"])):
                    self.Negative["QN"][self.Negative["NegXS"][i]] = self.results_1d[
                        "q"
                    ][self.results_1d["xs"] == self.Negative["NegXS"][i]]

                self.Negative["QN"].index = self.xs_hydrograph.index

                if plot:
                    plt.figure(30, figsize=(15, 8))
                    for i in range(len(self.Negative["NegXS"])):
                        plt.plot(self.Negative["QN"][self.Negative["NegXS"][i]])

                    plt.title("Discharge ", fontsize=25)
                    plt.legend(self.Negative["NegXS"], fontsize=15)
                    plt.xlabel("Time", fontsize=15)
                    plt.ylabel("Discharge m3/s", fontsize=15)

            else:
                logger.debug("There is no -ve Discharge")

        elif TS == "1min":
            assert hasattr(
                self, "q"
            ), "please use the results_1d method to read the result of this sub-basin first"
            # neg_qmin = pd.DataFrame()
            NegQmin = self.q
            NegQmin.loc[:, "date"] = self.q.index[:]
            NegQmin.index = range(len(NegQmin.index))
            f = NegQmin[NegQmin[self.xs_names[0]] < 0]

            for i in range(len(self.xs_names[1:])):
                f = f.append(NegQmin[NegQmin[self.xs_names[i + 1]] < 0])

            self.NegQmin = f

    def readRRMHydrograph(
        self,
        station_id: int,
        from_day: Union[int, str] = None,
        to_day: Union[int, str] = None,
        path: str = None,
        date_format: str = "%d_%m_%Y",
        location: int = 1,
        path2: str = None,
    ):
        """readRRMHydrograph.

            ReadHydrographs method reads the results of the Rainfall-runoff model for the given node id for
            a specific period.

        Parameters
        ----------
        station_id : [Integer]
            DESCRIPTION.
        from_day : [Integer], optional
            start day of the period you wanrt to read its results.
            The default is [].
        to_day : [Integer], optional
            end day of the period you wanrt to read its results.
            The default is [].
        path: [str]
            path to the directory where the result files. if not given the
            river.rrm_path should be given. default is ''
        date_format: [str]
            format of the date string, default is "%d_%m_%Y"
        location: [1]
            1 if there is results for the rrm at one location, 2 if the are
            results for the rrm at two locations. default is 1
        path2: [str]
            path where the results of the rrm at the second location, this
            parameter is needed only in case location=2. default is ''
        Returns
        -------
        RRM:[data frame attribute]
            containing the computational node and rainfall-runoff results
            (hydrograph)with columns ['id', Nodeid ]
        """
        if not isinstance(self.RRM, DataFrame):
            self.RRM = pd.DataFrame()

        if location == 2 and not isinstance(self.RRM2, DataFrame):
            # create a dataframe for the 2nd time series of the rainfall runoff
            # model at the second location
            self.RRM2 = pd.DataFrame()

        if not path:
            path = self.rrm_path

        if location == 2 and not path2:
            raise ValueError(
                "path2 argument has to be given for the location of the 2nd rainfall run-off time series"
            )

        if location == 1:
            self.RRM[station_id] = self._readRRMResults(
                self.version,
                self.rrm_reference_index,
                path,
                station_id,
                from_day,
                to_day,
                date_format,
            )[station_id].tolist()
        else:
            self.RRM[station_id] = self._readRRMResults(
                self.version,
                self.rrm_reference_index,
                path,
                station_id,
                from_day,
                to_day,
                date_format,
            )[station_id].tolist()
            try:
                self.RRM2[station_id] = self._readRRMResults(
                    self.version,
                    self.rrm_reference_index,
                    path2,
                    station_id,
                    from_day,
                    to_day,
                    date_format,
                )[station_id].tolist()
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"The directory you have given for the location 2 {path2}, is not correct "
                    f"please check"
                )

        logger.info("RRM time series for the gauge " + str(station_id) + " is read")

        if not from_day:
            from_day = 1
        if not to_day:
            to_day = len(self.RRM[station_id])

        start = self.rrm_reference_index.loc[from_day, "date"]
        end = self.rrm_reference_index.loc[to_day, "date"]

        if location == 1:
            self.RRM.index = pd.date_range(start, end, freq="D")
        else:
            self.RRM.index = pd.date_range(start, end, freq="D")
            self.RRM2.index = pd.date_range(start, end, freq="D")
        # get the simulated hydrograph and add the cutted HQ2

    def resample(
        self,
        xsid,
        ColumnName,
        from_day: Union[int, str] = "",
        to_day: Union[int, str] = "",
        Delete=False,
    ):
        """Resample. Resample method extract the value at the last hour of the dat.

        [hour == 24] from the 1D Result  file, for the discharge, water level,
        and water depth.

        Parameters
        ----------
        xsid : [Integer]
            cross-section id.
        ColumnName : [string]
            the column name you want to resample in the results1D. ColumnName
            could be 'q' for discharge, 'wl' for water level, and 'h' for
            water depth.
        from_day : [integer], optional
            starting day. The default is ''.
        to_day : [integer], optional
            end day. The default is ''.
        Delete : [boolen], optional
            to delete the previously resampled data frame to create another one.
            The default is False.

        Returns
        -------
        resampled_q, resampled_wl, resampled_h: [dataframe attribute]
            depends on the given ColumnName the attribute will be created,
            if 'q' the attribute will be resampled_q, and the same for "wl", and "H"
            and inside the resampled_q a column will be created with the given xsid
            containing the resampled valeus
        """
        assert hasattr(self, "results_1d"), "please read the 1D results"

        if from_day == "":
            from_day = self.results_1d.loc[0, "day"]
        if to_day == "":
            to_day = self.results_1d.loc[len(self.results_1d) - 1, "day"]

        # start = self.IndexToDate(from_day)
        # end = self.IndexToDate(to_day)

        # start = self.reference_index.loc[from_day,'date']
        # end = self.reference_index.loc[to_day,'date']

        ind = pd.date_range(
            self.indexToDate(from_day), self.indexToDate(to_day), freq="D"
        )

        if ColumnName == "q" and not hasattr(self, "resampled_q"):
            self.resampled_q = pd.DataFrame(index=ind)
        elif ColumnName == "q":
            if Delete:
                del self.resampled_q

        if ColumnName == "wl" and not hasattr(self, "resampled_wl"):
            self.resampled_wl = pd.DataFrame(index=ind)
        elif ColumnName == "wl":
            if Delete:
                del self.resampled_wl

        if ColumnName == "h" and not hasattr(self, "resampled_h"):
            self.resampled_h = pd.DataFrame(index=ind)
        elif ColumnName == "h":
            if Delete:
                del self.resampled_h

        Q = self.results_1d[self.results_1d["xs"] == xsid][
            self.results_1d["hour"] == 24
        ]
        Q = Q[ColumnName][self.results_1d["day"] >= from_day][
            self.results_1d["day"] <= to_day
        ]

        # self.Q = Q
        if ColumnName == "q":
            self.resampled_q.loc[:, xsid] = Q.tolist()
        elif ColumnName == "wl":
            self.resampled_wl.loc[:, xsid] = Q.tolist()
        elif ColumnName == "h":
            self.resampled_h.loc[:, xsid] = Q.tolist()

    def detailedStatisticalCalculation(self, T):
        """DetailedStatisticalCalculation.

            DetailedStatisticalCalculation method calculates the discharge related to a specific given return period.

        Parameters
        ----------
        T : TYPE
            DESCRIPTION.

        Returns
        -------
        None.
        """
        assert hasattr(self, "SP"), "you "
        F = 1 - (1 / T)
        self.Qrp = pd.DataFrame()
        self.Qrp["RP"] = T
        self.Qrp["Q"] = gumbel_r.ppf(
            F, loc=self.SP.loc[0, "loc"], scale=self.SP.loc[0, "scale"]
        )

    def detailedOvertopping(self, eventdays):
        """DetailedOvertopping. DetailedOvertopping method takes list of days and get the left and right overtopping for the sub-basin each day.

        Parameters
        ----------
            1-eventdays : [list]
                list od daysof an event.

        Returns
        -------
            1- detailed_overtopping_left:[data frame attribute]
                containing the computational node and rainfall-runoff results
                (hydrograph)with columns ['id', Nodeid ]
            2-detailed_overtopping_right:[data frame attribute]
                containing the computational node and rainfall-runoff results
                (hydrograph)with columns ['id', Nodeid ]
            3-all_overtopping_vs_xs:
            4-all_overtopping_vs_time:
        """
        # River.DetailedOvertopping(self, [self.id], eventdays)
        XSs = self.cross_sections.loc[:, "xsid"].tolist()
        columns = [self.id] + XSs + ["sum"]
        self.detailed_overtopping_left = pd.DataFrame(
            index=eventdays + ["sum"], columns=columns
        )
        self.detailed_overtopping_left.loc[:, columns] = 0
        self.detailed_overtopping_right = pd.DataFrame(
            index=eventdays + ["sum"], columns=columns
        )
        self.detailed_overtopping_right.loc[:, columns] = 0
        # Left Bank
        try:
            # try to open and read the overtopping file
            data = pd.read_csv(
                f"{self.one_d_result_path}{self.id}{self.left_over_topping_suffix}",
                header=None,
                delimiter=r"\s+",
            )

            data.columns = ["day", "hour", "xsid", "q", "wl"]
            # get the days in the sub
            days = list(set(data.loc[:, "day"]))

            for j in range(len(eventdays)):
                # check whether this sub basin has flooded in this particular day
                if eventdays[j] in days:
                    # filter the dataframe to the discharge column (3) and the days
                    self.detailed_overtopping_left.loc[
                        eventdays[j], self.id
                    ] = data.loc[data["day"] == eventdays[j], "q"].sum()
                    # get the xss that was overtopped in that particular day
                    XSday = list(
                        set(data.loc[data["day"] == eventdays[j], "xsid"].tolist())
                    )

                    for i in range(len(XSday)):
                        # dataXS = data['q'].loc[data['day'] == eventdays[j]][data['xsid'] == XSday[i]].sum()
                        self.detailed_overtopping_left.loc[eventdays[j], XSday[i]] = (
                            data["q"]
                            .loc[data["day"] == eventdays[j]][data["xsid"] == XSday[i]]
                            .sum()
                        )
                else:
                    self.detailed_overtopping_left.loc[eventdays[j], self.id] = 0
        except:
            self.detailed_overtopping_left.loc[:, self.id] = 0

        # right Bank
        try:
            # try to open and read the overtopping file
            data = pd.read_csv(
                rf"{self.one_d_result_path}\{self.id}{self.right_overtopping_suffix}",
                header=None,
                delimiter=r"\s+",
            )
            data.columns = ["day", "hour", "xsid", "q", "wl"]
            # get the days in the sub
            days = list(set(data.loc[:, "day"]))

            for j in range(len(eventdays)):
                # check whether this sub basin has flooded in this particular day
                if eventdays[j] in days:
                    # filter the dataframe to the discharge column (3) and the days
                    self.detailed_overtopping_right.loc[
                        eventdays[j], self.id
                    ] = data.loc[data["day"] == eventdays[j], "q"].sum()
                    # get the xss that was overtopped in that particular day
                    XSday = list(
                        set(data.loc[data["day"] == eventdays[j], "xsid"].tolist())
                    )

                    for i in range(len(XSday)):
                        # dataXS = data['q'].loc[data['day'] == eventdays[j]][data['xsid'] == XSday[i]].sum()
                        self.detailed_overtopping_right.loc[eventdays[j], XSday[i]] = (
                            data["q"]
                            .loc[data["day"] == eventdays[j]][data["xsid"] == XSday[i]]
                            .sum()
                        )

                else:
                    self.detailed_overtopping_right.loc[eventdays[j], self.id] = 0
        except:
            # logger.debug("file did not open")
            self.detailed_overtopping_right.loc[:, self.id] = 0

        # sum overtopping for each day
        for j in range(len(eventdays)):
            self.detailed_overtopping_left.loc[
                eventdays[j], "sum"
            ] = self.detailed_overtopping_left.loc[eventdays[j], XSs].sum()
            self.detailed_overtopping_right.loc[
                eventdays[j], "sum"
            ] = self.detailed_overtopping_right.loc[eventdays[j], XSs].sum()
        # sum overtopping for each sub basin
        for j in range(len(XSs)):
            self.detailed_overtopping_left.loc[
                "sum", XSs[j]
            ] = self.detailed_overtopping_left.loc[:, XSs[j]].sum()
            self.detailed_overtopping_right.loc[
                "sum", XSs[j]
            ] = self.detailed_overtopping_right.loc[:, XSs[j]].sum()

        self.detailed_overtopping_left.loc[
            "sum", self.id
        ] = self.detailed_overtopping_left.loc[:, self.id].sum()
        self.detailed_overtopping_right.loc[
            "sum", self.id
        ] = self.detailed_overtopping_right.loc[:, self.id].sum()

        self.all_overtopping_vs_xs = (
            self.detailed_overtopping_left.loc["sum", XSs]
            + self.detailed_overtopping_right.loc["sum", XSs]
        )

        self.all_overtopping_vs_time = pd.DataFrame()
        self.all_overtopping_vs_time["id"] = eventdays
        self.all_overtopping_vs_time.loc[:, "Overtopping"] = (
            self.detailed_overtopping_left.loc[eventdays, "sum"]
            + self.detailed_overtopping_right.loc[eventdays, "sum"]
        ).tolist()
        self.all_overtopping_vs_time.loc[:, "date"] = (
            self.reference_index.loc[eventdays[0] : eventdays[-1], "date"]
        ).tolist()

    def saveHydrograph(self, xsid: int, path: str = None, Option: int = 1):
        """Save Hydrograph.

            - SaveHydrograph method saves the hydrograph of any cross-section in the segment.
            - Mainly the method is created to to be used to save the last cross-section hydrograph to use it as as a
            boundary condition for the downstream segment.

        Parameters
        ----------
        xsid : [integer]
            the id of the cross section.
        path : [string], optional
            path to the directory where you want to save the file to. if not given
            the files are going to be saved in the 'customized_runs_path' path, The
            default is ''.
        Option : [integer]
            1 to write water depth results, 2 to write water level results

        Returns
        -------
        None.
        """
        if not path:
            if not self.customized_runs_path:
                raise ValueError(
                    "please enter the value of the customized_runs_path or use the path "
                    "argument to specify where to save the file"
                )
            path = self.customized_runs_path

        ts = self.xs_hydrograph[xsid].resample("D").last().to_frame()
        val = [self.xs_hydrograph[xsid][0]] + self.xs_hydrograph[xsid].resample(
            "D"
        ).last().values.tolist()[:-1]
        ts[xsid] = val

        f = pd.DataFrame(index=ts.index)
        f["date"] = ["'" + str(i)[:10] + "'" for i in ts.index]
        f["discharge(m3/s)"] = ts

        if Option == 1:
            val = [self.xs_water_depth[xsid][0]] + self.xs_water_depth[xsid].resample(
                "D"
            ).last().values.tolist()[:-1]
            f["water depth(m)"] = val
        else:
            val = [self.xs_water_level[xsid][0]] + self.xs_water_level[xsid].resample(
                "D"
            ).last().values.tolist()[:-1]
            f["water level(m)"] = val

        f.to_csv(f"{path}{self.id}.txt", index=False, float_format="%.3f")

    def plotHydrographProgression(
        self,
        xss: list,
        start: str = None,
        end: str = None,
        from_xs: int = None,
        to_xs: int = None,
        line_width: int = 4,
        spacing: int = 5,
        fig_size: tuple = (7, 5),
        xlabels: Union[bool, int] = False,
        fmt="%Y-%m-%d",
    ) -> Tuple[Figure, object]:
        """PlotHydrographProgression.

            - plot the hydrograph for several vross section in the segment, cross section are chosen based on the
            spacing (spacing equal 5 mean from the beginning take eavery fifth cross section)

        Parameters
        ----------
        xss : [list]
            DESCRIPTION.
        start : TYPE
            DESCRIPTION.
        end : TYPE
            DESCRIPTION.
        from_xs: [str, int]
            default "".
        to_xs: [str, int]
            default is ""
        line_width : [integer], optional
            width of the plots. The default is 4.
        spacing : [integer]
            hydrographs are going to be plots every spacing. The default is 5.
        fig_size: [tuple]
            default is (7, 5).
        xlabels: [bool, int]
            defaulr is False.
        fmt: [string]
            format of the date. fmt="%Y-%m-%d %H:%M:%S".

        Returns
        -------
        None.
        """
        if start is None:
            start = self.first_day
        else:
            start = dt.datetime.strptime(start, fmt)

        if end is None:
            end = self.last_day
        else:
            end = dt.datetime.strptime(end, fmt)

        if from_xs is None:
            from_xs = self.first_xs

        if to_xs is None:
            to_xs = self.last_xs
            xss.append(to_xs)

        from_xs = self.xs_names.index(from_xs)
        to_xs = self.xs_names.index(to_xs)
        xs_list = self.xs_names[from_xs : to_xs + 1 : spacing]

        xs_list = xs_list + xss

        # to remove repeated XSs
        xs_list = list(set(xs_list))
        # extract the XS hydrographs
        for i in range(len(xs_list)):
            self.read1DResult(xsid=xs_list[i])

        # xs_list = [self.first_xs] + xs_list + [self.last_xs]
        xs_list.sort()

        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=fig_size)

        for i in range(len(xs_list)):
            ax.plot(
                self.xs_hydrograph.loc[start:end, xs_list[i]],
                label=f"XS-{xs_list[i]}",
                linewidth=line_width,
            ),  # color = XScolor,zorder=XSorder

        ax.legend(fontsize=10, loc="best")
        ax.set_xlabel("Time", fontsize=10)
        ax.set_ylabel("Discharge m3/s", fontsize=10)
        if type(xlabels) != bool:
            start, end = ax.get_xlim()
            ax.xaxis.set_ticks(np.linspace(start, end, xlabels))

        plt.tight_layout()

        return fig, ax

    def readUSHydrograph(
        self,
        from_day: int = None,
        to_day: int = None,
        path: str = None,
        date_format: str = "'%Y-%m-%d'",
    ):
        """readUSHydrograph.

            Read the hydrograph of the upstream reaches.

        Parameters
        ----------
        from_day : [int], optional
                the day you want to read the result from, the first day is 1 not zero.The default is ''.
        to_day : [int], optional
                the day you want to read the result to.
        path : [str], optional
            path to read the results from. if path is not given the customized_runs_path
             attribute for the river instance should be given. The default is ''.
        date_format : "TYPE, optional
            DESCRIPTION. The default is "'%Y-%m-%d'".

        Returns
        -------
        us_hydrographs : [dataframe attribute].
            dataframe contains the hydrograph of each of the upstream reachs
            with segment id as a column name and a column 'total' contains the
            sum of all the hydrographs.
        """
        self.us_hydrographs = pd.DataFrame()

        if not path:
            path = self.customized_runs_path

        if len(self.usnode) > 1:
            # there is more than one upstream segment
            if isinstance(self.usnode, list):
                for i in range(len(self.usnode)):
                    Nodeid = self.usnode[i]
                    try:
                        self.us_hydrographs[Nodeid] = self._readRRMResults(
                            self.version,
                            self.rrm_reference_index,
                            path,
                            Nodeid,
                            from_day,
                            to_day,
                            date_format,
                        )[Nodeid]
                        logger.info(f"the US hydrograph '{Nodeid}' has been read")
                    except FileNotFoundError:
                        msg = (
                            f" the Path - {path} does not contain the routed hydrographs for the the "
                            f"segment - {Nodeid}"
                        )
                        logger.info(msg)
                        return

            # there is one upstream segment
        elif self.usnode:
            Nodeid = self.usnode[0]
            try:
                self.us_hydrographs[Nodeid] = self._readRRMResults(
                    self.version,
                    self.rrm_reference_index,
                    path,
                    Nodeid,
                    from_day,
                    to_day,
                    date_format,
                )[Nodeid]
                logger.info(f"the US hydrograph '{Nodeid}' has been read")
            except FileNotFoundError:
                logger.info(
                    f"The Path - {path} does not contain the routed hydrographs for the "
                    f"segment - {Nodeid}"
                )
                return
        else:
            logger.info(
                "the Segment Does not have any Upstream Segments, or you have "
                "not read the river network in the river instance"
            )
            return

        self.us_hydrographs["total"] = self.us_hydrographs.sum(axis=1)
        if not from_day:
            from_day = self.us_hydrographs.index[0]
        if not to_day:
            to_day = self.us_hydrographs.index[-1]

        start = self.reference_index.loc[from_day, "date"]
        end = self.reference_index.loc[to_day, "date"]

        self.us_hydrographs.index = pd.date_range(start, end, freq="D")

    def getUSHydrograph(self, River):
        """GetUSHydrograph. GetUSHydrograph methods gets the sum of all the upstream hydrographs whither it is routed inside the model or a boundary condition.

        Parameters
        ----------
        River : [object]
            the object of the river.

        Returns
        -------
        us_hydrographs : [array].
            array of the hydrograph
        """
        self.us_hydrographs = np.zeros(shape=River.no_time_steps)

        if len(self.usnode) > 1:
            # there is more than one upstream segment
            if type(self.usnode) == list:
                for i in range(len(self.usnode)):
                    Nodeid = self.usnode[i]
                    # get the order of the segment
                    River.Segments.index(Nodeid)
                    self.us_hydrographs = (
                        self.us_hydrographs
                        + River.routed_q[:, River.Segments.index(Nodeid)]
                    )
            # there is one upstream segment
        elif self.usnode:
            Nodeid = self.usnode[0]
            River.Segments.index(Nodeid)
            self.us_hydrographs = (
                self.us_hydrographs + River.routed_q[:, River.Segments.index(Nodeid)]
            )

        if type(self.BC) != bool:
            self.us_hydrographs = self.us_hydrographs + self.BC.values.reshape(
                len(self.us_hydrographs)
            )

    def getXSGeometry(self):
        """GetXSGeometry. calculate the area and  perimeter for the cross section highest and lowest point.

        Returns
        -------
        None.
        """
        AreaPerLow = np.zeros(shape=(self.xsno, 2))
        AreaPerHigh = np.zeros(shape=(self.xsno, 2))
        for i in range(self.xsno):
            geom = self.cross_sections.loc[i, :]
            H = min(geom["hl"], geom["hr"]) + geom["dbf"]
            Coords = self.getVortices(
                H,
                geom["hl"],
                geom["hr"],
                geom["bl"],
                geom["br"],
                geom["b"],
                geom["dbf"],
            )
            AreaPerLow[i, :] = self.polygonGeometry(Coords)
            H = max(geom["hl"], geom["hr"]) + geom["dbf"]
            Coords = self.getVortices(
                H,
                geom["hl"],
                geom["hr"],
                geom["bl"],
                geom["br"],
                geom["b"],
                geom["dbf"],
            )
            AreaPerHigh[i, :] = self.polygonGeometry(Coords)
        self.AreaPerHigh = AreaPerHigh[:, :]
        self.AreaPerLow = AreaPerLow[:, :]

    def getFlow(
        self,
        IF,
        from_day: Union[int, str] = "",
        to_day: Union[int, str] = "",
        date_format="%d_%m_%Y",
    ):
        """getFlow.

            Extract the lateral flow and boundary condition (if exist) time series of the segment from the whole
            river segment.

        Parameters
        ----------
        IF : [Interface object]
            You Have to create the interface object then read the laterals and the
            boundary conditions first.
        from_day : [string], optional
            the starting day. The default is ''.
        to_day : [string], optional
            the ending day. The default is ''.
        date_format : [string], optional
            the format of the given dates. The default is "%d_%m_%Y".

        Returns
        -------
        BC : [dataframe attribute].
            dataframe containing the boundary condition under a column by the name
            of the segment id.
        Laterals : [dataframe attribute].
            dataframe containing a column for each cross section that has a lateral.
        """
        if hasattr(IF, "BC"):
            if not isinstance(IF.BC, DataFrame):
                raise ValueError(
                    "The boundary condition does not exist you have to read it first using the "
                    "'ReadBoundaryConditions' method in the interface model"
                )
        if hasattr(IF, "Laterals"):
            if not isinstance(IF.Laterals, DataFrame):
                raise ValueError(
                    "The Laterals does not exist you have to read it first "
                    "using the 'ReadLaterals' method in the interface model"
                )

        if from_day == "":
            from_day = IF.BC.index[0]
        else:
            from_day = dt.datetime.strptime(from_day, date_format)

        if to_day == "":
            to_day = IF.BC.index[-1]
        else:
            to_day = dt.datetime.strptime(to_day, date_format)

        # get the id of the boundary condition
        xs_as_set = set(self.xs_names)
        bclist = [int(i) for i in IF.bc_table["xsid"].tolist()]
        bcids = list(xs_as_set.intersection(bclist))

        if len(bcids) == 0:
            self.BC = False
        elif len(bcids) > 1:
            raise ValueError("There are more than one BC for this Reach-basin")
        else:
            self.BC = IF.BC.loc[from_day:to_day, bcids[0]].to_frame()

        if len(IF.laterals_table) > 0:
            self.laterals_table = [
                value
                for value in self.xs_names
                if value in IF.laterals_table["xsid"].tolist()
            ]
            self.Laterals = pd.DataFrame(
                index=pd.date_range(from_day, to_day, freq="D"),
                columns=self.laterals_table,
            )

            for i in self.laterals_table:
                self.Laterals.loc[:, i] = IF.Laterals.loc[from_day:to_day, i]

            self.Laterals["total"] = self.Laterals.sum(axis=1)
            # if the rrm hydrograph at the location of the hm or at the location of the rrm is read
            if isinstance(IF.routed_rrm, DataFrame):
                self.rrm_progression = pd.DataFrame(
                    index=pd.date_range(from_day, to_day, freq="D"),
                    columns=self.laterals_table,
                )
                for i in self.laterals_table:
                    self.rrm_progression.loc[:, i] = IF.routed_rrm.loc[
                        from_day:to_day, i
                    ]
        else:
            self.laterals_table = []
            self.Laterals = pd.DataFrame()

    def getLaterals(self, xsid: int):
        """GetLaterals.

            GetLaterals method gets the sum of the laterals of all the cross sections in the reach upstream of a given xsid.

        Parameters
        ----------
        xsid : [integer]
            id of the cross section.

        Returns
        -------
        dataframe
            sum of the laterals of all the cross sections in the reach
            upstream of a given xsid.
        """
        if not isinstance(self.laterals_table, list) and not isinstance(
            self.Laterals, DataFrame
        ):
            raise ValueError("please read the Laterals Table and the Laterals first")

        USgauge = self.laterals_table[: bisect(self.laterals_table, xsid)]
        return self.Laterals[USgauge].sum(axis=1).to_frame()

    def getTotalFlow(self, gaugexs: int):
        """getTotalFlow.

            GetTotalFlow extracts all the laterals upstream of a certain xs and also extracts the Upstream/BC hydrograph.

        Parameters
        ----------
        gaugexs : [integer]
            id of the cross section.

        Returns
        -------
        total_flow : [dataframe attribute]
            dataframe containing the total upstream hydrograph for the location
            of the given xs, the column name is "total"
        """
        # Sum the laterals and the BC/US hydrograph
        if not isinstance(self.Laterals, DataFrame):
            raise ValueError("Please read the lateral flows first using the 'GetFlow'")

        if gaugexs not in self.xs_names:
            raise ValueError(
                f"The given XS {gaugexs} does not locate in the current river reach"
                f"First XS is {self.first_xs} and "
                f"Last XS is {self.last_xs}"
            )
        Laterals = self.getLaterals(gaugexs)
        try:
            s1 = Laterals.index[0]
            e1 = Laterals.index[-1]
        except IndexError:
            logger.info("there are no laterals for the given reach")
            return

        if isinstance(self.BC, DataFrame):
            s2 = self.BC.index[0]
            s = max(s1, s2)
            e2 = self.BC.index[-1]
            e = min(e1, e2)

            self.TotalFlow = pd.DataFrame(index=pd.date_range(s, e, freq="D"))
            self.TotalFlow.loc[s:e, "total"] = (
                Laterals.loc[s:e, 0].values
                + self.BC.loc[s:e, self.BC.columns[0]].values
            )
            logger.info(f"Total flow for the XS-{gaugexs} has been calculated")
        elif (
            isinstance(self.us_hydrographs, DataFrame) and len(self.us_hydrographs) > 0
        ):
            s2 = self.us_hydrographs.index[0]
            s = max(s1, s2)
            e2 = self.us_hydrographs.index[-1]
            e = min(e1, e2)

            self.TotalFlow = pd.DataFrame(index=pd.date_range(s, e, freq="D"))
            self.TotalFlow.loc[s:e, "total"] = (
                Laterals.loc[s:e, 0].values
                + self.us_hydrographs.loc[s:e, "total"].values
            )
            logger.info(f"Total flow for the XS-{gaugexs} has been calculated")
        else:
            logger.info(
                f"The US Hydrograph/BC of the given River reach-{self.id} is not read yet "
                "please use the 'ReadUSHydrograph' method to read it"
            )

    def H2Q(self, Q):
        """H2Q. H2Q method convert the discharge for a certain cross section into water depth using manning equation.

        Parameters
        ----------
        Q : TYPE
            DESCRIPTION.

        Returns
        -------
        H : TYPE
            DESCRIPTION.
        """
        H = np.zeros(shape=(len(Q)))

        for i in range(len(Q)):
            # if Qbnd >  calculated Q for the highest depth in the table
            # highest depth = (dike height + 15 m)
            if Q[i] > self.HQ[-1, 1]:
                # depth = highest depth
                H[i] = self.HQ[-1, 0]
                # if not calculate the Q for each discretized depth in the table
                # and take the one with the smallest difference from the q given
            else:
                qq = Q[i]
                diff = abs(qq - self.HQ[:, 1])
                H[i] = self.HQ[np.argmin(diff), 0]

        return H

    plot_discharge_args = dict(
        Calib={"type": Any},
        gaugexs={"type": int},
        start={"type": str},
        end={"type": str},
        stationname={"type": int},
        gaugename={"type": [str, int]},
        segment_xs={"type": str},
        plotlaterals={"type": bool, "default": True},
        latcolor={"type": [str, tuple], "default": (0.3, 0, 0)},
        latorder={"type": int, "default": 4},
        latstyle={"type": int, "default": 9},
        plotus={"type": bool, "default": True},
        ushcolor={"type": [str, tuple], "default": "grey"},
        ushorder={"type": int, "default": 7},
        ushstyle={"type": int, "default": 7},
        plottotal={"type": bool, "default": True},
        totalcolor={"type": [str, tuple], "default": "k"},
        totalorder={"type": int, "default": 6},
        totalstyle={"type": int, "default": 4},
        specificxs={"type": [bool, int], "default": False},
        xscolor={"type": [str, tuple], "default": (164 / 255, 70 / 255, 159 / 255)},
        xsorder={"type": int, "default": 1},
        xslinestyle={"type": int, "default": 3},
        plotrrm={"type": bool, "default": True},
        rrmcolor={"type": [str, tuple], "default": "green"},
        rrmorder={"type": int, "default": 3},
        rrmlinestyle={"type": int, "default": 6},
        rrm2color={"type": [str, tuple], "default": (227 / 255, 99 / 255, 80 / 255)},
        rrm2linesytle={"type": int, "default": 8},
        plotgauge={"type": bool, "default": True},
        gaugecolor={"type": [str, tuple], "default": "#DC143C"},
        gaugeorder={"type": int, "default": 5},
        gaugestyle={"type": int, "default": 7},
        hmcolor={"type": [str, tuple], "default": "#004c99"},
        hmorder={"type": int, "default": 6},
        linewidth={"type": int, "default": 4},
        figsize={"type": tuple, "default": (6, 5)},
        fmt={"type": str, "default": "%Y-%m-%d"},
        xlabels={"type": [bool, int, list], "default": False},
        ylabels={"type": [bool, int, list], "default": False},
        # plotRRMProgression
        plothm={"type": bool, "default": True},
        rrmlinesytle={"type": int, "default": 8},
        # plotWL
        hmstyle={"type": int, "default": 6},
        legendsize={"type": Union[int, float], "default": 15},
        nxlabels={"type": int, "default": 4},
    )

    @class_method_parse(plot_discharge_args)
    def plotQ(
        self,
        Calib,
        gaugexs: int,
        start: str,
        end: str,
        stationname: int,
        gaugename: Union[str, int],
        segment_xs: str,
        *args,
        **kwargs,
    ):
        """PlotQ.

            plot the hydrograph at the  gauge location for the hm, rrm  (at two location is availabe),
            sum of all laterals, upstream hydrograph, boundary condition hydrograph and the gauge time series.

        Parameters
        ----------
        Calib : [Calibration object]
            DESCRIPTION.
        gaugexs : integer
            the xsid of the gauge.
        start : [string]
            start date of the plot.
        end : [string]
            end date of the plot.
        stationname : [string]
            station name.
        gaugename : TYPE
            DESCRIPTION.
        segment_xs : TYPE
            DESCRIPTION.
        kwargs:
            plotlaterals : TYPE, optional
                DESCRIPTION. The default is True.
            plotus : TYPE, optional
                DESCRIPTION. The default is True.
            specificxs : TYPE, optional
                DESCRIPTION. The default is False.
            plotrrm : TYPE, optional
                DESCRIPTION. The default is True.
            plotgauge : TYPE, optional
                DESCRIPTION. The default is True.
            hmcolor : TYPE, optional
                DESCRIPTION. The default is "#004c99".
            gaugecolor : TYPE, optional
                DESCRIPTION. The default is "#DC143C".
            rrmcolor : TYPE, optional
                DESCRIPTION. The default is "green".
            latcolor : TYPE, optional
                DESCRIPTION. The default is (0.3,0,0).
            xscolor : TYPE, optional
                DESCRIPTION. The default is "grey".
            line_width : TYPE, optional
                DESCRIPTION. The default is 4.
            hmorder : TYPE, optional
                DESCRIPTION. The default is 6.
            gaugeorder : TYPE, optional
                DESCRIPTION. The default is 5.
            rrmorder : TYPE, optional
                DESCRIPTION. The default is 4.
            ushorder : TYPE, optional
                DESCRIPTION. The default is 2.
            xsorder : TYPE, optional
                DESCRIPTION. The default is 1.
            fmt: [string]
                format of the date. fmt="%Y-%m-%d %H:%M:%S"
            xlabels : [bool, int], optional
                DESCRIPTION. The default is False.
            ylabels : [bool, int], optional
                DESCRIPTION. The default is False.
            rrm2color: []
                Description
            gaugestyle: []
                Description
            rrm2linesytle: []
                Description
            ushstyle: []
                Description
            xslinestyle: []
                Description
            latorder: []
                Description
            ushcolor: []
                Description
            latstyle: []
                Description
            plottotal: [bool]
                default is True.
            totalcolor: [str, tuple]
                default is "k".
            totalorder: [int]
                default is 6.
            totalstyle: [int]
                default is 4.
            rrmlinestyle: [int]
                default is 6.
            fig_size: [tuple]
                default is (6, 5).

        Returns
        -------
        fig : TYPE
            DESCRIPTION.
        ax : TYPE
            DESCRIPTION.
        """
        start = dt.datetime.strptime(start, self.fmt)
        end = dt.datetime.strptime(end, self.fmt)

        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=self.figsize)

        if self.xs_hydrograph is not None:
            # plot if you read the results using ther read1DResults
            try:
                ax.plot(
                    self.xs_hydrograph.loc[start:end, gaugexs],
                    label="RIM",
                    zorder=self.hmorder,
                    linewidth=self.linewidth,
                    linestyle=V.getLineStyle(6),
                    color=self.hmcolor,
                )
            except KeyError:
                logger.debug(
                    f"the xs given -{gaugexs} - does not exist in the river reach"
                )

            # laterals
            if self.plotlaterals:
                try:
                    Laterals = self.getLaterals(gaugexs)
                except AssertionError:
                    logger.debug("please read the laterals first to be able to plot it")

                # BC

                if isinstance(self.BC, DataFrame):
                    ax.plot(
                        self.BC.loc[start:end, self.BC.columns[0]],
                        label="BC",
                        zorder=self.ushorder,
                        linewidth=self.linewidth,
                        linestyle=V.getLineStyle(self.ushstyle),
                        color=self.ushcolor,
                    )
                # Laterals
                if (
                    isinstance(self.laterals_table, list)
                    and len(self.laterals_table) > 0
                ):
                    ax.plot(
                        Laterals.loc[start:end, 0],
                        label="Laterals",
                        zorder=self.latorder,
                        linewidth=self.linewidth,
                        linestyle=V.getLineStyle(self.latstyle),
                        color=self.latcolor,
                    )
                if self.plottotal:
                    # total flow
                    try:
                        ax.plot(
                            self.TotalFlow.loc[start:end, "total"],
                            label="US/BC + Laterals",
                            zorder=self.totalorder,
                            linewidth=self.linewidth,
                            linestyle=V.getLineStyle(self.totalstyle),
                            color=self.totalcolor,
                        )
                    except AttributeError:
                        logger.debug(
                            "there are no totalFlow for this reach please use the 'GetTotalFlow' method to create it"
                        )

            # US hydrograph
            if self.usnode != [] and self.plotus:
                try:
                    ax.plot(
                        self.us_hydrographs.loc[start:end, "total"],
                        label="US Hydrograph",
                        zorder=self.ushorder,
                        linewidth=self.linewidth,
                        linestyle=V.getLineStyle(self.ushstyle),
                        color=self.ushcolor,
                    )
                except KeyError:
                    msg = (
                        "Please read the routed hydrograph of the upstream reachs using the "
                        "'ReadUSHydrograph' method"
                    )

                    logger.debug(msg)

            # Gauge
            if self.plotgauge:
                # plot the gauge data
                ax.plot(
                    Calib.q_gauges.loc[start:end, stationname],
                    label="Gauge",
                    linewidth=self.linewidth,
                    zorder=self.gaugeorder,
                    color=self.gaugecolor,
                    linestyle=V.getLineStyle(self.gaugestyle),
                )

            # specific XS
            if not isinstance(self.specificxs, bool):
                # first extract the time series of the given xs
                self.read1DResult(xsid=self.specificxs)
                # plot the xs
                ax.plot(
                    self.xs_hydrograph.loc[start:end, self.specificxs],
                    label="XS-" + str(self.specificxs),
                    zorder=self.xsorder,
                    linewidth=self.linewidth,
                    color=self.xscolor,
                    linestyle=V.getLineStyle(self.xslinestyle),
                )
            # RRM
            if self.plotrrm:
                if isinstance(self.RRM, DataFrame):
                    try:
                        ax.plot(
                            self.RRM.loc[start:end, stationname],
                            label="mHM-RIM Loc",
                            zorder=self.rrmorder,
                            linewidth=self.linewidth,
                            linestyle=V.getLineStyle(self.rrmlinestyle),
                            color=self.rrmcolor,
                        )
                    except KeyError:
                        logger.debug(
                            f" Station {gaugename} does not have the first RRM discharge time series"
                        )

                if isinstance(self.RRM2, DataFrame):
                    try:
                        ax.plot(
                            self.RRM2.loc[start:end, stationname],
                            label="mHM-mHM Loc",
                            zorder=self.rrmorder,
                            linewidth=self.linewidth,
                            linestyle=V.getLineStyle(self.rrm2linesytle),
                            color=self.rrm2color,
                        )
                    except KeyError:
                        logger.debug(
                            f" Station {gaugename} does not have a second RRM discharge time series"
                        )

        elif isinstance(Calib.calibration_q, DataFrame):
            # plot if you read the data using ReadCalirationResult
            ax.plot(
                Calib.calibration_q[segment_xs],
                label="RIM",
                zorder=3,
                linewidth=self.linewidth,
                linestyle=V.getLineStyle(6),
                color=self.hmcolor,
            )
            # plot the gauge data
            ax.plot(
                Calib.q_gauges.loc[
                    Calib.calibration_q.index[0] : Calib.calibration_q.index[-1],
                    stationname,
                ],
                label="Gauge-" + str(self.id),
                linewidth=self.linewidth,
                color=self.gaugecolor,
            )
            if self.plotrrm:
                ax.plot(
                    self.RRM.loc[
                        Calib.calibration_q.index[0] : Calib.calibration_q.index[-1],
                        stationname,
                    ],
                    label="RRM",
                )

        if not isinstance(self.xlabels, bool):
            start, end = ax.get_xlim()
            if isinstance(self.xlabels, int):
                ax.xaxis.set_ticks(np.linspace(start, end, self.xlabels))
            else:
                start = self.round(start, self.xlabels[0])
                end = self.round(end, self.xlabels[0])

                ax.yaxis.set_ticks(np.arange(start, end, self.xlabels[0]))

        if not isinstance(self.ylabels, bool):
            start, end = ax.get_ylim()
            if isinstance(self.ylabels, int):
                if start < 0:
                    start = 0
                ax.yaxis.set_ticks(np.linspace(start, end, self.ylabels))
            else:
                start = self.round(start, self.ylabels[0])
                end = self.round(end, self.ylabels[0])

                ax.yaxis.set_ticks(np.arange(start, end, self.ylabels[0]))

        ax.set_title("Discharge - " + gaugename, fontsize=20)

        ax.legend(fontsize=12)
        ax.set_xlabel("Time", fontsize=12)
        ax.set_ylabel("Discharge m3/s", fontsize=12)
        plt.tight_layout()

        return fig, ax

    @class_method_parse(plot_discharge_args)
    def plotRRMProgression(self, specificxs, start, end, *args, **kwargs):
        """PlotRRMProgression.

            plot the hydrograph at the  gauge location for the hm, rrm  (at two location is availabe),
            sum of all laterals, upstream hydrograph, boundary condition hydrograph and the gauge time series.

        Parameters
        ----------
        specificxs : integer
            the xsid of the gauge.
        start : [string]
            start date of the plot.
        end : [string]
            end date of the plot.
        kwargs:
            plotlaterals : TYPE, optional
                DESCRIPTION. The default is True.
            plotus : TYPE, optional
                DESCRIPTION. The default is True.
            specificxs : TYPE, optional
                DESCRIPTION. The default is False.
            hmcolor : TYPE, optional
                DESCRIPTION. The default is "#004c99".
            rrmcolor : TYPE, optional
                DESCRIPTION. The default is "green".
            latcolor : TYPE, optional
                DESCRIPTION. The default is (0.3,0,0).
            line_width : TYPE, optional
                DESCRIPTION. The default is 4.
            hmorder : TYPE, optional
                DESCRIPTION. The default is 6.
            rrmorder : TYPE, optional
                DESCRIPTION. The default is 4.
            ushorder : TYPE, optional
                DESCRIPTION. The default is 2.
            fmt: [string]
                format of the date. fmt="%Y-%m-%d %H:%M:%S"
            ushstyle: []
                Description
            latorder: []
                Description
            ushcolor: []
                Description
            latstyle: []
                Description
            xlabels: [int, bool]
                default is False.
            ylabels: [int, bool]
                default is False.
            fig_size: [tuple]
                default is (6, 5).
            rrmlinesytle: [int]
                default is 8
            plottotal: [bool]
                default is True.
            totalcolor: [str, tuple]
                default is "k".
            totalorder: [int]
                default is 6.
            totalstyle: [int]
                default is 11.
            plothm: [bool]
                default is True.

        Returns
        -------
        fig : TYPE
            DESCRIPTION.
        ax : TYPE
            DESCRIPTION.
        """
        start = dt.datetime.strptime(start, self.fmt)
        end = dt.datetime.strptime(end, self.fmt)

        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=self.figsize)

        # laterals
        if self.plotlaterals:
            Laterals = self.getLaterals(specificxs)

            # BC
            if type(self.BC) != bool:
                ax.plot(
                    self.BC.loc[start:end, self.BC.columns[0]],
                    label="BC",
                    zorder=self.ushorder,
                    linewidth=self.linewidth,
                    linestyle=V.getLineStyle(self.ushstyle),
                    color=self.ushcolor,
                )
            # Laterals
            if len(self.laterals_table) > 0:
                ax.plot(
                    Laterals.loc[start:end, 0],
                    label="Laterals Sum \n up to - XS-" + str(specificxs),
                    zorder=self.latorder,
                    linewidth=self.linewidth,
                    linestyle=V.getLineStyle(self.latstyle),
                    color=self.latcolor,
                )
            if self.plottotal:
                # total flow
                self.getTotalFlow(specificxs)
                ax.plot(
                    self.TotalFlow.loc[start:end, "total"],
                    label="US/BC \n+ Laterals",
                    zorder=self.totalorder,
                    linewidth=self.linewidth,
                    linestyle=V.getLineStyle(self.totalstyle),
                    color=self.totalcolor,
                )

        # US hydrograph
        if self.usnode != [] and self.plotus:
            ax.plot(
                self.us_hydrographs.loc[start:end, "total"],
                label="US Hydrograph",
                zorder=self.ushorder,
                linewidth=self.linewidth,
                linestyle=V.getLineStyle(self.ushstyle),
                color=self.ushcolor,
            )

        # specific XS
        if self.plothm:
            # first extract the time series of the given xs
            self.read1DResult(xsid=specificxs)
            # plot the xs
            ax.plot(
                self.xs_hydrograph.loc[start:end, specificxs],
                label="RIM",
                zorder=self.hmorder,
                linewidth=self.linewidth,
                linestyle=V.getLineStyle(6),
                color=self.hmcolor,
            )
        # RRM
        # if plotrrm:
        if hasattr(self, "routed_rrm"):
            try:
                ax.plot(
                    self.rrm_progression.loc[start:end, specificxs],
                    label="mHM",
                    zorder=self.rrmorder,
                    linewidth=self.linewidth,
                    linestyle=V.getLineStyle(self.rrmlinesytle),
                    color=self.rrmcolor,
                )
            except KeyError:
                logger.debug(
                    " XS " + str(specificxs) + "does not exist in the  'routed_rrm'"
                )
        else:
            msg = (
                "please read the RRM hydrographs using the 'ReadRRMProgression'"
                "in the interface module"
            )
            logger.debug(msg)

        if type(self.xlabels) != bool:
            start, end = ax.get_xlim()
            if type(self.xlabels) == int:
                ax.xaxis.set_ticks(np.linspace(start, end, self.xlabels))

        if type(self.ylabels) != bool:
            start, end = ax.get_ylim()
            if type(self.ylabels) == int:
                if start < 0:
                    start = 0
                ax.yaxis.set_ticks(np.linspace(start, end, self.ylabels))
            else:
                start = self.round(start, self.ylabels[0])
                end = self.round(end, self.ylabels[0])

                ax.yaxis.set_ticks(np.arange(start, end, self.ylabels[0]))

        ax.set_title("XS - " + str(specificxs), fontsize=20)

        ax.legend(fontsize=12)
        ax.set_xlabel("Time", fontsize=12)
        ax.set_ylabel("Discharge m3/s", fontsize=12)
        plt.tight_layout()

        return fig, ax

    def calculateQMetrics(
        self,
        Calib,
        stationname: int,
        gaugexs: int,
        Filter: bool = False,
        start: str = "",
        end: str = "",
        fmt: str = "%Y-%m-%d",
    ):
        """CalculateQMetrics. calculates the performance metrices for the discharge time series.

        Parameters
        ----------
        Calib : TYPE
            DESCRIPTION.
        stationname : TYPE
            DESCRIPTION.
        gaugexs : [int]
            DESCRIPTION.
        start : [str]
            DESCRIPTION.
        end : [str]
            DESCRIPTION.
        Filter : TYPE, optional
            DESCRIPTION. The default is False.
        fmt: [string]
            format of the date. fmt="%Y-%m-%d %H:%M:%S"

        Returns
        -------
        rmse: [float]
            root mean square error.
        kge: [float]
            Kling-gupta metric.
        wb: [float]
            water balance metrix.
        nsehf: [float]
            Nash-sutcliffe for high values metric.
        nse: [float]
            Nash-sutcliffe metric.
        """
        QHM = pd.DataFrame()

        try:
            GaugeStart = Calib.hm_gauges.loc[
                Calib.hm_gauges["xsid"] == gaugexs, "Qstart"
            ].values[0]
            GaugeEnd = Calib.hm_gauges.loc[
                Calib.hm_gauges["xsid"] == gaugexs, "Qend"
            ].values[0]
        except IndexError:
            logger.debug("The XS you provided does not exist in the hm_gauges")
            return

        if Filter:
            start = dt.datetime.strptime(start, fmt)
            end = dt.datetime.strptime(end, fmt)
            # get the latest date of the filter date and the first date in the result
            # get the earliest date of the end and the last date in the result
            st2 = max(GaugeStart, start, self.first_day_results)
            end2 = min(GaugeEnd, end, self.last_day)

            # get the observed discharge
            Qobs = Calib.q_gauges.loc[st2:end2, stationname]

            # resample the times series to average daily
            ind = pd.date_range(
                self.first_day_results, self.last_day + dt.timedelta(days=1), freq="h"
            )[:-1]

            Q = self.results_1d[self.results_1d["xs"] == self.last_xs]
            Q.index = ind
            QHM["q"] = Q["q"].resample("D").mean()
            QHM["q"] = QHM.loc[st2:end2, "q"]

            # try:
            #     sub.Resample(gaugexs, 'q', starti, endi, Delete=True)
            # except:
            #     sub.Resample(gaugexs, 'q', starti, endi, Delete=False)
            # q_hm['q']  = sub.resampled_q[gaugexs][:]
            # q_hm.index = pd.date_range(st2, end2)

        else:
            st2 = max(GaugeStart, self.first_day_results)
            end2 = min(GaugeEnd, self.last_day)
            # get the observed discharge
            Qobs = Calib.q_gauges.loc[st2:end2, stationname]

            # resample the times series to average daily
            ind = pd.date_range(
                self.first_day_results, self.last_day + dt.timedelta(days=1), freq="h"
            )[:-1]
            Q = self.results_1d[self.results_1d["xs"] == self.last_xs]
            Q.index = ind
            QHM["q"] = Q["q"].resample("D").mean()
            QHM["q"] = QHM.loc[st2:end2, "q"]

            # old
            # q_hm['q'] = sub.results_1d['q'][sub.results_1d['xs'] == gaugexs][sub.results_1d['hour'] == 24][:]
            # q_hm.index = pd.date_range(st2, end2)
        qsim = QHM.loc[st2:end2, "q"].tolist()
        rmse = round(Pf.RMSE(Qobs, qsim), 0)
        kge = round(Pf.KGE(Qobs, qsim), 2)
        wb = round(Pf.WB(Qobs, qsim), 0)
        nsehf = round(Pf.NSEHF(Qobs, qsim), 2)
        nse = round(Pf.NSE(Qobs, qsim), 2)
        logger.debug("--------------------")
        logger.debug("RMSE = " + str(rmse))
        logger.debug("KGE = " + str(kge))
        logger.debug("WB = " + str(wb))
        logger.debug("NSEHF = " + str(nsehf))
        logger.debug("NSE = " + str(nse))

        return rmse, kge, wb, nsehf, nse

    @class_method_parse(plot_discharge_args)
    def plotWL(
        self,
        Calib,
        start: str,
        end: str,
        gaugexs: int,
        stationname: str,
        gaugename: str,
        *args,
        **kwargs,
        # gaugecolor: Union[tuple, str] = "#DC143C",
        # hmcolor: Union[tuple, str] = "#004c99",
        # line_width: Union[int, float] = 2,
        # hmorder: int = 1,
        # gaugeorder: int = 0,
        # hmstyle: int = 6,
        # gaugestyle: int = 0,
        # plotgauge=True,
        # fmt: str = "%Y-%m-%d",
        # legendsize: Union[int, float] = 15,
        # fig_size: tuple = (6, 5),
        # xlabels_number: int = 4,
    ):
        """Plot water level surface.

        plot water level hydrograph

        Parameters
        ----------
        Calib : TYPE
            DESCRIPTION.
        start : TYPE
            DESCRIPTION.
        end : TYPE
            DESCRIPTION.
        gaugexs : TYPE
            DESCRIPTION.
        stationname : TYPE
            DESCRIPTION.
        gaugename : TYPE
            DESCRIPTION.
        kwargs:
            gaugecolor : TYPE, optional
                DESCRIPTION. The default is "#DC143C".
            hmcolor : TYPE, optional
                DESCRIPTION. The default is "#004c99".
            line_width : TYPE, optional
                DESCRIPTION. The default is 2.
            hmorder : TYPE, optional
                DESCRIPTION. The default is 1.
            gaugeorder : TYPE, optional
                DESCRIPTION. The default is 0.
            plotgauge : TYPE, optional
                DESCRIPTION. The default is True.
            fmt: [string]
                format of the date. fmt="%Y-%m-%d %H:%M:%S"
            hmstyle: [int]
                default is 6
            gaugestyle: [int]
                default is 0.
            legendsize: [int, float]
                default is 15.
            fig_size: tuple=(6, 5),
            xlabels_number: [int]
                default is 4.

        Returns
        -------
        ax : TYPE
            DESCRIPTION.
        """
        start = dt.datetime.strptime(start, self.fmt)
        end = dt.datetime.strptime(end, self.fmt)

        if self.plotgauge:

            GaugeStart = Calib.hm_gauges[Calib.hm_gauges["xsid"] == gaugexs]["WLstart"]
            GaugeEnd = Calib.hm_gauges[Calib.hm_gauges["xsid"] == gaugexs]["WLend"]

            try:
                GaugeStart = GaugeStart.values[0]
                GaugeEnd = GaugeEnd.values[0]

                if GaugeStart > start and GaugeStart > end:
                    logger.debug(
                        f"Availabel data for the gauge starts from {GaugeStart}"
                    )
                    logger.debug(
                        f"The period you provided is between {start} and {end}"
                    )
                    plotgauge = False
                elif GaugeEnd < start and GaugeStart < end:
                    logger.debug(f"Availabel data for the gauge starts from {GaugeEnd}")
                    logger.debug("Out of Gauge dates")
                    plotgauge = False
            except (IndexError, TypeError):
                logger.debug("The XS you provided does not exist in the hm_gauges")
                plotgauge = False

        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=self.figsize)

        # extract the water levels at the gauge cross section
        self.extractXS(gaugexs)

        ax.plot(
            self.xs_water_level.loc[start:end, gaugexs],
            label="RIM",
            zorder=self.hmorder,
            linewidth=self.linewidth,
            color=self.hmcolor,
            linestyle=V.getLineStyle(self.hmstyle),
        )

        if self.plotgauge:
            ax.plot(
                Calib.wl_gauges.loc[start:end, stationname],
                label="Gauge",
                zorder=self.gaugeorder,
                linewidth=self.linewidth,
                color=self.gaugecolor,
                linestyle=V.getLineStyle(self.gaugestyle),
            )

        start, end = ax.get_xlim()
        ax.xaxis.set_ticks(np.linspace(start, end, self.nxlabels))

        ax.set_title("Water Level - " + gaugename, fontsize=20)
        plt.legend(fontsize=self.legendsize)
        ax.set_xlabel("Time", fontsize=15)
        ax.set_ylabel("Water Level m", fontsize=15)
        plt.tight_layout()

        return fig, ax

    def calculateWLMetrics(
        self,
        Calib,
        stationname: int,
        gaugexs: int,
        Filter: bool = False,
        start: Union[dt.datetime, str] = "",
        end: Union[dt.datetime, str] = "",
        fmt: str = "%Y-%m-%d",
    ):
        """CalculateWLMetrics. calculate the performance metrics for the water level time series.

        fmt: [string]
            format of the date. fmt="%Y-%m-%d %H:%M:%S"
        """
        try:
            GaugeStart = Calib.hm_gauges[Calib.hm_gauges["xsid"] == gaugexs][
                "WLstart"
            ].values[0]
            GaugeEnd = Calib.hm_gauges[Calib.hm_gauges["xsid"] == gaugexs][
                "WLend"
            ].values[0]
        except IndexError:
            logger.debug("The XS you provided does not exist in the hm_gauges")
            return

        if isinstance(GaugeStart, int):
            logger.debug("No water level data for this river reach")
            return

        if Filter:
            if isinstance(start, str):
                start = dt.datetime.strptime(start, fmt)
            if isinstance(end, str):
                end = dt.datetime.strptime(end, fmt)

            st2 = max(GaugeStart, start, self.first_day_results)
            end2 = min(GaugeEnd, end, self.last_day)
            # observed
            obs = np.array(Calib.wl_gauges.loc[st2:end2, stationname])

            # RIM
            ind = pd.date_range(
                self.first_day_results, self.last_day + dt.timedelta(days=1), freq="h"
            )[:-1]
            mod = self.results_1d[self.results_1d["xs"] == self.last_xs]
            mod.index = ind
            mod = mod["wl"].resample("D").mean()
            mod = mod.loc[st2:end2]

            # RIM
            # try:
            #     sub.Resample(gaugexs, 'wl', River.DateToIndex(st2),
            #                   River.DateToIndex(end2), Delete = True)
            # except:
            #     sub.Resample(gaugexs, 'wl', River.DateToIndex(st2),
            #                   River.DateToIndex(end2), Delete = False)
            # series1 = np.array(sub.resampled_wl[gaugexs])
        else:
            st2 = max(GaugeStart, self.first_day_results)
            end2 = min(GaugeEnd, self.last_day)
            # Observed
            obs = np.array(Calib.wl_gauges.loc[st2:end2, stationname])

            # RIM
            ind = pd.date_range(
                self.first_day_results, self.last_day + dt.timedelta(days=1), freq="h"
            )[:-1]
            mod = self.results_1d[self.results_1d["xs"] == gaugexs]
            mod.index = ind
            mod = mod["wl"].resample("D").mean()
            mod = mod.loc[st2:end2]

            # RIM
            # sub.Resample(gaugexs, 'wl', River.DateToIndex(st2),
            #               River.DateToIndex(end2), Delete = False)
            # series1 = np.array(sub.resampled_wl[gaugexs])

        if len(obs) != len(mod) or len(mod) == 0:
            logger.debug(
                "Availabel data for the gauge starts from "
                + str(GaugeStart)
                + " To "
                + str(GaugeEnd)
            )
            return

        MBE = round(Pf.MBE(obs, mod), 2)
        MAE = round(Pf.MAE(obs, mod), 2)
        RMSE = round(Pf.RMSE(obs, mod), 2)
        KGE = round(Pf.KGE(obs, mod), 2)
        NSEHF = round(Pf.NSEHF(obs, mod), 2)
        NSE = round(Pf.NSE(obs, mod), 2)

        logger.debug("RMSE= " + str(RMSE))
        logger.debug("KGE= " + str(KGE))
        logger.debug("NSEHF= " + str(NSEHF))
        logger.debug("NSE= " + str(NSE))
        logger.debug("MBE= " + str(MBE))
        logger.debug("MAE= " + str(MAE))

        return MBE, MAE, RMSE, KGE, NSEHF, NSE

    def histogram(
        self,
        Day,
        BaseMapF,
        ExcludeValue,
        OccupiedCellsOnly,
        Map=1,
        filter1=0.2,
        filter2=15,
    ):
        """Histogram.

        Histogram Extracts the values that are located in the same location in the BaseMap as the Reach-basin

        :param Day:
        :param BaseMapF:
        :param ExcludeValue:
        :param OccupiedCellsOnly: [boolean] True if you want to count only cells that is not zero and not
                                    to extract the values.
        :param Map: [1/2/3] 1 for depthmax maps, 2 for duration maps, 3 for return period maps
        :param filter1: [real] execlude lower values than filter1
        :param filter2: [real] execlude values higher than filter2
        :return:
            extracted_values [list] list of extracted values
        """
        # check if the object has the attribute extracted_values
        if hasattr(self, "extracted_values"):
            # depth map
            if Map == 1:
                path = self.twodresultpath + self.depthprefix + str(Day) + ".zip"
            elif Map == 2:
                path = self.twodresultpath + self.durationprefix + str(Day) + ".zip"
            else:
                path = (
                    self.twodresultpath + self.returnperiod_prefix + str(Day) + ".zip"
                )

            ExtractedValues, NonZeroCells = raster.overlayMap(
                path, BaseMapF, ExcludeValue, self.compressed, OccupiedCellsOnly
            )

            self.ExtractedValues = ExtractedValues[self.id]
        # filter values
        ExtractedValues = [j for j in ExtractedValues if j > filter1]
        ExtractedValues = [j for j in ExtractedValues if j < filter2]
        # plot
        fig, ax1 = plt.subplots(figsize=(10, 8))
        ax1.hist(ExtractedValues, bins=15, alpha=0.4)  # width = 0.2,
        ax1.set_ylabel("Frequency RIM1.0", fontsize=15)
        ax1.yaxis.label.set_color("#27408B")
        ax1.set_xlabel("Depth Ranges (m)", fontsize=15)
        # ax1.cla

        ax1.tick_params(axis="y", color="#27408B")

    def ListAttributes(self):
        """Print Attributes List."""
        logger.debug("\n")
        logger.debug(
            f"Attributes List of: {repr(self.__dict__['name'])} - {self.__class__.__name__}  Instance\n"
        )
        self_keys = list(self.__dict__.keys())
        self_keys.sort()
        for key in self_keys:
            if key != "name":
                logger.debug(str(key) + " : " + repr(self.__dict__[key]))

        logger.debug("\n")

    def plotBC(self, date: str, fmt: str = "%Y-%m-%d"):
        """PlotBC. plot the boundary condition discharge and water depth.

        Parameters
        ----------
        date : TYPE
            DESCRIPTION.
        fmt: [string] optional
            format of the date. fmt="%Y-%m-%d %H:%M:%S", default is fmt="%Y-%m-%d"

        Returns
        -------
        None.
        """
        date = dt.datetime.strptime(date, fmt)

        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        ax1.plot(self.h_bc_1min.loc[date])
        ax1.set_xlabel("Date", fontsize=15)
        ax1.set_ylabel("H", fontsize=15)
        ax1.set_xlim(0, 1440)
        ax2.plot(self.q_bc_1min.loc[date])
        ax2.set_ylabel("Q", fontsize=15)
