# pylint: disable=redefined-outer-name
"""
Tests for MSEclipse
"""
import os
import sys
import pickle
import pytest
import numpy as np
import pandas as pd
import bmxp.eclipse as ms


@pytest.fixture()
def filepath_1():
    """
    First file path for test
    """
    print("*****************", os.getcwd())
    return "tests/test1.csv"


@pytest.fixture()
def filepath_2():
    """
    Second file path for test
    """
    return "tests/test2.csv"


@pytest.fixture()
def filepath_3():
    """
    Third file path for test
    """
    return "tests/test3.csv"


@pytest.fixture()
def dataframe_1(filepath_1):
    """
    First dataframe for test
    """
    return pd.read_csv(filepath_1)


@pytest.fixture()
def dataframe_2(filepath_2):
    """
    Second dataframe for test
    """
    return pd.read_csv(filepath_2)


@pytest.fixture()
def dataframe_3(filepath_3):
    """
    Third dataframe for test
    """
    return pd.read_csv(filepath_3)


@pytest.fixture()
def pickled_ms():
    """
    Load pickled file
    """
    return pickle.load(
        open("tests/mseclipse.pickle", "rb")  # pylint: disable=consider-using-with
    )


def test_initialize_add(filepath_1, filepath_2, dataframe_1, dataframe_2):
    """
    Test MSAligner initializes or throws errors
    """

    # example test: show that importing and utilizing the class is successful
    ms.MSAligner(filepath_1, filepath_2, names=["hp1", "hp2"])

    # Check that dataframes can be read
    ms.MSAligner(dataframe_1, dataframe_2, names=["hp1", "hp2"])

    # datasets require names
    with pytest.raises(ValueError) as e:
        ms.MSAligner(dataframe_1, dataframe_2)
    assert "must be provided" in str(e.value)

    # check mismatch in length
    with pytest.raises(ValueError) as e:
        ms.MSAligner(filepath_1, filepath_2, names=["hp1", "hp2", "hp3"])
    assert "The number of names" in str(e.value)

    # check duplicate names
    with pytest.raises(ValueError) as e:
        ms.MSAligner(filepath_1, filepath_2, names=["hp2", "hp2"])
    assert "duplicate" in str(e.value)


def test_add_dataset(filepath_1, filepath_2, dataframe_1, dataframe_2):
    """
    Test MSAligner add_dataset method
    """
    a = ms.MSAligner()

    # example test: show that importing and utilizing the class is successful
    a.add_dataset(filepath_1, "hp1")
    a.add_dataset(dataframe_2, "hp2")

    # check duplicate names
    with pytest.raises(ValueError) as e:
        a.add_dataset(filepath_2, "hp2")
    assert "duplicate" in str(e.value)

    # test dataframe can be added
    a.add_dataset(dataframe_1, "hp3")

    # dataframes require names
    with pytest.raises(ValueError) as e:
        a.add_dataset(dataframe_2)
    assert "must be provided" in str(e.value)


def test_alignment_methods(dataframe_1, dataframe_2, pickled_ms):
    """
    Test the methods associated with alignment
    """

    a = ms.MSAligner(dataframe_1, dataframe_2, names=["HP1", "HP2"])

    # Test anchors
    a.gen_anchors()
    assert a.anchors["HP1"] == pickled_ms.anchors["HP1"]
    assert a.anchors["HP2"] == pickled_ms.anchors["HP2"]

    # Test coarse matching
    a.gen_coarse()
    assert np.equal(
        a.coarse_matches["HP1"]["HP2"].values,
        pickled_ms.coarse_matches["HP1"]["HP2"].values,
    ).all()

    # Test scaler generation; RT, MZ, and intensity
    a.gen_scalers()
    hp1_scalers = a.scalers["HP1"]["HP2"]
    pickled_scalers = pickled_ms.scalers["HP1"]["HP2"]
    assert np.isclose(hp1_scalers["RT"]["y"], pickled_scalers["RT"]["y"]).all()
    assert np.isclose(hp1_scalers["RT"]["x"], pickled_scalers["RT"]["x"]).all()
    assert np.isclose(hp1_scalers["MZ"]["y"], pickled_scalers["MZ"]["y"]).all()
    assert np.isclose(hp1_scalers["MZ"]["x"], pickled_scalers["MZ"]["x"]).all()
    assert np.isclose(
        hp1_scalers["Intensity"]["x"], pickled_scalers["Intensity"]["x"]
    ).all()
    assert np.isclose(
        hp1_scalers["Intensity"]["y"], pickled_scalers["Intensity"]["y"]
    ).all()

    # Test scaling functions
    a.gen_scaled_values()
    scaled_values = a.scaled_values["HP1"]["HP2"]
    pickled_values = pickled_ms.scaled_values["HP1"]["HP2"]
    assert np.isclose(scaled_values["RT"], pickled_values["RT"]).all()
    assert np.isclose(scaled_values["MZ"], pickled_values["MZ"]).all()
    assert np.isclose(scaled_values["Intensity"], pickled_values["Intensity"]).all()

    # Test standard deviation calculations
    a.gen_stds()
    assert np.isclose(a.stds["HP1"]["HP2"]["RT"], pickled_ms.stds["HP1"]["HP2"]["RT"])
    assert np.isclose(a.stds["HP1"]["HP2"]["MZ"], pickled_ms.stds["HP1"]["HP2"]["MZ"])
    assert np.isclose(
        a.stds["HP1"]["HP2"]["Intensity"], pickled_ms.stds["HP1"]["HP2"]["Intensity"]
    )

    # Test matches
    a.gen_matches()
    assert a.matches["HP1"]["HP2"].equals(pickled_ms.matches["HP1"]["HP2"])

    # Check that align passes
    a = ms.MSAligner(dataframe_1, dataframe_2, names=["HP1", "HP2"])
    a.align()

    # Check that custom scalers are not overwritten
    rt = ms.calc_scalers([1, 2, 3], [1.1, 2.2, 3.3])
    mz = ms.calc_scalers([100, 200, 300], [100.0005, 200.0008, 300.0009])
    intensity = ms.calc_scalers([2, 3, 4], [3, 4, 5])

    a = ms.MSAligner(dataframe_1, dataframe_2, names=["HP1", "HP2"])
    a.set_scalers(
        {
            "HP1": {
                "HP2": {"RT": zip(*rt), "MZ": zip(*mz), "Intensity": zip(*intensity),}
            }
        },
        rec=False,
    )
    a.align()
    a_scalers = a.scalers["HP1"]["HP2"]
    assert np.equal(a_scalers["RT"]["x"], rt[0]).all()
    assert np.equal(a_scalers["RT"]["y"], rt[1]).all()
    assert np.equal(a_scalers["MZ"]["x"], mz[0]).all()
    assert np.equal(a_scalers["MZ"]["y"], mz[1]).all()
    assert np.equal(a_scalers["Intensity"]["x"], intensity[0]).all()
    assert np.equal(a_scalers["Intensity"]["y"], intensity[1]).all()

    # check reciprocity for scaler generation works
    a = ms.MSAligner(dataframe_1, dataframe_2, names=["HP1", "HP2"])
    a.set_scalers(
        {
            "HP1": {
                "HP2": {"RT": zip(*rt), "MZ": zip(*mz), "Intensity": zip(*intensity),}
            }
        },
        rec=True,
    )
    a.align()
    a_scalers = a.scalers["HP2"]["HP1"]
    assert np.equal(a_scalers["RT"]["x"], rt[0] + rt[1]).all()
    assert np.equal(a_scalers["RT"]["y"], -rt[1]).all()
    new_mzs = mz[0] + mz[0] * mz[1] / 1000000
    assert np.equal(a_scalers["MZ"]["x"], new_mzs).all()
    assert np.equal(a_scalers["MZ"]["y"], -mz[1] * mz[0] / new_mzs).all()
    assert np.equal(a_scalers["Intensity"]["x"], intensity[0] + intensity[1]).all()
    assert np.equal(a_scalers["Intensity"]["y"], -intensity[1]).all()


