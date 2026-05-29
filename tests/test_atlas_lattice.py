"""Tests for the atlas_lattice package."""

import json
import pytest
from atlas_lattice import Coordinate, HOUSE_NAMES, SPHERE_NAMES, NODE_NAMES


class TestCoordinateParse:
    def test_parse_valid(self):
        coord = Coordinate.parse("H04-S09-N02")
        assert coord.house == 4
        assert coord.sphere == 9
        assert coord.node == 2

    def test_parse_case_insensitive(self):
        coord = Coordinate.parse("h04-s09-n02")
        assert coord.house == 4

    def test_parse_address_roundtrip(self):
        addr = "H04-S09-N02"
        assert Coordinate.parse(addr).address == addr

    def test_parse_invalid_format(self):
        with pytest.raises(ValueError):
            Coordinate.parse("A04.B09.C02")

    def test_parse_out_of_range(self):
        with pytest.raises(ValueError):
            Coordinate.parse("H13-S01-N01")

    def test_parse_zero(self):
        with pytest.raises(ValueError):
            Coordinate.parse("H00-S01-N01")

    def test_boundary_max(self):
        coord = Coordinate.parse("H12-S12-N12")
        assert coord.house == 12
        assert coord.sphere == 12
        assert coord.node == 12


class TestCoordinateLabels:
    def test_house_label(self):
        coord = Coordinate.parse("H04-S09-N02")
        assert coord.house_label == "Information Architecture"

    def test_sphere_label(self):
        coord = Coordinate.parse("H04-S09-N02")
        assert coord.sphere_label == "Knowledge Graph"

    def test_node_label(self):
        coord = Coordinate.parse("H04-S09-N02")
        assert coord.node_label == "Artifact"

    def test_all_house_names(self):
        assert len(HOUSE_NAMES) == 12

    def test_all_sphere_names(self):
        assert len(SPHERE_NAMES) == 12

    def test_all_node_names(self):
        assert len(NODE_NAMES) == 12


class TestCoordinateCellIndex:
    def test_first_cell(self):
        assert Coordinate.parse("H01-S01-N01").cell_index == 0

    def test_last_cell(self):
        assert Coordinate.parse("H12-S12-N12").cell_index == 1727

    def test_total_cells(self):
        assert 12 * 12 * 12 == 1728


class TestCoordinateToDict:
    def test_to_dict_keys(self):
        d = Coordinate.parse("H04-S09-N02").to_dict()
        assert set(d.keys()) == {"address", "house", "sphere", "node", "cell_index"}

    def test_to_dict_json_serializable(self):
        d = Coordinate.parse("H04-S09-N02").to_dict()
        assert json.dumps(d)  # should not raise


class TestCoordinateStr:
    def test_str_contains_address(self):
        coord = Coordinate.parse("H04-S09-N02")
        assert "H04-S09-N02" in str(coord)

    def test_str_contains_labels(self):
        coord = Coordinate.parse("H04-S09-N02")
        s = str(coord)
        assert "Information Architecture" in s
        assert "Knowledge Graph" in s
        assert "Artifact" in s


class TestFromIndices:
    def test_from_indices(self):
        coord = Coordinate.from_indices(4, 9, 2)
        assert coord.address == "H04-S09-N02"