def test_calc_score():
    """
    Test score calculation
    """
    score = ms.calc_score(
        {"RT": 1, "MZ": 200, "Intensity": 100},
        {"RT": 2, "MZ": 200.0002, "Intensity": 1000},
        {"RT": "linear", "MZ": "ppm", "Intensity": "log10"},
        {"RT": 1, "MZ": 1, "Intensity": 1},
        {"RT": 1, "MZ": 1, "Intensity": 1},
    )
    assert np.isclose(score, 3)


@pytest.mark.filterwarnings("ignore:invalid value")
def test_calc_scalers():
    """
    Supplemental tests to calculating scalers
    """

    # Will only return nans. Test it does not make an infinite loop
    assert np.isnan(
        ms.calc_scalers(
            np.array([0, 0, 1]), np.array([1, 1, 2]), smoothing="lowess", mode="linear"
        )[1]
    ).all()


def test_adding_intensity_column(dataframe_3):
    """
    Tests to see if intensity is autocalculated when missing
    """
    # Create Dataframes without Intensity
    df_3_no_intensity = dataframe_3.drop(columns="Intensity")

    a = ms.MSAligner()
    a.add_dataset(df_3_no_intensity, "df3")
    # Test that _calc_intensity functions on its own
    assert np.isclose(a.datasets["df3"]["Intensity"], dataframe_3["Intensity"]).all()


def test_dataset_selection(dataframe_1, dataframe_2, dataframe_3):
    """
    Tests the wrappers which control the inner and outer dataframe for loops
    """
    # test all works
    names = ["HP1", "HP2", "HP3"]
    a = ms.MSAligner(dataframe_1, dataframe_2, dataframe_3, names=names)
    a.align()
    assert list(a.matches) == ["HP1", "HP2", "HP3"]
    assert list(a.matches["HP1"]) == ["HP2", "HP3"]
    assert list(a.matches["HP2"]) == ["HP1", "HP3"]
    assert list(a.matches["HP3"]) == ["HP1", "HP2"]

    # test list to all
    a = ms.MSAligner(dataframe_1, dataframe_2, dataframe_3, names=names)
    a.align(["HP1", "HP2", "HP3"])
    assert list(a.matches) == ["HP1", "HP2", "HP3"]
    assert list(a.matches["HP1"]) == ["HP2", "HP3"]
    assert list(a.matches["HP2"]) == ["HP1", "HP3"]
    assert list(a.matches["HP3"]) == ["HP1", "HP2"]

    # test one way to all
    a = ms.MSAligner(dataframe_1, dataframe_2, dataframe_3, names=names)
    a.align("HP1")
    assert list(a.matches) == ["HP1"]
    assert list(a.matches["HP1"]) == ["HP2", "HP3"]

    # test one to one
    a = ms.MSAligner(dataframe_1, dataframe_2, dataframe_3, names=names)
    a.align("HP1", "HP2")
    assert list(a.matches) == ["HP1"]
    assert list(a.matches["HP1"]) == ["HP2"]
